---
title: [CSS-285] CSS 动画与 JS 动画的取舍：WAAPI 是什么
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-285：CSS 动画与 JS 动画的取舍：WAAPI 是什么

**答**：
- 三种手段：CSS transition（状态切换）、CSS animation（关键帧序列）、WAAPI（Element.animate，JS 驱动的声明式动画）
- WAAPI 定位：CSS 动画的能力 + JS 的动态性——关键帧可运行时生成（数据驱动的粒子/仪表盘）、动画对象可控制（pause/seek/reverse）
- 与 rAF JS 动画的区别：WAAPI 在合成器侧运行（transform/opacity 动画脱离主线程），rAF 每帧跑主线程
- 取舍：简单状态过渡用 CSS；需要「动态参数/进度控制/取消」用 WAAPI；复杂物理效果用动画库（GSAP/motion）
- Promise 支持：`anim.finished` 等待动画结束，告别 animationend 监听

```javascript
const anim = el.animate([
  { transform: 'scale(1)', opacity: 1 },
  { transform: 'scale(1.2)', opacity: 0 },
], { duration: 300, easing: 'ease-out', fill: 'forwards' });
await anim.finished;
el.remove(); // 比 animationend 事件可靠（不冒泡/不延迟）
```
