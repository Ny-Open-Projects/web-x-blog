---
title: [NODE-251] Koa 中间件机制的源码精读？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-251：Koa 中间件机制的源码精读？
**答**：
- 核心只有两个函数：compose（洋葱执行，DP-203 源码）与 createContext（每次请求创建 ctx，合并 req/res/ctx/app）。
- compose 的两个安全检查：next() 调用两次抛错（index 游标防重入）、middleware 非函数直接抛错（fail-fast）。
- ctx 代理：ctx.body = x 实际写到 ctx.response.body（delegate 代理到 response）——响应延迟写（NODE-299 mini-koa）。
- 执行时机：handleResponse 在中间件全走完（Promise resolve）后统一写响应——洋葱"出"阶段改 body 仍生效。

```javascript
// Koa 源码级精读
class Application {
  use(fn) { this.middleware.push(fn); return this; }
  async handleRequest(ctx, fnMiddleware) {
    await fnMiddleware(ctx);                    // 洋葱全走完
    respond(ctx);                               // 统一写出（body 在"出"阶段改仍生效）
  }
  createCtx(req, res) {
    const ctx = Object.create(this.context);    // 原型继承 app 级 context
    ctx.app = this; ctx.req = req; ctx.res = res;
    ctx.response = Object.create(this.response); ctx.request = Object.create(this.request);
    return ctx;
  }
}
// delegate：ctx.body → ctx.response.body
delegate(proto, 'response').access('body').access('status');
// respond(ctx)：按 body 类型写（string/buffer/stream/json）——stream 类型用 pipe（背压联动 NODE-214）
```
