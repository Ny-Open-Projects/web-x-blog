---
title: [PER-1223] 如何评估性能平台"该自研还是采购"（Sentry/Datadog vs 自建）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1223：如何评估性能平台"该自研还是采购"（Sentry/Datadog vs 自建）

**答**：
- 评估维度：需求匹配度（自定义指标/数据出境/多端）、成本（License vs 人力）、数据主权（合规要求私有化）、生态整合（现有数据平台）。
- 混合策略：RUM 采购（Sentry）+ 业务指标自建管道 + 归因能力自研——避免全自研陷阱。
- 决策记录：按 1115 ADR 模板记录，含退出成本（数据可导出性）。
- 常见结论：采集 SDK 用开源（web-vitals），存储与看板按合规要求定。

```javascript
// 自研/采购决策评分
function buildVsBuy(options) {
  const W = { fit: 3, cost: 2, sovereignty: 4, ecosystem: 1 };
  return options.map(o => ({ ...o,
    score: W.fit * o.fit + W.cost * o.cost + W.sovereignty * o.sovereignty +
           W.ecosystem * o.ecosystem }))
    .sort((a, b) => b.score - a.score)[0];
}
// options: [{ name: 'Sentry', fit: 4, cost: 3, sovereignty: 2, ecosystem: 4 },
//           { name: '自建', fit: 5, cost: 1, sovereignty: 5, ecosystem: 3 }]
```
