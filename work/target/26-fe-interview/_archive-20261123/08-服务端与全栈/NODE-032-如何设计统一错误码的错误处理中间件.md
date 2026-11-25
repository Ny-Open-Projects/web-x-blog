---
title: [NODE-032] 如何设计统一错误码的错误处理中间件？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-032：如何设计统一错误码的错误处理中间件？
**答**：
- 三层设计：① **业务异常类** `BizError`（携带 code/message/status/logLevel）；② **错误中间件**（区分已知业务错误与未知异常，500 脱敏不外泄堆栈）；③ **全局兜底**（`app.on('error')` 记结构化日志 + 告警）。
- 错误码规范建议：数字段（如 `10001` 用户未登录）或 `DOMAIN_REASON` 字符串（`AUTH_EXPIRED`），HTTP status 与业务 code 解耦——HTTP 只表达传输层语义，code 表达业务语义。
- 必备细节：错误日志带 traceId 便于全链路追踪；未捕获的 async 异常必须收敛到这条链路；不要把 `err.stack` 返回给客户端。

```javascript
const Koa = require('koa');
const app = new Koa();

// 业务异常基类
class BizError extends Error {
  constructor(code, message, status = 400) {
    super(message);
    this.code = code; this.status = status;
  }
}
const Errors = {
  UNAUTHORIZED: () => new BizError('AUTH_REQUIRED', '请先登录', 401),
  FORBIDDEN: () => new BizError('AUTH_FORBIDDEN', '无权限', 403),
  NOT_FOUND: (what) => new BizError('RES_NOT_FOUND', `${what}不存在`, 404),
  RATE_LIMIT: () => new BizError('REQ_RATE_LIMIT', '请求过于频繁', 429),
};

// 错误中间件：最外层
app.use(async (ctx, next) => {
  const traceId = ctx.get('x-trace-id') || crypto.randomUUID();
  ctx.set('x-trace-id', traceId);
  const start = Date.now();
  try {
    await next();
  } catch (err) {
    const isBiz = err instanceof BizError;
    const status = err.status || 500;
    ctx.status = status;
    ctx.body = {
      code: isBiz ? err.code : 'INTERNAL_ERROR',
      message: isBiz ? err.message : '系统繁忙，请稍后重试', // 未知错误脱敏
      traceId,
    };
    ctx.app.emit('error', err, ctx);
    console.error(JSON.stringify({          // 结构化错误日志
      level: isBiz ? 'warn' : 'error',
      traceId, method: ctx.method, url: ctx.url,
      status, cost: Date.now() - start,
      msg: err.message,
      stack: isBiz ? undefined : err.stack, // 业务错误不记堆栈
    }));
  }
});

// 业务代码
app.use(async (ctx) => {
  if (!ctx.get('authorization')) throw Errors.UNAUTHORIZED();
  if (ctx.path === '/goods') ctx.body = { code: 'OK', data: [{ id: 1 }] };
  else throw Errors.NOT_FOUND('接口');
});

app.on('error', (err) => { /* 接入 Sentry/自建告警 */ });
app.listen(3000);
```

---

## 五、鉴权与会话
