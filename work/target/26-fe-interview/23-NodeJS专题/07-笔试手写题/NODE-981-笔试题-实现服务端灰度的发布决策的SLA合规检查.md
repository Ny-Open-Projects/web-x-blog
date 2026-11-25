---
title: [NODE-981] 笔试题——实现发布决策 SLA 合规检查（决策时效合规）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-981：手写 SLA 合规

**需求与边界**：
- 需求：决策 SLA 合规（SCN-OPS-970/981）——① 决策时效合规检查（历史决策延迟 vs SLA——SCN-OPS-970）；② 违规报告（SCN-OPS-970）；③ 合规的改进（SCN-OPS-227）；④ 合规的审计（SCN-OPS-273）。
- 边界：① 合规的分位（P50/P99——SCN-SLA-725）；② 分级（SCN-OPS-210）；③ 报告（SCN-OPS-868）。

**答**：
```javascript
async function decisionSlaCompliance(period) {
  const decisions = decisionChain(period);
  const byLevel = groupBy(decisions, d => d.level);
  const compliance = Object.fromEntries(Object.entries(byLevel).map(([lvl, list]) => {
    const delays = list.map(d => d.decidedAt - d.triggeredAt).sort((a, b) => a - b);
    return [lvl, { p50: quantile(delays, 0.5), p99: quantile(delays, 0.99),   // 分位（SCN-SLA-725）
      withinSla: delays.every(d => d <= SLA_TIERS[lvl].maxDelay) }];   // SCN-OPS-970
  }));
  return { compliance, violations: violationsOf(compliance),
    actions: violations.map(v => improvementItem(v)) };   // 改进（SCN-OPS-227）
}
```

**评分点**:
- 分位合规（SCN-SLA-725）。
- 分级约束（SCN-OPS-210）。
- 改进项（SCN-OPS-227）。
