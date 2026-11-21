---
title: [NODE-024] Koa2 的 async 中间件中，try/catch 应该放在哪里？错误如何冒泡？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-024：Koa2 的 async 中间件中，try/catch 应该放在哪里？错误如何冒泡？
**答**：
- Koa 的错误冒泡沿 `await next()` 链**向上抛**：`app.on('error')` 只是日志钩子，真正兜底是 `app.use` 的最外层 try/catch 或 ctx.app.emit。
- 最佳实践：**最外层放一个统一的错误处理中间件**（记录日志、转换错误码、脱敏内部错误），内层业务代码只管 `throw`，不重复 try/catch；context 上挂 `ctx.throw(status, msg)` 抛出带状态码的业务异常。
- 高频坑：Koa 只捕获 **Promise 链上的异常**，`setTimeout` 里的 throw 与 EventEmitter 的 `error` 事件不会进入洋葱，必须额外处理（domain 已废弃，用 process 级兜底 + 显式 emit）。

```javascript
const Koa = require('koa');
const app = new Koa();

// 统一错误处理：最外层第一个中间件
app.use(async (ctx, next) => {
  const start = Date.now();
  try {
    await next();
  } catch (err) {
    const status = err.status || err.statusCode || 500;
    ctx.status = status;
    ctx.body = {
      code: err.code || (status >= 500 ? 'INTERNAL' : 'BAD_REQUEST'),
      message: status >= 500 ? 'Internal Server Error' : err.message, // 500 脱敏
    };
    ctx.app.emit('error', err, ctx);   // 交给全局 error 事件记日志
    console.error(`[${ctx.method} ${ctx.url}] ${status} ${Date.now() - start}ms`, err);
  }
});

// 业务中间件：只管 throw / ctx.throw
app.use(async (ctx) => {
  const { id } = ctx.query;
  if (!id) ctx.throw(400, '缺少参数 id');        // 抛出 400 业务异常
  const user = await Promise.reject(new Error('db down')); // 500 自动冒泡到最外层
  ctx.body = user;
});

// 日志钩子（注意：它只收 emit，不改变响应）
app.on('error', (err, ctx) => {
  console.error(JSON.stringify({ level: 'error', msg: err.message, url: ctx?.url }));
});

// 不进洋葱的异常：setTimeout 内的 throw
process.on('uncaughtException', (err) => console.error('未捕获异常，告警后决定是否退出:', err));

app.listen(3000);
```
