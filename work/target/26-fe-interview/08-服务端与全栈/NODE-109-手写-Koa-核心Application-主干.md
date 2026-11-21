---
title: [NODE-109] 手写 Koa 核心——Application 主干、compose 与错误收口？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-109：手写 Koa 核心——Application 主干、compose 与错误收口？
**答**：
- Application = **Emitter + middleware 数组 + callback()**：`listen` 把 `compose(middleware)` 包装成 http 回调，每个请求新建 ctx。
- 执行链：`compose` 洋葱核心（NODE-023）→ resolve 后 `respond` 收口推导响应（对象自动 JSON、204/304 空 body）。
- 错误收口：中间件链的 Promise `catch` 后 `app.emit('error')`；Application 必须默认注册 onerror——否则 Emitter 无监听器会抛异常直接崩进程。
- 本题与 NODE-025 的差异：补齐生产细节（错误兜底、respond 状态码语义、compose 防重复 next）。

```javascript
const http = require('http');
const Emitter = require('events');

const compose = (mw) => (ctx, next) => {
  let i = -1;
  return dispatch(0);
  function dispatch(j) {
    if (j <= i) return Promise.reject(new Error('next() called multiple times'));
    i = j;
    const fn = j === mw.length ? next : mw[j];
    if (!fn) return Promise.resolve();
    return Promise.resolve(fn(ctx, () => dispatch(j + 1)));
  }
};

class Application extends Emitter {
  constructor() { super(); this.middleware = []; }
  use(fn) { this.middleware.push(fn); return this; }
  listen(...args) { return http.createServer(this.callback()).listen(...args); }
  callback() {
    const fn = compose(this.middleware);
    if (!this.listenerCount('error')) this.on('error', this.onerror); // 无监听器时兜底，防崩进程
    return (req, res) => {
      const ctx = { app: this, req, res, request: {}, response: { status: 200, body: undefined } };
      // ctx 短路代理（原理见 NODE-110）
      for (const k of ['status', 'body'])
        Object.defineProperty(ctx, k, {
          get: () => ctx.response[k], set: (v) => (ctx.response[k] = v),
        });
      Object.defineProperty(ctx, 'url', { get: () => req.url });
      fn(ctx).then(() => respond(ctx)).catch((err) => {
        this.emit('error', err, ctx);
        if (!res.headersSent) res.statusCode = 500;
        res.end('Internal Server Error');
      });
    };
  }
  onerror(err) { console.error('[koa]', err.stack || err); }
}

function respond(ctx) {
  const { res, status, body } = ctx;
  if (['204', '304', '404'].includes(String(status)) || body == null) return res.end();
  if (typeof body === 'string' || Buffer.isBuffer(body)) return res.end(body);
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(body)); // 对象默认 JSON 序列化
}
```
