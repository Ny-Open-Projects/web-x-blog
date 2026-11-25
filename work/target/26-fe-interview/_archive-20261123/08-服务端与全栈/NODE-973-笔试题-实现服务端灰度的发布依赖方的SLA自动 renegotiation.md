---
title: [NODE-973] 笔试题——实现 SLA 自动 renegotiation（使用率驱动配额调整）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-973：手写 SLA renegotiation

**需求与边界**：
- 需求：SLA renegotiation（SCN-NODE-822/973）——① 使用率驱动（配额使用率 80% → 协商——SCN-NODE-822）；② renegotiation 的流程（提案/确认/生效——SCN-NODE-822）；③ renegotiation 的审计（SCN-OPS-220）；④ 降级 renegotiation（使用率持续低——降配额，SCN-NODE-822）。
- 边界：① 双向（升/降——SCN-NODE-822）；② 协商的确认（双方——SCN-OPS-241）；③ 生效的灰度（SCN-OPS-228）。

**答**：
```javascript
async function slaRenegotiate(consumer) {
  const usage = await quotaUsagePct(consumer);
  if (usage > 0.8) return negotiateUp(consumer);       // 升（SCN-NODE-822）
  if (usage < 0.3 && monthsLow(consumer) >= 3) return negotiateDown(consumer);   // 降（SCN-NODE-822）
}
async function negotiateUp(consumer) {
  const granted = await requestQuota(consumer, { wanted: quota(consumer) * 1.5 });   // SCN-NODE-822
  if (granted.ok) { applyQuota(consumer, granted); audit({ consumer, granted }); }   // 审计
  else escalate(consumer);
}
```

**评分点**:
- 双向 renegotiation（升/降——SCN-NODE-822）。
- 使用率驱动 + 持续低检测。
- 确认 + 审计（SCN-OPS-241/220）。
