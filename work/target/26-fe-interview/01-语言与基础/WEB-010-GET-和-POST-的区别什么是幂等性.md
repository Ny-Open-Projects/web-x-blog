---
title: [WEB-010] GET 和 POST 的区别？什么是幂等性？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-010：GET 和 POST 的区别？什么是幂等性？
**答**：
- 语义上 GET 是安全幂等的（只读、重复执行结果一致），POST 非幂等（重复提交会重复创建）。
- GET 参数在 URL 里，受长度与缓存影响，可被收藏/缓存；POST 参数在 Body，默认不缓存。
- 本质上都是 TCP 上的报文，"GET 有长度限制"是浏览器和服务器对 URL 的限制，不是协议限制。
- 幂等性直接影响重试策略：GET/PUT/DELETE 可安全重试，POST 重试必须带幂等键（如 Idempotency-Key）。

```javascript
// 用幂等键防止 POST 重复提交，这是支付/下单场景的标准做法
async function createOrder(order) {
  const key = crypto.randomUUID(); // 同一笔订单业务侧应保持同一个 key
  const res = await fetch('/api/orders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Idempotency-Key': key, // 服务端对该 key 去重，网络重试不会重复下单
    },
    body: JSON.stringify(order),
  });
  if (!res.ok) throw new Error(`create order failed: ${res.status}`);
  return res.json();
}

// 对比：GET 失败可以直接无脑重试，因为它幂等
async function safeGet(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) return res.json();
    } catch (e) {
      /* 网络错误，继续重试 */
    }
  }
  throw new Error('get failed after retries');
}
```

## 二、HTTPS 与 TLS
