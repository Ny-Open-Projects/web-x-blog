---
title: [H5-020] Canvas 高分屏模糊怎么解决？基础绘制流程是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-020：Canvas 高分屏模糊怎么解决？基础绘制流程是什么？
**答**：
- Canvas 默认 1 个 CSS 像素对应 1 个物理像素，DPR 大于 1 的屏幕上被拉伸发虚。
- 修法：画布实际尺寸 = CSS 尺寸 × devicePixelRatio，再 `ctx.scale(dpr, dpr)` 让绘制坐标仍按 CSS 像素写。
- 基础流程：拿到 2d context → 设置样式（fillStyle/strokeStyle/lineWidth）→ path 绘制 → fill/stroke。
- 注意 canvas 的 width/height 特性是绘图分辨率，CSS 宽高是显示尺寸，两者解耦。

```html
<canvas id="board" style="width: 400px; height: 300px;"></canvas>

<script>
  const canvas = document.getElementById('board');
  const dpr = window.devicePixelRatio || 1;

  // 高分屏适配：物理像素尺寸
  canvas.width = 400 * dpr;
  canvas.height = 300 * dpr;

  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr); // 后续坐标仍按 400x300 的 CSS 逻辑像素书写

  // 基础绘制
  ctx.fillStyle = '#3367d6';
  ctx.fillRect(20, 20, 120, 80); // 实心矩形

  ctx.strokeStyle = '#ff3b30';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(240, 60, 40, 0, Math.PI * 2); // 圆
  ctx.stroke();

  ctx.font = '16px sans-serif';
  ctx.fillStyle = '#333';
  ctx.fillText('Hello Canvas', 160, 180);
</script>
```
