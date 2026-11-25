---
title: [NODE-114] Koa 的 onerror 机制如何设计完整错误边界？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-114：Koa 的 onerror 机制如何设计完整错误边界？
**答**：
- 三层边界：**ctx.onerror**（框架内，把异常转 HTTP 响应）→ **app.on('error')**（应用级统一记录）→ **process 兜底**（uncaughtException 记录后退出交给守护拉起）。
- Koa 约定：`err.status` 决定响应码（无则 500）；`err.expose` 决定 message 是否暴露给客户端——内部错误只回笼统文案，防栈与 SQL 泄漏。
- `app.emit('error')` 无监听器时 Emitter 会抛异常崩进程，所以 Application 必须默认 onerror（NODE-109）。
- 响应体里带 traceId，用户报障可直接按 id 查日志（NODE-133）。

```javascript
// 应用级错误中间件（洋葱最外层，业务抛错沿 Promise 冒泡到这）
app.use(async (ctx, next) => {
  try {
    await next();
  } catch (err) {
    ctx.status = err.status ?? 500;
    ctx.body = {
      code: err.code ?? 'INTERNAL_ERROR',
      // expose 标记的业务错误才回传 message，内部错误统一文案防泄漏
      message: err.expose ? err.message : 'Internal Server Error',
      traceId: als.getStore()?.traceId,
    };
    ctx.app.emit('error', err, ctx); // 交给 app.onerror 统一记录
  }
});

app.on('error', (err, ctx) => {
  const level = (err.status ?? 500) >= 500 ? 'error' : 'warn';
  logger[level]({ stack: err.stack, status: err.status, url: ctx?.url,
    traceId: ctx?.state?.traceId }, 'request error');
});

// 进程级兜底：记录后退出优于带病运行，PM2/K8s 负责拉起（NODE-142/184）
process.on('uncaughtException', (err) => {
  logger.fatal({ stack: err.stack }, 'uncaught exception, exiting');
  process.exit(1);
});
process.on('unhandledRejection', (err) => logger.error({ stack: err?.stack }, 'unhandled rejection'));
```

---

## 十三、网络与协议深入
