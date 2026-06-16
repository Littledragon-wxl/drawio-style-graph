# Style 2: Dark Terminal

Adapted from fireworks-tech-graph Style 2. Neon-on-dark hacker aesthetic.

## Color Palette → Draw.io Mapping

Canvas background: `#0f0f1a` (set in mxGraphModel `background` attribute or as page background)

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (AI/ML) | `#1e1b4b` | `#7c3aed` | AI/ML, LLM, model nodes |
| success (database) | `#052e16` | `#059669` | databases, storage |
| warning (queue) | `#1c1917` | `#ea580c` | queues, async messaging |
| accent (gateway/API) | `#1e3a5f` | `#3b82f6` | gateways, APIs, network |
| danger (error) | `#450a0a` | `#dc2626` | errors, alerts |
| secondary (security) | `#1e1b4b` | `#a855f7` | security, auth |
| neutral (external) | `#0f172a` | `#334155` | external systems |

## Typography → Draw.io Mapping

```
fontFamily=SF Mono,Fira Code,Cascadia Code,Courier New,Microsoft YaHei,SimHei,monospace
fontSize=13        (labels)
fontSize=11        (sub-labels)
fontSize=15        (titles)
fontStyle=1        (bold, for titles/section headers)
fontColor=#e2e8f0  (primary text — near white)
fontColor=#94a3b8  (secondary text — muted)
```

## Shape Preferences

```
rounded=1          (rounded corners, 6px equivalent)
whiteSpace=wrap
html=1
```

For AI/ML nodes (primary role): add `shadow=1;` for glow effect.
For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
For queues: `rounded=1;whiteSpace=wrap;html=1;`

## Edge Style → Draw.io Mapping

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;
```

Arrow colors (append to edge style):
| Flow Type | strokeColor | Additional |
|-----------|-------------|------------|
| Purple (AI/ML) | `#a855f7` | — |
| Orange (compute/API) | `#f97316` | — |
| Blue (network/gateway) | `#3b82f6` | — |
| Green (storage/DB) | `#10b981` | — |
| Gold (highlight) | `#eab308` | — |
| Async/event | `#94a3b8` | `dashed=1` |

## Extras

```
strokeWidth=1.5   (on all shapes)
shadow=1          (on primary nodes for glow)
sketch=0
```

## Complete Vertex Style Template

For an AI/ML node (primary role):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#1e1b4b;strokeColor=#7c3aed;strokeWidth=1.5;fontFamily=SF Mono,Fira Code,Cascadia Code,Courier New,Microsoft YaHei,SimHei,monospace;fontSize=13;fontColor=#e2e8f0;shadow=1;
```

## Page Background

Set in `<mxGraphModel>` or `<diagram>`:
```xml
<mxGraphModel background="#0f0f1a">
```
