---
title: [ALG-186] 轨迹回放功能：GPS 上报的定位点有噪声且跳变，直接连线播放像抽搐。如何用 Catmull-Rom 样条做轨迹平滑并逐帧驱动动画？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-186：轨迹回放功能：GPS 上报的定位点有噪声且跳变，直接连线播放像抽搐。如何用 Catmull-Rom 样条做轨迹平滑并逐帧驱动动画？
**答**：Catmull-Rom 样条：对每段 [P1, P2]，用两侧邻居 P0、P3 作为切向约束，t ∈ [0,1] 插值，曲线过所有控制点且二阶连续，无需解方程组（对比 Bezier 还要算控制点）。实现：控制点序列两两成段，每段均匀采样 N 个点展开成逐帧位置；首尾段缺失邻居时复制端点。平滑后 O(段数 × 采样数) 一次性预计算，动画时只查表。

```javascript
function catmullRom(p0, p1, p2, p3, t) { // 在 P1 P2 之间插值，P0 P3 控制形状
  const t2 = t * t, t3 = t2 * t;
  const f = (a, b, c, d) =>
    0.5 * ((2 * b) + (-a + c) * t +
      (2 * a - 5 * b + 4 * c - d) * t2 +
      (-a + 3 * b - 3 * c + d) * t3);
  return { x: f(p0.x, p1.x, p2.x, p3.x), y: f(p0.y, p1.y, p2.y, p3.y) };
}
function smoothTrack(points, samples = 20) {
  const out = [];
  for (let i = 0; i < points.length - 1; i++) {
    // 首尾缺邻居：复制端点补齐 4 点约束
    const p0 = points[Math.max(0, i - 1)], p1 = points[i];
    const p2 = points[i + 1], p3 = points[Math.min(points.length - 1, i + 2)];
    for (let s = 0; s < samples; s++) {
      out.push(catmullRom(p0, p1, p2, p3, s / samples));
    }
  }
  out.push(points[points.length - 1]); // 终点
  return out;                          // 逐帧动画：rAF 里按帧号取 out[i]
}
```
