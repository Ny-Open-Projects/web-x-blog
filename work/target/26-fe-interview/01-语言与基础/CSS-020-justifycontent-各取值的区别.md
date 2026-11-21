---
title: [CSS-020] justify-content 各取值的区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-020：justify-content 各取值的区别？

**答**：
- `flex-start/flex-end/center`：起点对齐/终点对齐/居中。
- `space-between`：两端贴边，中间等分剩余空隙。
- `space-around`：每个项目两侧空隙相等，所以项目之间空隙是边缘的两倍。
- `space-evenly`：所有空隙（含边缘）完全相等。
- 剩余空间不足时这些都收拢为 flex-start，配合 overflow 处理。

```css
.demo {
  display: flex;
  gap: 8px;
}
.demo.start  { justify-content: flex-start; }
.demo.center { justify-content: center; }
.demo.between{ justify-content: space-between; }
.demo.around { justify-content: space-around; }
.demo.evenly { justify-content: space-evenly; }
/* 三个子项宽度 100，容器 500，剩余 200：
   between 边缘 0 / 中间 100
   around 边缘 33.3 / 中间 66.7
   evenly 边缘 50 / 中间 50 */
```
