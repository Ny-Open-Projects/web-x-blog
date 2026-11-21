---
title: [H5-130] createPattern 平铺与渐变（linear/radial）的正确用法与坑？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-130：createPattern 平铺与渐变（linear/radial）的正确用法与坑？
**答**：
- 渐变坐标定义在**当前坐标系**里：translate/scale 画布时旧渐变对象不会跟着"想象中"移动——元素位置变化时按目标矩形重建渐变，不要复用。
- `addColorStop` 位置必须 0~1 且 stop 是按添加顺序应用的；径向渐变是"内圆到外圆"插值，常用于高光/光晕。
- `createPattern` 的源可以是 Image/Canvas/Video；Image 必须等 `onload`，Canvas 可立即使用。
- pattern 的平铺原点跟随当前变换矩阵——想让纹理"固定"需重置变换后绘制。

```javascript
const ctx = canvas.getContext('2d');

// 1) 线性渐变：坐标定义在"当前坐标系"
const g = ctx.createLinearGradient(10, 10, 210, 10);
g.addColorStop(0, '#3b82f6');
g.addColorStop(1, '#ef4444');
ctx.fillStyle = g;
ctx.fillRect(10, 10, 200, 60);

// 2) 缩放/移动元素时不要复用旧渐变对象 —— 按目标矩形重建
function gradientFor(x, y, w) {
  const lg = ctx.createLinearGradient(x, y, x + w, y);
  lg.addColorStop(0, '#3b82f6');
  lg.addColorStop(1, '#ef4444');
  return lg;
}

// 3) 径向渐变：内圆到外圆插值，做高光/光晕
const rg = ctx.createRadialGradient(110, 130, 2, 110, 130, 44);
rg.addColorStop(0, 'rgba(255,255,255,.9)');
rg.addColorStop(1, 'rgba(255,255,255,0)');
ctx.fillStyle = rg;
ctx.fillRect(66, 86, 88, 88);

// 4) pattern 平铺：源是 canvas 可立即用；是 Image 必须等 onload
const tile = document.createElement('canvas');
tile.width = tile.height = 16;
const tc = tile.getContext('2d');
tc.strokeStyle = '#94a3b8';
tc.beginPath(); tc.moveTo(0, 16); tc.lineTo(16, 0); tc.stroke();   // 斜线纹理
const p = ctx.createPattern(tile, 'repeat');   // repeat/repeat-x/no-repeat...
ctx.fillStyle = p;
ctx.fillRect(10, 190, 200, 60);
// 坑：pattern 的平铺原点跟随当前变换矩阵 —— translate 后纹理会"跟着动"，
// 需要"固定纹理"时：save 重置变换，在目标位置重画，restore
```
