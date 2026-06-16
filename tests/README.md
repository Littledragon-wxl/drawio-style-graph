# Tests — drawio-style-graph

## Quick Start

```bash
# Run all automated tests
python3 tests/test_scripts.py

# Fast tests only (skip autolayout which needs Graphviz)
python3 tests/test_scripts.py --quick

# Verbose output
python3 tests/test_scripts.py --verbose

# Style mapping validation
python3 tests/test_styles.py

# Style mapping with full report
python3 tests/test_styles.py --report
```

## Test Structure

```
tests/
├── README.md              ← this file
├── test_scripts.py        ← automated tests for all 11 scripts + data + styles
├── test_styles.py         ← style mapping validation (8 styles × token coverage)
└── fixtures/
    ├── valid.drawio        ← well-formed .drawio with shapes + edges
    ├── invalid.drawio      ← has dangling edge, duplicate id, self-closing edge
    └── simple-graph.json   ← graph JSON for autolayout tests
```

## Test Coverage

### `test_scripts.py` — Automated Script Tests (30+ test cases)

| Test Class | Tests | What it checks |
|-----------|-------|----------------|
| `TestShapesearch` | 5 | Index loading, keyword search, JSON output, error handling |
| `TestAiicons` | 5 | Brand listing, OpenAI/Claude lookup, 6 brands spot-check, error handling |
| `TestValidate` | 3 | Valid file passes, invalid file flagged, nonexistent file error |
| `TestRepairPng` | 2 | Corrupted PNG repair, valid PNG no-op |
| `TestEncodeDrawioUrl` | 3 | Viewer URL, editor URL (--edit), nonexistent file |
| `TestAutolayout` | 2 | JSON → .drawio, JSON validation |
| `TestStyleReferences` | 4 | File existence, color palette, role definitions, complete templates |
| `TestIntegration` | 2 | End-to-end: generate + validate, hex color validity |
| `TestDataFiles` | 3 | shape-index.json.gz, lobe-icons.json, notice file |
| `TestPresets` | 2 | Built-in presets valid JSON, schema valid JSON |

### `test_styles.py` — Style Mapping Validation

Checks all 8 style reference files for:
- Required role definitions (7 roles minimum)
- Valid hex color values
- Typography settings (fontFamily, fontSize, fontColor)
- Shape preferences (rounded, strokeWidth)
- Edge style base
- Complete vertex style templates
- Canvas background (for dark styles)

## Prerequisites

- Python 3.8+
- Graphviz (`dot`) — optional, needed only for autolayout tests
  - `brew install graphviz` (macOS)
  - `sudo apt install graphviz` (Linux)
  - Skip with `--quick` flag

## Adding New Tests

1. Add test fixtures to `tests/fixtures/`
2. Add test methods to `test_scripts.py` (for script tests) or
   `test_styles.py` (for style validation)
3. Follow the existing pattern: small, focused test methods with descriptive names
