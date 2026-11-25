---
title: [NODE-1006] 笔试题——实现应急降级 SLA 豁免管理（豁免的审批与追溯）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1006：手写 SLA 豁免

**需求与边界**：
- 需求：SLA 豁免管理（SCN-OPS-229/985）——① 豁免的申请（应急降级——SCN-OPS-985）；② 豁免的审批（SCN-OPS-229）；③ 豁免的追溯（SCN-OPS-248）；④ 豁免的统计（豁免率——SCN-OPS-289）。
- 边界：① 豁免的边界（SCN-OPS-229 分级）；② 豁免的过期（SCN-OPS-229）；③ 豁免的审计（SCN-OPS-273）。

**答**：
```javascript
async function slaExemptionRequest(degradation, sla) {
  const exempt = degradationMatrix[degradation.type]?.slaExempt;   // SCN-OPS-329 声明
  if (exempt) return { exempt: true, auto: true };     // 声明豁免自动生效
  const approved = await requireApprovals(['owner', 'sla-team']);   // 审批（SCN-OPS-229）
  await recordExemption({ degradation, sla, approved, expiresAt: inHours(24) });   // 过期（SCN-OPS-229）
  audit({ exempt: true, approved });                   // 审计（SCN-OPS-273）
  exemptionRate.track(sla);                            // 豁免率（SCN-OPS-289）
}
```

**评分点**:
- 声明豁免自动生效 + 审批豁免（SCN-OPS-329/229）。
- 豁免过期 + 审计（SCN-OPS-229/273）。
- 豁免率监控（SCN-OPS-289）。
