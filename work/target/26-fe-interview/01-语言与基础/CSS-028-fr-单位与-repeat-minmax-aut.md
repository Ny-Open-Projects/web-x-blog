---
title: [CSS-028] fr 单位与 repeat、minmax、auto-fill 如何配合实现响应式列？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-028：fr 单位与 repeat、minmax、auto-fill 如何配合实现响应式列？

**答**：
- `fr` 表示剩余空间的份数，`grid-template-columns: 1fr 2fr` 即 1:2 分配。
- `repeat(auto-fill, minmax(200px, 1fr))` 是响应式卡片栅格的万能模板：列宽最小 200px，能放几列放几列，剩余均分。
- `auto-fill` 尽可能多地创建轨道（空轨道保留），`auto-fit` 会折叠空轨道让内容拉伸填满。
- minmax 限定轨道尺寸范围，避免过窄或过宽。

```css
/* 响应式卡片栅格：无需媒体查询 */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}

/* 1:2 两列 */
.split {
  display: grid;
  grid-template-columns: 1fr 2fr;
}

/* auto-fill 与 auto-fit 的差异在项目少时可见 */
.fill  { display: grid; grid-template-columns: repeat(auto-fill,  minmax(100px, 1fr)); }
.fit   { display: grid; grid-template-columns: repeat(auto-fit,   minmax(100px, 1fr)); }
```
