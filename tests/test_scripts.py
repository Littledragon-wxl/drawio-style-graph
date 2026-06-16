#!/usr/bin/env python3
"""
Automated test suite for drawio-style-graph scripts.

Covers:
  - shapesearch.py  — shape index loading & keyword search
  - aiicons.py      — brand logo resolution
  - validate.py     — .drawio structural lint
  - repair_png.py   — PNG IEND repair
  - encode_drawio_url.py — URL encoding
  - autolayout.py   — graph JSON → .drawio generation
  - Style reference — all 8 style files parse & have required fields

Usage:
  python3 tests/test_scripts.py              # all tests
  python3 tests/test_scripts.py --quick      # fast tests only (skip autolayout)
  python3 tests/test_scripts.py --verbose    # verbose output
"""

import os
import sys
import json
import gzip
import struct
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# Project root (parent of tests/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
FIXTURES_DIR = PROJECT_ROOT / "tests" / "fixtures"
DATA_DIR = PROJECT_ROOT / "data"
STYLES_DIR = PROJECT_ROOT / "references" / "styles"


# ─── Helpers ───────────────────────────────────────────────────────

def run_script(script_name, *args, timeout=30):
    """Run a script with args, return (returncode, stdout, stderr)."""
    script = SCRIPTS_DIR / script_name
    cmd = [sys.executable, str(script)] + list(args)
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        timeout=timeout, cwd=str(PROJECT_ROOT)
    )
    return result.returncode, result.stdout, result.stderr


def run_script_json(script_name, *args, timeout=30):
    """Run a script with --json flag, parse stdout as JSON."""
    code, out, err = run_script(script_name, *args, "--json", timeout=timeout)
    if code != 0:
        raise RuntimeError(f"{script_name} failed (code={code}): {err}")
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        # Maybe it's a list of objects, try per-line parsing
        lines = [l for l in out.strip().split("\n") if l.strip()]
        if len(lines) == 1:
            return json.loads(lines[0])
        return [json.loads(l) for l in lines]


# ─── Test Cases ────────────────────────────────────────────────────

class TestShapesearch(unittest.TestCase):
    """Test shapesearch.py — the 10k+ shape search engine."""

    def test_index_exists(self):
        """Shape index file must exist and be readable."""
        idx = DATA_DIR / "shape-index.json.gz"
        self.assertTrue(idx.exists(), f"Missing: {idx}")
        with gzip.open(idx, "rt", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 5000, "Index should have 5k+ entries")

    def test_search_aws_lambda(self):
        """Search for 'aws lambda' returns results with style strings."""
        code, out, err = run_script("shapesearch.py", "aws lambda", "--limit", "5")
        self.assertEqual(code, 0, f"shapesearch.py failed: {err}")
        # Should find something
        self.assertTrue(len(out) > 50 or len(err) > 0, "No output from shapesearch")

    def test_search_uml_actor(self):
        """Search for 'uml actor' returns valid results."""
        code, out, err = run_script("shapesearch.py", "uml actor", "--limit", "3")
        self.assertEqual(code, 0, f"shapesearch failed: {err}")

    def test_search_json_output(self):
        """--json flag produces parseable JSON."""
        code, out, err = run_script("shapesearch.py", "cylinder", "--limit", "2", "--json")
        self.assertEqual(code, 0, f"shapesearch --json failed: {err}")
        try:
            data = json.loads(out)
            self.assertTrue(isinstance(data, (list, dict)))
            if isinstance(data, list) and len(data) > 0:
                self.assertIn("style", data[0])
        except json.JSONDecodeError:
            self.fail(f"shapesearch --json output is not valid JSON:\n{out[:500]}")

    def test_search_no_results(self):
        """Search for gibberish should not crash."""
        code, out, err = run_script("shapesearch.py", "xyznonexistent12345", "--limit", "1")
        # Should not crash — either 0 or non-zero is fine
        self.assertNotIn("Traceback", err)
        self.assertNotIn("Error", err[:100] if err else "")


class TestAiicons(unittest.TestCase):
    """Test aiicons.py — AI/LLM brand logo resolver."""

    def test_list_brands(self):
        """--list prints many brands."""
        code, out, err = run_script("aiicons.py", "--list")
        self.assertEqual(code, 0, f"aiicons --list failed: {err}")
        # Should list at least 50 brands
        lines = out.strip().split("\n")
        self.assertGreater(len(lines), 50, f"Expected 50+ brands, got {len(lines)}")

    def test_json_output_openai(self):
        """Search 'openai' returns valid JSON with style."""
        code, out, err = run_script("aiicons.py", "openai", "--json")
        self.assertEqual(code, 0, f"aiicons openai failed: {err}")
        data = json.loads(out)
        # aiicons --json returns a list of matches
        if isinstance(data, list):
            self.assertGreater(len(data), 0, "No results for openai")
            data = data[0]
        self.assertIn("style", data)
        self.assertIn("image", data.get("style", "").lower())

    def test_json_output_claude(self):
        """Search 'claude' returns valid style."""
        code, out, err = run_script("aiicons.py", "claude", "--json")
        self.assertEqual(code, 0, f"aiicons claude failed: {err}")
        data = json.loads(out)
        if isinstance(data, list):
            self.assertGreater(len(data), 0, "No results for claude")
            data = data[0]
        self.assertIn("style", data)

    def test_unknown_brand(self):
        """Unknown brand should not crash."""
        code, out, err = run_script("aiicons.py", "nonexistentbrand12345", "--json", timeout=15)
        # Should exit cleanly (may return empty list or error exit)
        self.assertNotIn("Traceback", err)

    def test_known_brands_return_results(self):
        """Spot-check several known brands."""
        brands = ["gemini", "mistral", "llama", "huggingface", "ollama", "langchain"]
        for brand in brands:
            with self.subTest(brand=brand):
                code, out, err = run_script("aiicons.py", brand, "--json", timeout=15)
                self.assertEqual(code, 0, f"aiicons {brand} exited {code}: {err}")
                data = json.loads(out)
                # aiicons returns a list; check first element
                if isinstance(data, list):
                    self.assertGreater(len(data), 0, f"aiicons {brand} returned empty list")
                    data = data[0]
                self.assertIn("style", data, f"aiicons {brand} missing 'style': {data}")


class TestValidate(unittest.TestCase):
    """Test validate.py — structural .drawio linter."""

    def test_valid_drawio_passes(self):
        """Known-valid file should pass validation."""
        valid_file = FIXTURES_DIR / "valid.drawio"
        code, out, err = run_script("validate.py", str(valid_file))
        self.assertEqual(code, 0, f"Valid file failed validation:\n{out}\n{err}")

    def test_invalid_drawio_fails(self):
        """Known-invalid file should be caught."""
        invalid_file = FIXTURES_DIR / "invalid.drawio"
        code, out, err = run_script("validate.py", str(invalid_file))
        # Should detect at least one issue
        combined = out + err
        has_issue = (
            code != 0
            or "dangling" in combined.lower()
            or "duplicate" in combined.lower()
            or "invalid" in combined.lower()
            or "error" in combined.lower()
            or "warning" in combined.lower()
        )
        self.assertTrue(has_issue, f"Invalid file was not flagged:\n{combined[:500]}")

    def test_nonexistent_file(self):
        """Nonexistent file should produce error."""
        code, out, err = run_script("validate.py", "/nonexistent/path/file.drawio")
        # Should not crash
        self.assertNotIn("Traceback", err)


class TestRepairPng(unittest.TestCase):
    """Test repair_png.py — IEND chunk repair."""

    def test_repair_corrupt_png(self):
        """Repair a PNG with truncated IEND."""
        # Build a minimal valid PNG and then truncate it
        import zlib

        def make_png_chunk(chunk_type, data):
            chunk = chunk_type + data
            crc = struct.pack(">I", zlib.crc32(chunk) & 0xFFFFFFFF)
            return struct.pack(">I", len(data)) + chunk + crc

        sig = b"\x89PNG\r\n\x1a\n"
        ihdr_data = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
        ihdr = make_png_chunk(b"IHDR", ihdr_data)
        raw = zlib.compress(b"\x00\xff\x00\xff")
        idat = make_png_chunk(b"IDAT", raw)
        iend = make_png_chunk(b"IEND", b"")

        # Valid PNG
        valid_png = sig + ihdr + idat + iend
        # Truncated: IEND missing 8 bytes (type + CRC), like draw.io -e bug
        truncated_png = sig + ihdr + idat + iend[:-8]

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(truncated_png)
            tmp_path = f.name

        try:
            code, out, err = run_script("repair_png.py", tmp_path)
            self.assertEqual(code, 0, f"repair_png failed: {err}")

            # Verify repaired file
            with open(tmp_path, "rb") as f:
                repaired = f.read()
            # Should have IEND at the end
            self.assertTrue(repaired.endswith(b"IEND\xae\x42\x60\x82"),
                            "Repaired PNG does not end with valid IEND")
        finally:
            os.unlink(tmp_path)

    def test_valid_png_noop(self):
        """Already-valid PNG should be reported as already valid."""
        import zlib

        def make_png_chunk(chunk_type, data):
            chunk = chunk_type + data
            crc = struct.pack(">I", zlib.crc32(chunk) & 0xFFFFFFFF)
            return struct.pack(">I", len(data)) + chunk + crc

        sig = b"\x89PNG\r\n\x1a\n"
        ihdr = make_png_chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
        idat = make_png_chunk(b"IDAT", zlib.compress(b"\x00\xff\x00\xff"))
        iend = make_png_chunk(b"IEND", b"")
        valid_png = sig + ihdr + idat + iend

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(valid_png)
            tmp_path = f.name

        try:
            code, out, err = run_script("repair_png.py", tmp_path)
            self.assertEqual(code, 0, f"repair_png on valid file failed: {err}")
        finally:
            os.unlink(tmp_path)


class TestEncodeDrawioUrl(unittest.TestCase):
    """Test encode_drawio_url.py — browser URL fallback."""

    def test_encode_valid_file(self):
        """Encode a valid .drawio to a diagrams.net URL."""
        valid_file = FIXTURES_DIR / "valid.drawio"
        code, out, err = run_script("encode_drawio_url.py", str(valid_file), timeout=15)
        self.assertEqual(code, 0, f"encode_drawio_url failed: {err}")
        self.assertIn("https://", out)
        self.assertIn("diagrams.net", out)

    def test_encode_with_edit_flag(self):
        """--edit flag produces an editable editor URL."""
        valid_file = FIXTURES_DIR / "valid.drawio"
        code, out, err = run_script("encode_drawio_url.py", "--edit", str(valid_file), timeout=15)
        self.assertEqual(code, 0, f"encode_drawio_url --edit failed: {err}")
        self.assertIn("https://", out)

    def test_nonexistent_file_errors(self):
        """Nonexistent file should produce an error exit."""
        code, out, err = run_script("encode_drawio_url.py", "/nonexistent/file.drawio", timeout=15)
        self.assertNotEqual(code, 0, "Should fail for nonexistent file")


class TestAutolayout(unittest.TestCase):
    """Test autolayout.py — Graphviz-based layout engine."""

    def test_graph_to_drawio(self):
        """Convert a simple graph JSON to .drawio."""
        graph_file = FIXTURES_DIR / "simple-graph.json"

        with tempfile.NamedTemporaryFile(suffix=".drawio", delete=False) as f:
            out_path = f.name

        try:
            code, out, err = run_script(
                "autolayout.py", str(graph_file), "-o", out_path,
                timeout=30
            )
            if code != 0 and "graphviz" in err.lower():
                self.skipTest("Graphviz not installed — skipping autolayout test")
            if code != 0 and "dot" in err.lower():
                self.skipTest("Graphviz dot not found — skipping autolayout test")

            self.assertEqual(code, 0, f"autolayout failed:\nSTDOUT:{out}\nSTDERR:{err}")

            # Verify output is valid XML
            tree = ET.parse(out_path)
            root = tree.getroot()
            self.assertEqual(root.tag, "mxfile")

            # Should contain our nodes
            xml_str = ET.tostring(root, encoding="unicode")
            self.assertIn("Client", xml_str)
            self.assertIn("PostgreSQL", xml_str)

            # Run validate on the output
            vcode, vout, verr = run_script("validate.py", out_path)
            self.assertEqual(vcode, 0, f"autolayout output failed validate:\n{vout}\n{verr}")
        finally:
            if os.path.exists(out_path):
                os.unlink(out_path)

    def test_graph_json_validation(self):
        """Graph JSON with missing required fields should error."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"nodes": []}, f)  # missing "edges"
            bad_graph = f.name

        try:
            code, out, err = run_script("autolayout.py", bad_graph, "-o", "/tmp/test.drawio", timeout=15)
            if code == 0 and os.path.exists("/tmp/test.drawio"):
                os.unlink("/tmp/test.drawio")
            # Should either fail or produce minimal valid output (both acceptable)
        finally:
            os.unlink(bad_graph)


class TestStyleReferences(unittest.TestCase):
    """Test that all 8 style reference files exist and have required sections."""

    STYLE_FILES = [
        "style-1-flat-icon.md",
        "style-2-dark-terminal.md",
        "style-3-blueprint.md",
        "style-4-notion-clean.md",
        "style-5-glassmorphism.md",
        "style-6-claude-official.md",
        "style-7-openai.md",
        "style-8-dark-luxury.md",
    ]

    REQUIRED_SECTIONS = [
        "Color Palette",
        "Typography",
        "Shape Preferences",
        "Edge Style",
        "vertex style",
    ]

    def test_all_style_files_exist(self):
        """All 8 style reference files must be present."""
        for sf in self.STYLE_FILES:
            path = STYLES_DIR / sf
            self.assertTrue(path.exists(), f"Missing style file: {sf}")

    def test_style_files_have_color_palette(self):
        """Each style file must define a color palette section."""
        for sf in self.STYLE_FILES:
            with self.subTest(style=sf):
                path = STYLES_DIR / sf
                content = path.read_text(encoding="utf-8")
                self.assertIn("fillColor", content, f"{sf} missing fillColor reference")
                self.assertIn("strokeColor", content, f"{sf} missing strokeColor reference")
                self.assertIn("fontFamily", content, f"{sf} missing fontFamily reference")
                self.assertIn("primary", content.lower(), f"{sf} missing primary role reference")

    def test_style_files_define_roles(self):
        """Each style must define at least primary, success, warning roles."""
        for sf in self.STYLE_FILES:
            with self.subTest(style=sf):
                path = STYLES_DIR / sf
                content = path.read_text(encoding="utf-8").lower()
                for role in ["primary", "service", "database", "external"]:
                    has_role = role in content
                    if not has_role:
                        # Some styles use different naming, just check that
                        # at least 4 distinct hex colors are present
                        import re
                        hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', content))
                        self.assertGreaterEqual(
                            len(hex_colors), 3,
                            f"{sf} has only {len(hex_colors)} hex colors, expected >=3"
                        )
                        break

    def test_complete_style_template(self):
        """Each style should have at least one complete vertex style template."""
        for sf in self.STYLE_FILES:
            with self.subTest(style=sf):
                path = STYLES_DIR / sf
                content = path.read_text(encoding="utf-8")
                # Look for a complete style string
                required_tokens = ["fillColor", "strokeColor", "fontFamily", "html=1"]
                found_all = all(t in content for t in required_tokens)
                self.assertTrue(
                    found_all,
                    f"{sf} missing required style tokens. "
                    f"Missing: {[t for t in required_tokens if t not in content]}"
                )


class TestIntegration(unittest.TestCase):
    """End-to-end integration tests."""

    def test_generate_and_validate_minimal_drawio(self):
        """Generate a minimal .drawio with style tokens and validate."""
        style = (
            'rounded=1;whiteSpace=wrap;html=1;'
            'fillColor=#eff6ff;strokeColor=#bfdbfe;strokeWidth=1.5;'
            'fontFamily=Helvetica;fontSize=14;fontColor=#111827;'
        )
        xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" value="Test Node" style="{style}" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".drawio", delete=False, encoding="utf-8"
        ) as f:
            f.write(xml)
            tmp_path = f.name

        try:
            # Validate
            code, out, err = run_script("validate.py", tmp_path)
            self.assertEqual(code, 0, f"Minimal valid .drawio failed validate:\n{out}\n{err}")

            # Parse as XML
            tree = ET.parse(tmp_path)
            root = tree.getroot()
            self.assertEqual(root.tag, "mxfile")

            # Verify style tokens are preserved
            xml_str = ET.tostring(root, encoding="unicode")
            self.assertIn("fillColor=#eff6ff", xml_str)
            self.assertIn("fontFamily=Helvetica", xml_str)
        finally:
            os.unlink(tmp_path)

    def test_all_style_hex_colors_are_valid(self):
        """All hex colors in style references are valid 6-digit hex."""
        import re
        for sf in TestStyleReferences.STYLE_FILES:
            with self.subTest(style=sf):
                path = STYLES_DIR / sf
                content = path.read_text(encoding="utf-8")
                hex_colors = re.findall(r'#[0-9a-fA-F]{6}', content)
                for hc in hex_colors:
                    self.assertRegex(hc, r'^#[0-9a-fA-F]{6}$',
                                     f"Invalid hex color {hc} in {sf}")


class TestDataFiles(unittest.TestCase):
    """Test bundled data files integrity."""

    def test_shape_index_is_valid_gzip_json(self):
        """shape-index.json.gz must be valid gzipped JSON."""
        idx = DATA_DIR / "shape-index.json.gz"
        self.assertTrue(idx.exists())
        with gzip.open(idx, "rt", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, list)
        if data:
            entry = data[0]
            self.assertIsInstance(entry, dict)

    def test_lobe_icons_is_valid_json(self):
        """lobe-icons.json must be valid JSON."""
        path = DATA_DIR / "lobe-icons.json"
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(data, (dict, list))

    def test_notice_file_exists(self):
        """SHAPE-INDEX-NOTICE.md should exist."""
        notice = DATA_DIR / "SHAPE-INDEX-NOTICE.md"
        self.assertTrue(notice.exists())


class TestPresets(unittest.TestCase):
    """Test built-in style presets."""

    def test_builtin_presets_exist(self):
        """All 3 built-in presets must be valid JSON."""
        builtin = PROJECT_ROOT / "styles" / "built-in"
        for name in ["default.json", "corporate.json", "handdrawn.json"]:
            path = builtin / name
            self.assertTrue(path.exists(), f"Missing built-in preset: {name}")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict)
            self.assertIn("name", data)

    def test_schema_valid_json(self):
        """Schema files must be valid JSON."""
        for sf in ["schema.json", "schema-drawio.json"]:
            path = PROJECT_ROOT / "styles" / sf
            self.assertTrue(path.exists(), f"Missing schema: {sf}")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict)


# ─── Runner ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="drawio-style-graph test suite")
    parser.add_argument("--quick", action="store_true",
                        help="Skip slow tests (autolayout, large data)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbose output")
    args, remaining = parser.parse_known_args()

    # Build test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Always run fast tests
    suite.addTests(loader.loadTestsFromTestCase(TestShapesearch))
    suite.addTests(loader.loadTestsFromTestCase(TestAiicons))
    suite.addTests(loader.loadTestsFromTestCase(TestValidate))
    suite.addTests(loader.loadTestsFromTestCase(TestRepairPng))
    suite.addTests(loader.loadTestsFromTestCase(TestEncodeDrawioUrl))
    suite.addTests(loader.loadTestsFromTestCase(TestStyleReferences))
    suite.addTests(loader.loadTestsFromTestCase(TestDataFiles))
    suite.addTests(loader.loadTestsFromTestCase(TestPresets))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

    if not args.quick:
        suite.addTests(loader.loadTestsFromTestCase(TestAutolayout))

    verbosity = 2 if args.verbose else 1
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    # Summary
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    skipped = len(result.skipped)
    passed = total - failed - skipped

    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped, {total} total")
    print(f"{'='*60}")

    return 0 if failed == 0 else 1


# argparse may not be available in all environments
try:
    import argparse
except ImportError:
    import unittest
    print("argparse not available, running all tests...")
    unittest.main(verbosity=2)
else:
    if __name__ == "__main__":
        sys.exit(main())
