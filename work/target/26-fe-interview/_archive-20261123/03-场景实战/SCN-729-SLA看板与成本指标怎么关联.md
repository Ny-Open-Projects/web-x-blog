---
title: [SCN-729] SLA 看板与成本/效率指标的关联（体验-成本权衡）怎么呈现？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-729：SLA 与成本关联怎么呈现？
**答**：
- 权衡可视化：优化决策常有「体验 vs 成本」权衡（CDN 加码降延迟 vs 带宽成本），看板提供「单位体验成本」派生指标（每降低 100ms P95 的月成本增量），供决策参考。
- 关联面板：SLA 指标旁挂对应成本趋势（带宽/算力），劣化治理投入与收益对照（投入 X 万，P95 改善 Y ms）。
- 预算联动：体验改善项目的 ROI 计算（流失率假设 + 转化提升模型）标注假设条件，不做虚假精确。
- 提醒克制：成本数据是决策辅助不是考核指标（一考核就有人砍监控采样省成本，损害数据可信度）。
- 追问钩子：为什么成本指标不能进考核——Goodhart 定律：考核什么就优化什么，把监控采样率调低「省成本」会让 SLA 数据失真，损失远大于节省。

```javascript
const costPanel = {
  derived: {
    costPer100ms: (cdnCost, p95) => cdnCost.delta / (p95.delta / 100),   // 决策辅助
  },
  roiTemplate: { assumption: 'conversion +0.3% per -200ms', markedAsAssumption: true },
  policy: 'cost metrics are advisory, never KPI',    // 防止砍采样省成本
};
```
