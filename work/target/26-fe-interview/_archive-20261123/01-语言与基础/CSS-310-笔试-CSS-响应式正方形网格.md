---
title: [CSS-310] 笔试：CSS 响应式正方形网格
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-310：笔试：CSS 响应式正方形网格

**题目**：实现自适应网格：不写媒体查询，列数随容器宽度自动变化（每列最小 160px）；所有格子保持正方形；图片填满裁剪。

**答**：
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 8px;
}
.grid > * {
  aspect-ratio: 1;              /* 正方形：无需 padding-top hack */
  overflow: hidden;
}
.grid img {
  width: 100%; height: 100%;
  object-fit: cover;            /* 填满裁剪 */
}
```
```css
/* 变体：容器查询版（组件级自适应，比视口断点更准） */
.widget { container-type: inline-size; }
@container (min-width: 500px) {
  .grid { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
}
```

**评分点**：
- repeat(auto-fill, minmax(160px, 1fr)) 的自动列数（核心，一行替代多个断点）
- auto-fill vs auto-fit 的区别能讲清（前者保留空轨道、后者拉伸合并）
- aspect-ratio 正方形（现代方案）与 padding-bottom: 100% 老方案对比
- object-fit: cover 裁剪
