---
title: [NODE-864] 笔试题——实现发布通知与 ack 门（未确认阻断）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-864：手写通知 ack 门

**需求与边界**：
- 需求：发布通知 ack（SCN-OPS-245/303）——① 依赖方识别（API 变更的消费方——SCN-OPS-303）；② ack 门（未确认阻断发布——SCN-OPS-245）；③ ack 超时升级（SCN-OPS-303）；④ 通知降噪（SCN-OPS-320）。
- 边界：① ack 的责任路由（依赖方的对接人——SCN-OPS-241 角色路由）；② ack 的豁免（紧急发布豁免——SCN-OPS-229）；③ ack 记录审计（SCN-OPS-220）。

**答**：
```javascript
async function preReleaseNotify(plan) {
  const dependents = await dependentsOf(plan.app);     // 依赖方（SCN-OPS-303）
  const needAck = dependents.filter(d => apiChanged(plan, d));
  for (const d of needAck) {
    await notify({ to: d.ownerRole,                    // 角色路由（SCN-OPS-241）
      payload: { apiDiff: plan.apiDiff, sunset: plan.sunset },
      ackRequired: true, escalateAfter: '24h' });      // 超时升级
  }
  const unacked = needAck.filter(d => !acked(d));
  if (unacked.length && !plan.hotfixWaiver)
    return { blocked: true, unacked };                 // ack 门（SCN-OPS-245）
  audit({ plan: plan.id, unacked, waived: !!plan.hotfixWaiver });   // 审计（SCN-OPS-220）
}
```

**评分点**:
- 依赖方识别（API 变更消费方——SCN-OPS-303）。
- ack 门阻断 + 超时升级（SCN-OPS-245）。
- 角色路由（SCN-OPS-241）。
- 豁免 + 审计（SCN-OPS-229/220）。
