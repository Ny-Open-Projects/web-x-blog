---
title: [PER-290] OffscreenCanvas 如何把渲染搬进 Worker？适合什么场景、有什么限制？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-290：OffscreenCanvas 如何把渲染搬进 Worker？适合什么场景、有什么限制？

**答**：
- 机制：把 canvas 的控制权 `transferControlToOffscreen()` 转移给 Worker，Worker 里用熟悉的 2D/WebGL API 绘制，主线程零渲染开销——绘制计算与位图光栅化都在 worker 线程。
- 适合：粒子/图表/地图渲染等每帧重算的绘制（主线程 rAF 被解放）、图片处理（解码+滤镜+缩放一条龙在 worker）、后台生成缩略图。
- 限制：① Safari 老版本支持不全，需特性检测；② transfer 之后主线程不能再直接操作该 canvas（绘制权唯一）；③ 与 DOM 无关的 API 才可用（getImageData 可用，但同步阻塞 worker 自己）；④ requestAnimationFrame 在 worker 里可用（OffscreenCanvas 上下文）。
- 数据流：canvas 尺寸变化用 ResizeObserver 在主线程测，postMessage 通知 worker 重设 canvas.width/height（width/height 是可同步属性）。

```javascript
// 主线程：转移控制权
const off = document.querySelector('#chart').transferControlToOffscreen();
worker.postMessage({ canvas: off, width, height }, [off]);    // 转移！
// worker.js：
let ctx;
self.onmessage = ({ data }) => {
  if (data.canvas) {
    data.canvas.width = data.width; data.canvas.height = data.height;
    ctx = data.canvas.getContext('2d');
    drawLoop();
  }
};
function drawLoop() {
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  drawParticles(ctx);                     // 绘制计算在 worker，主线程 rAF 完全空闲
  requestAnimationFrame(drawLoop);        // worker 内可用 rAF（配 OffscreenCanvas）
}
```
