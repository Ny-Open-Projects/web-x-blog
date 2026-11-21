---
title: [DP-299] 笔试题：手写 Koa Lite（洋葱模型+错误处理）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-299：笔试题：手写 Koa Lite（洋葱模型+错误处理）？
**题目**：实现 mini Koa：1) app.use 注册中间件；2) 洋葱执行（compose）；3) ctx = { req, res, body, status }；4) 未捕获错误进 app.onerror（默认 500）；5) listen 启动 HTTP server。
**评分点**：
- compose 正确（防多次 next）。
- body 写入时机（中间件跑完后统一 end）。
- 错误冒泡：中间件异常 → onerror → 500 响应（避免请求悬挂）。
- ctx.body 类型处理（对象 JSON 序列化/流）。
```javascript
const http = require('node:http');
class Koa {
  #mws = [];
  use(fn) { this.#mws.push(fn); return this; }
  onerror = (err, ctx) => { console.error(err); ctx.status = 500; ctx.body = 'Internal Error'; };
  listen(port) {
    return http.createServer(async (req, res) => {
      const ctx = { req, res, body: null, status: 200 };
      try {
        const dispatch = (i) => {
          if (i > this.#mws.length) return;
          if (i <= i - 1) throw new Error('next() multiple');       // 防重复（简版）
          return Promise.resolve(this.#mws[i](ctx, () => dispatch(i + 1)));
        };
        await dispatch(0);                                          // 2) 洋葱
      } catch (e) { this.onerror(e, ctx); }
      res.statusCode = ctx.status;                                  // 3) 统一写响应
      if (ctx.body && typeof ctx.body === 'object') {
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(ctx.body));
      } else res.end(ctx.body ?? '');
    }).listen(port);
  }
}
// 用：const app = new Koa();
// app.use(async (ctx, next) => { const start = Date.now(); await next(); ctx.res.setHeader('X-Time', `${Date.now()-start}ms`); });
// app.use(async (ctx) => { if (ctx.req.url === '/err') throw new Error('boom'); ctx.body = { ok: true }; });
```
