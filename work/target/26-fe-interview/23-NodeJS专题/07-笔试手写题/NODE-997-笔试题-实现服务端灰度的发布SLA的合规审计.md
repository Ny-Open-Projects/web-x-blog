---
title: [NODE-997] 笔试题——实现 SLA 合规审计（SLA 体系的审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-997：手写 SLA 审计

**需求与边界**：
- 需求：SLA 审计（SCN-SLA-997/OPS-289）——① SLA 体系审计项（承诺 vs 实际/报告 vs 数据/预算 vs 冻结——SCN-SLA-987）；② 审计的自动化（跑数据——SCN-OPS-289）；③ 审计的闭环（发现→修复——SCN-OPS-227）；④ 审计的报告（SCN-OPS-728）。
- 边界：① 审计项的来源（事故/合规——SCN-OPS-289）；② 审计的周期（月度——SCN-OPS-289）；③ 审计的报告（SCN-OPS-728）。

**答**：
```javascript
async function slaAudit() {
  const checks = [
    { name: 'slo-strict-than-sla', run: sloSlaAlignment },   // SCN-SLA-987
    { name: 'report-replicable', run: () => verifyReplication(reports) },   // SCN-OPS-284
    { name: 'budget-freeze-executed', run: () => freezeExecuted(burnouts) },   // SCN-OPS-944
    { name: 'breach-tracked', run: () => breachesClosed(breaches) },   // SCN-SLA-974
  ];
  const failures = (await Promise.all(checks.map(c => c.run()))).filter(r => !r.ok);
  audit({ slaAudit: true, failures });                 // 审计（SCN-OPS-220）
  return { failures, fixes: failures.map(f => fixOf(f)) };   // 闭环（SCN-OPS-227）
}
```

**评分点**:
- 四项审计（SLO 对齐/可复核/冻结执行/违约跟踪——SCN-SLA-987/284/944/974）。
- 跑数据自动化（SCN-OPS-289）。
- 闭环（SCN-OPS-227）。
