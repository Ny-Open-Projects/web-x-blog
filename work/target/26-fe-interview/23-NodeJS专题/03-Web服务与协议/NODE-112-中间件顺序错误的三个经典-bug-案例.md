---
title: [NODE-112] 中间件顺序错误的三个经典 bug 案例？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-112：中间件顺序错误的三个经典 bug 案例？
**答**：
- 案例 1：**bodyparser 注册在路由之后** → 路由里 `ctx.request.body` 永远 undefined，症状诡异极难联想到顺序。
- 案例 2：**错误处理中间件注册位置不对** → Koa 全局 catch 覆盖不到它之后的链路；Express 中在它之前抛出的错没人接，直接 500 裸奔。
- 案例 3：**健康检查放在鉴权与限流之后** → 探活流量被限流误杀引发监控误报、K8s 误重启；日志中间件放最后 → 404 请求无日志。
- 铁律顺序：traceId/错误处理最前 → parser/cors → 鉴权 → 业务路由 → 兜底 404 → 兜底错误日志。

```javascript
// ── 案例 1：错误顺序 ──
app.use(router.routes()); // 错：路由先执行，此时 body 还没解析
app.use(bodyParser());
// 修复：parser 一定在消费它的中间件之前
app.use(bodyParser());
app.use(router.routes());

// ── 案例 2：Express 注册位次 ──
app.use(requestLogger);    // 1. 日志与 traceId
app.use(auth);             // 2. 鉴权，可能抛 401
app.use(router);           // 3. 业务，可能抛错
app.use(notFoundHandler);  // 4. 404 兜底
app.use(errorHandler);     // 5. 4 参错误中间件最后注册但覆盖前面全部

// ── 案例 3：健康检查短路 ──
app.use(async (ctx, next) => {
  if (ctx.path === '/healthz') { ctx.body = 'ok'; return; } // 先于限流短路
  await next();
});
app.use(rateLimit({ qps: 1000 })); // 探活不计入限流
```
