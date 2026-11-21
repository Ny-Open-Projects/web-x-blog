---
title: [NODE-398] Node 服务的 Webhook 推送可靠性如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-398：Webhook 推送可靠性
**答**:
- 推送即"对外投递"：至少一次语义 + 重试退避（1m/5m/30m/2h... 指数，最多 24h）+ 死信（最终失败通知接入方走主动拉取兜底接口）。
- 投递幂等：每事件带 eventId，接入方去重（文档声明）；重试时 eventId 不变。
- 签名：每次推送 HMAC 签名（secret + body），接入方验签防伪造（NODE-363 timingSafeEqual）；secret 支持轮换（双 secret 过渡）。
- 端点健康：连续失败自动暂停推送（熔断）+ 告警接入方；恢复探测；超时设置（5s 快速失败优于长等）。
- 安全：SSRF 防护（NODE-356：回调 URL 注册时校验），HTTPS 强制；推送体大小限制。
- 可观测：每端点成功率/延迟看板、重试队列深度、接入方可自助重发（管理台"重新推送"按钮）。
```javascript
async function pushWebhook(endpoint, event) {
  const body = JSON.stringify(event);
  const sign = hmac(endpoint.secret, body);
  try {
    await fetch(endpoint.url, { method: 'POST', body, signal: AbortSignal.timeout(5000),
      headers: { 'x-signature': sign, 'x-event-id': event.id } });
    markDelivered(event.id, endpoint.id);
  } catch {
    await retryQueue.add(event, { delay: backoff(endpoint.failCount) });  // 退避重试
  }
}
```
