# drawio-style-graph

[English](README.md) · **中文**

> **8 种专业视觉风格 × draw.io 可编辑格式。**
> 用自然语言描述你的系统 —— 获得一张带风格、可编辑的 .drawio 图表。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![8 Visual Styles](https://img.shields.io/badge/Styles-8-purple)]()
[![14 Diagram Types](https://img.shields.io/badge/Diagram%20Types-14-green)]()
[![10k+ Shapes](https://img.shields.io/badge/Shapes-10,446-blue)]()
[![321 AI Logos](https://img.shields.io/badge/AI%20Logos-321-orange)]()

---

## 这是什么？

两个优秀的开源图表工具，融合为一：

| 🔥 fireworks-tech-graph | 📐 drawio-skill |
|---|---|
| 作者 [@yizhiyanhua-ai](https://github.com/yizhiyanhua-ai) | 作者 [@Agents365-ai](https://github.com/Agents365-ai) |
| **8 种精心设计的视觉风格**<br>Flat Icon、Dark Terminal、Blueprint、<br>Notion Clean、Glassmorphism、<br>Claude Official、OpenAI、Dark Luxury | **完整的 draw.io 引擎**<br>10,446 个厂商图标、321 个 AI Logo、<br>图表类型预设、自动布局、<br>PNG/SVG/PDF 导出管线 |
| 🎨 色彩体系 · 字体系统<br>箭头语义 · 设计 Token | 🔍 shapesearch.py · 🤖 aiicons.py<br>✅ validate.py · 🔧 repair_png.py<br>📐 autolayout.py · 🌐 encode_drawio_url.py |

两套生态完全内置 —— 无需安装任何其他 skill：

```
fireworks-tech-graph                  drawio-skill
(SVG 设计 Token)                      (draw.io 引擎 + 脚本)

    │                                      │
    │  8 种视觉风格                       │  10,446 形状搜索
    │  色彩体系                           │  321 AI 品牌 Logo
    │  字体系统                           │  图表类型预设
    │  箭头语义                           │  自动布局 (Graphviz)
    │  形状偏好                           │  验证 + 修复
    │  特效 (阴影/玻璃/手绘)              │  浏览器回退 URL
    │                                      │
    └──────────────┬───────────────────────┘
                   │  SVG Token → draw.io style= 字符串映射
                   ▼
          ┌─────────────────────┐
          │ drawio-style-graph  │
          │                     │
          │  8 种风格            │
          │  ×                  │
          │  .drawio 格式        │
          │                     │
          │  完全自包含           │
          │  零额外安装           │
          └─────────────────────┘
```

**最终效果：** 拥有 fireworks-tech-graph SVG 风格的视觉品质，
同时输出为完全**可编辑的 .drawio 文件**，可使用 draw.io 的全部形状生态。

---

## 8 种内置风格

每种风格都是完整的设计系统，已映射为 draw.io `style=` token 字符串：

| # | 风格 | 色板 | 字体 | 特征 |
|---|------|------|------|------|
| 1 | **Flat Icon** | 蓝 · 绿 · 橙 · 紫 | Helvetica, 14px | `rounded=1` |
| 2 | **Dark Terminal** | 紫 · 蓝 · 绿 霓虹 | SF Mono, 13px | `shadow=1`, 背景 `#0f0f1a` |
| 3 | **Blueprint** | 青 · 绿 · 橙 | Courier New, 13px | `rounded=0`, 背景 `#0a1628` |
| 4 | **Notion Clean** | 暖灰 · 单蓝色强调 | System UI, 14px | 极简 · 扁平 |
| 5 | **Glassmorphism** | 蓝 · 紫 · 绿 光晕 | Inter, 14px | `glass=1;shadow=1`, 背景 `#0d1117` |
| 6 | **Claude Official** | 青绿 · 蓝 · 米色 · 灰 | System UI, 16px | `strokeWidth=2.5`, 粗边框 |
| 7 | **OpenAI Official** | 白 · `#10a37f` 绿色强调 | System UI, 16px | `strokeWidth=1.5`, 精密 |
| 8 | **Dark Luxury** | 6色语义桶 · 金色箭头 | Georgia + Sans, 14px | 双字体, 背景 `#0a0a0a` |

→ [风格-图表类型兼容矩阵](references/style-diagram-matrix.md)&nbsp;&nbsp;← [如何应用风格](references/style-application-guide.md)

---

## 快速开始

### 安装

```bash
npx skills add Littledragon-wxl/drawio-style-graph
```

或通过 npm：

```bash
npm install @littledragon_wxl/drawio-style-graph
```

### 更新到最新版本

```bash
# 使用 npm 更新
npm update @littledragon_wxl/drawio-style-graph

# 或重新安装最新版本
npm install @littledragon_wxl/drawio-style-graph@latest

# 查看当前版本
npm list @littledragon_wxl/drawio-style-graph
```

### 前置条件

1. 安装 draw.io 桌面版：[下载](https://github.com/jgraph/drawio-desktop/releases)
2. Python 3（用于辅助脚本）
3. Graphviz（可选）：`brew install graphviz`

**仅此而已。** 无需安装其他 skill —— 一切已内置。

### 使用方式

```
"用 Dark Terminal 风格画一个微服务架构图"
"用 Notion Clean 风格生成博客系统的 ER 图"
"用 Glassmorphism 风格生成一个 AI Agent 架构图"
```

---

## SVG Token 到 Draw.io 的映射

| SVG / 设计 Token | Draw.io 等效写法 |
|---|---|
| `fill: #eff6ff` | `fillColor=#eff6ff`（顶点 style 中） |
| `stroke: #bfdbfe` | `strokeColor=#bfdbfe`（顶点 style 中） |
| `rx: 8px`（圆角半径） | `rounded=1`（`rounded=0` 为直角） |
| `font-family: Helvetica` | `fontFamily=Helvetica`（顶点 style 中） |
| `font-size: 14px` | `fontSize=14`（顶点 style 中） |
| `font-weight: 600` | `fontStyle=1`（粗体，顶点 style 中） |
| `color: #111827` | `fontColor=#111827`（顶点 style 中） |
| 箭头 marker `fill` | `strokeColor=#xxxxxx`（边上） |
| `stroke-dasharray: 5,3` | `dashed=1`（边上） |
| `filter: drop-shadow` | `shadow=1` 或 `glass=1`（顶点 style 中） |
| 手绘/粗糙边缘 | `sketch=1`（顶点 + 边 style 中） |

---

## 内置内容

| 目录 | 内容 |
|------|------|
| `scripts/` | 11 个 Python 脚本：shapesearch（10,446 形状）、aiicons（321 AI Logo）、validate、repair_png、autolayout、encode_drawio_url，以及 5 个项目结构导入器 |
| `data/` | `shape-index.json.gz` + `lobe-icons.json` |
| `references/` | diagram-types.md、shapes.md、troubleshooting.md、autolayout.md、style-presets.md、style-extraction.md、style-diagram-matrix.md、style-application-guide.md，以及 8 个风格参考文件 |
| `styles/` | 3 个 draw.io 内置预设（`default.json`、`corporate.json`、`handdrawn.json`）+ 2 个 JSON Schema |

**支持的图表类型：** 架构图 · 数据流图 · 流程图 · Agent/记忆架构 ·
时序图 · UML 类图 · 用例图 · 状态机 · ER 图 · 网络拓扑 ·
ML/DL 模型 · 思维导图 · 对比矩阵 · 时间线/甘特图

---

## 许可证

MIT

---

## 致谢

本项目站在两个优秀开源社区的肩膀上：

### 🔥 fireworks-tech-graph

8 种视觉风格及其设计 Token 改编自
**[fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**
作者 [@yizhiyanhua-ai](https://github.com/yizhiyanhua-ai)。

继承的能力：为每种语义角色精心调配的色板（primary `#eff6ff`/`#bfdbfe`、
success `#f0fdf4`/`#bbf7d0`、warning `#fff7ed`/`#fed7aa`、accent `#faf5ff`/`#e9d5ff`、
danger `#fef2f2`/`#fecaca`、secondary `#f0fdfa`/`#ccfbf1`、neutral `#f9fafb`/`#e5e7eb`），
完整的字体系统（从 Helvetica 到 SF Mono 到 Georgia），按流向类型颜色编码的箭头语义，
风格与图表类型兼容性研究（14 种类型 × 8 种风格），以及 AI 创作的 Dark Luxury 风格
（双衬线/无衬线字体系统，6 语义色桶）。

### 📐 drawio-skill

draw.io 引擎整合自
**[drawio-skill](https://github.com/Agents365-ai/drawio-skill)**
作者 [@Agents365-ai](https://github.com/Agents365-ai)。

继承的能力：11 个经过生产环境验证的 Python 脚本，覆盖完整的 draw.io 生命周期 ——
跨 10,446 个厂商图标的形状搜索（AWS/Azure/GCP/Cisco/K8s）、AI/LLM 品牌 Logo 解析
（321 个品牌，通过 lobe-icons + simple-icons CDN）、确定性结构验证（悬空边、重复 ID、
断裂的父引用）、针对 draw.io CLI 截断 bug 的 PNG IEND 块修复、基于 Graphviz 的大图
自动布局、浏览器回退 URL 编码，以及 Python/JS-TS/Go/Rust 的项目结构导入器。此外还有
图表类型预设系统（ERD/UML Class/Sequence/ML-DL/Flowchart）和风格预设学习/保存/管理框架。

### 图标库

- AI/LLM 品牌 Logo 来自 [lobe-icons](https://github.com/lobehub/lobe-icons)（MIT）
- 数据存储图标来自 [simple-icons](https://simpleicons.org)（CC0）
