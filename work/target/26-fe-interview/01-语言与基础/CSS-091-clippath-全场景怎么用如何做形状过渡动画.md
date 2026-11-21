---
title: [CSS-091] clip-path 全场景怎么用？如何做形状过渡动画？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-091：clip-path 全场景怎么用？如何做形状过渡动画？

**答**：
- `polygon()` 画三角形/箭头/斜切卡，`circle()/ellipse()` 画圆与椭圆，`inset()` 做缺角与圆角裁剪。
- 两端关键帧的顶点数一致时，clip-path 可直接 transition，实现形状 morph。
- 头像变圆、卡片展开、图片揭示动画都是 clip-path 过渡的典型场景。
- 裁剪不改变布局占位（不同于 display），过渡期间无重排，性能好。
- 老浏览器需 `-webkit-clip-path`，现代浏览器可省。

```css
/* 1. 三角形提示 */
.tri { width: 20px; height: 20px; background: var(--bg-elevated);
       clip-path: polygon(0 0, 100% 0, 50% 100%); }

/* 2. 头像：方形 hover 变圆（顶点语义匹配的 morph） */
.avatar-morph {
  clip-path: inset(0 round 4px);
  transition: clip-path 0.4s var(--ease-out);
}
.avatar-morph:hover { clip-path: inset(0 round 50%); }

/* 3. 图片揭示：对角线展开 */
.reveal-clip {
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  transition: clip-path 0.6s var(--ease-out);
}
.reveal-clip.is-in {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
```
