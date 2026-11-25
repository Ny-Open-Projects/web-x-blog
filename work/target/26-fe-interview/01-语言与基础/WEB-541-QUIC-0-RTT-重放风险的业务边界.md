---
title: [WEB-541] QUIC 0-RTT 重放风险的业务边界怎么划
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-541：QUIC 0-RTT 重放风险的业务边界怎么划

**答**：
- 0-RTT 数据没有防重放保护：攻击者可截获首包重放，服务端会执行两次，所以 0-RTT 只允许「幂等且无害」的请求
- 边界划法：静态资源、探测接口、登录前的配置拉取可开 0-RTT；下单、支付、改密码等写操作必须在 1-RTT 之后且服务端校验新鲜性
- 服务端要主动限制：0-RTT 只做「提前发送应用数据」，服务端可配置接受 0-RTT 的最大数据量，并拒绝在 0-RTT 里携带敏感 Cookie
- 前端配合：关键接口请求头带时间戳 + nonce，服务端短期去重表兜底，即使传输层被重放业务层也拦截
- 与 TLS1.3 早数据（early data）语义一致：`Early-Data: 1` 头到达源站时，源站必须能识别并拒绝非幂等处理

```javascript
// 业务层防重放兜底（0-RTT 请求可能被重放）
async function pay(orderId) {
  const nonce = crypto.randomUUID();
  const ts = Date.now();
  const res = await fetch('/api/pay', {
    method: 'POST',
    headers: { 'x-ts': String(ts), 'x-nonce': nonce },
    body: JSON.stringify({ orderId, ts, nonce }),
  });
  if (res.status === 425) return retryAfterHandshake(orderId); // Too Early
  return res.json();
}
// 服务端：nonce 短期去重（Redis SETNX + TTL 60s）+ ts 偏移校验
```
