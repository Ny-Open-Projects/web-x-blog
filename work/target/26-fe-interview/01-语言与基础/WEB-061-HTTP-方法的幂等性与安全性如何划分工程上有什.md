---
title: [WEB-061] HTTP 方法的幂等性与安全性如何划分？工程上有什么用？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-061：HTTP 方法的幂等性与安全性如何划分？工程上有什么用？
**答**：
- 安全方法：GET、HEAD、OPTIONS，只读不改变服务器状态；幂等方法：GET、HEAD、OPTIONS、PUT、DELETE、TRACE，重复执行效果与一次相同。
- POST 既不安全也不幂等；PATCH 理论上幂等性未定义，取决于补丁语义（如"加 1"操作重复执行结果不同）。
- 工程意义：幂等方法可以安全重试——网络超时后重发 PUT/DELETE 不会造成重复副作用；支付下单等 POST 不能盲目重试，需要幂等键（Idempotency-Key）兜底。
- 浏览器与代理对幂等方法有预判：GET/HEAD 可被缓存、失败自动重连，POST 则不会。

```javascript
// 只有幂等方法才允许自动重试，这是网关和请求库的核心设计
async function requestWithRetry(url, options, maxRetry = 2) {
  const idempotent = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'DELETE'].includes(options.method);
  for (let i = 0; ; i++) {
    try {
      return await fetch(url, options);
    } catch (err) {
      // 非幂等请求超时重试可能造成重复下单，必须直接抛出
      if (!idempotent || i >= maxRetry) throw err;
      await new Promise((r) => setTimeout(r, 2 ** i * 500)); // 指数退避
    }
  }
}
```
