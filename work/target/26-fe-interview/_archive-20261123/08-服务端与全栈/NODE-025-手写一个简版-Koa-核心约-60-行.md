---
title: [NODE-025] 手写一个简版 Koa（核心约 60 行）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-025：手写一个简版 Koa（核心约 60 行）？
**答**：
- 核心三件套：① `context` 对象（把 req/res 能力代理到 `ctx.request`/`ctx.response`，核心是 `ctx.body` 的 getter/setter 延迟写响应）；② 中间件数组 + compose；③ `handleRequest`：合并 ctx → compose 执行 → 统一 `respond` 输出 `ctx.body`。
- 理解点：`ctx.body = xxx` **不是立即发送**，而是在整个洋葱跑完后由 respond 统一判断类型（string/JSON/stream/Buffer）写出——这是 Koa 与 Express 直接操作 res 的根本不同。
- 面试要求 60 行内写清主干，体现"委托 + compose + 延迟响应"三概念。

```javascript
const http = require('node:http');
const compose = require('./compose'); // NODE-023 的 compose

class Application {
  constructor() { this.middleware = []; }
  use(fn) { this.middleware.push(fn); return this; }

  listen(...args) {
    const server = http.createServer(this.handleRequest.bind(this));
    return server.listen(...args);
  }

  // 构造 ctx：最小委托
  createContext(req, res) {
    const ctx = {
      req, res,
      method: req.method,
      url: req.url,
      app: this,
      state: {},
      _body: undefined,
    };
    Object.defineProperty(ctx, 'body', {
      get() { return ctx._body; },
      set(v) { ctx._body = v; },           // 延迟赋值，不立即响应
    });
    ctx.set = (k, v) => res.setHeader(k, v);
    ctx.throw = (status, msg) => { const e = new Error(msg); e.status = status; throw e; };
    return ctx;
  }

  // 统一响应输出
  respond(ctx) {
    const { res, body } = ctx;
    if (body === undefined) { res.statusCode = 404; return res.end('Not Found'); }
    if (typeof body === 'string' || Buffer.isBuffer(body)) return res.end(body);
    if (body && typeof body.pipe === 'function') return body.pipe(res); // 流直接接 res
    res.setHeader('content-type', 'application/json; charset=utf-8');
    res.end(JSON.stringify(body));
  }

  handleRequest(req, res) {
    const ctx = this.createContext(req, res);
    compose(this.middleware)(ctx)
      .then(() => this.respond(ctx))       // 洋葱跑完才响应
      .catch((err) => {
        ctx.status = err.status || 500;
        res.end(err.message || 'Internal Error');
        this.emit?.('error', err, ctx);
      });
  }
}

// 使用（与真 Koa 用法一致）
const app = new Application();
app.use(async (ctx, next) => { try { await next(); } catch (e) { ctx.status = e.status || 500; ctx.body = { code: e.status, msg: e.message }; } });
app.use(async (ctx, next) => { ctx.set('x-powered-by', 'mini-koa'); await next(); });
app.use(async (ctx) => { if (ctx.url === '/hi') ctx.body = { hello: 'koa' }; else ctx.throw(404, 'not found'); });
app.listen(3000);
```
