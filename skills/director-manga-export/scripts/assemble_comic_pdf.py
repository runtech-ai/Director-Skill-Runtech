#!/usr/bin/env python3
"""Assemble finished comic page images; no art generation or lettering."""

import argparse
import hashlib
import json
import math
from pathlib import Path
import tempfile

from PIL import Image
from pypdf import PdfReader
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def positive(value, label, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"Invalid {label}: {value}")
    return float(value)


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest() if hasattr(hashlib, "file_digest") else _hash_stream(stream)


def _hash_stream(stream):
    digest = hashlib.sha256()
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


def preflight(manifest):
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("format") != "director-comic-pages" or type(data.get("version")) is not int or data["version"] != 1:
        raise ValueError("Expected director-comic-pages manifest version 1")
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("A nonblank title is required")
    direction = data.get("reading_direction", "ltr")
    fit = data.get("fit", "strict")
    if direction not in ("ltr", "rtl") or fit not in ("strict", "contain"):
        raise ValueError("reading_direction must be ltr/rtl; fit must be strict/contain")
    size = data.get("page_size_mm", [148, 210])
    if not isinstance(size, list) or len(size) != 2:
        raise ValueError("page_size_mm must contain width and height")
    width, height = [positive(v, "page_size_mm") * 72 / 25.4 for v in size]
    margin = positive(data.get("margin_mm", 0), "margin_mm", True) * 72 / 25.4
    area_w, area_h = width - 2 * margin, height - 2 * margin
    if min(area_w, area_h) <= 0:
        raise ValueError("Margins leave no page area")
    floor = positive(data.get("minimum_dpi", 150), "minimum_dpi")
    target = positive(data.get("target_dpi", 300), "target_dpi")
    if floor > target:
        raise ValueError("minimum_dpi cannot exceed target_dpi")
    pages = data.get("pages")
    if not isinstance(pages, list) or not pages:
        raise ValueError("pages must be a nonempty ordered list")
    prepared, ids, warnings = [], set(), []
    for index, page in enumerate(pages, 1):
        if not isinstance(page, dict):
            raise ValueError(f"Page {index} must be an object")
        pid, image_path = page.get("id"), page.get("image")
        if not isinstance(pid, str) or not pid.strip() or pid in ids:
            raise ValueError(f"Page {index} needs a unique nonblank id")
        ids.add(pid)
        if not isinstance(image_path, str) or not image_path:
            raise ValueError(f"{pid}: image path is required")
        image_path = (manifest.parent / image_path).resolve()
        chapter = page.get("chapter")
        if chapter is not None and (not isinstance(chapter, str) or not chapter.strip()):
            raise ValueError(f"{pid}: chapter must be a nonblank string")
        with Image.open(image_path) as image:
            image.verify()
        with Image.open(image_path) as image:
            if image.format not in ("PNG", "JPEG") or getattr(image, "n_frames", 1) != 1:
                raise ValueError(f"{pid}: expected a single PNG or JPEG page")
            if image.getexif().get(274, 1) != 1:
                raise ValueError(f"{pid}: export a page with normalized EXIF orientation first")
            pixels_w, pixels_h = image.size
        ratio_error = abs((pixels_w / pixels_h) / (area_w / area_h) - 1)
        if fit == "strict" and ratio_error > 0.01:
            raise ValueError(f"{pid}: aspect mismatch; recompose the page or use fit=contain")
        scale = min(area_w / pixels_w, area_h / pixels_h)
        placed_w, placed_h = pixels_w * scale, pixels_h * scale
        dpi = 72 / scale
        if dpi + 1e-6 < floor:
            raise ValueError(f"{pid}: {dpi:.1f} DPI is below minimum_dpi={floor:g}")
        if dpi + 1e-6 < target:
            warnings.append(f"{pid}: {dpi:.1f} effective DPI is below target {target:g}")
        prepared.append({"id": pid, "image": str(image_path), "sha256": sha256(image_path),
                         "pixels": [pixels_w, pixels_h], "effective_dpi": round(dpi, 2),
                         "placement_pt": [(width - placed_w) / 2, (height - placed_h) / 2, placed_w, placed_h],
                         "chapter": chapter})
    return data, (width, height), prepared, warnings


def assemble(manifest, output, overwrite=False):
    manifest, output = Path(manifest).resolve(), Path(output).resolve()
    if output.suffix.lower() != ".pdf":
        raise ValueError("Output must have a .pdf extension")
    report_path = output.with_suffix(".report.json")
    data, size, pages, warnings = preflight(manifest)
    inputs = {manifest} | {Path(page["image"]) for page in pages}
    if output in inputs or report_path in inputs:
        raise ValueError("Output would overwrite an input")
    if not overwrite and (output.exists() or report_path.exists()):
        raise ValueError("Output or report already exists; use --overwrite only for an authorized revision")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".pdf", delete=False) as stream:
            temporary = Path(stream.name)
        pdf = canvas.Canvas(str(temporary), pagesize=size, pageCompression=1)
        pdf.setTitle(data["title"])
        pdf.setCreator("Director to Manhwa / Manga PDF")
        pdf.setViewerPreference("Direction", "R2L" if data.get("reading_direction", "ltr") == "rtl" else "L2R")
        for index, page in enumerate(pages):
            path = Path(page["image"])
            if sha256(path) != page["sha256"]:
                raise ValueError(f"Page changed during export: {page['id']}")
            pdf.setFillColorRGB(1, 1, 1)
            pdf.rect(0, 0, *size, fill=1, stroke=0)
            with Image.open(path) as image:
                image.load()
                pdf.drawImage(ImageReader(image), *page["placement_pt"], mask="auto")
            if page["chapter"]:
                key = f"chapter-{index}"
                pdf.bookmarkPage(key)
                pdf.addOutlineEntry(page["chapter"], key, level=0)
            pdf.showPage()
        pdf.save()
        with temporary.open("rb") as stream:
            reader = PdfReader(stream)
            if len(reader.pages) != len(pages):
                raise ValueError("Exported page count mismatch")
            for page in reader.pages:
                if any(abs(actual - expected) > 0.05 for actual, expected in zip((float(page.mediabox.width), float(page.mediabox.height)), size)):
                    raise ValueError("Exported page dimensions mismatch")
            expected = "/R2L" if data.get("reading_direction", "ltr") == "rtl" else "/L2R"
            if reader.trailer["/Root"]["/ViewerPreferences"]["/Direction"] != expected:
                raise ValueError("Exported reading direction mismatch")
        report = {"structural_export": "pass", "pdf": str(output), "pdf_sha256": sha256(temporary),
                  "source_manifest": str(manifest), "manifest_sha256": sha256(manifest),
                  "page_count": len(pages), "page_size_pt": list(size),
                  "reading_direction": data.get("reading_direction", "ltr"), "pages": pages,
                  "warnings": warnings, "searchable_dialogue": False,
                  "source_coverage": "unverified", "artwork_review": "unverified",
                  "lettering_review": "unverified", "rendered_pdf_review": "unverified"}
        temporary.replace(output)
        temporary = None
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return report
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        report = assemble(args.manifest, args.output, args.overwrite)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    print(json.dumps({"pdf": report["pdf"], "pages": report["page_count"], "warnings": report["warnings"]}))


if __name__ == "__main__":
    main()
