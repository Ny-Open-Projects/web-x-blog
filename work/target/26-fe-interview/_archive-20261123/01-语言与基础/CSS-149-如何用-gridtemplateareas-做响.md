---
title: [CSS-149] 如何用 grid-template-areas 做响应式重排？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-149：如何用 grid-template-areas 做响应式重排？

**答**：
- 把区域命名成“地图”，组件只挂 `grid-area: 名字`；响应式只需在每个断点重画地图，组件声明零改动。
- 这是“结构与断点解耦”的最佳实践：新增断点 = 新增一张地图，不碰任何组件选择器。
- 注意：同一区域名必须连成矩形，L 形区域非法会整条声明失效。
- 与 order 相比，areas 重排不影响可访问性（不改变 DOM），配合媒体查询是后台/门户页标准方案。

```css
/* 结构：.dash > nav + main + aside，三者只声明 grid-area */
.dash {
  display: grid;
  gap: 12px;
  grid-template-areas:
    "nav  main"
    "nav  side";
  grid-template-columns: 220px 1fr;
  grid-template-rows: 1fr auto;
  min-height: 100dvh;
}
.dash nav  { grid-area: nav; }
.dash main { grid-area: main; }
.dash aside { grid-area: side; }

/* 断点重排：只换地图，组件不动 */
@media (max-width: 768px) {
  .dash {
    grid-template-areas:
      "nav"
      "main"
      "side";
    grid-template-columns: 1fr;
    grid-template-rows: 56px 1fr auto;
  }
}
```
