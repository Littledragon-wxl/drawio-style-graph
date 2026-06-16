# Style 1: Flat Icon (Default)

Adapted from fireworks-tech-graph Style 1. Clean, colorful, draw.io-native aesthetic.

## Color Palette → Draw.io Mapping

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#eff6ff` | `#bfdbfe` | services, clients, main components |
| success (database) | `#f0fdf4` | `#bbf7d0` | databases, storage |
| warning (queue) | `#fff7ed` | `#fed7aa` | queues, decisions |
| accent (gateway/API) | `#faf5ff` | `#e9d5ff` | gateways, APIs, orchestration |
| danger (error) | `#fef2f2` | `#fecaca` | errors, alerts |
| secondary (security) | `#f0fdfa` | `#ccfbf1` | security, auth |
| neutral (external) | `#f9fafb` | `#e5e7eb` | external systems, neutral |

## Typography → Draw.io Mapping

```
fontFamily=Helvetica Neue,Helvetica,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif
fontSize=14        (labels)
fontSize=12        (sub-labels)
fontSize=16        (titles)
fontStyle=1        (bold, for titles)
fontColor=#111827  (primary text)
fontColor=#6b7280  (secondary text)
```

## Shape Preferences

```
rounded=1          (rounded corners, 8px equivalent)
whiteSpace=wrap
html=1
```

For standard boxes: `rounded=1;whiteSpace=wrap;html=1;`
For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
For decisions: `rhombus;whiteSpace=wrap;html=1;`
For clouds: `cloud;whiteSpace=wrap;html=1;`
For documents: `shape=document;whiteSpace=wrap;html=1;`

## Edge Style → Draw.io Mapping

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;
```

Arrow colors (append to edge style):
| Flow Type | strokeColor | Additional |
|-----------|-------------|------------|
| Primary data flow | `#2563eb` | — |
| Secondary/alt | `#dc2626` | — |
| Data/retrieval | `#16a34a` | — |
| Async/event | `#9333ea` | `dashed=1` |
| Control/trigger | `#ea580c` | — |

## Extras

```
strokeWidth=1.5   (on all shapes)
sketch=0          (no sketch mode)
shadow=0          (no drop shadows)
```

## Complete Vertex Style Template

For a service node (primary role):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#bfdbfe;strokeWidth=1.5;fontFamily=Helvetica Neue,Helvetica,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=14;fontColor=#111827;
```

## Complete Edge Style Template

For a primary data flow edge:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2563eb;strokeWidth=1.5;
```
