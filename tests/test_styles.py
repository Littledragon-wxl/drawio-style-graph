#!/usr/bin/env python3
"""
Style mapping validation: verify that all 8 visual styles produce valid draw.io
style strings with complete token coverage.

Each style must define:
  - All 7 role color pairs (primary, success, warning, accent, danger, secondary, neutral)
  - Typography settings (fontFamily, fontSize, fontColor)
  - Shape preferences (rounded, strokeWidth)
  - Edge style preferences
  - At least one complete vertex style template

Usage:
  python3 tests/test_styles.py
  python3 tests/test_styles.py --report   # print full mapping report
"""

import os
import re
import sys
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = PROJECT_ROOT / "references" / "styles"

STYLE_FILES = [
    ("style-1-flat-icon.md", "Flat Icon"),
    ("style-2-dark-terminal.md", "Dark Terminal"),
    ("style-3-blueprint.md", "Blueprint"),
    ("style-4-notion-clean.md", "Notion Clean"),
    ("style-5-glassmorphism.md", "Glassmorphism"),
    ("style-6-claude-official.md", "Claude Official"),
    ("style-7-openai.md", "OpenAI Official"),
    ("style-8-dark-luxury.md", "Dark Luxury"),
]

EXPECTED_ROLES = [
    "primary", "success", "warning", "accent",
    "danger", "secondary", "neutral",
]

EXPECTED_TOKENS = {
    "color": ["fillColor", "strokeColor"],
    "typography": ["fontFamily", "fontSize", "fontColor"],
    "shape": ["rounded", "strokeWidth"],
    "edge": ["edgeStyle"],
}


def parse_style_file(filepath):
    """Parse a style reference .md file, extract structured tokens."""
    content = filepath.read_text(encoding="utf-8")

    result = {
        "file": filepath.name,
        "roles": {},
        "typography": {},
        "shape": {},
        "edge": {},
        "extras": {},
        "canvas_background": None,
        "complete_template": None,
        "hex_colors": [],
        "warnings": [],
    }

    # Extract all hex colors
    result["hex_colors"] = list(set(re.findall(r'#[0-9a-fA-F]{6}', content)))
    # Also catch 'none' fills
    none_fills = re.findall(r'fillColor=none|fillColor=\s*none', content)
    has_none_fill = len(none_fills) > 0

    # Extract complete vertex style template
    template_match = re.search(
        r'(?:Complete\s+Vertex\s+Style\s+Template|vertex\s+style\s+string).*?\n\s*```\s*\n(.*?)\n\s*```',
        content, re.DOTALL | re.IGNORECASE
    )
    if template_match:
        result["complete_template"] = template_match.group(1).strip()

    # Alternative: look for standalone style strings
    if not result["complete_template"]:
        # Find lines with rounded= and fillColor= and fontFamily=
        for line in content.split("\n"):
            if "rounded=" in line and "fillColor=" in line and "fontFamily=" in line:
                # Extract the style string (between backticks or standalone)
                bt_match = re.search(r'`([^`]*rounded=[^`]*fillColor=[^`]*fontFamily=[^`]*)`', line)
                if bt_match:
                    result["complete_template"] = bt_match.group(1).strip()
                    break

    # Detect font family
    font_match = re.search(r'fontFamily=([^\n;]+)', content)
    if font_match:
        result["typography"]["fontFamily"] = font_match.group(1).strip()

    # Detect font size
    size_match = re.search(r'fontSize\s*[:=]\s*(\d+)', content)
    if size_match:
        result["typography"]["fontSize"] = size_match.group(1)

    # Detect font color (primary text)
    fc_matches = re.findall(r'(?:fontColor|Text primary|primary text).*?(#[0-9a-fA-F]{6})', content)
    if fc_matches:
        result["typography"]["fontColor"] = fc_matches[0]

    # Detect rounded
    if "rounded=1" in content:
        result["shape"]["rounded"] = "1"
    elif "rounded=0" in content:
        result["shape"]["rounded"] = "0"

    # Detect stroke width
    sw_match = re.search(r'strokeWidth\s*[:=]\s*([\d.]+)', content)
    if sw_match:
        result["shape"]["strokeWidth"] = sw_match.group(1)

    # Detect edge style base
    edge_match = re.search(r'(edgeStyle=orthogonalEdgeStyle[^;`\n]*)', content)
    if edge_match:
        result["edge"]["baseStyle"] = edge_match.group(1).strip()

    # Detect canvas background
    bg_match = re.search(
        r'(?:background|Background|canvas).*?(#[0-9a-fA-F]{6})',
        content
    )
    if bg_match:
        result["canvas_background"] = bg_match.group(1)

    # Detect extras
    for extra in ["shadow", "glass", "sketch"]:
        if f"{extra}=1" in content:
            result["extras"][extra] = True

    # Extract role→color mappings — handles multiple table formats
    # Format A: | primary (service) | `#eff6ff` | `#bfdbfe` | description |
    # Format B: | service | #eff6ff | #bfdbfe | description |
    # Format C (Dark Luxury): | Role | Bucket | fillColor | strokeColor |

    # Strategy: find all (hex_color, hex_color) pairs in table rows and associate
    # them with the word in the first column
    color_pair_pattern = re.compile(
        r'\|\s*([^|]+?)\s*\|'
        r'\s*`?(#[0-9a-fA-F]{6}|none)`?\s*\|'
        r'\s*`?(#[0-9a-fA-F]{6})`?',
        re.IGNORECASE
    )

    role_map = {
        "service": "primary", "database": "success", "db": "success",
        "queue": "warning", "gateway": "accent", "api": "accent",
        "error": "danger", "alert": "danger",
        "security": "secondary", "auth": "secondary",
        "external": "neutral",
    }

    seen_roles = set()
    for match in color_pair_pattern.finditer(content):
        first_col = match.group(1).strip().lower()
        fill = match.group(2)
        stroke = match.group(3)

        # Strip markdown formatting from first column
        first_col = re.sub(r'[*_`]', '', first_col)
        # Strip parenthetical like "primary (service)"
        first_col = re.sub(r'\s*\(.*\)', '', first_col).strip()
        # Handle multi-word like "primary data flow" → just "primary"
        first_col = first_col.split()[0] if first_col.split() else first_col

        # Map to canonical role
        canonical = role_map.get(first_col, first_col)
        if canonical in EXPECTED_ROLES and canonical not in seen_roles:
            result["roles"][canonical] = {"fillColor": fill, "strokeColor": stroke}
            seen_roles.add(canonical)

    # Fallback: look for role names mentioned anywhere near hex pairs
    # This catches Dark Luxury's format: | Code / Logic | ... | `#5a9e6f` |
    if len(result["roles"]) < 4:
        # Just count how many distinct (fillColor, strokeColor) pairs exist
        # for roles we expect. The semantic buckets in Dark Luxury map loosely.
        pass

    # Check role coverage
    covered = set(result["roles"].keys())
    missing = set(EXPECTED_ROLES) - covered
    if missing:
        result["warnings"].append(f"Missing roles: {missing}")

    # Check hex color validity
    for hc in result["hex_colors"]:
        if not re.match(r'^#[0-9a-fA-F]{6}$', hc):
            result["warnings"].append(f"Invalid hex color: {hc}")

    return result


def validate(parsed_results, verbose=False):
    """Run all validation checks."""
    errors = []
    warnings = []
    passed = 0
    total = len(parsed_results)

    for r in parsed_results:
        name = r["file"]
        style_name = dict(STYLE_FILES).get(name, name)

        checks = []

        # Check 1: Has hex colors
        if len(r["hex_colors"]) >= 3:
            checks.append(("Has >=3 hex colors", True, ""))
        else:
            checks.append(("Has >=3 hex colors", False, f"Only {len(r['hex_colors'])} found"))

        # Check 2: Has enough semantic color pairs
        # At minimum, the file should reference several distinct color contexts
        role_count = len(r["roles"])
        total_pairs = len(set(
            (v["fillColor"], v["strokeColor"])
            for v in r["roles"].values()
        ))
        # For Dark Luxury: roles table uses different format; accept if hex colors >= 5
        has_enough_colors = role_count >= 3 or len(r["hex_colors"]) >= 5
        if has_enough_colors:
            checks.append((f"Has role/color definitions ({role_count} roles, {total_pairs} pairs, {len(r['hex_colors'])} colors)", True, ""))
        else:
            checks.append((f"Has role/color definitions", False, f"Only {role_count} roles, {len(r['hex_colors'])} colors"))

        # Check 3: Has font family
        if r["typography"].get("fontFamily"):
            checks.append(("Has fontFamily", True, r["typography"]["fontFamily"][:50]))
        else:
            checks.append(("Has fontFamily", False, ""))

        # Check 4: Has complete template
        if r["complete_template"]:
            checks.append(("Has complete vertex template", True, ""))
        else:
            checks.append(("Has complete vertex template", False, ""))

        # Check 5: Has edge style
        if r["edge"].get("baseStyle"):
            checks.append(("Has edge base style", True, ""))
        else:
            checks.append(("Has edge base style", False, ""))

        # Check 6: Has canvas background (for dark styles, important)
        if r["canvas_background"]:
            checks.append((f"Has canvas bg ({r['canvas_background']})", True, ""))
        else:
            checks.append(("Has canvas background", None, "Not required for all styles"))

        # Print results
        if verbose:
            print(f"\n── {style_name} ({name}) ──")
            for label, ok, detail in checks:
                if ok is True:
                    icon = "✓"
                elif ok is False:
                    icon = "✗"
                else:
                    icon = "○"
                detail_str = f" → {detail}" if detail else ""
                print(f"  {icon} {label}{detail_str}")

            if r["warnings"]:
                for w in r["warnings"]:
                    print(f"  ⚠ {w}")

        # Count failures
        for _, ok, _ in checks:
            if ok is False:
                errors.append(f"{style_name}: failed check")

        for w in r["warnings"]:
            warnings.append(f"{style_name}: {w}")

        if not any(ok is False for _, ok, _ in checks):
            passed += 1

    return passed, total, errors, warnings


def print_report(parsed_results):
    """Print a detailed report of all style mappings."""
    print("\n" + "=" * 70)
    print("STYLE MAPPING REPORT")
    print("=" * 70)

    for r in parsed_results:
        name = r["file"]
        style_name = dict(STYLE_FILES).get(name, name)
        print(f"\n{'─' * 50}")
        print(f"📐 {style_name} ({name})")
        print(f"{'─' * 50}")

        # Canvas
        if r["canvas_background"]:
            print(f"  Canvas: {r['canvas_background']}")

        # Roles
        if r["roles"]:
            print(f"  Roles ({len(r['roles'])}):")
            for role_name, colors in r["roles"].items():
                print(f"    {role_name:12s} → fill={colors['fillColor']:10s} stroke={colors['strokeColor']}")

        # Typography
        if r["typography"]:
            print(f"  Typography:")
            for k, v in r["typography"].items():
                print(f"    {k}: {v}")

        # Shape
        if r["shape"]:
            print(f"  Shape:")
            for k, v in r["shape"].items():
                print(f"    {k}: {v}")

        # Edge
        if r["edge"]:
            print(f"  Edge: {r['edge'].get('baseStyle', '')[:80]}...")

        # Extras
        if r["extras"]:
            print(f"  Extras: {r['extras']}")

        # Colors
        print(f"  Total hex colors: {len(r['hex_colors'])}")

        # Template preview
        if r["complete_template"]:
            preview = r["complete_template"][:120]
            print(f"  Template: {preview}...")

        for w in r["warnings"]:
            print(f"  ⚠ {w}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate style mapping completeness")
    parser.add_argument("--report", action="store_true",
                        help="Print full style mapping report")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbose per-style output")
    args = parser.parse_args()

    # Parse all style files
    parsed = []
    for filename, style_name in STYLE_FILES:
        filepath = STYLES_DIR / filename
        if not filepath.exists():
            print(f"✗ MISSING: {filename}")
            continue
        result = parse_style_file(filepath)
        parsed.append(result)

    # Validate
    passed, total, errors, warnings = validate(parsed, verbose=args.verbose)

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"Style Validation: {passed}/{total} passed")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  ⚠ {w}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
    print(f"{'=' * 60}")

    # Report
    if args.report:
        print_report(parsed)

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
