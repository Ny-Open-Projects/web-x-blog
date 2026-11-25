---
title: [WEB-095] DPR 是什么？Pixel 管道如何完成从 CSS 像素到物理像素的缩放？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-095：DPR 是什么？Pixel 管道如何完成从 CSS 像素到物理像素的缩放？
**答**：
- DPR（devicePixelRatio）= 物理像素 / CSS 像素，Retina 屏为 2 或 3；CSS 写 100px，实际占 200/300 物理像素。
- 管道：布局在 CSS 像素空间 → Paint 产出绘制指令 → 光栅化按 DPR 放大成物理位图 → GPU 合成输出。
- Canvas/SVG 等自绘内容必须手动按 DPR 放大画布，否则被拉伸发虚；位图图片要提供 2x 资源或用 srcset 适配。
- 动态 DPR：浏览器缩放、跨屏拖动窗口都会改变 DPR，可用 matchMedia 监听分辨率变化重设画布。

```javascript
// Canvas 按 DPR 高清渲染的标准三步
const canvas = document.querySelector('canvas');
const rect = canvas.getBoundingClientRect();
canvas.width  = Math.round(rect.width * devicePixelRatio);   // 1. 物理像素尺寸
canvas.height = Math.round(rect.height * devicePixelRatio);
const ctx = canvas.getContext('2d');
ctx.scale(devicePixelRatio, devicePixelRatio);               // 2. 缩放坐标系
ctx.fillStyle = 'tomato';
ctx.fillRect(10, 10, 100, 100);                              // 3. 逻辑坐标照常画

// 响应 DPR 变化（缩放/跨屏拖动）
const mq = matchMedia(`(resolution: ${devicePixelRatio}dppx)`);
mq.addEventListener('change', () => location.reload() /* 或重设画布 */);
```

## 十七、缓存与存储进阶
