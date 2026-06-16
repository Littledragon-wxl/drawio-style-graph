# Changelog

## 1.0.0 (2026-06-16)

### Initial Release — Fully Self-Contained

- **8 visual styles** adapted from fireworks-tech-graph:
  - Style 1: Flat Icon (default) — clean, colorful, draw.io-native
  - Style 2: Dark Terminal — neon-on-dark, monospace font
  - Style 3: Blueprint — cyan-on-navy, sharp corners, technical feel
  - Style 4: Notion Clean — minimal, warm gray, documentation-friendly
  - Style 5: Glassmorphism — frosted glass, layered depth on dark bg
  - Style 6: Claude Official — warm, Anthropic-style, thick borders
  - Style 7: OpenAI Official — clean, precise, minimal borders
  - Style 8: Dark Luxury — gold-on-black, premium editorial

- **Style to Draw.io token mapping** for all 8 styles

- **Style Application Guide** with role-to-color mapping

- **Style-to-Diagram-Type Compatibility Matrix** (14 types x 8 styles)

- **JSON Schema** for validating style presets

- **Bundled drawio-skill engine** (no external dependency):
  - 11 Python scripts (shapesearch, aiicons, validate, repair_png, autolayout,
    encode_drawio_url, pyimports, jsimports, goimports, rustimports, pyclasses)
  - Shape index data (10,446 shapes) and AI brand icons database (321 brands)
  - All references (diagram types, shapes, troubleshooting, autolayout, style presets)

- Full workflow: gather requirements > load style > plan > generate .drawio >
  export preview > self-check > review > final export
