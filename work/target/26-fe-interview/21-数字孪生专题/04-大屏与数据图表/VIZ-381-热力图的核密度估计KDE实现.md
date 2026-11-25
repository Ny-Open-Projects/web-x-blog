---
title: [VIZ-381] 热力图的核密度估计（KDE）实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-381：热力图的核密度估计（KDE）实现

**答**：
- KDE：每个点贡献一个高斯核，叠加后归一化——带宽 h 决定平滑度（h 大更糊）。
- 性能：预计算核查找表（1D 高斯）+ 网格累加（而非逐点全图卷积）。
- 渲染：密度值 -> 色带映射（viridis 等感知均匀色带），支持 alpha 渐变叠加底图。

```javascript
// KDE 网格累加
function kde(points, { w = 512, h = 512, bandwidth = 8 } = {}) {
  const grid = new Float32Array(w * h);
  const R = bandwidth * 3;
  const kernel = new Float32Array(2 * R + 1);
  for (let i = -R; i <= R; i++)
    kernel[i + R] = Math.exp(-(i * i) / (2 * bandwidth * bandwidth));
  for (const { x, y, w: wt = 1 } of points) {
    const x0 = Math.max(0, Math.floor(x - R)), x1 = Math.min(w - 1, Math.ceil(x + R));
    for (let i = x0; i <= x1; i++)
      for (let j = Math.max(0, Math.floor(y - R));
           j <= Math.min(h - 1, Math.ceil(y + R)); j++)
        grid[j * w + i] += wt * kernel[i - Math.floor(x) + R] * kernel[j - Math.floor(y) + R];
  }
  return { grid, w, h };
}
```
