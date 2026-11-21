---
title: [CSS-182] element.animate（WAAPI）与 CSS 动画如何分工协调？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-182：element.animate（WAAPI）与 CSS 动画如何分工协调？

**答**：
- WAAPI 适合：起止值由 JS 计算的动画、需要暂停/反向/变速、需要 `finished` Promise 做时序编排的动画。
- CSS 适合：hover 态、循环装饰动画、纯状态切换——声明式、零 JS。
- 桥梁 API：`element.getAnimations()` 能把 CSS 动画也抓过来统一控制（暂停、updatePlaybackRate），调试与全局动效开关很实用。
- 性能上两者一致（都走合成器可加速 transform/opacity）；WAAPI `fill: forwards` 会永久占住样式，结束记得 `commitStyles()` 或取消。

```javascript
// WAAPI：JS 计算起止 + 时序编排
const anim = el.animate(
  [
    { transform: 'translateX(0)', opacity: 1 },
    { transform: `translateX(${targetX}px)`, opacity: .6 },
  ],
  { duration: 300, easing: 'ease-out', fill: 'forwards' }
);
await anim.finished;          // Promise 时机，精确于 setTimeout
anim.commitStyles();          // 固化最终状态到内联样式
anim.cancel();                // 释放 fill 占用

// 控制能力：暂停/反向/变速
anim.pause();
anim.play();
anim.reverse();
anim.updatePlaybackRate(2);

// 桥梁：接管页面上的 CSS 动画，全局开关
document.getAnimations().forEach(a => {
  a.pause();                  // 演示模式全部暂停
  // a.updatePlaybackRate(0.5);
});

// 分工：hover/循环用 CSS；入场链路、物理推算用 WAAPI
```
