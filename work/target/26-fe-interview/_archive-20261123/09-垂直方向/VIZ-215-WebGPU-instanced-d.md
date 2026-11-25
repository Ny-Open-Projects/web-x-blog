---
title: [VIZ-215] WebGPU instanced draw 的 cull 与 LOD 联动：百万点分级渲染
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-215：WebGPU instanced draw 的 cull 与 LOD 联动：百万点分级渲染

**答**：
- 题目：百万级散点在 WebGPU 中渲染，帧率不稳。设计分级方案：CPU 剔除 + LOD 三档（zoom 大→全精度、中→抽样、小→聚合像素密度）。
- 思路：zoom 阈值三档：高档 draw 全量实例；中档 GPU compute 预抽样（每 4 点取 1）；低档 CPU 聚合到网格（每格 1 点 + 权重）。
- 评分点：分档阈值与切换滞后（防抖）；聚合密度可视化（点大小=权重）；drawCount 动态。

```javascript
function lodLevel(zoom) { return zoom > 8 ? 0 : zoom > 3 ? 1 : 2; }
function prepareFrame(points, zoom) {
  const level = lodLevel(zoom);
  if (level === 0) return { drawCount: points.length, data: points };
  if (level === 1) return { drawCount: points.length / 4,
    data: points.filter((_, i) => i % 4 === 0) };         // 抽样
  // 低档：网格聚合（每 cell 一个代表点，size = 权重）
  const grid = new Map();
  for (const p of points) {
    const cell = `${Math.floor(p.x * 50)},${Math.floor(p.y * 50)}`;
    grid.set(cell, { x: p.x, y: p.y, w: (grid.get(cell)?.w ?? 0) + 1 });
  }
  return { drawCount: grid.size, data: [...grid.values()],
    agg: true };                                          // 着色器按 w 调整点大小
}
// 切换防抖：zoom 变化后 200ms 才切档——避免连续缩放时档位抖动
```
