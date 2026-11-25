---
title: [NODE-1005] 笔试题——实现 SLA 合规变更管理（SLA 变更的合规审查）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1005：手写合规变更

**需求与边界**：
- 需求：合规变更（SCN-SLA-965/1005）——① SLA 变更的合规审查（数据保护/合同条款——SCN-OPS-289 审计）；② 变更的通知（合同方——SCN-OPS-245）；③ 变更的审计（SCN-OPS-273）；④ 变更的双跑（SCN-SLA-710）。
- 边界：① 合规的审查项（SCN-OPS-289）；② 变更的权限（SCN-OPS-253）；③ 变更的归档（SCN-OPS-248）。

**答**：
```javascript
async function slaComplianceChange(consumer, newSla) {
  const compliance = await complianceReview(newSla, { checks: ['gdpr', 'contract-terms'] });   // 合规审查（SCN-OPS-289）
  if (!compliance.ok) return { blocked: compliance.issues };
  const approvals = await requireApprovals(['legal', 'owner']);   // 权限（SCN-OPS-253）
  await dualRun(consumer, { oldSla, newSla, duration: '14d' });   // 双跑（SCN-SLA-710）
  await notify({ to: consumer.contractParty, payload: { newSla } });   // 通知（SCN-OPS-245）
  await archiveSlaChange({ consumer, newSla, approvals });   // 归档（SCN-OPS-248）
  audit({ consumer, change: 'sla' });                  // 审计（SCN-OPS-273）
}
```

**评分点**:
- 合规审查（GDPR/合同——SCN-OPS-289）。
- 权限 + 通知 + 归档（SCN-OPS-253/245/248）。
- 双跑（SCN-SLA-710）。
