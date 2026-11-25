---
title: [AGT-813] 给企业开发者开放 Agent 能力（API/Webhook/SDK），开放平台怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-813：给企业开发者开放 Agent 能力（API/Webhook/SDK），开放平台怎么设计

**答**：
- 开放三件套：同步 API（发起任务/查询结果）、流式订阅（SSE/Webhook 回调任务事件）、SDK（带重试/幂等/类型）；开放面最小化：先只开放「任务发起+结果查询+事件订阅」三原语，编排能力暂不开放（防滥用）。
- Webhook 可靠性：签名验证+重试（指数退避 24h）+死信队列+投递报表；消费者幂等约定（eventId 判重）写进文档。
- 限流与配额：按应用（API key）维度配额，与人用配额分离；滥用检测（异常模式自动限流）。

```javascript
app.post('/v1/tasks', auth, async (req) => {
  const task = await runtime.dispatch(req.body, {
    idempotencyKey: req.header('Idempotency-Key'),  // 幂等必选
    quota: 'app:' + req.app.id,
  });
  return { taskId: task.id, stream: `/v1/tasks/${task.id}/events` };
});
function signWebhook(payload, secret) {
  return { 'x-signature': hmac(payload, secret),
    'x-event-id': genId(), 'x-timestamp': Date.now() }; // 重放防护
}
```

