---
title: [OPT-035] OffscreenCanvas 适用什么场景？怎么用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-035：OffscreenCanvas 适用什么场景？怎么用？

**答**：
- 问题：主线程上高频 `canvas` 绘制（图表动画、粒子、滤镜预览）会与交互争抢主线程，掉帧。
- OffscreenCanvas 把 Canvas 2D/WebGL 上下文**整体搬进 Worker**：绘制逻辑在子线程跑，主线程只剩一个占位 `<canvas>` 元素。
- 落地：`transferControlToOffscreen()` 拿到 OffscreenCanvas，作为 Transferable 传给 Worker；Worker 内正常用 2d/webgl API 绘制。
- 限制：Worker 内无 DOM（不能 addEventListener 交互，需主线程转发事件）；Safari 16.4+ 才完整支持，需特性检测降级。

```javascript
// 一一对应：把 canvas 绘制搬进 Worker
// main.js
const canvasEl = document.querySelector('#chart');
// 主线程的 canvas 移交给 OffscreenCanvas 控制
const offscreen = canvasEl.transferControlToOffscreen();

const worker = new Worker('render-worker.js');
// OffscreenCanvas 是 Transferable，零拷贝交给 worker
worker.postMessage({ canvas: offscreen, width: canvasEl.width }, [offscreen]);

// 主线程只负责转发交互数据，绘制全在子线程
window.addEventListener('resize', () => {
  worker.postMessage({ type: 'resize', width: innerWidth });
});

// render-worker.js
// self.onmessage = ({ data }) => {
//   const ctx = data.canvas.getContext('2d'); // worker 里同样能拿 2d/webgl 上下文
//   function draw() {
//     ctx.clearRect(0, 0, data.width, 300);
//     ctx.beginPath();
//     ctx.moveTo(0, 150 + Math.sin(Date.now() / 500) * 80);
//     ctx.lineTo(data.width, 150 + Math.cos(Date.now() / 500) * 80);
//     ctx.stroke();
//     requestAnimationFrame(draw); // worker 内也有 rAF
//   }
//   draw();
// };
```
