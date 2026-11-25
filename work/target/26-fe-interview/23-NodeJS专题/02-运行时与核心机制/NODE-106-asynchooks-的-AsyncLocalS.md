---
title: [NODE-106] async_hooks 的 AsyncLocalStorage 如何追踪请求上下文？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-106：async_hooks 的 AsyncLocalStorage 如何追踪请求上下文？
**答**：
- 问题：一条请求链路上任意深度的异步函数都想要 traceId/uid，逐层传参太丑，全局变量会串请求。
- `AsyncLocalStorage.run(store, cb)` 建立**异步作用域**：作用域内派生的所有异步操作（promise/定时器/流回调）都能 `getStore()` 取到同一 store。
- 原理：async_hooks 在每个异步资源创建时捕获当前 execution context，形成异步作用域树，ALS 沿树读取。
- 坑：连接池借用连接的回调可能脱离作用域、`setTimeout` 长寿命回调要小心；跨池边界建议显式传参兜底。

```javascript
const { AsyncLocalStorage } = require('async_hooks');
const { randomUUID } = require('crypto');
const als = new AsyncLocalStorage();

// Koa 中间件：进入时建立上下文存储
app.use((ctx, next) =>
  als.run({ traceId: ctx.get('x-trace-id') || randomUUID(), uid: ctx.state.uid }, next));

// 深层工具函数：不传任何上下文参数也能打全链路日志
async function orderDbQuery(sql, params) {
  const { traceId, uid } = als.getStore() ?? {};
  logger.info({ traceId, uid, sql }, 'db query');
  return db.query(sql, params);
}

// HTTP 客户端自动透传 traceId（NODE-136）
function upstreamHeaders(extra = {}) {
  return { 'x-trace-id': als.getStore()?.traceId, ...extra };
}
```
