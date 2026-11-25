---
title: [CSS-253] masonry 瀑布流的原生 CSS 方案现状
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-253：masonry 瀑布流的原生 CSS 方案现状

**答**：
- 三个候选方案：① Grid 的 `grid-template-rows/columns: masonry`（规范主线）② columns 多列布局（现行可用的近似）③ flex 分列（JS 计算）
- Grid masonry 争议：masonry 放置算法与「行序可访问性」矛盾（Tab 顺序乱），W3C 内部有分歧，Safari 推、Mozilla 存疑——落地时间不确定
- 现行生产方案：`columns: 4; column-gap: 16px;` + 子项 `break-inside: avoid`——简单但顺序是「列优先」（视觉顺序 ≠ DOM 顺序）
- 需要行序时的替代：CSS Grid 的 dense 填充（近似）或 JS Masonry 库
- 面试话术：先问「顺序敏感吗」再选方案，体现方案对比意识

```css
/* 现行可用：列优先瀑布流 */
.gallery { columns: 4; column-gap: 16px; }
.gallery > * { break-inside: avoid; margin-bottom: 16px; }

/* 未来：Grid masonry（实验中） */
/* .gallery { display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: masonry; } */
```
