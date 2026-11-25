---
title: [H5-353] 移动端 Canvas 绘图性能：脏区、离屏与分层
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-353：移动端 Canvas 绘图性能：脏区、离屏与分层

**答**：
- 全量重绘 vs 脏区：小画布/简单图形全量重绘可行；复杂场景只重绘变化区域（dirty rect）可省 80% 绘制时间
- 离屏缓存：静态背景（网格/底图）画到 OffscreenCanvas 一次，每帧 drawImage 拷贝而不是重画矢量——重图场景是数量级差异
- 分层画布：动与静拆多个叠加 canvas（背景层不动、动画层重绘），CSS 合成替代每帧重绘背景
- 移动端 DPR 处理：canvas 实际尺寸 = CSS 尺寸 × dpr（上限 2~3），否则高分屏糊/超清屏内存爆；小屏低端机可降 dpr 换流畅
- 上下文切换成本：少 save/restore、合并同色绘制、路径复用 Path2D；每帧 new ImageData 是高频泄漏源，复用缓冲

```javascript
const dpr = Math.min(devicePixelRatio || 1, 2);
cv.width = w * dpr; cv.height = h * dpr; ctx.scale(dpr, dpr);

// 静态层离屏
const bgLayer = new OffscreenCanvas(w * dpr, h * dpr);
drawGrid(bgLayer.getContext('2d'));

function frame() {
  ctx.clearRect(0, 0, w, h);
  ctx.drawImage(bgLayer, 0, 0, w, h);      // 背景一次拷贝
  drawDirtyRect();                          // 只画变化区
  requestAnimationFrame(frame);
}
```
