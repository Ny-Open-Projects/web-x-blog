---
title: [VIZ-017] 如何用离屏 Canvas 缓存复杂图层？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-017：如何用离屏 Canvas 缓存复杂图层？
**答**：把不常变的复杂内容（网格线、坐标轴、背景纹理、复杂贝塞尔底图）**画一次**缓存到离屏 canvas（OffscreenCanvas 或隐藏 canvas），主循环里一次 `drawImage` 贴回，把 N 次绘制压成 1 次位块拷贝。失效时机：容器 resize、主题切换、坐标轴范围变化时重画缓存。OffscreenCanvas 还能转移到 Worker 渲染，彻底不占主线程。注意缓存尺寸要含 DPR，drawImage 时按逻辑尺寸铺回。

```javascript
// 静态图层（网格/坐标轴/背景）画一次缓存到离屏 canvas，每帧 drawImage 贴回
const bg = typeof OffscreenCanvas !== 'undefined'
  ? new OffscreenCanvas(800, 600)
  : Object.assign(document.createElement('canvas'), { width: 800, height: 600 });
const bgCtx = bg.getContext('2d');
function drawGrid(c) {
  c.strokeStyle = '#eee';
  for (let x = 0; x <= 800; x += 50) { c.beginPath(); c.moveTo(x, 0); c.lineTo(x, 600); c.stroke(); }
  for (let y = 0; y <= 600; y += 50) { c.beginPath(); c.moveTo(0, y); c.lineTo(800, y); c.stroke(); }
}
drawGrid(bgCtx); // 只在尺寸/主题变化时重画缓存

function renderFrame(ctx) {
  ctx.clearRect(0, 0, 800, 600);
  ctx.drawImage(bg, 0, 0, 800, 600); // 一次位块拷贝，远快于几百次 lineTo
  drawDynamicPoints(ctx);            // 只有动态数据走实时绘制
}
```
