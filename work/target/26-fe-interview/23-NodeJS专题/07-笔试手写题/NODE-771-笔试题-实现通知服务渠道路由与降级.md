---
title: [NODE-771] 笔试题——实现通知服务渠道路由（矩阵 + 回执 + 降级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-771：手写通知路由

**需求与边界**：
- 需求：通知服务（SCN-NODE-685）——① 渠道路由矩阵（事件级 → 渠道清单——SCN-OPS-612）；② 频控（用户日上限——SCN-联想-557）；③ 回执状态机（发送/送达/失败——SCN-NODE-683 语义）；④ 失败降级链（短信→语音/Push——SCN-联想-558）。
- 边界：① 退订即停（合规——退订名单前置检查）；② 渠道费率与配额（渠道配额池——SCN-NODE-710 契约）；③ 内容模板化 + 审核（运营配置——SCN-OPS-610）。

**答**：
```javascript
async function notify(event, user) {
  if (unsubscribed(user, event.type)) return { skipped: 'UNSUBSCRIBED' };   // 退订前置
  if (await overDailyQuota(user, event.type)) return { skipped: 'QUOTA' };   // 频控（SCN-联想-557）
  const channels = routeMatrix[event.type](user);      // 路由矩阵（SCN-OPS-612）
  for (const ch of channels) {                         // 降级链（SCN-联想-558）
    const result = await withRetry(() => channelSend(ch, user, event), 2);
    if (result.ok) { markSent(event.id, ch); return { sent: ch }; }
    report({ type: 'CHANNEL_FAIL', ch, event: event.type });   // 降级前记录
  }
  await dlq(event); alert('ALL_CHANNELS_FAILED');      // 全失败死信
}
// 回执状态机
receiptConsumer.on('receipt', (r) => {
  updateState(r.msgId, r.status);                      // sent→delivered/failed（SCN-NODE-683）
  r.status === 'FAILED' && scheduleRetryOrFallback(r);
});
```

**评分点**:
- 路由矩阵 + 频控 + 退订三前置（SCN-OPS-612/联想-557）。
- 渠道降级链（失败逐渠道尝试——SCN-联想-558）。
- 回执状态机闭环（失败可见可补偿——SCN-NODE-683/685）。
- 全失败死信告警（显式兜底）。
