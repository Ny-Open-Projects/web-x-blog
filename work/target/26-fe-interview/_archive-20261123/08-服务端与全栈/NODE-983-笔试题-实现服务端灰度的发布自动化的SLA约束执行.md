---
title: [NODE-983] 笔试题——实现发布自动化的 SLA 约束执行（自动决策受 SLA 约束）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-983：手写 SLA 约束执行

**需求与边界**：
- 需求：SLA 约束执行（SCN-OPS-976/983）——① 自动决策的 SLA 约束（决策时效——SCN-OPS-970）；② 约束违反的处理（降级为人工——SCN-OPS-210 升级）；③ 约束的审计（SCN-OPS-273）；④ 约束的演练（SCN-OPS-215）。
- 边界：① 约束的分级（SCN-OPS-210）；② 约束的动态（SCN-NODE-663）；③ 违反的告警（SCN-OPS-276）。

**答**：
```javascript
async function automatedDecisionWithSla(decision) {
  const sla = SLA_TIERS[decision.level];               // 分级（SCN-OPS-210）
  const result = await Promise.race([
    executeDecision(decision),                         // SCN-OPS-960
    sleep(sla.maxDelay).then(() => ({ escalated: true })),   // 超时升级（SCN-OPS-210）
  ]);
  if (result.escalated) {
    alert({ type: 'AUTO_DECISION_SLA_BREACH', decision });   // 告警（SCN-OPS-276）
    return humanEscalation(decision);                  // 降级为人工（SCN-OPS-210）
  }
  audit({ decision, result });                         // 审计（SCN-OPS-273）
  return result;
}
```

**评分点**:
- 自动决策受 SLA 约束（SCN-OPS-970）。
- 超时降级人工（SCN-OPS-210）。
- 告警 + 审计（SCN-OPS-276/273）。
