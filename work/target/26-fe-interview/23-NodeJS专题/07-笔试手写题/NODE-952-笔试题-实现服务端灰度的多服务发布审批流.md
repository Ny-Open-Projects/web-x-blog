---
title: [NODE-952] 笔试题——实现多服务发布审批流（组合审批路由）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-952：手写组合审批

**需求与边界**：
- 需求：组合审批（SCN-OPS-241/935）——① 组合审批路由（多服务发布——SCN-OPS-935 风险）；② 代理与升级（SCN-OPS-241）；③ 审批摘要（SCN-OPS-241）；④ 审批的审计（SCN-OPS-220）。
- 边界：① 组合审批的级别（组合风险——SCN-OPS-935）；② 审批人的冲突检测（SCN-OPS-253 自批）；③ 审批的时效（SCN-OPS-241）。

**答**：
```javascript
async function comboApprovalFlow(plans) {
  const comboRisk = comboRiskAssessment(plans);        // 组合风险（SCN-OPS-935）
  const nodes = APPROVAL_TEMPLATES[comboRisk.level];   // 风险分级路由（SCN-OPS-241）
  const flow = nodes.map(n => ({
    role: n.role, approvers: activeMembers(n.role)
      .filter(u => !plans.some(p => p.by === u)),      // 自批防御（SCN-OPS-253）
    brief: comboBrief(plans),                          // 摘要（SCN-OPS-241）
    timeout: n.timeout, escalate: n.escalateTo,
  }));
  audit({ combo: plans.map(p => p.app), flow });       // 审计（SCN-OPS-220）
  return { flow };
}
```

**评分点**:
- 组合风险路由（SCN-OPS-935）。
- 自批防御 + 摘要（SCN-OPS-253/241）。
- 超时升级（SCN-OPS-241）。
- 审计（SCN-OPS-220）。
