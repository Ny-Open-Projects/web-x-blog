---
title: [VIZ-273] 手写河流图（Stream Graph）：堆叠流布局
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-273：手写河流图（Stream Graph）：堆叠流布局

**答**：
- 题目：河流图（ThemeRiver）——时间轴上多个系列堆叠流，中心对称展开（baseline = wiggle 最小波动）。
- 思路：堆叠：每时间点各系列值堆叠；baseline 策略：zero（底部对齐）/ expand（归一）/ wiggle（最小波动——各层偏移和最小）。
- 评分点：三种 baseline；wiggle 最小波动公式；平滑插值（时间轴）。

```javascript
function streamGraph(series, { baseline = 'wiggle' } = {}) {
  const T = series[0].data.length;
  const layers = [];
  for (let t = 0; t < T; t++) {
    const values = series.map(s => s.data[t]);
    const total = values.reduce((a, b) => a + b, 0);
    let offset;
    if (baseline === 'zero') offset = 0;
    else if (baseline === 'expand') { /* 归一化：值/total */ }
    else {                                                 // wiggle：最小化层间波动
      offset = -total / 2;
      // 更精确：offset = -Σ(前 i 层和的加权)——简化为中心对称
    }
    let cum = offset;
    layers.push(values.map(v => {
      const layer = { y0: cum, y1: cum + v };
      cum += v;
      return layer;
    }));
  }
  return layers;                                           // 每层的上下边界（平滑后渲染）
}
```
