---
title: [WEB-129] OffscreenCanvas 与后台渲染怎么理解？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-129：OffscreenCanvas 与后台渲染怎么理解？
**答**：
- `canvas.transferControlToOffscreen()` 把画布控制权交给 Worker：绘制逻辑在 Worker 线程跑，主线程只负责展示——重绘动画不再挤占主线程。
- OffscreenCanvas 在 Worker 中可用完整 2D/WebGL 上下文，配合 `requestAnimationFrame`（Worker 中也可用）实现主线程繁忙时动画不掉帧。
- 更广的"后台渲染"还包括 Service Worker 里的图片处理、Web Worker 池做像素级计算，共性是"渲染/计算与交互线程解耦"。
- 注意：控制权转移后主线程不能再 getContext 该画布；Safari 对 OffscreenCanvas 的支持成熟度需检查。

```javascript
// main.js：画布控制权转移给 Worker
const canvas = document.querySelector('canvas');
const offscreen = canvas.transferControlToOffscreen(); // 控制权一次性转移
const worker = new Worker('/render-worker.js');
worker.postMessage({ canvas: offscreen, dpr: devicePixelRatio }, [offscreen]); // 转移所有权

// render-worker.js：在 Worker 线程持续渲染，主线程卡顿也不掉帧
self.onmessage = (e) => {
  const { canvas: c, dpr } = e.data;
  c.width = c.width * dpr;
  const ctx = c.getContext('2d');
  ctx.scale(dpr, dpr);
  let t = 0;
  const draw = () => {
    t += 0.02;
    ctx.clearRect(0, 0, 300, 150);
    ctx.beginPath();
    ctx.arc(150, 75, 40 + Math.sin(t) * 10, 0, Math.PI * 2);
    ctx.fill();
    setTimeout(draw, 16); // Worker 中绘制循环
  };
  draw();
};
```
