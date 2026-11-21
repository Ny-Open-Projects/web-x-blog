---
title: [VIZ-129] 大规模时序数据的降采样算法如何选择？（LTTB/min-max/平均，压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-129：大规模时序数据的降采样算法如何选择？（LTTB/min-max/平均，压轴）
**答**：目标：可视窗口内每像素只保留代表点。对比：① **等距平均**——每桶取均值，实现最简单，但**会抹平尖峰**（监控场景致命）；② **min-max**——每桶保留最大 + 最小，不丢极值，告警/监控首选，点数 ×2；③ **LTTB（Largest-Triangle-Three-Buckets）**——按三角形面积最大选点，保留视觉形状最好，缩放体验佳；④ **M4**——每桶保留 x/y 各 min/max 共 4 点。选型：监控告警用 min-max，探索分析用 LTTB，报表缩略用平均；缩放时缓存多级降采样（金字塔）。

```javascript
// 三种降采样算法对比实现
function bucketAvg(data, buckets) {       // 平滑但会丢尖峰
  const size = data.length / buckets, out = [];
  for (let b = 0; b < buckets; b++) {
    let s = 0, n = 0;
    for (let i = Math.floor(b * size); i < Math.floor((b + 1) * size); i++) { s += data[i][1]; n++; }
    out.push([data[Math.floor((b + 0.5) * size)][0], s / n]);
  }
  return out;
}
function bucketMinMax(data, buckets) {    // 保留极值，监控首选
  const size = data.length / buckets, out = [];
  for (let b = 0; b < buckets; b++) {
    let lo = data[Math.floor(b * size)], hi = lo;
    for (let i = Math.floor(b * size); i < Math.floor((b + 1) * size); i++) {
      if (data[i][1] < lo[1]) lo = data[i];
      if (data[i][1] > hi[1]) hi = data[i];
    }
    out.push(lo, hi);
  }
  return out;
}
function lttb(data, threshold) {          // Largest-Triangle-Three-Buckets
  // 简化实现：参考点取下一桶首点；标准 LTTB 用下一桶全部点的均值作参考点
  const n = data.length, every = (n - 2) / (threshold - 2), sampled = [data[0]];
  let a = 0;
  for (let i = 0; i < threshold - 2; i++) {
    const rangeOffs = Math.floor(i * every) + 1, rangeTo = Math.floor((i + 1) * every) + 1;
    const avg = data[Math.min(rangeTo, n - 1)];
    let maxArea = -1, next = rangeOffs;
    for (let j = rangeOffs; j < rangeTo; j++) {
      const area = Math.abs((data[a][0] - avg[0]) * (data[j][1] - data[a][1]) -
                            (data[a][0] - data[j][0]) * (avg[1] - data[a][1])) * 0.5;
      if (area > maxArea) { maxArea = area; next = j; }
    }
    sampled.push(data[next]); a = next;
  }
  sampled.push(data[n - 1]);
  return sampled;
}
```
