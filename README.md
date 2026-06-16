# drawio-style-graph

**English** · [中文](README_zh.md)

> **8 professional visual styles x draw.io editable format.**
> Describe your system in natural language — get a styled, editable .drawio diagram.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![8 Visual Styles](https://img.shields.io/badge/Styles-8-purple)]()
[![14 Diagram Types](https://img.shields.io/badge/Diagram%20Types-14-green)]()
[![10k+ Shapes](https://img.shields.io/badge/Shapes-10,446-blue)]()
[![321 AI Logos](https://img.shields.io/badge/AI%20Logos-321-orange)]()

---

## What Is This?

Two excellent open-source diagram tools, fused into one:

| 🔥 fireworks-tech-graph | 📐 drawio-skill |
|---|---|
| by [@yizhiyanhua-ai](https://github.com/yizhiyanhua-ai) | by [@Agents365-ai](https://github.com/Agents365-ai) |
| **8 hand-crafted visual styles**<br>Flat Icon, Dark Terminal, Blueprint,<br>Notion Clean, Glassmorphism,<br>Claude Official, OpenAI, Dark Luxury | **Complete draw.io engine**<br>10,446 vendor shapes, 321 AI logos,<br>diagram type presets, auto-layout,<br>PNG/SVG/PDF export pipeline |
| 🎨 Color palettes · Typography systems<br>Arrow semantics · Design tokens | 🔍 shapesearch.py · 🤖 aiicons.py<br>✅ validate.py · 🔧 repair_png.py<br>📐 autolayout.py · 🌐 encode_drawio_url.py |

Both ecosystems are fully bundled — no external skill dependencies:

```
fireworks-tech-graph                  drawio-skill
(SVG design tokens)                   (draw.io engine + scripts)

    │                                      │
    │  8 visual styles                    │  10,446 shapes search
    │  color palettes                     │  321 AI brand logos
    │  typography systems                 │  diagram type presets
    │  arrow semantics                    │  auto-layout (Graphviz)
    │  shape preferences                  │  validation + repair
    │  extras (shadow/glass/sketch)       │  browser fallback URLs
    │                                      │
    └──────────────┬───────────────────────┘
                   │  SVG tokens mapped to draw.io style= strings
                   ▼
          ┌─────────────────────┐
          │ drawio-style-graph  │
          │                     │
          │  8 styles           │
          │  x                  │
          │  .drawio format     │
          │                     │
          │  Fully self-contained
          │  Zero extra installs │
          └─────────────────────┘
```

**The result:** the visual polish of fireworks-tech-graph's SVG styles,
rendered as fully **editable .drawio files** with draw.io's entire shape ecosystem.

---

## 8 Built-in Styles

Each style is a complete design system mapped to draw.io `style=` token strings:

| # | Style | Palette | Typography | Signature |
|---|-------|---------|------------|-----------|
| 1 | **Flat Icon** | Blue · Green · Orange · Purple | Helvetica, 14px | `rounded=1` |
| 2 | **Dark Terminal** | Purple · Blue · Green neon | SF Mono, 13px | `shadow=1`, bg `#0f0f1a` |
| 3 | **Blueprint** | Cyan · Green · Orange | Courier New, 13px | `rounded=0`, bg `#0a1628` |
| 4 | **Notion Clean** | Warm gray · Single blue accent | System UI, 14px | Minimal · Flat |
| 5 | **Glassmorphism** | Blue · Purple · Green glow | Inter, 14px | `glass=1;shadow=1`, bg `#0d1117` |
| 6 | **Claude Official** | Teal · Blue · Beige · Gray | System UI, 16px | `strokeWidth=2.5`, thick borders |
| 7 | **OpenAI Official** | White · `#10a37f` green accent | System UI, 16px | `strokeWidth=1.5`, precision |
| 8 | **Dark Luxury** | 6-color buckets · Gold arrows | Georgia + Sans, 14px | Dual font, bg `#0a0a0a` |

→ [Style-diagram compatibility matrix](references/style-diagram-matrix.md)&nbsp;&nbsp;← [How to apply styles](references/style-application-guide.md)

---

## Quick Start

### Install

```bash
npx skills add Littledragon-wxl/drawio-style-graph
```

Or via npm:

```bash
npm install @littledragon_wxl/drawio-style-graph
```

### Prerequisites

1. Install draw.io desktop: [download](https://github.com/jgraph/drawio-desktop/releases)
2. Python 3 (for helper scripts)
3. Graphviz (optional): `brew install graphviz`

**That's it.** No other skills needed — everything is bundled.

### Usage

```
"Draw a microservices architecture with Dark Terminal style"
"Create an ERD for a blog system with Notion Clean style"
"Generate an AI agent architecture diagram with Glassmorphism style"
```

---

## How SVG Tokens Map to Draw.io

| SVG / Design Token | Draw.io Equivalent |
|---|---|
| `fill: #eff6ff` | `fillColor=#eff6ff` in vertex style |
| `stroke: #bfdbfe` | `strokeColor=#bfdbfe` in vertex style |
| `rx: 8px` (border-radius) | `rounded=1` (or `rounded=0` for sharp) |
| `font-family: Helvetica` | `fontFamily=Helvetica` in vertex style |
| `font-size: 14px` | `fontSize=14` in vertex style |
| `font-weight: 600` | `fontStyle=1` (bold) in vertex style |
| `color: #111827` | `fontColor=#111827` in vertex style |
| Arrow marker `fill` | `strokeColor=#xxxxxx` on edge |
| `stroke-dasharray: 5,3` | `dashed=1` on edge |
| `filter: drop-shadow` | `shadow=1` or `glass=1` in vertex style |
| Sketch/rough edges | `sketch=1` in vertex + edge styles |

---

## What's Bundled

| Directory | Contents |
|-----------|----------|
| `scripts/` | 11 Python scripts: shapesearch (10,446 shapes), aiicons (321 AI logos), validate, repair_png, autolayout, encode_drawio_url, 5 project importers |
| `data/` | `shape-index.json.gz` + `lobe-icons.json` |
| `references/` | diagram-types.md, shapes.md, troubleshooting.md, autolayout.md, style-presets.md, style-extraction.md, style-diagram-matrix.md, style-application-guide.md, 8 style reference files |
| `styles/` | 3 built-in draw.io presets (`default.json`, `corporate.json`, `handdrawn.json`) + 2 JSON schemas |

**Supported diagram types:** Architecture · Data Flow · Flowchart · Agent/Memory ·
Sequence · UML Class · Use Case · State Machine · ER Diagram · Network Topology ·
ML/DL Model · Mind Map · Comparison Matrix · Timeline/Gantt

---

## License

MIT

---

## Acknowledgments

This project stands on the shoulders of two excellent open-source communities:

### 🔥 fireworks-tech-graph

The 8 visual styles and their design tokens are adapted from
**[fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**
by [@yizhiyanhua-ai](https://github.com/yizhiyanhua-ai).

What we inherited: meticulously crafted color palettes for every semantic role
(primary `#eff6ff`/`#bfdbfe`, success `#f0fdf4`/`#bbf7d0`, warning `#fff7ed`/`#fed7aa`,
accent `#faf5ff`/`#e9d5ff`, danger `#fef2f2`/`#fecaca`, secondary `#f0fdfa`/`#ccfbf1`,
neutral `#f9fafb`/`#e5e7eb`), complete typography systems (from Helvetica to SF Mono
to Georgia), color-coded arrow semantics by flow type, style-to-diagram-type
compatibility research (14 types x 8 styles), and the Dark Luxury AI-authored style
with its dual serif/sans typography and 6 semantic color buckets.

### 📐 drawio-skill

The draw.io engine is integrated from
**[drawio-skill](https://github.com/Agents365-ai/drawio-skill)**
by [@Agents365-ai](https://github.com/Agents365-ai).

What we inherited: 11 production-hardened Python scripts covering the complete
draw.io lifecycle — shape search across 10,446 vendor icons (AWS/Azure/GCP/Cisco/K8s),
AI/LLM brand logo resolution (321 brands via lobe-icons + simple-icons CDN),
deterministic structural validation (dangling edges, duplicate IDs, broken parent
references), PNG IEND chunk repair for draw.io's CLI truncation bug,
Graphviz-based auto-layout for large diagrams, browser-fallback URL encoding,
and project structure importers for Python, JS/TS, Go, and Rust. Also the
diagram-type preset system (ERD/UML Class/Sequence/ML-DL/Flowchart) and the
style preset learn/save/manage framework.

### Icon Libraries

- AI/LLM brand logos via [lobe-icons](https://github.com/lobehub/lobe-icons) (MIT)
- Data store icons via [simple-icons](https://simpleicons.org) (CC0)
