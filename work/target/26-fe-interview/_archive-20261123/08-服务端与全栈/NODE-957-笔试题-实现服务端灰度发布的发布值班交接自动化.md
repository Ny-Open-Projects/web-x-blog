---
title: [NODE-957] 笔试题——实现发布值班交接自动化（班次摘要→交接）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-957：手写交接自动化

**需求与边界**：
- 需求：值班交接（SCN-OPS-210/746）——① 班次摘要自动生成（SCN-联想-746 班次摘要）；② 交接清单（灰度档位/待办/遗留——SCN-OPS-210）；③ 交接的确认（双方签字——SCN-OPS-210）；④ 交接的审计（SCN-OPS-220）。
- 边界：① 交接的数据源（FSM 日志/哨兵/告警——SCN-OPS-292/798）；② 交接的时效（班次结束前 30min——SCN-OPS-210）；③ 遗留的升级（SCN-OPS-210）。

**答**：
```javascript
async function shiftHandover(shift) {
  const summary = await shiftSummary(shift);           // SCN-联想-746 班次摘要
  const grayStates = activeGrays().map(g => ({
    app: g.app, stage: g.stage, nextGate: g.nextGate }));   // 灰度档位（SCN-OPS-210）
  const carry = summary.carryOver;                     // 遗留（SCN-联想-746）
  await ackHandover({ from: shift.oncall, to: nextOncall,
    summary, grayStates, carry });                     // 双方确认（SCN-OPS-210）
  audit({ handover: shift.id });                       // 审计（SCN-OPS-220）
}
```

**评分点**:
- 班次摘要复用（SCN-联想-746）。
- 灰度档位/遗留清单（SCN-OPS-210）。
- 双方确认 + 审计（SCN-OPS-210/220）。
