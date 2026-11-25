---
title: [NODE-252] Koa 错误处理的 ctx.throw 与 error 事件？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-252：Koa 错误处理的 ctx.throw 与 error 事件？
**答**:
- ctx.throw(404)：构造 HttpError（带 status/expose）→ 洋葱里继续向上抛 → app 的默认 error 中间件捕获。
- error 事件：app.on('error') 兜底所有未捕获错误（中间件回调里的异常都会冒到这里）——接入监控上报（NODE-37x）。
- expose 语义：err.expose = true（4xx）时输出 message 给客户端，5xx 不输出（防信息泄漏）。
- 统一错误中间件实践：捕获 → 归一化错误码（NODE-032）→ 上报 → 按态返回（JSON/HTML）。

```javascript
// Koa 错误链
app.use(async (ctx, next) => {
  try {
    await next();
  } catch (err) {
    err.status ??= 500;
    monitor.report(err, ctx);                     // 上报（含 trace id）
    ctx.status = err.status;
    ctx.body = err.expose || err.status < 500
      ? { code: err.code ?? 'ERR', message: err.message }
      : { code: 'INTERNAL', message: '服务开小差了' };   // 5xx 不暴露内部信息
    ctx.app.emit('error', err, ctx);              // error 事件兜底记录
  }
});
// 业务侧：ctx.throw(403, '无权限', { code: 'PERM_DENIED', expose: true })
```
