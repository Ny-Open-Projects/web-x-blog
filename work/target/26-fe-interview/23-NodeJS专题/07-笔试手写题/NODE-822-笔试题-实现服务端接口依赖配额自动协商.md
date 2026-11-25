---
title: [NODE-822] 笔试题——实现上下游配额自动协商（超限预警与再分配）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-822：手写配额协商

**需求与边界**：
- 需求：配额管理（SCN-NODE-710）——① 使用率监控（逼近上限告警——SCN-NODE-710）；② 配额再分配（大促上游间调配——SCN-NODE-710 可协商）；③ 协商协议（向下游请求临时配额——自动化协商 API）；④ 全局一致性校验（SCN-NODE-699）。
- 边界：① 协商的授权（再分配需双方同意——API 确认语义）；② 临时配额的 TTL（活动期——到期回收）；③ 配额协商的审计（SCN-OPS-220）。

**答**：
```javascript
// 使用率监控 → 协商触发
setInterval(() => {
  const used = quotaUsedPct('order-svc');
  if (used > 0.8 && !negotiating) negotiateQuota('order-svc');
}, 60_000);
async function negotiateQuota(downstream) {
  const request = { current: quota(downstream), wanted: quota(downstream) * 1.5,
    reason: '大促扩容', until: endOfCampaign() };
  const granted = await downstreamQuotaAPI.request(request, {   // 自动协商（确认语义——SCN-NODE-710）
    auth: CONTRACT_ADMIN_TOKEN });
  if (granted.ok) {
    quota.set(downstream, granted.newQuota);           // 生效
    audit({ action: 'quota-negotiated', downstream, granted });   // 审计（SCN-OPS-220）
    scheduleRevert(downstream, request.until);         // TTL 到期回收
  } else escalateQuotaConflict(downstream, granted);   // 协商失败升级（人工）
}
```

**评分点**:
- 使用率监控触发协商（80% 告警前置——SCN-NODE-710）。
- 自动协商 API（确认语义 + TTL 回收）。
- 协商失败升级人工（可解释冲突——SCN-OPS-278）。
- 审计留痕（SCN-OPS-220）。
