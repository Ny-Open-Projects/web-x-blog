---
title: [CSS-085] 滚动驱动动画 scroll-timeline 怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-085：滚动驱动动画 scroll-timeline 怎么用？

**答**：
- `animation-timeline: scroll()` 建立匿名滚动时间线，动画进度跟随滚动位置而非时间。
- `scroll(nearest root block)` 可指定参照滚动容器与轴向；`view()` 则跟随元素进出视口的进度。
- 经典场景：顶部阅读进度条、视差背景、图片进入视口时 reveal。
- 时间线跨层级共享用 `timeline-scope` 把子树的命名时间线提升到公共祖先。
- Chrome 115+ 支持，用 `@supports not (animation-timeline: scroll())` 降级，JS IntersectionObserver 兜底。

```css
/* 顶部阅读进度条：进度 = 文档滚动比例 */
.progress {
  position: fixed;
  inset-block-start: 0;
  inset-inline-start: 0;
  width: 100%; height: 4px;
  background: var(--brand);
  transform-origin: 0 50%;
  transform: scaleX(0);
  animation: grow linear both;
  animation-timeline: scroll(root block); /* 进度绑定整页滚动 */
}
@keyframes grow { to { transform: scaleX(1); } }

/* 图片进入视口渐显：进度跟随自身可见比例 */
.reveal img {
  animation: reveal linear both;
  animation-timeline: view(block);
  animation-range: entry 0% cover 40%;    /* 进入视口到覆盖 40% 之间播放 */
}
@keyframes reveal { from { opacity: 0; transform: translateY(24px); } }

@supports not (animation-timeline: scroll()) {
  .progress { display: none; }            /* 降级：直接隐藏进度条 */
}
```
