---
title: [NODE-111] 手写 koa-router 核心——路径参数如何编译成正则？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-111：手写 koa-router 核心——路径参数如何编译成正则？
**答**：
- 注册时把 `/user/:id/posts/:pid` 编译为 **正则 + 参数名表**，请求时 match 提取 `ctx.params`。
- 关键点：`/:id` → `([^/]+)`（不跨段，斜杠停止）；尾部 `*` 通配；提取值需 `decodeURIComponent`。
- 组成部分：`routes()` 返回中间件（match → 挂 params → compose 路由级中间件数组），`allowedMethods()` 兜底 405/501。
- path-to-regexp 6+ 同思想，增量支持量词（`:id?` `:id+` `:id*`）与自定义正则（`:id(\\d+)`）。

```javascript
class Router {
  constructor() { this.stack = []; }
  register(method, path, middleware) {
    const keys = [];
    const source = path
      .replace(/\/:([A-Za-z0-9_]+)/g, (_, k) => (keys.push(k), '/([^/]+)')) // 命名参数
      .replace(/\*$/, '(.*)');                                              // 尾部通配
    this.stack.push({ method, keys, regexp: new RegExp(`^${source}$`), middleware });
  }
  get(path, mw) { this.register('GET', path, mw); }
  post(path, mw) { this.register('POST', path, mw); }

  match(method, pathname) {
    for (const layer of this.stack) {
      if (layer.method !== method) continue;
      const m = pathname.match(layer.regexp);
      if (m) return { layer, params: Object.fromEntries(
        layer.keys.map((k, i) => [k, decodeURIComponent(m[i + 1])])) };
    }
    return null;
  }
  routes() {
    const router = this;
    return async (ctx, next) => {
      const hit = router.match(ctx.method, ctx.path);
      if (!hit) return next(); // 不归我管，交给后续中间件（如静态服务）
      ctx.params = hit.params;
      return compose(hit.layer.middleware)(ctx, next); // 路由级中间件 + 尾部 next 串成洋葱
    };
  }
}

// 使用：/user/123 → ctx.params = { id: '123' }
const router = new Router();
router.get('/user/:id', async (ctx, next) => { ctx.body = { id: ctx.params.id }; });
app.use(router.routes());
```
