---
title: [SCN-1160] SCADA 大屏的产量统计与 OEE 计算
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1160：SCADA 大屏的产量统计与 OEE 计算

**答**：
- OEE：设备综合效率 = 时间稼动率 × 性能稼动率 × 良品率——三因子分解展示。
- 损失：停机损失（计划/故障）/速度损失/不良损失分解（帕累托）。
- 对比：产线/班组/日历维度对比（哪条线拖后腿）。

```javascript
// OEE 计算
function oee(availability, performance, quality) {
  const o = availability * performance * quality;
  return { oee: +(o * 100).toFixed(1) + '%',
    factors: { availability: +(availability * 100).toFixed(1) + '%',
      performance: +(performance * 100).toFixed(1) + '%',
      quality: +(quality * 100).toFixed(1) + '%' },
    pareto: lossesPareto(availability, performance, quality),   // 损失分解
  };
}
function lossesPareto(a, p, q) {
  return [{ type: '停机损失', pct: 1 - a }, { type: '速度损失', pct: a * (1 - p) },
    { type: '不良损失', pct: a * p * (1 - q) }]
    .sort((x, y) => y.pct - x.pct);
}
```
