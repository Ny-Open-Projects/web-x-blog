---
title: [VIZ-271] 手写仪表盘仪表（Gauge）：SVG 弧形与指针动画
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-271：手写仪表盘仪表（Gauge）：SVG 弧形与指针动画

**答**：
- 题目：仪表盘——弧形刻度盘（270° 扫角）、指针按值旋转（带缓动动画）、色段（红黄绿区间）。
- 思路：SVG path arc（极坐标→弧线 d）；指针 transform rotate（过渡动画）；色段分段弧。
- 评分点：极坐标弧 path 生成；指针角度映射；色段边界。

```javascript
function gaugeArc(cx, cy, r, startDeg, endDeg) {          // 极坐标弧 path
  const toXY = (deg) => [cx + r * Math.cos(deg * Math.PI / 180),
    cy + r * Math.sin(deg * Math.PI / 180)];
  const [x1, y1] = toXY(startDeg), [x2, y2] = toXY(endDeg);
  const large = endDeg - startDeg > 180 ? 1 : 0;
  return `M${x1},${y1} A${r},${r} 0 ${large} 1 ${x2},${y2}`;
}
function gauge(value, { min = 0, max = 100, startDeg = 135, sweep = 270 } = {}) {
  const ratio = (value - min) / (max - min);
  const angle = startDeg + ratio * sweep;                  // 值→角度
  return {
    track: gaugeArc(100, 100, 80, startDeg, startDeg + sweep),
    pointer: `rotate(${angle} 100 100)`,                   // 指针旋转
    transition: 'transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)',   // 缓动
    zones: [[0, 0.6, 'green'], [0.6, 0.85, 'yellow'], [0.85, 1, 'red']]
      .map(([a, b, c]) => ({ path: gaugeArc(100, 100, 80,
        startDeg + a * sweep, startDeg + b * sweep), color: c })),
  };
}
```
