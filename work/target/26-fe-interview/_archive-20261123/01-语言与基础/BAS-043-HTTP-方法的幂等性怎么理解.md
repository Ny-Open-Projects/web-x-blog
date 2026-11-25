---
title: [BAS-043] HTTP 方法的幂等性怎么理解？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-043：HTTP 方法的幂等性怎么理解？
**答**：
- 幂等：同一请求执行一次和执行多次，服务器状态结果相同。
- GET/PUT/DELETE 幂等；POST 不幂等（每次都创建新资源）；PATCH 不保证幂等。
- 工程意义：幂等请求可以安全重试；POST 重试需要幂等键（Idempotency-Key）让服务端去重。

```javascript
// GET 超时后重试是安全的
const res = await fetch('/api/list');
// POST 创建订单不能盲目重试：带上幂等键，服务端按键去重
await fetch('/api/order', {
  method: 'POST',
  headers: { 'Idempotency-Key': crypto.randomUUID() },
  body: JSON.stringify({ sku: 'A001', num: 1 }),
});
```
