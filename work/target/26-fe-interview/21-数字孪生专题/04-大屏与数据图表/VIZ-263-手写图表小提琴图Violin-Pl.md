---
title: [VIZ-263] 手写图表小提琴图（Violin Plot）：核密度估计渲染
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-263：手写图表小提琴图（Violin Plot）：核密度估计渲染

**答**：
- 题目：实现小提琴图——每组数据做核密度估计（KDE，高斯核），密度曲线对称展开成「小提琴」形状，Canvas 渲染。
- 思路：KDE：f(x) = Σ N(x; xi, bandwidth)；带宽 Silverman 公式；密度值 → 对称宽度 → path 渲染。
- 评分点：KDE 公式与带宽；对称展开成 path；采样密度与渲染点数平衡。

```javascript
function violinPlot(groups, { width = 40, samples = 50 } = {}) {
  return groups.map((values, gi) => {
    const n = values.length;
    const mean = values.reduce((s, x) => s + x, 0) / n;
    const std = Math.sqrt(values.reduce((s, x) => s + (x - mean) ** 2, 0) / n);
    const bandwidth = 1.06 * std * Math.pow(n, -1 / 5);     // Silverman 带宽
    const lo = Math.min(...values) - bandwidth, hi = Math.max(...values) + bandwidth;
    const step = (hi - lo) / samples;
    const curve = [];
    for (let x = lo; x <= hi; x += step) {                  // KDE 采样
      const density = values.reduce((s, xi) =>
        s + Math.exp(-((x - xi) ** 2) / (2 * bandwidth ** 2)), 0)
        / (n * bandwidth * Math.sqrt(2 * Math.PI));
      curve.push({ x, density });
    }
    const maxD = Math.max(...curve.map(c => c.density));
    const path = curve.map(c =>                             // 对称展开
      `${c.density / maxD * width / 2}`).join(',');
    return { group: gi, curve, path };                      // 渲染层映射像素
  });
}
```
