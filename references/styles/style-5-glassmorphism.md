# Style 5: Glassmorphism

Adapted from fireworks-tech-graph Style 5. Frosted glass cards on dark background.

## Color Palette → Draw.io Mapping

Canvas background: `#0d1117` (dark, simulating the gradient base)

Note: True glassmorphism (backdrop-filter blur) is not natively supported in draw.io.
We simulate it with low-opacity fills, light borders, and shadow effects.

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#1a2332` | `#58a6ff` | services, main components (blue glow) |
| success (database) | `#1a2e1a` | `#3fb950` | databases, storage (green glow) |
| warning (queue) | `#2e1f1a` | `#f78166` | queues (orange glow) |
| accent (gateway/API) | `#1f1a2e` | `#bc8cff` | gateways, APIs (purple glow) |
| danger (error) | `#2e1a1a` | `#f85149` | errors, alerts |
| secondary (security) | `#1a2332` | `#58a6ff` | security |
| neutral (external) | `#161b22` | `#30363d` | external systems (muted) |

## Typography → Draw.io Mapping

```
fontFamily=Inter,-apple-system,SF Pro Display,PingFang SC,Microsoft YaHei,SimHei,sans-serif
fontSize=14        (labels)
fontSize=12        (sub-labels)
fontSize=20        (hero titles)
fontStyle=1        (bold, for titles)
fontStyle=0        (semi-bold equivalent for labels)
fontColor=#f0f6fc  (primary text — near white)
fontColor=#8b949e  (secondary text — muted)
```

## Shape Preferences

```
rounded=1          (rounded corners, 12px equivalent)
whiteSpace=wrap
html=1
glass=1            (draw.io's built-in glass effect)
shadow=1           (simulates glow)
```

The `glass=1` style in draw.io creates a semi-transparent look that approximates the frosted glass effect.

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;glass=1;`

## Edge Style → Draw.io Mapping

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;
```

Arrow colors (match source node's glow color):
| Flow Type | strokeColor | Additional |
|-----------|-------------|------------|
| Blue flow | `#58a6ff` | — |
| Purple flow | `#bc8cff` | — |
| Green flow | `#3fb950` | — |
| Orange flow | `#f78166` | — |
| Async/event | `#8b949e` | `dashed=1` |

## Extras

```
strokeWidth=1     (thin borders for glass cards)
glass=1           (on all shapes)
shadow=1          (on all shapes)
sketch=0
```

## Complete Vertex Style Template

For a service node (primary, blue glow):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#1a2332;strokeColor=#58a6ff;strokeWidth=1;fontFamily=Inter,-apple-system,SF Pro Display,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=14;fontColor=#f0f6fc;glass=1;shadow=1;
```

## Page Background

```xml
<mxGraphModel background="#0d1117">
```
