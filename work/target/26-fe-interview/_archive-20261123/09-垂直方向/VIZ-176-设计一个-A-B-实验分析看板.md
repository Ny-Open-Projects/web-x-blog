---
title: [VIZ-176] 设计一个 A/B 实验分析看板。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-176：设计一个 A/B 实验分析看板。
**答**：① **实验元信息**——流量比例、假设描述、主指标/护栏指标；② **核心展示**——指标对比表：各组 vs 对照组，**95% 置信区间误差线** + 显著性标记（p<0.05 星号），不显著不标星防误读；③ **趋势**——日粒度两组差值曲线（累积效应是否稳定）；④ **防误读设计**——样本量不足提示、多指标 FDR 校正说明、实验到期提醒；⑤ **交互**——分群（segment）下钻重算。统计口径必须与数据团队对齐，前端只做展示不做 p 值计算。

```javascript
// 实验指标对比：置信区间误差线 + 显著性标记
function abOption(variants, control) {
  return {
    xAxis: { type: 'category', data: variants.map(v => v.name) },
    yAxis: { type: 'value', name: '转化率' },
    series: [{
      type: 'line',                                   // 点 + 误差线形式
      data: variants.map(v => v.rate),
      itemStyle: { color: p => p.dataIndex > 0 && variants[p.dataIndex].p < 0.05
        ? '#10b981' : '#9ca3af' },                    // 显著绿色，否则灰色
      markPoint: { data: variants.map((v, i) =>
        ({ coord: [i, v.rate], value: v.p < 0.05 ? '★' : 'ns' })) },
    ]/* 误差线用 custom series 或 markLine 区间 [ci_lo, ci_hi] */,
  };
}
// 误差线（custom）核心：ci = mean ± 1.96 * sqrt(p(1-p)/n)
```
