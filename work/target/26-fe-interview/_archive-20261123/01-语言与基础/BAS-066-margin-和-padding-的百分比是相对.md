---
title: [BAS-066] margin 和 padding 的百分比是相对什么计算的？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-066：margin 和 padding 的百分比是相对什么计算的？
**答**：
- 四个方向的百分比一律参照包含块的**宽度**，包括 margin-top/bottom、padding-top/bottom。
- 因此 `padding-top: 56.25%` 可做出宽随容器、高为宽 16:9 的自适应占位框（老式响应式视频方案）。
- 背错成"上下参照高度"会导致布局计算全错，这是高频陷阱题。

```css
.ratio-box {
  width: 80%;
  padding-top: 56.25%;   /* 高度 = 宽度 * 0.5625，即 16:9 */
  position: relative;
}
.ratio-box > iframe {
  position: absolute; inset: 0; width: 100%; height: 100%;
}
```
