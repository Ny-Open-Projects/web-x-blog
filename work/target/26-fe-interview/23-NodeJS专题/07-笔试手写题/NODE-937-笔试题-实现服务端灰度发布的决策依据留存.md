---
title: [NODE-937] 笔试题——实现灰度决策依据留存（决策→快照→审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-937：手写决策留存

**需求与边界**：
- 需求：决策依据留存（SCN-OPS-273/244）——① 决策快照（决策时的看板/指标——SCN-OPS-273 计划冻结语义）；② 决策人/依据/时间（SCN-OPS-273）；③ 快照的检索（复盘——SCN-OPS-248）；④ 依据的完整性校验（SCN-OPS-309 要素）。
- 边界：① 快照的不可变（append-only——SCN-NODE-775）；② 决策的权限（SCN-OPS-253）；③ 快照的消费（演练/审计——SCN-OPS-220）。

**答**：
```javascript
async function recordDecision(release, decision) {
  requireRole(decision.by, decision.requires);         // 权限（SCN-OPS-253）
  const snapshot = {
    board: await grayBoard(release),                   // 决策时看板（SCN-OPS-858）
    metrics: await versionMetrics(release),
    decision, by: decision.by, ts: Date.now(),
  };
  await appendDecision(snapshot);                      // append-only（SCN-NODE-775）
  audit({ decision: decision.action, by: decision.by });   // 审计（SCN-OPS-273）
  return { recorded: true };
}
// 完整性校验（SCN-OPS-309）
const missing = REQUIRED_DECISION_FIELDS.filter(f => !(f in decision));
```

**评分点**:
- 决策快照（看板+指标——SCN-OPS-273 计划冻结）。
- append-only + 权限（SCN-NODE-775/OPS-253）。
- 检索消费（SCN-OPS-248）。
- 完整性校验（SCN-OPS-309）。
