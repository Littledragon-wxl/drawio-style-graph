# Style 8: Dark Luxury

Adapted from fireworks-tech-graph Style 8. Deep black canvas with champagne-gold accents.
Premium editorial aesthetic.

## Color Palette → Draw.io Mapping

Canvas background: `#0a0a0a` (deepest black, no blue tint)

Six semantic color buckets:

| Role | Bucket | fillColor | strokeColor | Use for |
|------|--------|-----------|-------------|---------|
| primary (service/API) | Service/API | `#111111` | `#a78bfa` | services, endpoints, APIs (soft violet) |
| success (database) | Data/Storage | `#111111` | `#38bdf8` | databases, tables, caches (sky blue) |
| warning (queue) | Infra/Config | `#111111` | `#fbbf24` | infra, pipelines, config (amber) |
| accent (gateway/API) | Service/API | `#111111` | `#a78bfa` | gateways (same as services) |
| danger (error) | Concept/Domain | `#111111` | `#f87171` | errors, concepts (soft rose) |
| secondary (logic) | Code/Logic | `#111111` | `#5a9e6f` | functions, modules, algorithms (sage) |
| neutral (external) | Meta/Doc | `#111111` | `#94a3b8` | external, docs, schemas (cool gray) |

**Gold accent**: `#d4a574` for titles, section headers, primary arrows.
**Bright gold**: `#e8c49a` for highlights.
**Dim gold**: `#c9a96e` for secondary accents.

## Typography → Draw.io Mapping

Dual-font strategy: Serif for titles, Sans-serif for body.

```
Title/Section font:  fontFamily=Georgia,Times New Roman,serif
                      fontSize=21 (diagram title), fontSize=14 (section labels)
                      fontStyle=1 (bold)
                      fontColor=#f5f0eb or fontColor=#c9a96e (gold for sections)

Node label font:     fontFamily=-apple-system,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,sans-serif
                      fontSize=13-14, fontStyle=1 (semi-bold 600)
                      fontColor=<bucket's strokeColor> (use the bucket's color for the label)

Sub-label font:      fontFamily=-apple-system,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,sans-serif
                      fontSize=10-11, fontColor=#a39787 or fontColor=#6b5f53

Code/path font:      fontFamily=Cascadia Code,SF Mono,Courier New,monospace
                      fontSize=10-11, fontColor=#a39787
```

**Rule**: Use serif only for diagram titles and section/cluster labels (≥14px). All node
names, edge labels, and fine print use sans-serif.

## Shape Preferences

```
rounded=1          (rounded corners, 6px equivalent)
whiteSpace=wrap
html=1
```

All nodes share: `fillColor=#111111`, `strokeWidth=1.5`, stroke color from bucket.

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
For gold-bordered containers: `strokeColor=#c9a96e;dashed=1;`

## Edge Style → Draw.io Mapping

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;
```

Arrow system:
| Flow Type | strokeColor | strokeWidth | Additional |
|-----------|-------------|-------------|------------|
| Primary/structural | `#d4a574` | 2 | — (gold) |
| Data flow | `#6ee7b7` | 1.5 | — (mint) |
| Control/trigger | `#fdba74` | 1.5 | — (amber-orange) |
| Reference/semantic | `#a39787` | 1 | `dashed=1` |
| Dependency | `#a78bfa` | 1 | `dashed=1` |
| Feedback/loop | `#d4a574` | 1.5 | `curved=1` |

## Extras

```
strokeWidth=1.5   (on all shapes)
sketch=0
shadow=0
```

## Complete Vertex Style Templates

For a service/API node (violet bucket):
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#111111;strokeColor=#a78bfa;strokeWidth=1.5;fontFamily=-apple-system,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,sans-serif;fontSize=13;fontColor=#a78bfa;fontStyle=1;
```

For a database node (sky blue bucket):
```
shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#111111;strokeColor=#38bdf8;strokeWidth=1.5;fontFamily=-apple-system,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,sans-serif;fontSize=13;fontColor=#38bdf8;fontStyle=1;
```

For a section title (serif, gold):
```
text;html=1;fontFamily=Georgia,Times New Roman,serif;fontSize=14;fontColor=#c9a96e;fontStyle=1;
```

## Page Background

```xml
<mxGraphModel background="#0a0a0a">
```
