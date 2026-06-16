# Style 4: Notion Clean

Adapted from fireworks-tech-graph Style 4. Minimal, documentation-friendly.

## Color Palette → Draw.io Mapping

| Role | fillColor | strokeColor | Use for |
|------|-----------|-------------|---------|
| primary (service) | `#f9fafb` | `#e5e7eb` | services, main components |
| success (database) | `#f9fafb` | `#e5e7eb` | databases, storage |
| warning (queue) | `#f9fafb` | `#e5e7eb` | queues, decisions |
| accent (gateway/API) | `#f9fafb` | `#e5e7eb` | gateways, APIs |
| danger (error) | `#fef2f2` | `#fecaca` | errors, alerts |
| secondary (security) | `#f9fafb` | `#e5e7eb` | security, auth |
| neutral (external) | `#ffffff` | `#e5e7eb` | external systems |

Note: This style intentionally uses minimal color variation — all standard nodes share the same fill/stroke. Only error/alert nodes get a pink tint to stand out.

## Typography → Draw.io Mapping

```
fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif
fontSize=14        (labels)
fontSize=11        (type labels, uppercase)
fontSize=18        (titles)
fontStyle=1        (bold, for titles)
fontColor=#111827  (primary text — near black)
fontColor=#374151  (secondary text — gray-700)
fontColor=#9ca3af  (muted — for type labels like "DATABASE")
```

## Shape Preferences

```
rounded=1          (rounded corners, 4px equivalent)
whiteSpace=wrap
html=1
```

For databases: `shape=cylinder3;whiteSpace=wrap;html=1;`
Container sections: `swimlane;startSize=30;dashed=1;` with muted borders

## Edge Style → Draw.io Mapping

This style uses a SINGLE arrow color for all connections (clean, minimal).

Base edge style:
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#3b82f6;strokeWidth=1.5;
```

Secondary flows (gray):
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#d1d5db;strokeWidth=1;dashed=1;
```

## Extras

```
strokeWidth=1     (on all shapes — thin borders)
sketch=0
shadow=0          (no shadows — flat design)
```

## Complete Vertex Style Template

For a standard node:
```
rounded=1;whiteSpace=wrap;html=1;fillColor=#f9fafb;strokeColor=#e5e7eb;strokeWidth=1;fontFamily=-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,PingFang SC,Microsoft YaHei,SimHei,sans-serif;fontSize=14;fontColor=#111827;
```

## Design Principles

- No decorative icons — geometric shapes only
- Generous whitespace — 24px+ padding
- Single arrow color for all primary flows
- Type labels in UPPERCASE 11px (e.g., "SERVICE", "DATABASE")
- No gradients, no shadows, strictly flat
