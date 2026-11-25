---
title: [VIZ-306] 手写数据降采样 LTTB 算法（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-306：手写数据降采样 LTTB 算法（笔试）

**答**：
- 题目：实现 LTTB（Largest-Triangle-Three-Buckets）降采样——保视觉形状的折线抽稀。三桶选「与前后点构成最大三角形面积」的代表点。
- 思路：分桶（每桶 = 目标点区间）；首点/末点保留；每桶选与「前选点+下一桶平均点」三角形面积最大的点。
- 评分点：三角形面积公式（叉积）；桶均值锚点；与 M4 的场景区分。

```javascript
function lttb(data, target) {                              // data: [{x, v}] 按序
  if (data.length <= target) return data;
  const bucketSize = (data.length - 2) / (target - 2);
  const out = [data[0]];                                   // 首点保留
  let prevIndex = 0;
  for (let b = 0; b < target - 2; b++) {
    // 当前桶与下一桶范围
    const from = Math.floor((b + 1) * bucketSize) + 1;
    const to = Math.min(Math.floor((b + 2) * bucketSize) + 1, data.length);
    const nextAvgX = avg(data.slice(from, to).map(d => d.x));
    const nextAvgV = avg(data.slice(from, to).map(d => d.v));
    const a = data[prevIndex];                             // 前选点
    let bestIdx = from, bestArea = -1;
    for (let i = Math.floor(b * bucketSize) + 1; i < from; i++) {   // 本桶内选代表
      const area = Math.abs(
        (a.x - nextAvgX) * (data[i].v - a.v) -
        (a.x - data[i].x) * (nextAvgV - a.v));             // 三角形面积（叉积）
      if (area > bestArea) { bestArea = area; bestIdx = i; }
    }
    out.push(data[bestIdx]);
    prevIndex = bestIdx;
  }
  out.push(data.at(-1));                                   // 末点保留
  return out;
}
```
