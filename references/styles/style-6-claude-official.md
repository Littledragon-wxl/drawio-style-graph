# Style 6: Claude Official

Adapted from fireworks-tech-graph Style 6. Warm, approachable, Anthropic-style.

## Color Palette → Draw.io Mapping

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#9dd4c7` | `#4a4a4a` | services, agent/process (teal-green) |
| success (database) | `#e8e6e3` | `#4a4a4a` | databases, storage (light gray) |
| warning (queue) | `#f4e4c1` | `#4a4a4a` | queues, bus, infrastructure (beige) |
| accent (gateway/API) | `#a8c5e6` | `#4a4a4a` | gateways, APIs, input (soft blue) |
| danger (error) | `#f4c1c1` | `#4a4a4a` | errors, alerts (soft pink) |
| secondary (security) | `#9dd4c7` | `#4a4a4a` | security (reuse agent color) |
| neutral (external) | `#f8f6f3` | `#4a4a4a` | external systems (background cream) |

Note: All nodes share the same dark gray stroke (`#4a4a4a`), creating visual cohesion.

## Typography → Draw.io Mapping

```
fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif
fontSize=16        (node labels, semi-bold)
fontSize=14        (descriptions)
fontSize=13        (arrow labels)
fontSize=18        (titles, bold)
fontStyle=1        (bold for labels and titles)
fontStyle=0        (regular for descriptions)
fontColor=#1a1a1a  (primary text — near black)
fontColor=#6a6a6a  (secondary text — medium gray)
fontColor=#5a5a5a  (arrow labels)
```

## Shape Preferences

```
rounded=1          (rounded corners, 12px equivalent)
whiteSpace=wrap
html=1
```

All boxes use `strokeWidth=2.5` for the thick, warm border look.

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`

## Edge Style → Draw.io Mapping

Base edge style — all arrows use the same dark gray:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#5a5a5a;strokeWidth=2;
```

Arrow semantics through dash patterns only:
| Flow Type | Additional |
|-----------|------------|
| Primary data flow | — (solid) |
| Memory write | `dashed=1` |
| Memory read | — (solid) |
| Control/trigger | `dashed=1` |

## Extras

```
strokeWidth=2.5   (thick warm borders on all shapes)
sketch=0
shadow=0
```

## Complete Vertex Style Template

For a service/agent node (primary, teal-green):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#9dd4c7;strokeColor=#4a4a4a;strokeWidth=2.5;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=16;fontColor=#1a1a1a;fontStyle=1;
```

For an input/source node (blue):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#a8c5e6;strokeColor=#4a4a4a;strokeWidth=2.5;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=16;fontColor=#1a1a1a;fontStyle=1;
```

For an infrastructure/bus node (beige):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#f4e4c1;strokeColor=#4a4a4a;strokeWidth=2.5;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=16;fontColor=#1a1a1a;fontStyle=1;
```
