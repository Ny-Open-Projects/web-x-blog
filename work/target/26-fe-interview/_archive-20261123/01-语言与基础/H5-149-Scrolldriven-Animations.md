---
title: [H5-149] Scroll-driven Animations（CSS scroll-timeline）怎么用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-149：Scroll-driven Animations（CSS scroll-timeline）怎么用？
**答**：
- 现代语法：`animation-timeline: scroll()`（滚动容器进度做时间轴）或 `view()`（元素进出视口的进度做时间轴），配合 `animation-range`（entry/cover/exit 区间）控制起止。
- 全程合成器驱动、零 JS——阅读进度条、视差、逐段高亮这类"进度映射"动画的最佳方案，替代监听 scroll 手算。
- `animation-duration: auto` 或 `linear both` 配合：时间轴替代时间驱动，动画进度 = 滚动进度。
- 降级：`@supports not (animation-timeline: scroll())` 包裹回退样式，保证不支持时内容可用。

```css
/* 1) scroll()：以滚动容器的滚动进度作为时间轴 */
.hero h1 {
  animation: fade-slide linear both;
  animation-timeline: scroll(root);       /* root = 文档滚动条 */
  animation-range: 0 60vh;                /* 滚过 0~60vh 区间完成动画 */
}
@keyframes fade-slide {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: none; }
}

/* 2) view()：元素自身进入/离开视口的进度 */
figure.reveal {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;    /* 从开始进入到占据视口 40% 之间 */
}
@keyframes reveal {
  from { opacity: 0; translate: 0 30px; }
  to   { opacity: 1; translate: 0 0; }
}

/* 3) 实用案例：顶部阅读进度条（原来要监听 scroll + 算高度，现在零 JS） */
#progress {
  position: fixed; inset: 0 100% 0 0;     /* right: 100% 起点为 0 宽 */
  background: #2563eb;
  transform-origin: 0 50%;
  animation: grow linear;
  animation-timeline: scroll(root);
}
@keyframes grow { from { scale: 0 1; } to { scale: 1 1; } }

/* 4) 降级：不支持时保证内容可用 */
@supports not (animation-timeline: scroll()) {
  .hero h1, figure.reveal { opacity: 1; }
}
/* 对照 JS 方案：IntersectionObserver + rAF 手算进度 —— 能做但每帧在主线程，
   代码量数倍；进度条/视差/逐段高亮这类"进度映射"首选 CSS 时间轴 */
```
