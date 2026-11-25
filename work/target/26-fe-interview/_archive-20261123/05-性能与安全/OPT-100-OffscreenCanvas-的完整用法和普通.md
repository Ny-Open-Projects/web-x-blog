---
title: [OPT-100] OffscreenCanvas 的完整用法？和普通 canvas 的区别在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-100：OffscreenCanvas 的完整用法？和普通 canvas 的区别在哪？

**答**：
- `transferControlToOffscreen()` 把 canvas 的绘制权**移交**给 Worker：主线程零绘制开销，Worker 里独立跑 rAF 渲染循环，主线程卡顿不影响动画帧率。
- 关键语义：转移后主线程不能再动这个 canvas 的 2d/webgl 上下文；OffscreenCanvas 本身也可作为 Transferable 直接转移。
- 适合：地图瓦片渲染、可视化大屏、粒子/游戏画面——绘制密集且与 UI 逻辑可分离的场景。
- 局限：Worker 内没有 DOM，事件（点击/滚轮）要主线程转发；getImageData 等同步读像素在 Worker 里同样昂贵，能用 GPU 就别回读。

```javascript
// 一一对应：OffscreenCanvas 移交 Worker 渲染循环
// main.js
const canvas = document.querySelector('#scene');
const offscreen = canvas.transferControlToOffscreen(); // 绘制权移交

const worker = new Worker('render-worker.js');
worker.postMessage(
  { canvas: offscreen, width: canvas.clientWidth, height: canvas.clientHeight },
  [offscreen] // OffscreenCanvas 本身是 Transferable，零拷贝移交
);

// 交互转发：Worker 没有 DOM，事件数据手动传
document.addEventListener('pointermove', (e) => {
  worker.postMessage({ type: 'pointer', x: e.offsetX, y: e.offsetY });
});

// render-worker.js —— 独立渲染循环：主线程再卡，画面帧率也不掉
let ctx, W, H, particles = [];
self.onmessage = (e) => {
  if (e.data.canvas) {
    ctx = e.data.canvas.getContext('2d');
    ({ width: W, height: H } = e.data);
    for (let i = 0; i < 2000; i++) {
      particles.push({ x: Math.random() * W, y: Math.random() * H, vy: Math.random() * 2 + 1 });
    }
    requestAnimationFrame(loop); // Worker 里同样支持 rAF
  } else if (e.data.type === 'pointer') {
    pointer = e.data;
  }
};
let pointer = { x: 0, y: 0 };
function loop() {
  ctx.clearRect(0, 0, W, H);
  for (const p of particles) {
    p.y = (p.y + p.vy) % H;
    ctx.fillRect(p.x, p.y, 2, 2);
  }
  requestAnimationFrame(loop);
}
// 对比：同样 2000 粒子跑在主线程，任何长任务都会让动画跳帧；
// OffscreenCanvas 方案里主线程长任务只影响事件转发延迟，不影响渲染
```
