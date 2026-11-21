---
title: [NODE-165] 设计一个 webhook 系统（签名/重试/死信）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-165：设计一个 webhook 系统（签名/重试/死信）？
**答**：
- 投递协议：POST JSON + **HMAC 签名头**（接收端用同一 secret 重算对比，防伪造与篡改）；带事件 id 供接收端幂等去重。
- 重试策略：指数退避（1/2/4/8/16s），**4xx 语义失败不重试**（签名错/参数错重试也没用），5xx 与 429 与网络错误重试。
- 死信：N 次失败入死信表 + 通知订阅方管理员，支持控制台手动重投。
- 接收端守则：验签在解析处理前、按事件 id 幂等、处理慢先 202 入本地队列（我们的重试会打挂同步处理方）。

```javascript
async function deliver(sub, event) {
  const payload = JSON.stringify({ id: event.id, type: event.type, data: event.data, ts: Date.now() });
  const sig = crypto.createHmac('sha256', sub.secret).update(payload).digest('hex');

  for (let attempt = 0; attempt < 5; attempt++) {
    try {
      const res = await fetch(sub.url, {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-webhook-signature': `sha256=${sig}`,   // 接收端验签依据
          'x-webhook-id': event.id,                  // 接收端幂等键
        },
        body: payload,
        signal: AbortSignal.timeout(5000),
      });
      if (res.ok) return recordSuccess(event, sub);
      if (res.status < 500 && res.status !== 429) return recordDead(event, sub, 'no-retry');
    } catch { /* 网络错误继续重试 */ }
    await sleep(2 ** attempt * 1000);                // 1s/2s/4s/8s/16s
  }
  await deadLetter(event, sub);                      // 死信表 + 通知订阅方
}
```
