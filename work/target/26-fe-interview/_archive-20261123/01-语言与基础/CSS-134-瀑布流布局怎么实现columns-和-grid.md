---
title: [CSS-134] 瀑布流布局怎么实现？columns 和 grid 两种方案各有什么坑？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-134：瀑布流布局怎么实现？columns 和 grid 两种方案各有什么坑？

**答**：
- columns 方案：`columns: 4 240px` + `break-inside: avoid`，纯 CSS 零 JS；但填充顺序是纵向的（先填满第一列），列表有顺序语义时不可接受。
- grid row span 方案：先按普通网格排（顺序正确），用 JS 把每个 item 的高度换算成 `grid-auto-rows` 的整数倍，设为 `--span`；顺序与视觉双正确，需要少量 JS。
- 通用坑：图片未加载完成时高度为 0，必须等图片加载后再测高（或预设宽高比占位）。
- 列间距 gap 两方案都支持；columns 方案的 item 底部 margin 在断列处会被裁掉，用 padding 代替。

```css
/* 方案一：columns，纯 CSS，顺序为纵向填充 */
.masonry-columns {
  columns: 4 240px;   /* 4 列，每列最小 240px，自动降列 */
  column-gap: 16px;
}
.masonry-columns .item {
  break-inside: avoid;      /* 禁止卡片被拆到两列 */
  margin-bottom: 16px;
}

/* 方案二：grid row span，顺序正确，JS 只负责算跨度 */
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 8px;      /* 最小跨度单位，决定纵向颗粒度 */
  gap: 0 16px;
}
.masonry-grid .item {
  grid-row-end: span var(--span, 12);
}
/* JS：item.style.setProperty('--span', Math.ceil((h + 16) / 8))
   h 为卡片实际高度（含底边距），渲染/图片 onload 后重算 */
```
