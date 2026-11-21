---
title: [CSS-025] flex-basis 与 width 谁优先生效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-025：flex-basis 与 width 谁优先生效？

**答**：
- 主轴为水平时，`flex-basis` 优先于 `width`；basis 为 `auto` 时才回退到 width。
- 主轴为垂直（column）时，basis 优先于 `height`。
- `flex-basis: 0` 与 `auto` 是 flex:1 和 flex:auto 行为差异的根源。
- min-width/max-width 仍会约束最终结果，优先级高于 basis 与 width。

```css
.item {
  width: 300px;
  flex-basis: 200px; /* 生效：主轴基准取 200 而非 300 */
}
.item-auto {
  width: 300px;
  flex-basis: auto;  /* 回退使用 width = 300 */
}
.item-max {
  flex: 1 0 500px;
  max-width: 400px;  /* 最终被 max-width 限制在 400 */
}
```
