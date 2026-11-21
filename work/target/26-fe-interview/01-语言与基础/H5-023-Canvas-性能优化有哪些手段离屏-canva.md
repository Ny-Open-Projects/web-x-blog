---
title: [H5-023] Canvas 性能优化有哪些手段？离屏 canvas 是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-023：Canvas 性能优化有哪些手段？离屏 canvas 是什么？
**答**：
- 离屏 canvas：在内存里预渲染不变的内容（复杂背景、精灵图），主循环里 drawImage 直接贴，避免每帧重画。
- 分层：静态背景与动态前景拆成两个叠放的 canvas，只重绘动态层。
- 控制 canvas 尺寸（不超过必要分辨率）、减少 save/restore、避免逐像素 fillRect、批量 path。
- 长列表/粒子多时用对象池；重计算（滤镜、物理引擎）放 Web Worker + OffscreenCanvas。

```javascript
// 离屏 canvas：复杂背景只渲染一次
const bgCanvas = document.createElement('canvas');
bgCanvas.width = 800;
bgCanvas.height = 600;
const bgCtx = bgCanvas.getContext('2d');
(function renderBgOnce() {
  for (let i = 0; i < 2000; i++) {
    bgCtx.fillStyle = `hsl(${i % 360}, 60%, 70%)`;
    bgCtx.fillRect(Math.random() * 800, Math.random() * 600, 4, 4); // 昂贵操作只做一次
  }
})();

const ctx = document.querySelector('canvas').getContext('2d');
function frame(now) {
  // 主循环只贴图 + 画动态元素，开销极小
  ctx.drawImage(bgCanvas, 0, 0); // 背景复用
  drawParticles(ctx, now);
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

// OffscreenCanvas：把绘制整体搬到 Worker（主线程完全不参与）
// worker.js:
// const off = new OffscreenCanvas(800, 600);
// const octx = off.getContext('2d');
// setInterval(() => { octx.fillRect(0, 0, 10, 10); }, 16);
```
