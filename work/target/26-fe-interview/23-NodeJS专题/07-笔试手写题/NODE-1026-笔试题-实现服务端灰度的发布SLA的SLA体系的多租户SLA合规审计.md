---
title: [NODE-1026] 笔试题——实现租户 SLA 合规审计（租户维度扩展）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1026：手写租户合规

**需求与边界**：
- 需求：租户合规（SCN-SLA-997/1014）——① 租户维度扩展（SCN-SLA-997 + 1000/1014）；② 审计自动化（SCN-OPS-289）；③ 闭环（SCN-OPS-227）；④ 报告（SCN-OPS-728）。
- 边界：① 分层审计（SCN-SLA-992）；② 闭环（SCN-OPS-227）；③ 报告（SCN-OPS-728）。

**答**：
```javascript
async function tenantSlaAudit() {
  const results = await Promise.all([
    ...baseChecks(),                                   // SCN-SLA-997 五项
    tenantFairnessCheck(),                             // SCN-SLA-1000
    crossServiceSlaCheck(depsGraph),                   // SCN-SLA-1004
    slaDegradeAlignment(),                             // SCN-1010
  ]);
  const failures = results.filter(r => !r.ok);
  audit({ tenantSlaAudit: true, failures });           // 审计（SCN-OPS-289）
  return { failures, improvements: improvementLoop(failures) };   // 闭环（SCN-OPS-227/1002）
}
```

**评分点**:
- 基础 + 租户 + 跨服务 + 降级对齐全链审计（SCN-SLA-997/1000/1004/1010）。
- 闭环复用（SCN-OPS-227/1002）。
