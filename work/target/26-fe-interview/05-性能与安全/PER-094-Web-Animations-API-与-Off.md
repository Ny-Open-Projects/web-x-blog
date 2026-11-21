---
title: [PER-094] Web Animations API 与 OffscreenCanvas 如何提升运行时性能？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-094：Web Animations API 与 OffscreenCanvas 如何提升运行时性能？

**答**：
- WAAPI 让浏览器把动画**放到合成器线程**执行（transform/opacity），主线程即使繁忙动画也不掉帧；CSS 动画 + `will-change` 同理。
- WAAPI 相比 rAF 手写的优势：声明式、可 `finished` promise 链、可 pause/persist、批量 `document.getAnimations()` 统一控制。
- OffscreenCanvas 把**绘制工作整体搬进 Worker**：canvas 转移控制权后，主线程零绘制开销，适合图表重绘、图像处理、游戏渲染。
- 前提：Worker 里的 OffscreenCanvas 需要浏览器支持（Safari 16.4+），降级方案是主线程 canvas + Worker 只做数据计算。

```javascript
// WAAPI：声明式动画交给合成器，主线程繁忙也不卡
el.animate(
  [
    { transform: 'translateX(0) scale(1)', opacity: 1 },
    { transform: 'translateX(300px) scale(1.1)', opacity: 0.6 },
  ],
  {
    duration: 400,
    easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
    fill: 'both',
    composite: 'replace',
  },
).finished.then(() => console.log('动画完成，无需 rAF 驱动'));
```

```javascript
// 主线程：把 canvas 控制权转移给 Worker，绘制不占主线程
const canvas = document.querySelector('#chart');
const offscreen = canvas.transferControlToOffscreen(); // 一次性转移

const worker = new Worker('render-worker.js');
worker.postMessage({ type: 'init', canvas: offscreen, data: chartData }, [offscreen]);

// render-worker.js 内部：
self.onmessage = ({ data }) => {
  if (data.type !== 'init') return;
  const ctx = data.canvas.getContext('2d'); // 在 Worker 里拿上下文
  let t = 0;
  setInterval(() => {
    ctx.clearRect(0, 0, data.canvas.width, data.canvas.height);
    ctx.beginPath();
    for (let x = 0; x < data.canvas.width; x++) {
      ctx.lineTo(x, 100 + Math.sin((x + t) / 50) * 60); // 重绘在 Worker，主线程零负担
    }
    ctx.stroke();
    t += 2;
  }, 16);
};
```
