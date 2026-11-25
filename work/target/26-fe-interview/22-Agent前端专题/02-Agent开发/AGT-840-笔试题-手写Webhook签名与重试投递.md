---
title: [AGT-840] 手写 WebhookDispatcher：HMAC签名、时间戳防重放、指数退避重试、死信队列、幂等eventId？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-840：手写 WebhookDispatcher：HMAC签名、时间戳防重放、指数退避重试、死信队列、幂等eventId

**需求与边界**：
- 实现 signWebhook(payload, secret) 与 dispatch(event, url)。
- 边界要求：① 签名覆盖 payload+timestamp（防篡改+防重放，5 分钟窗口）；② 重试 5 次指数退避（1m/2m/4m/8m/16m），24h 内完成；③ 死信入队并告警；④ eventId 幂等（同事件不重复投递成功后重发）；⑤ 消费方响应 2xx 才算成功。

**答**：
```javascript
function signWebhook(payload, secret) {
  const ts = Date.now();
  const body = JSON.stringify(payload);
  return { body, headers: {
    'x-signature': hmac(`${ts}.${body}`, secret),
    'x-timestamp': ts, 'x-event-id': payload.id } };
}
function verifyWebhook(headers, body, secret, { window = 5 * 60000 } = {}) {
  if (Math.abs(Date.now() - headers['x-timestamp']) > window)
    return false;                                  // 重放窗口
  return timingSafeEq(headers['x-signature'],
    hmac(`${headers['x-timestamp']}.${body}`, secret));
}
class WebhookDispatcher {
  async dispatch(event, url, secret) {
    for (let i = 0; i < 5; i++) {
      const { body, headers } = signWebhook(event, secret);
      const res = await fetch(url, { method: 'POST', body, headers });
      if (res.ok) return { delivered: true, attempts: i + 1 };
      await sleep(Math.min(60000 * 2 ** i, 16 * 60000)); // 退避
    }
    await dlq.push(event, { url });                // 死信
    alert({ type: 'webhook_dlq', event: event.id });
    return { delivered: false };
  }
}
```

**评分点**:
- 签名绑定时间戳+重放窗口校验；timingSafeEq 防时序攻击。
- 退避封顶 16m 且总时长 24h 内；死信+告警不静默丢弃。
- 2xx 判成功（消费方幂等约定靠 eventId）。

