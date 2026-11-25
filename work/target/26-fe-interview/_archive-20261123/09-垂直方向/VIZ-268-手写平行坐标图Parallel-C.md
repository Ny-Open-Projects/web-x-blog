---
title: [VIZ-268] 手写平行坐标图（Parallel Coordinates）：多维数据渲染与刷选
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-268：手写平行坐标图（Parallel Coordinates）：多维数据渲染与刷选

**答**：
- 题目：平行坐标图——N 维各画一条垂直轴，样本连折线穿过各轴；轴刷选（区间过滤）联动高亮。高维轴可交换重排。
- 思路：每维独立线性比例尺（可 log）；折线 = 各轴 y 值连线；刷选 = 轴上区间 → 过滤样本 → 重渲染（高亮命中）。
- 评分点：多维比例尺独立；刷选过滤联动；轴交换重排（相关性观察）。

```javascript
class ParallelCoords {
  constructor(dims, data, size) {
    this.axes = dims.map((d, i) => ({ dim: d, x: i / (dims.length - 1) * size.w,
      scale: linearScale(domainOf(data, d), [size.h, 0]) }));
    this.data = data;
  }
  render(filter) {                                         // filter: {dim: [lo, hi]}
    const pass = this.data.filter(d =>
      Object.entries(filter ?? {}).every(([dim, [lo, hi]]) =>
        d[dim] >= lo && d[dim] <= hi));
    return pass.map(d => ({
      points: this.axes.map(a => [a.x, a.scale(d[a.dim])]),   // 折线坐标
      highlighted: true,
    }));
  }
  swapAxes(i, j) { [this.axes[i], this.axes[j]] = [this.axes[j], this.axes[i]]; }   // 轴交换
}
```
