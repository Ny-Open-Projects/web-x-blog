---
title: [CSS-347] 滚动时间线：scroll() 与 view() 驱动动画
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-347：滚动时间线：scroll() 与 view() 驱动动画

**答**：
- 两种时间线：scroll()（滚动容器进度：scroll(root) 整页 / scroll(nearest) 最近滚动祖先）、view()（元素在视口中的进出进度：view(block)）——动画进度由合成器从滚动位置直接推导
- 架构价值：滚动驱动动画（视差/进度条/吸顶淡入）不再监听 scroll 事件（主线程）——合成器直接吃滚动偏移驱动，主线程零成本，掉帧时动画与滚动仍同步
- timeline-scope：动画元素与滚动容器不是祖先关系时，用 timeline-scope 把命名时间线提升到公共祖先
- range 控制：view-timeline 的 animation-range（entry/exit/cover 等区间）精确控制动画触发的视口区段——「进入视口 20% 时淡入」这类声明
- 降级：不支持时回退 scroll 事件 + rAF 方案；@supports (animation-timeline: scroll()) 分支

```css
/* 阅读进度条: 合成器驱动, 零主线程 */
.progress {
  transform-origin: 0 50%;
  transform: scaleX(0);
  animation: grow linear;
  animation-timeline: scroll(root);
}
@keyframes grow { to { transform: scaleX(1); } }

/* 进入视口淡入 */
.reveal {
  animation: fade-in linear both;
  animation-timeline: view(block);
  animation-range: entry 20% cover 40%;
}
@keyframes fade-in { from { opacity: 0; transform: translateY(20px); } }
```
