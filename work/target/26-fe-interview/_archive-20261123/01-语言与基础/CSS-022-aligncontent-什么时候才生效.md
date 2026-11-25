---
title: [CSS-022] align-content 什么时候才生效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-022：align-content 什么时候才生效？

**答**：
- 只在容器**换行**（`flex-wrap: wrap` 或 wrap-reverse）且交叉轴有剩余空间时生效。
- 作用对象是“多根轴线”，即多行整体在交叉轴上的分布。
- 单行 flex 布局设置它没有任何效果，这是高频易错点。
- 常用组合：`flex-wrap: wrap` + `align-content: flex-start` 解决多行卡片列表被拉开的问题。

```css
.grid-cards {
  display: flex;
  flex-wrap: wrap;
  height: 600px;
  align-content: flex-start; /* 多行整体靠上，而不是默认 stretch 拉开 */
  gap: 16px;
}
.grid-cards .card {
  width: calc((100% - 32px) / 3);
}
/* 若去掉 align-content，行数少时行间距会被自动拉大 */
```
