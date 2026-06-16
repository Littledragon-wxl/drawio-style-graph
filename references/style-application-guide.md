# Style Application Guide

How to apply a visual style to a draw.io diagram generation.

## Quick Reference: Style → Draw.io Tokens

When a style is selected, use these mappings to construct `mxCell` style strings:

### Step 1: Determine Role → Color

For each node, determine its semantic role, then look up the `(fillColor, strokeColor)` pair
from the selected style reference file:

| Role | Style Reference Key | Example Use |
|------|---------------------|-------------|
| Service / component | `primary` | API service, microservice, worker |
| Database / storage | `success` | PostgreSQL, Redis, S3, vector store |
| Queue / message bus | `warning` | Kafka, RabbitMQ, SQS |
| Gateway / API / LB | `accent` | API Gateway, Load Balancer, Proxy |
| Error / alert | `danger` | Error handler, monitoring alert |
| Security / auth | `secondary` | OAuth service, IAM, Vault |
| External system | `neutral` | Third-party API, external service |

### Step 2: Build Vertex Style String

Template:
```
{shape_keyword};whiteSpace=wrap;html=1;fillColor={fillColor};strokeColor={strokeColor};strokeWidth={strokeWidth};fontFamily={fontFamily};fontSize={fontSize};fontColor={fontColor};{extras}
```

Where each variable comes from the style reference:

| Variable | Style Reference Field |
|----------|----------------------|
| `shape_keyword` | "Shape Preferences" section (e.g., `rounded=1`) |
| `fillColor` | Role's fillColor from palette table |
| `strokeColor` | Role's strokeColor from palette table |
| `strokeWidth` | Extras section (default: 1.5) |
| `fontFamily` | Typography section |
| `fontSize` | Typography section (labels size) |
| `fontColor` | Typography section (primary text) |
| `extras` | Extras section (e.g., `glass=1;shadow=1;`) |

### Step 3: Build Edge Style String

Template:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor={flowColor};strokeWidth={edgeWidth};{dashPattern};exitX={exitX};exitY={exitY};entryX={entryX};entryY={entryY};
```

| Variable | Source |
|----------|--------|
| `flowColor` | Edge Style section, pick by flow type |
| `edgeWidth` | Edge Style section or infer from strokeWidth |
| `dashPattern` | `dashed=1` if flow type says dashed |
| `exitX/Y`, `entryX/Y` | Routing rules (see SKILL.md) |

### Step 4: Set Page Background

For dark styles (2, 3, 5, 8), set the background on the mxGraphModel:

```xml
<mxGraphModel background="#0f0f1a">
```

For light styles (1, 4, 6, 7), use default or white:
```xml
<mxGraphModel background="#ffffff">
```

## Style-Specific Notes

### Style 1 (Flat Icon)
- Use `rounded=1` for all boxes
- Colorful palette — different fill for each role
- Default edge color: `#2563eb` (blue)
- Arrow semantics use different colors per flow type

### Style 2 (Dark Terminal)
- Always set `background="#0f0f1a"`
- Use monospace font for all text
- Add `shadow=1` on primary (AI/ML) nodes
- Edge colors match source node's theme

### Style 3 (Blueprint)
- Always set `background="#0a1628"`
- Use `rounded=0` (sharp corners)
- Monospace font, cyan-based text colors
- External nodes use `fillColor=none;dashed=1`

### Style 4 (Notion Clean)
- All standard nodes share `fillColor=#f9fafb;strokeColor=#e5e7eb`
- Only error nodes get pink tint
- Single arrow color: `#3b82f6`
- Uppercase type labels at 11px

### Style 5 (Glassmorphism)
- Always set `background="#0d1117"`
- Add `glass=1;shadow=1` to all vertex styles
- Edge colors match the source node's glow color bucket
- Semi-transparent look in draw.io

### Style 6 (Claude Official)
- All nodes share `strokeColor=#4a4a4a;strokeWidth=2.5`
- Warm teal/beige/blue/gray fill colors per role
- Consistent `#5a5a5a` for all arrows
- Bold 16px labels with `fontStyle=1`

### Style 7 (OpenAI Official)
- Almost all nodes: `fillColor=#ffffff;strokeColor=#e5e5e5`
- Thin borders: `strokeWidth=1.5`
- Color only in edges: `#10a37f` (green), `#71717a` (gray)
- No shadows, no decorations

### Style 8 (Dark Luxury)
- Always set `background="#0a0a0a"`
- All nodes: `fillColor=#111111` with colored stroke per bucket
- Dual font: serif for titles, sans-serif for nodes
- Gold edges (`#d4a574`) for primary flows
- 6 semantic buckets with distinct stroke colors
