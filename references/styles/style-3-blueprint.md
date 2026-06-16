# Style 3: Blueprint

Adapted from fireworks-tech-graph Style 3. Engineering blueprint aesthetic.

## Color Palette → Draw.io Mapping

Canvas background: `#0a1628` (deep navy)

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#0d1f3c` | `#00b4d8` | services, components |
| success (database) | `#0d1f3c` | `#06d6a0` | databases, storage |
| warning (queue) | `#0d1f3c` | `#f77f00` | queues, alerts |
| accent (gateway/API) | `#0d1f3c` | `#48cae4` | gateways, APIs |
| danger (error) | `#0d1f3c` | `#f77f00` | errors (orange) |
| secondary (security) | `#0d1f3c` | `#00b4d8` | security |
| neutral (external) | `none` | `#48cae4` | external (dashed, no fill) |

## Typography → Draw.io Mapping

```
fontFamily=Courier New,Lucida Console,Microsoft YaHei,SimHei,monospace
fontSize=13        (labels)
fontSize=10        (annotations)
fontSize=16        (titles, bold)
fontStyle=1        (bold, for titles)
fontColor=#caf0f8  (primary text — light cyan)
fontColor=#90e0ef  (secondary text)
fontColor=#00b4d8  (label accents)
```

## Shape Preferences

```
rounded=0          (sharp corners, 2px equivalent for technical feel)
whiteSpace=wrap
html=1
```

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
For external/optional: `dashed=1;` on the vertex style
Note: draw.io does not natively support blueprint grid backgrounds. The dark navy canvas and cyan strokes evoke the blueprint feel without needing a grid pattern.

## Edge Style → Draw.io Mapping

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

Arrow colors:
| Flow Type | strokeColor | Additional |
|-----------|-------------|------------|
| Primary flow | `#00b4d8` | — |
| Secondary | `#48cae4` | — |
| Read/retrieval | `#06d6a0` | — |
| Async/event | `#48cae4` | `dashed=1` |
| Alert/warning | `#f77f00` | — |

## Extras

```
strokeWidth=1     (thin lines for technical precision)
sketch=0
shadow=0
```

## Complete Vertex Style Template

For a service node (primary role):
```
rounded=0;whiteSpace=wrap;html=1;fillColor=#0d1f3c;strokeColor=#00b4d8;strokeWidth=1;fontFamily=Courier New,Lucida Console,Microsoft YaHei,SimHei,monospace;fontSize=13;fontColor=#caf0f8;
```

For an external node (neutral, dashed):
```
rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#48cae4;strokeWidth=1;dashed=1;fontFamily=Courier New,Lucida Console,Microsoft YaHei,SimHei,monospace;fontSize=13;fontColor=#caf0f8;
```

## Page Background

```xml
<mxGraphModel background="#0a1628">
```
