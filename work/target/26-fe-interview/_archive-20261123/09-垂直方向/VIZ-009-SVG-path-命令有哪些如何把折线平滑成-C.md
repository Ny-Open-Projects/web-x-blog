---
title: [VIZ-009] SVG path 命令有哪些？如何把折线平滑成 Catmull-Rom 曲线？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-009：SVG path 命令有哪些？如何把折线平滑成 Catmull-Rom 曲线？
**答**：path 基本命令：M/L 绝对直线、H/V 水平垂直、C 三次贝塞尔、Q 二次贝塞尔、A 圆弧、Z 闭合。折线平滑的本质是把 Catmull-Rom 样条**转换为三次贝塞尔**：每段曲线的两个控制点取自"相邻点差值的 1/6"，张力系数可调。相比 d3.curveCatmullRom，自己实现才能精确控制端点行为与过冲（overshoot）。

```javascript
// Catmull-Rom 样条转三次贝塞尔：控制点取相邻点切线方向差值 / 6
function catmullRomPath(points, tension = 1) {
  if (points.length < 2) return '';
  let d = `M${points[0][0]},${points[0][1]}`;
  for (let i = 0; i < points.length - 1; i++) {
    const p0 = points[i - 1] || points[i];
    const p1 = points[i], p2 = points[i + 1];
    const p3 = points[i + 2] || p2;
    const c1x = p1[0] + ((p2[0] - p0[0]) / 6) * tension;
    const c1y = p1[1] + ((p2[1] - p0[1]) / 6) * tension;
    const c2x = p2[0] - ((p3[0] - p1[0]) / 6) * tension;
    const c2y = p2[1] - ((p3[1] - p1[1]) / 6) * tension;
    d += `C${c1x.toFixed(2)},${c1y.toFixed(2)} ${c2x.toFixed(2)},${c2y.toFixed(2)} ${p2[0]},${p2[1]}`;
  }
  return d;
}
console.log(catmullRomPath([[0, 50], [50, 20], [100, 60], [150, 30]]));
```
