---
title: [CSS-333] 布局引擎深水：Format Context 如何决定布局
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-333：布局引擎深水：Format Context 如何决定布局

**答**：
- 布局本质：每个盒子按其建立的 Formatting Context（BFC/IFC/FFC/GFC）排布子盒子——display 决定内外两侧：`display: grid` 外部 block 级、内部建立 GFC；`inline-flex` 外部 inline、内部 FFC
- BFC 独立布局规则：内部浮动参与高度计算（清浮动原理）、不与浮动重叠（两栏自适应）、margin 不与外界折叠——BFC 是隔离边界
- Flex/Grid 内部的 margin 折叠不存在（FFC/GFC 中子项 margin 不折叠），这与 block 布局心智不同——迁移布局时最常见的「间距怎么变了」
- 尺寸解析顺序：min/max-width 约束 → flex-basis/auto 展开 → 百分比依赖包含块解析；百分比高度要求包含块有确定高度，绝对定位元素包含块是最近的定位祖先
- 布局失效粒度：改子项宽度只失效该 flex 容器子树；改视口相关单位（vw/vh）失效范围更大——用 DevTools Layout 区域（Layout Shift 区域/性能面板 Layout 事件）观察

```css
/* BFC 应用: 自适应两栏 */
.sidebar { float: left; width: 200px; }
.main { overflow: hidden; }        /* 建立 BFC, 不与浮动重叠, 自动避开侧栏 */
/* FFC 中 margin 不折叠 */
.flex { display: flex; }
.flex > div { margin: 10px 0; }    /* 相邻子项间距 20px, 不会折叠成 10px */
```
