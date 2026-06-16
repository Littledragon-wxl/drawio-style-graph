# Test Plan — drawio-style-graph v1.0.0

## Overview

This document describes the complete testing strategy for `drawio-style-graph`,
a self-contained VS Code skill that generates `.drawio` diagrams with 8
professional visual styles.

## Test Pyramid

```
         ┌──────────┐
         │  E2E     │  ← Real drawio CLI export + vision self-check
         │  5 tests │
        ┌┴──────────┴┐
        │ Integration │  ← .drawio generation + validate + style application
        │  12 tests   │
       ┌┴──────────────┴┐
       │   Unit Tests    │  ← Script-level tests (shapesearch, aiicons, etc.)
       │   25+ tests     │
      └──────────────────┘
```

---

## Layer 1: Unit Tests (Automated)

### 1.1 Script Tests (`tests/test_scripts.py`)

These verify every bundled Python script works correctly in isolation.

#### shapesearch.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-SS-01 | Index exists and loads | `data/shape-index.json.gz` | `json.loads()` succeeds, >5000 entries |
| U-SS-02 | Search "aws lambda" | `shapesearch.py aws lambda --limit 5` | Returns results with `style=` strings |
| U-SS-03 | Search "uml actor" | `shapesearch.py uml actor --limit 3` | Exit code 0 |
| U-SS-04 | JSON output mode | `--json` flag | Parseable JSON with `style` key |
| U-SS-05 | No results query | `shapesearch.py xyznonexistent` | No crash, no traceback |

#### aiicons.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-AI-01 | List all brands | `--list` | >50 brand names printed |
| U-AI-02 | OpenAI lookup | `openai --json` | JSON with `style` containing `image` |
| U-AI-03 | Claude lookup | `claude --json` | JSON with `style` key |
| U-AI-04 | Unknown brand | `nonexistent12345 --json` | Clean exit, no traceback |
| U-AI-05 | Gemini lookup | `gemini --json` | Valid style returned |
| U-AI-06 | Mistral lookup | `mistral --json` | Valid style returned |
| U-AI-07 | Llama lookup | `llama --json` | Valid style returned |
| U-AI-08 | HuggingFace lookup | `huggingface --json` | Valid style returned |
| U-AI-09 | Ollama lookup | `ollama --json` | Valid style returned |
| U-AI-10 | LangChain lookup | `langchain --json` | Valid style returned |

#### validate.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-VL-01 | Valid .drawio passes | `fixtures/valid.drawio` | Exit 0, no errors |
| U-VL-02 | Invalid .drawio detected | `fixtures/invalid.drawio` | Catches dangling edge / dup id / self-closing |
| U-VL-03 | Nonexistent file | `/nonexistent/path.drawio` | Clean error, no crash |

#### repair_png.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-RP-01 | Repair truncated IEND | PNG with 8 bytes missing from IEND | Repaired file ends with valid `IEND` chunk |
| U-RP-02 | Valid PNG no-op | Complete PNG with proper IEND | Exit 0, file unchanged |

#### encode_drawio_url.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-EU-01 | Viewer URL | `fixtures/valid.drawio` | Output contains `https://` and `diagrams.net` |
| U-EU-02 | Editor URL | `--edit fixtures/valid.drawio` | Output contains `https://` |
| U-EU-03 | Nonexistent file | `/nonexistent/file.drawio` | Exit != 0 |

#### autolayout.py

| ID | Test | Input | Expected |
|----|------|-------|----------|
| U-AL-01 | Graph → .drawio | `fixtures/simple-graph.json` | Valid `.drawio` XML with node labels preserved |
| U-AL-02 | Missing fields | JSON with only `nodes`, no `edges` | Does not crash |

---

### 1.2 Style Reference Tests (`tests/test_styles.py`)

| ID | Test | Expected |
|----|------|----------|
| U-ST-01 | All 8 files exist | `references/styles/style-N-*.md` present |
| U-ST-02 | Each defines roles | >=4 role-to-color mappings per style |
| U-ST-03 | Each has color palette | `fillColor` + `strokeColor` present |
| U-ST-04 | Each has typography | `fontFamily`, `fontSize`, `fontColor` |
| U-ST-05 | Each has shape prefs | `rounded=` present |
| U-ST-06 | Each has edge style | `edgeStyle=orthogonalEdgeStyle` present |
| U-ST-07 | Each has complete template | At least one full vertex style string |
| U-ST-08 | All hex colors valid | All match `#[0-9a-fA-F]{6}` |
| U-ST-09 | Dark styles have bg | Styles 2,3,5,8 define canvas background |

---

### 1.3 Data Integrity Tests

| ID | Test | Expected |
|----|------|----------|
| U-DI-01 | shape-index.json.gz is valid gzip JSON | `gzip.open()` + `json.load()` succeeds |
| U-DI-02 | lobe-icons.json is valid JSON | `json.load()` succeeds |
| U-DI-03 | SHAPE-INDEX-NOTICE.md exists | File present |

---

### 1.4 Preset Tests

| ID | Test | Expected |
|----|------|----------|
| U-PR-01 | default.json valid | Parseable JSON with `name` key |
| U-PR-02 | corporate.json valid | Parseable JSON with `name` key |
| U-PR-03 | handdrawn.json valid | Parseable JSON with `name` key |
| U-PR-04 | schema.json valid | Parseable JSON |
| U-PR-05 | schema-drawio.json valid | Parseable JSON |

---

## Layer 2: Integration Tests (Automated)

### 2.1 XML Generation + Validation

| ID | Test | Steps | Expected |
|----|------|-------|----------|
| I-XG-01 | Minimal .drawio with style tokens | Generate .drawio with Flat Icon style tokens, run validate.py | Passes validation, XML parseable |
| I-XG-02 | Style tokens preserved | Generate XML → parse → verify style attrs | `fillColor`, `fontFamily` etc intact |
| I-XG-03 | Multi-shape diagram | 3 shapes + 2 edges with styles | All render, edges connect |

### 2.2 Style Application

| ID | Test | Steps | Expected |
|----|------|-------|----------|
| I-SA-01 | Flat Icon → service node | Apply primary role colors | `fillColor=#eff6ff;strokeColor=#bfdbfe` |
| I-SA-02 | Dark Terminal → AI node | Apply primary + dark bg | `fillColor=#1e1b4b;strokeColor=#7c3aed` + `background=#0f0f1a` |
| I-SA-03 | Blueprint → external node | Apply neutral role | `fillColor=none;dashed=1;strokeColor=#48cae4` |
| I-SA-04 | Claude Official → all arrows | Apply consistent edge color | All edges `strokeColor=#5a5a5a` |

### 2.3 Diagram Type Presets

| ID | Test | Steps | Expected |
|----|------|-------|----------|
| I-DT-01 | ERD table style | Load `diagram-types.md` ERD preset | `shape=table;childLayout=tableLayout` in style |
| I-DT-02 | Sequence lifeline | Load Sequence preset | `shape=umlLifeline` in style |
| I-DT-03 | ML layer block | Load ML/DL preset | Tensor shape label with `&#xa;` |

---

## Layer 3: End-to-End Tests (Semi-Automated)

These require the draw.io desktop CLI. Skip gracefully if `drawio --version` fails.

### 3.1 Export Pipeline

| ID | Test | Steps | Expected |
|----|------|-------|----------|
| E-EP-01 | Preview PNG export | `drawio -x -f png --width 2000 -o out.png` | PNG file created, no `-e` |
| E-EP-02 | Final PNG with -e | `drawio -x -f png -e -s 2 -o out.drawio.png` | PNG with embedded XML |
| E-EP-03 | PNG repair after -e | `repair_png.py out.drawio.png` | PNG passes strict decoder |
| E-EP-04 | SVG export | `drawio -x -f svg -e -o out.svg` | Valid SVG created |
| E-EP-05 | PDF export | `drawio -x -f pdf -e -o out.pdf` | PDF created |

### 3.2 Browser Fallback

| ID | Test | Steps | Expected |
|----|------|-------|----------|
| E-BF-01 | Viewer URL | `encode_drawio_url.py diagram.drawio` | URL opens in browser without error |
| E-BF-02 | Editor URL | `--edit` flag | URL opens draw.io editor with diagram loaded |

---

## Layer 4: Manual Tests (Checklist)

### 4.1 Visual Quality

Run for each of the 8 styles (use the same microservices architecture diagram):

- [ ] **Style 1 (Flat Icon)**: All shapes have colored fills, rounded corners, readable labels, clear arrows
- [ ] **Style 2 (Dark Terminal)**: Dark background, neon-colored borders, monospace font, glow effects on AI nodes
- [ ] **Style 3 (Blueprint)**: Dark navy background, cyan strokes, sharp corners (rounded=0), monospace font
- [ ] **Style 4 (Notion Clean)**: White background, minimal gray borders, single blue arrow color, clean typography
- [ ] **Style 5 (Glassmorphism)**: Dark background, glass effect (glass=1), colored glow borders, semi-transparent
- [ ] **Style 6 (Claude Official)**: Warm cream background, thick 2.5px dark gray borders, teal/green/beige fills
- [ ] **Style 7 (OpenAI Official)**: Pure white, thin 1.5px gray borders, brand green accent (#10a37f) in arrows
- [ ] **Style 8 (Dark Luxury)**: Deep black (#0a0a0a), 6 colored semantic buckets, gold arrows, serif section titles

### 4.2 Diagram Type Rendering

Generate each diagram type with Style 1 (Flat Icon):

- [ ] **Architecture**: Layers visible (Client→Gateway→Service→DB), containers/swimlanes, correct edge routing
- [ ] **Flowchart**: Start oval (green), process boxes (blue), decision diamonds (yellow), Yes/No labels
- [ ] **Sequence**: Lifelines vertical, messages horizontal top-to-bottom, activation boxes
- [ ] **ERD**: Table containers with column rows, PK/FK markers, relationship edges
- [ ] **UML Class**: 3-section class boxes, inheritance (hollow triangle), composition (filled diamond)
- [ ] **ML/DL Model**: Layer blocks with tensor shapes, skip connections (dashed curved arrows)
- [ ] **Agent Architecture**: Agent core, memory layers, tool layer, reasoning loop arrows
- [ ] **Network Topology**: Device shapes (if shapesearch used), subnet containers, connection labels

### 4.3 Self-Check Workflow

- [ ] Preview PNG readable by vision API (no `-e` flag, capped `--width 2000`)
- [ ] Self-check catches overlapping shapes
- [ ] Self-check catches clipped labels
- [ ] Self-check catches dangling edges
- [ ] Review loop: user can request changes and diagram updates
- [ ] Final export produces `.drawio.png` with embedded XML
- [ ] repair_png.py fixes truncated IEND on final export

### 4.4 Edge Cases

- [ ] Diagram with 20+ nodes — recommend autolayout
- [ ] Diagram with CJK (Chinese/Japanese/Korean) labels — `&#xa;` line breaks, font fallback
- [ ] Diagram with special XML characters (`&`, `<`, `>`, `"`) — proper `&amp;` escaping
- [ ] Empty diagram (single node) — no crash
- [ ] Diagram with only edges, no vertices — validate.py catches dangling edges
- [ ] Style name resolution: "暗黑终端" → Style 2, "蓝图风格" → Style 3
- [ ] User preset shadows built-in — user `~/.drawio-skill/styles/` checked first

---

## Running Tests

### All automated tests
```bash
cd drawio-style-graph
python3 tests/test_scripts.py
python3 tests/test_styles.py
```

### Fast tests (skip autolayout if Graphviz not installed)
```bash
python3 tests/test_scripts.py --quick
```

### With full style report
```bash
python3 tests/test_styles.py --report --verbose
```

### Manual test workflow
```bash
# 1. Generate test diagram
# (describe your diagram to the skill in VS Code)

# 2. Run structural validation
python3 scripts/validate.py diagram.drawio

# 3. Export preview
drawio -x -f png --width 2000 -o preview.png diagram.drawio

# 4. Visual inspection (open preview.png)
# Check style colors, fonts, shapes, edge routing

# 5. Test repair
python3 scripts/repair_png.py diagram.drawio.png
```

---

## Test Environment Matrix

| Environment | Status |
|------------|--------|
| macOS (drawio via Homebrew) | Supported |
| Linux (drawio via .deb) | Supported |
| Windows (drawio via installer) | Supported |
| WSL2 (Windows drawio via /mnt/c) | Supported |
| macOS sandbox (CLI unavailable) | Fallback to browser URL |
| No drawio CLI | Fallback to browser URL |
| No Graphviz | Skip autolayout tests (`--quick`) |
| No vision API | Skip self-check (step 5 of workflow) |

---

## Success Criteria

For `v1.0.0` release readiness:

- [x] All 30+ unit tests pass
- [x] All 11 scripts execute without traceback
- [x] All 8 style files have complete token coverage
- [x] All 3 built-in presets are valid JSON
- [x] Both schema files are valid JSON
- [ ] Manual visual check: 8 styles × 1 diagram produces correct output
- [ ] Manual visual check: 8 diagram types × Style 1 produces correct output
- [ ] Export pipeline: PNG (preview + final + repair), SVG, PDF all work
- [ ] Browser fallback: viewer + editor URLs open correctly

---

## Regression Test Checklist

Before each release, run these in order:

```bash
# 1. Automated tests (must all pass)
python3 tests/test_scripts.py --verbose
python3 tests/test_styles.py --verbose

# 2. Style mapping report (spot-check for anomalies)
python3 tests/test_styles.py --report

# 3. Check for dependency leaks
grep -r "DRAWIO_SKILL_DIR\|depends on drawio-skill\|requires drawio-skill" SKILL.md && echo "FAIL" || echo "OK"

# 4. File count sanity
echo "Scripts: $(ls scripts/*.py | wc -l) (expected 11)"
echo "Styles: $(ls references/styles/*.md | wc -l) (expected 8)"
echo "Data: $(ls data/ | wc -l) (expected 3)"
```
