---
title: [OPT-107] canvas 性能优化：离屏预渲染和脏矩形怎么实现？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-107：canvas 性能优化：离屏预渲染和脏矩形怎么实现？

**答**：
- canvas 慢的两大原因：每帧全画布重绘（本可以只画变化区域）、每帧重复执行昂贵的绘制指令（本可以预渲染成位图）。
- **离屏预渲染**：把不变的复杂背景/精美图形画到 OffscreenCanvas/createOffscreenCanvas 一次，之后每帧一次 `drawImage` 贴上去——把 O(指令数) 变 O(1)。
- **脏矩形重绘**：只 clearRect + 重绘发生变化的区域，配合分层 canvas（背景层静态、动效层独立）让静态层零重绘。
- 配套细节：坐标取整避免亚像素抗锯齿开销、绘制状态（save/restore）最小化、能用 fillRect 不用 shadowBlur。

```javascript
// 一一对应：分层 canvas + 离屏预渲染 + 脏矩形三合一
const bg = document.querySelector('#bg').getContext('2d'); // 静态层
const fg = document.querySelector('#fg').getContext('2d'); // 动效层

// 1. 离屏预渲染：复杂背景只画一次
const bgCache = new OffscreenCanvas(1920, 1080);
const bgCtx = bgCache.getContext('2d');
function renderBackgroundOnce() {
  for (let i = 0; i < 500; i++) {          // 500 条昂贵贝塞尔/渐变
    bgCtx.beginPath();
    bgCtx.strokeStyle = `hsl(${i}, 60%, 50%)`;
    bgCtx.moveTo(Math.random() * 1920, Math.random() * 1080);
    bgCtx.bezierCurveTo(100, 200, 400, 500, 800, 800);
    bgCtx.stroke();
  }
}
renderBackgroundOnce();
bg.drawImage(bgCache, 0, 0); // 静态层从此不再动

// 2. 脏矩形：动效层只清玩家区域，不清全屏
let prevRect = { x: 0, y: 0, w: 0, h: 0 };
function drawPlayer(x, y) {
  const rect = { x: x - 40, y: y - 40, w: 80, h: 80 };
  fg.clearRect(prevRect.x, prevRect.y, prevRect.w, prevRect.h); // 只擦上一帧的痕迹
  fg.fillRect(rect.x + 40, rect.y + 40, 20, 20);
  prevRect = rect;
}

// 3. 主循环：只跑动效层
function loop() {
  drawPlayer(pointer.x, pointer.y);
  requestAnimationFrame(loop);
}

// 4. 通用微优化：坐标取整，避免亚像素采样
fg.fillRect(Math.round(x), Math.round(y), 20, 20);
// 验证：Performance 面板 GPU 轨道对比全屏重绘 vs 脏矩形的光栅化耗时
```
