# Style 7: OpenAI Official

Adapted from fireworks-tech-graph Style 7. Clean, minimal, precise.

## Color Palette → Draw.io Mapping

This style is extremely minimal — almost all nodes are white with light gray borders.
Color is reserved for accents only.

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#ffffff` | `#e5e5e5` | services, main components |
| success (database) | `#ffffff` | `#e5e5e5` | databases, storage |
| warning (queue) | `#ffffff` | `#e5e5e5` | queues |
| accent (gateway/API) | `#ffffff` | `#e5e5e5` | gateways, APIs |
| danger (error) | `#fef2f2` | `#fecaca` | errors, alerts |
| secondary (security) | `#ffffff` | `#e5e5e5` | security |
| neutral (external) | `#ffffff` | `#e5e5e5` | external systems |

**Accent colors** (used for left-border accent strip or edge colors):
- `#10a37f` — OpenAI brand green (primary accent)
- `#1d4ed8` — blue accent (links, secondary)
- `#f97316` — orange accent (warnings, highlights)
- `#71717a` — gray (default edges, neutral)

## Typography → Draw.io Mapping

```
fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,PingFang SC,Microsoft YaHei,SimHei,sans-serif
fontSize=16        (node labels, semi-bold)
fontSize=13        (descriptions)
fontSize=12        (arrow labels)
fontStyle=1        (bold, for titles — font weight 600)
fontStyle=0        (medium equivalent for labels — font weight 500)
fontColor=#0d0d0d  (primary text — near black)
fontColor=#6e6e80  (secondary text — muted gray)
```

## Shape Preferences

```
rounded=1          (rounded corners, 8px equivalent)
whiteSpace=wrap
html=1
```

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
Note: In the original SVG style, accent nodes have a 4px colored left border. draw.io
doesn't support this directly, but you can achieve a similar effect by using
`verticalAlign=top;align=left;spacingLeft=8;` for left-aligned text with an accent
colored `strokeColor` on the container.

## Edge Style → Draw.io Mapping

Base edge style — thin, precise:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;
```

Arrow colors:
| Flow Type | strokeColor | Usage |
|-----------|-------------|-------|
| Default connection | `#71717a` | most edges |
| Accent/green | `#10a37f` | primary data paths |
| Blue action | `#1d4ed8` | action/trigger |
| Orange warning | `#f97316` | edge cases, warnings |

## Extras

```
strokeWidth=1.5   (thin, precise borders on all shapes)
sketch=0
shadow=0
```

## Complete Vertex Style Template

For a standard node:
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e5e5e5;strokeWidth=1.5;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=16;fontColor=#0d0d0d;fontStyle=1;
```

For an error/alert node:
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#fecaca;strokeWidth=1.5;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=16;fontColor=#0d0d0d;fontStyle=1;
```

## Design Principles

- No gradients, no shadows, no decorative elements
- White fill with light gray borders for all nodes
- Color appears only in edges and accent details
- Precision and clarity above all
- System font stack for maximum compatibility
