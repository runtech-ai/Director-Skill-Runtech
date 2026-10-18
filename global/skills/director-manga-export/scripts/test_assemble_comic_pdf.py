"""Offline exporter checks using synthetic page fixtures, not comic artwork."""

import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from pypdf import PdfReader

from assemble_comic_pdf import assemble


class ComicExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        Image.new("RGB", (300, 400), "red").save(self.root / "a.png")
        Image.new("RGB", (300, 400), "blue").save(self.root / "z.png")
        self.manifest = self.root / "pages.json"
        self.output = self.root / "book.pdf"
        self.data = {"format": "director-comic-pages", "version": 1, "title": "Fixture",
                     "reading_direction": "rtl", "page_size_mm": [76.2, 101.6],
                     "minimum_dpi": 75, "target_dpi": 300,
                     "pages": [{"id": "P1", "image": "z.png", "chapter": "Opening"},
                               {"id": "P2", "image": "a.png"}]}

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def test_manifest_order_direction_pixels_and_review_status(self):
        self.write()
        report = assemble(self.manifest, self.output)
        reader = PdfReader(self.output)
        self.assertEqual(len(reader.pages), 2)
        self.assertEqual(reader.trailer["/Root"]["/ViewerPreferences"]["/Direction"], "/R2L")
        self.assertAlmostEqual(float(reader.pages[0].mediabox.width), 216, places=3)
        self.assertEqual(reader.outline[0].title, "Opening")
        self.assertEqual(list(reader.pages[0].images)[0].image.getpixel((0, 0)), (0, 0, 255))
        self.assertEqual(list(reader.pages[1].images)[0].image.getpixel((0, 0)), (255, 0, 0))
        self.assertEqual(report["rendered_pdf_review"], "unverified")
        self.assertFalse(report["searchable_dialogue"])
        self.assertEqual(len(report["warnings"]), 2)
        with self.assertRaisesRegex(ValueError, "already exists"):
            assemble(self.manifest, self.output)

    def test_aspect_mismatch_then_contain_without_crop(self):
        self.data["page_size_mm"] = [100, 100]
        self.write()
        with self.assertRaisesRegex(ValueError, "aspect mismatch"):
            assemble(self.manifest, self.output)
        self.assertFalse(self.output.exists())
        self.data["fit"] = "contain"
        self.write()
        report = assemble(self.manifest, self.output)
        x, y, width, height = report["pages"][0]["placement_pt"]
        self.assertGreater(x, 0)
        self.assertAlmostEqual(y, 0)
        self.assertAlmostEqual(width / height, 0.75)
        self.assertAlmostEqual(height, 100 * 72 / 25.4)

    def test_missing_page_cannot_replace_existing_pdf(self):
        self.write()
        assemble(self.manifest, self.output)
        original = self.output.read_bytes()
        self.data["pages"][1]["image"] = "missing.png"
        self.write()
        with self.assertRaises(FileNotFoundError):
            assemble(self.manifest, self.output, overwrite=True)
        self.assertEqual(self.output.read_bytes(), original)

    def test_duplicate_ids_and_low_resolution_rejected(self):
        self.data["pages"][1]["id"] = "P1"
        self.write()
        with self.assertRaisesRegex(ValueError, "unique"):
            assemble(self.manifest, self.output)
        self.data["pages"][1]["id"] = "P2"
        self.data["minimum_dpi"] = 200
        self.write()
        with self.assertRaisesRegex(ValueError, "below minimum"):
            assemble(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_bad_geometry_and_input_collision_rejected(self):
        self.data["page_size_mm"] = [float("nan"), 100]
        self.write()
        with self.assertRaisesRegex(ValueError, "Invalid"):
            assemble(self.manifest, self.output)
        self.data["page_size_mm"] = [76.2, 101.6]
        self.data["margin_mm"] = 100
        self.write()
        with self.assertRaisesRegex(ValueError, "no page area"):
            assemble(self.manifest, self.output)
        self.data["margin_mm"] = 0
        self.manifest = self.root / "book.report.json"
        self.write()
        with self.assertRaisesRegex(ValueError, "overwrite an input"):
            assemble(self.manifest, self.output, overwrite=True)


if __name__ == "__main__":
    unittest.main()
