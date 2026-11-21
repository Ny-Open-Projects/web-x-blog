---
title: [CSS-268] width: auto/min/max/fit-content 的区别详解
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-268：width: auto / min-content / max-content / fit-content 详解

**答**：
- max-content：按「内容不换行」的理想宽度（长文本一行到底）
- min-content：按「最小可换行宽度」（每词/每字都换行后的最宽单元）
- fit-content：min(max-content, 可用空间)——先想要理想宽，不够再收缩；`fit-content(400px)` 带上限
- auto（块级默认）：撑满容器（与 fit-content 不同）；flex/grid 里的 auto 有「分配剩余空间」语义
- 实用组合：表格列 `grid-template-columns: minmax(min-content, 1fr)` 防内容溢出；标签胶囊 `width: fit-content`

```css
.tag { width: fit-content; padding: 4px 10px; }   /* 收缩到内容宽 */
td {
  /* grid 列：不小于最长单词，可伸展 */
  grid-template-columns: minmax(min-content, 1fr) 2fr;
}
.clamp { max-width: max-content; }                  /* 气泡按内容自适应 */
```
