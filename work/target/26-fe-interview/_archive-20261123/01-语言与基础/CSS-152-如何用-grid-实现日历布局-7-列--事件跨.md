---
title: [CSS-152] 如何用 grid 实现日历布局（7 列 + 事件跨行跨列）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-152：如何用 grid 实现日历布局（7 列 + 事件跨行跨列）？

**答**：
- 骨架：`repeat(7, 1fr)` 七列 + `grid-auto-rows` 定行高，日期格子按“第几周第几天”用 CSS 变量定位 `--col/--row`。
- 跨天事件：`grid-column: var(--col) / span var(--span)` 横向延伸，`--span` 由 JS 按天数算出。
- 事件层压在日期层上：两个层各自 `grid-row` 定位，事件 `z-index` 抬高。
- 全月固定 6 行时高度稳定；不固定行数时用隐式行 auto-rows 兜底。

```css
/* 结构：.calendar > 42 个 .day + 若干 .event
   JS 为每个元素计算 --col 列号 1~7、--row 行号、--span 跨越天数 */
.calendar {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 64px;          /* 每周一行，行高固定 */
  gap: 1px;
  background: #e5e7eb;           /* 缝隙当分割线 */
}
.calendar .day {
  background: #fff;
  grid-column: var(--col);
  grid-row: var(--row);
  padding: 4px;
  font-size: 12px;
}
/* 跨天事件：从起始列横向 span N 天 */
.calendar .event {
  grid-column: var(--col) / span var(--span, 1);
  grid-row: var(--row);
  z-index: 1;                    /* 压在日期格上方 */
  align-self: center;
  margin: 0 2px;
  padding: 2px 6px;
  border-radius: 4px;
  background: #096;
  color: #fff;
  font-size: 12px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
/* 示例：周三开始持续 3 天的事件
   style="--col: 3; --row: 2; --span: 3" */
```

## 二十五、动效实战案例
