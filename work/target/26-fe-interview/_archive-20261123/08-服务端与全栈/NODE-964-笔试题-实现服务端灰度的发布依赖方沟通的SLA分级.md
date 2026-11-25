---
title: [NODE-964] 笔试题——实现沟通 SLA 分级（通知时效分级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-964：手写沟通分级

**需求与边界**：
- 需求：沟通分级（SCN-OPS-891/964）——① 通知时效分级（P0 即时/P1 1h/P2 日摘要——SCN-OPS-891 SLA）；② 时效的监控（通知延迟——SCN-OPS-964）；③ 分级的审计（SCN-OPS-220）。
- 边界：① 分级的配置（SCN-OPS-663 热更）；② 分级与渠道联动（SCN-OPS-612）；③ 延迟告警（SCN-OPS-964）。

**答**：
```javascript
const SLA_TIERS = { P0: { maxDelay: 0, channel: 'im+sms' }, P1: { maxDelay: 3600_000 },
  P2: { maxDelay: 86400_000, channel: 'digest' } };    // 分级（SCN-OPS-891）
async function notifyWithSla(event, consumer) {
  const tier = SLA_TIERS[consumer.sla];
  const sentAt = await send(event, tier.channel);      // 渠道联动（SCN-OPS-612）
  const delay = sentAt - event.ts;
  if (delay > tier.maxDelay) alert({ type: 'NOTIFY_SLA_BREACH', delay, tier: consumer.sla });   // 延迟告警
  audit({ event: event.id, delay });
}
```

**评分点**:
- 分级定义（P0/P1/P2——SCN-OPS-891）。
- 延迟监控告警（SCN-OPS-964）。
- 渠道联动（SCN-OPS-612）。
