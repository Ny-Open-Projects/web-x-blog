---
title: [CSS-192] CSS 动画的性能预算与帧率监控怎么做？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-192：CSS 动画的性能预算与帧率监控怎么做？

**答**：
- 预算基线：交互动画响应 ≤ 100ms、过渡 200~300ms、每帧主线程脚本 ≤ 8ms（60fps 留一半给渲染）。
- 监控手段：rAF 间隔统计（越 16.7ms 越掉帧）、PerformanceObserver 的 longtask、DevTools Performance 面板回放。
- 只允许 transform/opacity/filter 进合成器；width/top/left 触发 layout 的动画属性一律白名单拦截。
- 生产监控：采样上报掉帧率与 longtask 分布，配合 CI 里的 trace 对比防劣化。

```javascript
// 1. 帧率监控：rAF 间隔统计
let last = performance.now(), frames = 0, dropped = 0;
function tick(now) {
  const dt = now - last;
  last = now;
  frames++;
  if (dt > 20) dropped++;               // 预算 50fps，超过即掉帧
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
setInterval(() => {
  report('fps', { rate: dropped / frames });  // 采样上报
  frames = 0; dropped = 0;
}, 5000);

// 2. 长任务监控：主线程阻塞来源
new PerformanceObserver(list => {
  for (const e of list.getEntries()) report('longtask', e.duration);
}).observe({ entryTypes: ['longtask'] });

// 3. 动画属性白名单（审查脚本示意）
const okProps = ['transform', 'opacity', 'filter'];
function auditAnimation(name) {
  const keyframes = document.getAnimations()
    .find(a => a.animationName === name)?.effect?.getKeyframes() || [];
  for (const kf of keyframes) {
    for (const prop of Object.keys(kf)) {
      if (!okProps.includes(prop) && prop !== 'offset' &&
          prop !== 'easing' && prop !== 'composite') {
        console.warn(`动画 ${name} 使用了非合成属性 ${prop}`);
      }
    }
  }
}
```
