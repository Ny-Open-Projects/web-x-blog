---
title: [AGT-663] 评测接入 CI 后越跑越贵越跑越慢，如何治理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-663：评测接入 CI 后越跑越贵越跑越慢，如何治理

**答**：
- 三道闸：触发闸（按改动影响面决定跑哪层，改文案不跑全量）、规模闸（并行+缓存+增量，见前面优化）、预算闸（单次 CI 评测预算上限，超预算降级为抽样子集跑并标注"抽样结论"）。
- 时长治理的杀手锏是「影响面映射」：维护提示词/工具→用例的映射表，diff 精确路由到受影响用例子集，比"全跑"快 10 倍且结论不损失。
- 费用归因：每次 CI 评测记账到 PR/团队，用数据推动"谁在让 CI 变贵"。

```javascript
function ciEvalPlan(pr) {
  const impact = diffImpact(pr);                  // 影响面映射
  const tier = impact.promptCore ? 'smoke+regress'
    : impact.copilot ? 'smoke(affected)' : 'smoke';
  const plan = { tier, cases: routeCases(impact, tier) };
  if (estCost(plan) > CI_BUDGET)
    plan.cases = sampleStratified(plan.cases, 0.5),
    plan.sampled = true;                          // 超预算抽样并标注
  return plan;
}
```

