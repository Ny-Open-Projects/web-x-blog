---
title: [VIZ-346] B 样条与 Catmull-Rom 样条何时用
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-346：B 样条与 Catmull-Rom 样条何时用

**答**：
- Catmull-Rom 过控制点（插值样条），适合"给点画平滑线"（路径回放）；B 样条逼近控制点（不过点），适合造型与平滑（局部控制好）。
- Catmull-Rom 每段只需前后 4 点，公式简单；张力参数可调锐度。
- 数据可视化里折线平滑用 Catmull-Rom（保真数据点），造型工具用 B 样条/NURBS。

```javascript
// Catmull-Rom 段插值
function catmullRom(p0, p1, p2, p3, t) {
  const t2 = t*t, t3 = t2*t;
  return [0, 1].map(i => 0.5 * (
    (2*p1[i]) +
    (-p0[i] + p2[i]) * t +
    (2*p0[i] - 5*p1[i] + 4*p2[i] - p3[i]) * t2 +
    (-p0[i] + 3*p1[i] - 3*p2[i] + p3[i]) * t3));
}
function smoothPath(points) {
  const out = [];
  for (let i = 0; i < points.length - 1; i++) {
    const p0 = points[Math.max(0, i-1)];
    const p3 = points[Math.min(points.length-1, i+2)];
    for (let t = 0; t < 1; t += 0.1)
      out.push(catmullRom(p0, points[i], points[i+1], p3, t));
  }
  out.push(points[points.length-1]);
  return out;
}
```
