---
title: [NODE-891] 笔试题——实现发布依赖方 SLA 风险分级（影响面排序）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-891：手写 SLA 分级

**需求与边界**：
- 需求：发布影响面 SLA 分级（SCN-OPS-885/643）——① 消费方 SLA 等级（P0/P1/P2——SCN-OPS-643）；② 风险排序（P0 消费方优先评估——SCN-OPS-885）；③ 影响面 × SLA 的风险评估矩阵（发布风险定级输入——SCN-OPS-202）；④ 分级联动通知（P0 优先 ack——SCN-OPS-864）。
- 边界：① SLA 等级的数据源（契约注册表——SCN-NODE-768）；② 分级规则的可解释（SCN-OPS-202 显式因素）；③ 分级的时效（SLA 变更同步——SCN-OPS-260）。

**答**：
```javascript
function slaRiskRanking(impacted, plan) {
  return impacted.map(c => ({
    consumer: c, sla: c.slaLevel,
    riskScore: SLA_WEIGHT[c.sla] * impactWeight(c, plan),   // 风险矩阵（SCN-OPS-202 因子）
    ackFirst: c.slaLevel === 'P0',                     // P0 优先 ack（SCN-OPS-864）
  })).sort((a, b) => b.riskScore - a.riskScore);       // 风险排序
  // 因子显式（SCN-OPS-202）：SLA 权重 × 调用频次 × 关键度
}
```

**评分点**:
- SLA 等级矩阵（SCN-OPS-643）。
- 风险因子显式（SCN-OPS-202）。
- P0 优先 ack（SCN-OPS-864）。
- 数据源契约（SCN-NODE-768）。
