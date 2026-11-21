---
title: [VIZ-076] 设计一个仪表盘组件（gauge 多指针）。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-076：设计一个仪表盘组件（gauge 多指针）。
**答**：结构：底盘弧（240° 起止角，0.75π → 2.25π）、刻度线与数值标签、多根指针（每根独立值/颜色/标签，从圆心指向 `angle = start + value/max × sweep`）。Canvas 实现要点：值转角度函数统一收敛；指针动画用补间（VIZ-092 的 Tween）避免跳变；中心盖帽遮住指针根部；刻度色带（红黄绿区间）用分段 arc + 颜色。多指针时避免标签重叠——按半径分层放置。

```javascript
// 多指针仪表盘：共享弧形刻度盘，每根指针独立角度与颜色
function drawGauge(ctx, cx, cy, r, pointers, maxValue = 100) {
  const START = Math.PI * 0.75, SWEEP = Math.PI * 1.5; // 240 度弧
  const valueToAngle = v => START + (v / maxValue) * SWEEP;
  const bands = [[0, 60, '#22c55e'], [60, 85, '#f59e0b'], [85, 100, '#ef4444']];
  ctx.lineWidth = 10;
  for (const [lo, hi, color] of bands) {           // 分段色带
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.arc(cx, cy, r, valueToAngle(lo), valueToAngle(hi));
    ctx.stroke();
  }
  for (const p of pointers) {                      // 每根指针独立绘制
    const a = valueToAngle(Math.min(p.value, maxValue));
    ctx.strokeStyle = p.color; ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + Math.cos(a) * (r - 12), cy + Math.sin(a) * (r - 12));
    ctx.stroke();
    ctx.fillStyle = p.color; ctx.font = '12px sans-serif';
    ctx.fillText(p.label, cx + Math.cos(a) * (r + 16) - 10, cy + Math.sin(a) * (r + 16));
  }
}
```
