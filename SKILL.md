---
name: drawio-style-graph
version: 1.0.0
description: >-
  Use when the user wants to create any technical diagram with custom visual
  styles — architecture, data flow, flowchart, sequence, agent/memory, ERD,
  UML, or concept map — and export as .drawio (editable) + PNG/SVG/PDF.
  8 built-in visual styles adapted from fireworks-tech-graph, rendered
  through draw.io's rich shape vocabulary and icon system.
  Self-contained — no other skills required.
  Trigger on: "风格图" "带风格的图" "暗黑风格" "蓝图风格" "极简风格"
  "玻璃风格" "奢华风格" "style diagram" "styled architecture"
  "drawio" "draw.io" ".drawio" "可编辑的图" "editable diagram"
  or when the user explicitly asks for drawio format or a specific visual style.
  Also trigger on "画图" "架构图" "流程图" ONLY when the user requests
  a specific visual style name, AI brand icons, or editable .drawio output.
  Do NOT trigger for: raw SVG generation, CSS-heavy effects, quick sketches,
  or mermaid/plantuml code blocks.
license: MIT
homepage: https://github.com/Agents365-ai/drawio-style-graph
install: npx skills add Littledragon-wxl/drawio-style-graph
compatibility: >-
  Requires draw.io desktop app CLI on PATH (macOS/Linux/Windows) for export.
  Core .drawio generation needs Python 3 only.
  Optional auto-layout (scripts/autolayout.py) needs Graphviz (dot).
platforms: [macos, linux, windows]
---

# Draw.io Style Graph

Generate `.drawio` XML files with 8 professional visual styles and export to
PNG/SVG/PDF/JPG locally using the native draw.io desktop app CLI.

**Supported formats:** PNG, SVG, PDF, JPG — no browser automation needed.
PNG, SVG, and PDF exports support `--embed-diagram` (`-e`) — opening the
exported file in draw.io recovers the editable diagram.

## Install

```bash
npx skills add Littledragon-wxl/drawio-style-graph
```

Or directly from npm:

```bash
npm install @littledragon_wxl/drawio-style-graph
```

No other skills required — everything is self-contained.

## When to use / when NOT to use

**Use this skill for:**
- Polished, precise diagrams with custom visual styles
- Architecture, network, UML, ERD, flowcharts, ML/DL models, sequence diagrams
- 10,000+ stock/branded shapes (AWS/Azure/GCP/Cisco/K8s)
- 321 AI/LLM brand logos (OpenAI, Claude, Gemini, Mistral, etc.)
- Swimlanes, custom geometry, solid opaque fills
- Export to editable PNG/SVG/PDF
- Diagrams needing a specific visual style (dark terminal, blueprint, glassmorphism, etc.)

**Do NOT use — route elsewhere — for:**
- A casual hand-drawn / whiteboard look → **excalidraw** or **tldraw**
- Diagrams-as-code that live in git / render in Markdown → **mermaid** or **plantuml**
- Freeform infinite-canvas sketching → **tldraw**
- Raw SVG with CSS backdrop-filter, complex gradients, or pixel-level effects → **fireworks-tech-graph**

## Relationship with Other Skills

This skill is a **superset of drawio-skill** and can replace it entirely.
Here is how the three diagram skills relate:

```
┌──────────────────────────────────────────────────┐
│  drawio-style-graph  ← 这个 (推荐保留)             │
│  .drawio 格式 · 可编辑 · 8 风格 · 10k+ 形状         │
│  = drawio-skill 的全部能力 + fireworks 的 8 种风格   │
├──────────────────────────────────────────────────┤
│  fireworks-tech-graph  ← 独立场景 (建议保留)        │
│  SVG+PNG 直出 · CSS 特效 · 像素级控制               │
│  draw.io 做不到的: backdrop-filter, 复杂渐变,       │
│  jump-over 弧线, foreignObject, 精确滤镜            │
├──────────────────────────────────────────────────┤
│  drawio-skill  ← 已被取代 (可以删除)                 │
│  drawio-style-graph 包含其全部脚本+数据+能力          │
└──────────────────────────────────────────────────┘
```

**建议配置：**
- ✅ 保留 `drawio-style-graph` + `fireworks-tech-graph`（分工明确，无冲突）
- ❌ 删除 `drawio-skill`（`drawio-style-graph` 已包含其全部能力）

**分工规则：**
| 用户说 | 路由到 |
|--------|--------|
| "画一个架构图" / "画个流程图" | `drawio-style-graph`（默认，输出可编辑 .drawio） |
| "用暗黑风格画图" / "用蓝图风格" | `drawio-style-graph`（风格关键词） |
| "生成 SVG 格式的架构图" / "导出 SVG" | `fireworks-tech-graph`（明确要 SVG） |
| "要做毛玻璃效果" / "要 CSS 特效" | `fireworks-tech-graph`（draw.io 做不到） |
| "画个可编辑的图" / "生成 drawio" | `drawio-style-graph`（明确要 drawio） |

## 8 Built-in Visual Styles

These styles are adapted from fireworks-tech-graph's design tokens, mapped to
draw.io-compatible `style=` attribute values.

| # | Style | Aesthetic | Load when |
|---|-------|-----------|-----------|
| 1 | **Flat Icon** | Clean, colorful, draw.io-native | Default style |
| 2 | **Dark Terminal** | Neon-on-dark, hacker aesthetic | AI/ML architecture, dev blogs |
| 3 | **Blueprint** | Technical blueprint, formal docs | UML, Network, Infrastructure |
| 4 | **Notion Clean** | Minimal, warm gray, sans-serif | Notion docs, clean documentation |
| 5 | **Glassmorphism** | Frosted glass, layered depth | Product demos, presentations |
| 6 | **Claude Official** | Warm, earthy, Anthropic-style | AI system docs, presentations |
| 7 | **OpenAI Official** | Clean, precise, minimal borders | API docs, technical specs |
| 8 | **Dark Luxury** | Gold-on-black, premium editorial | Premium docs, keynotes |

Each style is defined in `references/styles/style-N-<name>.md` with:
- Color palette → `fillColor`/`strokeColor` pairs for each role
- Typography → `fontFamily`, `fontSize`, `fontColor` settings
- Shape preferences → `rounded`, shape keywords per role
- Edge style → base edge style, arrow colors, dash patterns
- Extras → `sketch`, `shadow`, `glass`, `strokeWidth` flags

For style-diagram compatibility recommendations, see `references/style-diagram-matrix.md`.
For detailed application instructions, see `references/style-application-guide.md`.

## Bundled Resources

When the workflow references one of these, read it on demand — none need to be in
context up front.

| File | Read it when |
|------|-------------|
| `references/styles/style-N-<name>.md` | A visual style is selected (8 files, one per style) |
| `references/style-application-guide.md` | You need to apply style tokens to draw.io shapes |
| `references/style-diagram-matrix.md` | Choosing which style works best for a diagram type |
| `references/diagram-types.md` | The user names a specific diagram type (ERD, UML class, sequence, architecture, ML/DL, flowchart) |
| `references/shapes.md` + `scripts/shapesearch.py` | The diagram needs a **specific shape** — cloud icons (AWS/Azure/GCP), Cisco/K8s/network symbols, UML/BPMN/ER elements. `shapesearch.py "<keywords>"` returns the exact official style for 10,446 shapes |
| `scripts/aiicons.py` | The diagram involves an **AI/LLM brand** (OpenAI, Claude, Gemini, Mistral, Llama, HuggingFace, Ollama, LangChain, …321 brands). Returns a draw.io `image` style for the brand logo |
| `references/style-presets.md` | The user asks to learn / save / list / set-default / delete a style preset |
| `references/style-extraction.md` | You're inside the Learn flow (called from `style-presets.md`) |
| `references/troubleshooting.md` | An export fails or rendering looks wrong |
| `scripts/repair_png.py` | After every `-e` PNG export — fixes draw.io's truncated IEND chunk |
| `scripts/encode_drawio_url.py` | The CLI is unavailable and you need a browser-fallback diagrams.net URL |
| `references/autolayout.md` | Large diagrams (>~15 nodes) — use Graphviz to place nodes + route edges |
| `scripts/pyimports.py` / `jsimports.py` / `goimports.py` / `rustimports.py` | Visualize a **Python/JS-TS/Go/Rust project** structure — extracts import graph |
| `scripts/pyclasses.py` | Visualize a **Python class hierarchy** — extracts classes + inheritance |
| `scripts/validate.py` | After generating `.drawio` — fast structural lint (dangling edges, dup ids, overlaps) |

## Prerequisites

The draw.io desktop app must be installed and the CLI accessible:

```bash
# macOS (Homebrew — `drawio`, not `draw.io`)
brew install --cask drawio
drawio --version

# macOS (full path)
/Applications/draw.io.app/Contents/MacOS/draw.io --version

# Windows
"C:\Program Files\draw.io\draw.io.exe" --version

# Linux
drawio --version
```

Install draw.io desktop if missing:
- macOS: `brew install --cask drawio` or download from https://github.com/jgraph/drawio-desktop/releases
- Windows: download from https://github.com/jgraph/drawio-desktop/releases
- Linux: download `.deb`/`.rpm` from https://github.com/jgraph/drawio-desktop/releases — **do not use snap**

**macOS sandbox note:** In sandboxed environments, the CLI may crash. Treat CLI
as unavailable in that case — use browser fallback or `.drawio` XML only.

## Workflow

### Step 0 — Gather Requirements

Before starting, assess the user's request. If key details are missing, ask
1-3 focused questions:

- **Diagram type** — architecture, flowchart, sequence, ERD, UML, ML/DL, mind map?
- **Visual style** — which of the 8 styles? (Default: Style 1 Flat Icon if not specified)
- **Output format** — PNG (default), SVG, PDF, or JPG?
- **Output location** — default is working dir; honor explicit paths.
- **Scope** — how many components? Specific technologies or labels?

Skip clarification if the request is clearly specified.

**Style resolution — check the user's message for style keywords:**
- "dark terminal", "暗黑", "terminal" → Style 2
- "blueprint", "蓝图" → Style 3
- "notion", "极简", "clean" → Style 4
- "glass", "玻璃", "glassmorphism" → Style 5
- "claude", "anthropic" → Style 6
- "openai" → Style 7
- "luxury", "奢华", "dark luxury" → Style 8
- No keyword → Style 1 (Flat Icon, default)

### Step 1 — Check Dependencies

Resolve the draw.io binary name:

```bash
if command -v drawio &>/dev/null; then
  DRAWIO="drawio"
elif command -v draw.io &>/dev/null; then
  DRAWIO="draw.io"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
elif grep -qi microsoft /proc/version 2>/dev/null && [ -f "/mnt/c/Program Files/draw.io/draw.io.exe" ]; then
  DRAWIO="/mnt/c/Program Files/draw.io/draw.io.exe"
fi
$DRAWIO --version
```

### Step 2 — Load Style, Plan, Generate

1. **Load the style reference** from `references/styles/style-N-<name>.md`
2. **Load diagram-type preset** (if applicable) from `references/diagram-types.md`
3. **Merge**: Diagram-type structural keywords + visual style colors/fonts/edges/extras.
   When both define a color, the visual style wins.
4. **Plan layout** — identify shapes, roles, relationships, layout direction (LR/TB).

**Role → Style Palette mapping:**
| Role | Style Slot | Example |
|------|-----------|---------|
| Service / component | primary | API service, microservice |
| Database / storage | success | PostgreSQL, Redis, S3 |
| Queue / message bus | warning | Kafka, RabbitMQ |
| Gateway / API / LB | accent | API Gateway, Load Balancer |
| Error / alert | danger | Error handler, monitoring |
| Security / auth | secondary | OAuth, IAM |
| External system | neutral | Third-party API |

### Step 3 — Generate & Validate .drawio

Write the `.drawio` file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- User shapes start at id="2" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Rules:**
- `id="0"` and `id="1"` are required root cells
- User shapes start at `id="2"`, increment sequentially
- All shapes have `parent="1"` (unless inside a container)
- Escape: `&amp;` `&lt;` `&gt;` `&quot;`
- Multi-line labels: `&#xa;` (not `\n`)
- Never use `--` in XML comments

For **large diagrams (>15 nodes)**, use auto-layout:

```bash
python3 scripts/autolayout.py graph.json -o output.drawio
```

After generating, run validation:

```bash
python3 scripts/validate.py output.drawio
```

Report the generated `.drawio` file path. Done.

### Optional: Export to PNG/SVG/PDF

If the user explicitly asks for an exported image, use the draw.io CLI:

```bash
# Resolve binary first
if command -v drawio &>/dev/null; then DRAWIO="drawio"
elif command -v draw.io &>/dev/null; then DRAWIO="draw.io"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
fi

# PNG (editable, embeds .drawio XML)
$DRAWIO -x -f png -e -s 2 -o diagram.drawio.png diagram.drawio
python3 scripts/repair_png.py diagram.drawio.png

# SVG
$DRAWIO -x -f svg -e -o diagram.svg diagram.drawio
```

If CLI is unavailable, use browser fallback:

```bash
python3 scripts/encode_drawio_url.py diagram.drawio        # viewer
python3 scripts/encode_drawio_url.py --edit diagram.drawio  # editor
```

### Optional: Preview in draw.io Browser

To open the generated `.drawio` file for live editing and preview in draw.io, use the 
built-in preview script:

```bash
# Opens in native draw.io desktop app (preferred if installed)
python3 scripts/open_drawio.py diagram.drawio

# Or force browser editor mode
python3 scripts/open_drawio.py diagram.drawio --edit

# Or force browser-based preview (if desktop app unavailable)
python3 scripts/open_drawio.py diagram.drawio --browser
```

**Supported platforms:**
- **macOS:** Automatically detects `/Applications/draw.io.app`
- **Windows:** Looks for `C:\Program Files\draw.io\draw.io.exe`
- **Linux:** Uses `drawio` command if in PATH
- **Browser fallback:** Generates a diagrams.net URL if desktop app unavailable

**Behind the scenes:**
1. Tries to open with the native draw.io app first (fastest, no browser needed)
2. Falls back to generating a diagrams.net URL if app not found
3. Automatically opens your default browser with the sharable URL

## Draw.io XML Quick Reference

### Vertex (Shape)

```xml
<mxCell id="2" value="Label" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontFamily=Helvetica;fontSize=14;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>
```

### Edge (Connector) — MUST include `<mxGeometry relative="1" as="geometry" />`

```xml
<mxCell id="10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

Self-closing edge cells (`<mxCell ... edge="1" ... />`) are **invalid** — always use expanded form.

### Container (Swimlane)

```xml
<mxCell id="svc1" value="Service Layer" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
<!-- Child — coordinates relative to container -->
<mxCell id="api1" value="REST API" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

### Common Shape Keywords

| Shape | Style keyword |
|-------|--------------|
| Rectangle | `rounded=0;` |
| Rounded rect | `rounded=1;` |
| Ellipse/Circle | `ellipse;` |
| Diamond | `rhombus;` |
| Cylinder (DB) | `shape=cylinder3;` |
| Cloud | `cloud;` |
| Parallelogram | `shape=parallelogram;perimeter=parallelogramPerimeter;` |
| Hexagon | `shape=hexagon;perimeter=hexagonPerimeter2;` |
| Document | `shape=document;` |

For vendor icons (AWS, Azure, GCP, Cisco, Kubernetes), **run shapesearch.py** —
never guess a `shape=mxgraph.*` name:

```bash
python3 scripts/shapesearch.py "aws lambda" --limit 5
```

For AI/LLM brand logos:

```bash
python3 scripts/aiicons.py "openai" --json
```

## Edge Routing

- Always include `rounded=1;orthogonalLoop=1;jettySize=auto` for smart routing
- Pin `exitX/exitY/entryX/entryY` when a node has 2+ connections
- Add `<Array as="points">` waypoints when routing around shapes
- Leave ≥20px for the final straight segment before arrowhead
- Distribute connections across shape perimeter:

| Position | exitX/entryX | exitY/entryY |
|----------|-------------|-------------|
| Top center | 0.5 | 0 |
| Top-left | 0.25 | 0 |
| Top-right | 0.75 | 0 |
| Right center | 1 | 0.5 |
| Bottom center | 0.5 | 1 |
| Left center | 0 | 0.5 |

## Spacing & Layout

| Complexity | Nodes | H-Gap | V-Gap |
|-----------|-------|-------|-------|
| Simple | ≤5 | 200px | 150px |
| Medium | 6-10 | 280px | 200px |
| Complex | >10 | 350px | 250px |

- Snap x, y, width, height to multiples of 10
- Leave 80px routing corridors between rows/columns
- Place hub nodes centrally, satellites around them
- Center-align children under parents (same center x)


## Style Presets System

Users can save custom style presets:

- User presets: 
- Built-in presets:  (, , )

For the full preset system — Learn flow, management ops, application rules —
read  and .

## Common Mistakes

| Symptom | Fix |
|---------|-----|
| Edge doesn't render | Add `<mxGeometry relative="1" as="geometry" />` child |
| Blank shape for vendor icon | Use `shapesearch.py`, don't guess `shape=mxgraph.*` |
| Text overflows shape | Increase width or use `&#xa;` for line breaks |
| Arrowhead overlaps bend | Increase spacing or add waypoints |
| PNG corrupted after `-e` export | Run `scripts/repair_png.py` |
| CLI unavailable | Use `scripts/encode_drawio_url.py` browser fallback |

For detailed troubleshooting, see `references/troubleshooting.md`.
