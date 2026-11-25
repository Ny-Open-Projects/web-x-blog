---
title: [NODE-026] Koa 路由的实现原理是什么？如何解析路径参数 ctx.params？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-026：Koa 路由的实现原理是什么？如何解析路径参数 ctx.params？
**答**：
- 路由本质是**中间件前置过滤**：`router.get('/user/:id', fn)` 内部把 pattern 编译成正则 + 命名分组（`/user/:id` → `^/user/([^/]+?)$`），请求来时逐条匹配，命中则把正则捕获组写入 `ctx.params` 再执行 fn。
- 需要处理的细节：方法过滤、`/` 结尾归一化、query 与 params 区分（query 在 `ctx.query`，路径参数在 `ctx.params`）、404 由路由中间件放行后由 Koa 默认响应。
- 高频追问：为什么 Koa 路由没有嵌套作用域问题（`router.prefix('/api')` 统一加前缀）；RESTful 动态路径 vs 通配符 `(.*)` 的正则区别。

```javascript
// 简版路由：pattern 编译 + ctx.params 注入
class Router {
  constructor() { this.routes = []; }

  register(method, path, handler) {
    // '/user/:id/posts/:postId' → { keys: ['id','postId'], regexp }
    const keys = [];
    const pattern = path.replace(/:([A-Za-z0-9_]+)/g, (_, key) => {
      keys.push(key);
      return '([^/]+)';                   // 捕获一个路径段
    });
    this.routes.push({ method, keys, regexp: new RegExp(`^${pattern}$`), handler });
    return this;
  }
  get(path, h) { return this.register('GET', path, h); }
  post(path, h) { return this.register('POST', path, h); }

  // 作为 Koa 中间件使用
  routes() {
    return async (ctx, next) => {
      const match = this.routes.find(
        (r) => r.method === ctx.method && r.regexp.test(ctx.url.split('?')[0]),
      );
      if (!match) return next();          // 放行 → 404 兜底
      const [, ...values] = ctx.url.split('?')[0].match(match.regexp);
      ctx.params = Object.fromEntries(match.keys.map((k, i) => [k, decodeURIComponent(values[i])]));
      await match.handler(ctx, next);     // handler 内可 await next() 回到洋葱
    };
  }
}

// 用法
const router = new Router();
router.get('/user/:id', async (ctx) => { ctx.body = { userId: ctx.params.id }; });
router.get(/^\/files\/(.+)$/, async (ctx) => { ctx.body = { wildcard: ctx.params[0] }; });
// app.use(router.routes()) → GET /user/42 → { userId: "42" }
```
