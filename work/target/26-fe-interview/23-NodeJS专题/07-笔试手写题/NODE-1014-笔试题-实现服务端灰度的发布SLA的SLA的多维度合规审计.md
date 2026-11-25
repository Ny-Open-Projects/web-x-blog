---
title: [NODE-1014] 笔试题——实现 SLA 多维度合规审计（五维扩展版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1014：手写多维合规

**需求与边界**：
- 需求：多维合规（SCN-SLA-997/1005）——① 五维扩展（+租户公平/跨服务一致——SCN-SLA-1000/1004）；② 审计自动化（SCN-OPS-289）；③ 闭环（SCN-OPS-227）；④ 报告（SCN-OPS-728）。
- 边界：① 七项审计（SCN-SLA-997 + 1000 + 1004）；② 周期（SCN-OPS-289）；③ 闭环（SCN-OPS-227）。

**答**：
```javascript
async function slaAuditExtended() {
  const checks = [
    ...baseChecks(),                                   // SCN-SLA-997 五项
    { name: 'tenant-fairness', run: tenantFairnessCheck },   // SCN-SLA-1000
    { name: 'cross-service-math', run: crossServiceSlaCheck },   // SCN-SLA-1004
    { name: 'degrade-alignment', run: slaDegradeAlignment },   // SCN-1010
  ];
  const failures = (await Promise.all(checks.map(c => c.run()))).filter(r => !r.ok);
  audit({ slaAudit: 'extended', failures });           // 审计（SCN-OPS-289）
  return { failures, improvements: improvementLoop(failures) };   // 闭环（SCN-OPS-227/1002）
}
```

**评分点**:
- 七项审计（基础五项 + 租户公平 + 跨服务 + 降级对齐）。
- 闭环复用（SCN-OPS-227/1002）。
