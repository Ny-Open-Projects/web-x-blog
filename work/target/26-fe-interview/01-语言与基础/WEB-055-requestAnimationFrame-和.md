---
title: [WEB-055] requestAnimationFrame 和 setTimeout 做动画有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-055：requestAnimationFrame 和 setTimeout 做动画有什么区别？
**答**：
- rAF 回调在浏览器下次重绘前执行，与显示器刷新率同步（60Hz 即每 16.7ms 一次），不重绘不浪费；标签页后台自动暂停，省电。
- setTimeout 间隔与刷新率无关，容易掉帧、抖动，且后台标签页被节流到 1s 以上。
- 计算下一帧动画状态时以时间为基准（delta time），帧率不同步时动画速度一致。
- rAF 回调属于渲染前步骤，其后紧跟样式计算、布局与绘制；rAF 里再塞大量 JS 同样会掉帧。

```javascript
// 用 rAF + delta time 实现帧率无关的动画
function animate(el, from, to, duration) {
  const start = performance.now();
  function frame(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1); // 0 -> 1
    const eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
    const x = from + (to - from) * eased;
    el.style.transform = `translateX(${x}px)`; // 只动 transform，纯合成
    if (progress < 1) requestAnimationFrame(frame); // 与刷新率同步的下一帧
  }
  requestAnimationFrame(frame);
}
animate(document.querySelector('.box'), 0, 300, 600);

// 对比：setTimeout 链在 60Hz 屏上间隔对不齐 16.7ms，且后台被节流
function badAnimate(el, x) {
  setTimeout(() => {
    x += 5;
    el.style.transform = `translateX(${x}px)`;
    if (x < 300) badAnimate(el, x); // 帧间隔不稳定，动画卡顿
  }, 16);
}
```

## 十一、Web Workers、PWA、模块化与前端路由
