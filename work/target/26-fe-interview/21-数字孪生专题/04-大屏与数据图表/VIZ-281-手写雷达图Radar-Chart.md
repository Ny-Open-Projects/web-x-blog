---
title: [VIZ-281] 手写雷达图（Radar Chart）：多维轴与面积填充
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-281：手写雷达图（Radar Chart）：多维轴与面积填充

**答**：
- 题目：雷达图——N 维轴均匀放射，样本值→轴上点连成多边形，面积填充半透明；多系列叠加对比。
- 思路：N 轴角度均分；值→半径（比例尺）；多边形 path（各轴点连线闭合）；面积 = shoelace 公式（可显示评分）。
- 评分点：轴放射与值映射；多边形闭合 path；多系列叠加透明度。

```javascript
function radarChart(series, dims, { maxRadius = 120 } = {}) {
  const angleStep = 2 * Math.PI / dims.length;
  return series.map(s => {
    const points = dims.map((dim, i) => {
      const ratio = (s.values[i] - s.domain[i][0]) / (s.domain[i][1] - s.domain[i][0]);   // 各维独立比例尺
      const r = ratio * maxRadius;
      const a = i * angleStep - Math.PI / 2;               // 顶部起始
      return [r * Math.cos(a), r * Math.sin(a)];
    });
    const d = points.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join('') + 'Z';
    return { series: s.name, path: d, fill: s.color + '33', stroke: s.color,   // 半透明填充
      points };                                            // 面积可用 shoelace 计算
  });
}
// shoelace 面积：Σ(x[i]×y[i+1] - x[i+1]×y[i]) / 2——可作「综合评分」标注
```
