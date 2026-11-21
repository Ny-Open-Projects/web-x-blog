---
title: [H5-295] 笔试：手写 Canvas 圆角矩形
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-295：笔试：手写 Canvas 圆角矩形

**题目**：实现 `roundRect(ctx, x, y, w, h, r)`：支持每个角独立半径（单值或 [tl,tr,br,bl] 数组），r 超过边长一半时自动收敛；提供 fill 与 stroke 两种模式。

**答**：
```javascript
function roundRect(ctx, x, y, w, h, r) {
  const [tl, tr, br, bl] = Array.isArray(r) ? r : [r, r, r, r];
  const clamp = (v) => Math.min(v, w / 2, h / 2); // 超大半径收敛
  const [t1, t2, b2, b1] = [clamp(tl), clamp(tr), clamp(br), clamp(bl)];
  ctx.beginPath();
  ctx.moveTo(x + t1, y);
  ctx.lineTo(x + w - t2, y);
  ctx.arcTo(x + w, y, x + w, y + t2, t2);      // 右上
  ctx.lineTo(x + w, y + h - b2);
  ctx.arcTo(x + w, y + h, x + w - b2, y + h, b2); // 右下
  ctx.lineTo(x + b1, y + h);
  ctx.arcTo(x, y + h, x, y + h - b1, b1);      // 左下
  ctx.lineTo(x, y + t1);
  ctx.arcTo(x, y, x + t1, y, t1);              // 左上
  ctx.closePath();
}

// 用法
const ctx = canvas.getContext('2d');
roundRect(ctx, 10, 10, 200, 100, 12);
ctx.fill();
// 径向不等角：roundRect(ctx, 10, 10, 200, 100, [12, 12, 0, 0])
```

**评分点**：
- arcTo 的三参数语义（起点拐角、终点拐角、半径）用对——不会写的用 arc + 平移也能得分
- 半径钳制（超边长一半必须收敛，否则路径错乱）是必踩边界
- 数组与单值两种入参兼容
- beginPath/closePath 的完整性（否则叠加绘制出鬼影）
