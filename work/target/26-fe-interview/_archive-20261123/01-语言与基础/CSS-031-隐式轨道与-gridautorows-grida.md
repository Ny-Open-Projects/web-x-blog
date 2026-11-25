---
title: [CSS-031] 隐式轨道与 grid-auto-rows、grid-auto-flow 是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-031：隐式轨道与 grid-auto-rows、grid-auto-flow 是什么？

**答**：
- 超出 `grid-template-*` 定义范围的单元格会落入隐式轨道，尺寸由 `grid-auto-rows/auto-columns` 决定。
- `grid-auto-flow: row/column/dense` 控制自动放置算法的方向，`dense` 会回填空隙。
- 列表长度不定时常用 `grid-auto-rows: minmax(100px, auto)` 统一隐式行。
- dense 适合瀑布流式填充，但会改变视觉顺序，注意可访问性。

```css
.masonry {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 10px;    /* 隐式行做最小刻度 */
  grid-auto-flow: dense;   /* 自动回填空隙 */
}
.masonry .item {
  grid-row: span 6;        /* 用行数近似瀑布流高度 */
}
.masonry .tall { grid-row: span 12; }
```
