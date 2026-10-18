# Lettering and PDF production

## Compose at the final reading size

Use the requested trim size. If unspecified, A5 portrait (148 x 210 mm) is a practical starting PDF size, not a publisher specification. Plan margins/gutters into the page design. For screen PDFs, avoid tiny balloons that only read at high zoom. For print, obtain the actual printer's bleed, safe-area, color-profile and binding requirements before claiming print readiness; a screen PDF is not automatically PDF/X or a press-ready file.

Create text-free comic art with space for balloons. Typeset exact dialogue, captions and sound effects separately in a page-layout/vector tool, SVG/HTML with a PDF renderer, or a PDF library. Use fonts that actually contain the source language's glyphs and a shaping engine that supports the script. Preserve text direction within balloons independently from panel reading direction. Do not replace unsupported glyphs with boxes, transliterate or switch languages silently. Check shaping, line breaks and punctuation visually; extracted text alone cannot prove correct lettering.

Use generous balloon padding, clear tails and a consistent hierarchy. Text must not cover the key action, faces, hands, mechanism evidence or page gutters. Split long lines across balloons at natural phrases while retaining their exact concatenated text. Render/read at the intended physical or screen size. Retain editable lettering and its line-ID mapping. Image-generated lettering is acceptable only after every word/glyph and placement passes the same checks; prefer deterministic typesetting for exact dialogue.

## Choose the export route

- **Vector lettering:** place accepted art and editable text into a document; export with embedded, licensed fonts and usable text encoding. Prefer this when searchable/selectable text or accessibility is requested. Verify actual text extraction, reading order and font embedding. Do not claim a tagged/accessible PDF without separate checks.
- **Flattened pages:** render each fully composed and lettered page to a PNG (JPEG is supported, but avoid lossy artifacts on linework). Use the bundled assembler below. This produces an image-based PDF; its metadata and bookmarks do not make dialogue searchable. Keep the editable lettering alongside it.

Resolve available runtime dependencies rather than hardcoding machine paths. In Codex desktop, `load_workspace_dependencies` can locate Python, ReportLab, Pillow, pypdf and Poppler. Otherwise use installed equivalents. Follow an available PDF skill's artifact-start/render requirements in its own environment; do not invent a missing host command. If the runtime or renderer is unavailable, preserve the plan/art and report the exact missing capability instead of claiming a verified PDF.

## Bundled assembler

Read [assemble_comic_pdf.py](../scripts/assemble_comic_pdf.py). It requires Python 3.10+, Pillow, ReportLab and pypdf. Run with the skill's actual directory:

```bash
python3 scripts/assemble_comic_pdf.py /absolute/path/comic-export/page-manifest.json --output /absolute/path/comic-export/output/book.pdf
```

The helper consumes **already composed and lettered page images**, not Director ZIPs, panel prompts or unlettered individual shots. It uses the explicit page array order; never rely on filename sorting. Relative image paths resolve from the manifest's directory. Image bytes are hashed into the report. Existing PDF/report outputs are protected unless `--overwrite` is explicitly passed for an authorized revision.

Example internal export manifest (not an importer record):

```json
{
  "format": "director-comic-pages",
  "version": 1,
  "title": "The Last Signal",
  "reading_direction": "rtl",
  "page_size_mm": [148, 210],
  "margin_mm": 0,
  "fit": "strict",
  "target_dpi": 300,
  "minimum_dpi": 150,
  "pages": [
    {"id": "P001", "image": "pages/P001.png", "chapter": "Chapter 1"},
    {"id": "P002", "image": "pages/P002.png"}
  ]
}
```

These DPI values are adjustable workflow defaults. `minimum_dpi` rejects inputs below the chosen floor; `target_dpi` reports lower-than-target pages without pretending that changing metadata adds detail. Compute effective DPI from pixels and the actual placed dimensions. A print request may need a higher floor and separate printer-specific preflight.

`fit: strict` rejects a page-image aspect ratio more than 1% away from the available page area. `fit: contain` preserves all artwork with white padding; neither mode stretches or crops. `margin_mm` is added outside the existing page image, so leave it at zero when margins are already designed into the image. Chapter labels on page entries create bookmarks at those pages. Right-to-left sets a viewer preference but does not reorder pages or mirror images. The helper reopens its temporary PDF, verifies page count/dimensions/direction, and replaces the output only after structural validation.

For double-page spreads, author a separate spread plan and use a suitable layout exporter; do not force the helper's uniform page size to cut key artwork across a binding. Single-page PDFs with deliberate reveal order are the default.

## Final verification and handoff

Render **all pages** from the final PDF with an available renderer such as Poppler:

```bash
pdftoppm -r 120 -png /absolute/path/book.pdf /absolute/path/review/page
```

Inspect bounded page batches at readable scale. Compare the final lettering against the line ledger and inspect source fidelity, identity, prop states, gutters, clipping, chapter starts, page sequence and legibility. Check dense dialogue and dark/screentone areas at higher zoom. Inspect decoded pixel dimensions and effective DPI; a requested generation size is not proof of delivery resolution. Keep extracted text/OCR as corroboration, not a substitute for visual reading.

The assembler's report proves only structural export checks. Add source coverage, art review, lettering and final rendered-PDF review separately to `validation.json` with pass/fail/unknown and evidence paths. If incomplete, label the export draft and list the missing scope; do not mark a partial book complete. Deliver the final PDF and keep editable sources for repairs. No video generation or live movie mutation is needed for comic export.
