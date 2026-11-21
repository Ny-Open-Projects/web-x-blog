---
title: [H5-131] shadowBlur 为什么慢？阴影有哪些优化手段？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-131：shadowBlur 为什么慢？阴影有哪些优化手段？
**答**：
- 阴影（`shadowBlur/shadowColor/shadowOffset*`）在绘制时触发**逐像素高斯模糊**，代价随 blur 半径增长，每帧对多个元素各自模糊时帧率崩塌。
- 优化 1：静态元素把"本体+阴影"预渲染进离屏 canvas，之后只是一次 `drawImage`（模糊只发生一次）。
- 优化 2：动态元素共享同一组 shadow 设置批量绘制，减少状态切换；优化 3：能走 DOM 的阴影用 CSS `box-shadow`（GPU 合成）；优化 4：降低 blur、缩小阴影元素数量、减少阴影层数。
- 用完记得关闭：`shadowColor = 'transparent'; shadowBlur = 0`，否则状态泄漏继续吃性能。

```javascript
const ctx = canvas.getContext('2d');
const dpr = devicePixelRatio || 1;
const shapes = [{ x: 20, y: 20, w: 80, h: 60 }, { x: 140, y: 20, w: 80, h: 60 }];

// 慢的写法：每个元素各自触发一次高斯模糊
function slowShadows() {
  for (const s of shapes) {
    ctx.shadowColor = 'rgba(0,0,0,.35)';
    ctx.shadowBlur = 20;              // blur 越大越贵，且按元素次数重复
    ctx.shadowOffsetY = 4;
    ctx.fillRect(s.x, s.y, s.w, s.h);
  }
  ctx.shadowColor = 'transparent'; ctx.shadowBlur = 0;   // 用完必须关
}

// 优化 1：静态元素把"本体+阴影"预渲染进离屏 canvas，之后只是 drawImage
function makeShadowSprite(w, h, pad = 24, blur = 20) {
  const off = document.createElement('canvas');
  off.width = (w + pad * 2) * dpr; off.height = (h + pad * 2) * dpr;
  const c = off.getContext('2d');
  c.scale(dpr, dpr);
  c.shadowColor = 'rgba(0,0,0,.35)';
  c.shadowBlur = blur; c.shadowOffsetY = 4;
  c.fillStyle = '#fff';
  c.fillRect(pad, pad, w, h);        // 模糊只发生这一次
  return { canvas: off, pad };
}
const sprite = makeShadowSprite(80, 60);
for (const s of shapes) {
  ctx.drawImage(sprite.canvas, s.x - sprite.pad, s.y - sprite.pad,
                sprite.canvas.width / dpr, sprite.canvas.height / dpr);
}

// 优化 2：动态元素必须实时画阴影时，共享同一组 shadow 设置批量绘制
ctx.shadowColor = 'rgba(0,0,0,.35)'; ctx.shadowBlur = 20; ctx.shadowOffsetY = 4;
ctx.fillStyle = '#fff';
for (const s of shapes) ctx.fillRect(s.x, s.y + 100, s.w, s.h);  // 一次设置连画
ctx.shadowColor = 'transparent'; ctx.shadowBlur = 0;
// 优化 3：纯 DOM 场景直接用 CSS box-shadow（合成器处理），别用 canvas 画阴影
```
