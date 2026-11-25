---
title: [NODE-1017] 笔试题——实现 SLA 改进项追踪（审计→改进→闭环）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1017：手写改进追踪

**需求与边界**：
- 需求：改进追踪（SCN-SLA-1002/OPS-227）——① 改进项声明（SCN-SLA-1002）；② 跟踪（期限/验证——SCN-OPS-227）；③ 闭环校验（SCN-OPS-227）；④ 逾期升级（SCN-OPS-227）。
- 边界：① 改进的可验证（SCN-OPS-227）；② 跟踪的工单（SCN-SLA-974）；③ 逾期升级（SCN-OPS-227）。

**答**：
```javascript
async function slaImprovementTracking(improvements) {
  for (const imp of improvements) {
    const ticket = await createTicket({ ...imp, due: imp.due, verify: imp.verify });   // 工单（SCN-SLA-974）
    ticket.onDue(async () => {
      const passed = await verifyImprovement(imp);     // 验证（SCN-OPS-227）
      passed ? closeTicket(ticket) : escalate(imp);    // 闭环/逾期升级（SCN-OPS-227）
    });
  }
}
```

**评分点**:
- 改进项声明（SCN-SLA-1002）。
- 工单跟踪 + 闭环 + 逾期升级（SCN-SLA-974/OPS-227）。
