---
title: [NODE-253] Fastify 的 hooks 生命周期？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-253：Fastify 的 hooks 生命周期？
**答**:
- 生命周期链：onRequest → preParsing → preValidation → preHandler → handler → preSerialization → onSend → onResponse——比中间件模型更细的切面点。
- onRequest：最早（连 body 都没解析）——鉴权/trace 起点在这里；onSend：响应序列化前（加响应头/改 payload）；onResponse：响应已发（上报收尾）。
- 与中间件的差异：hooks 是精确切面（各有专属职责），middleware 是全链洋葱——Fastify 推荐用 hooks 做切面、routes 做业务。
- scope 语法：server.addHook('onRequest', fn) 全局 / route.register({ onRequest }) 路由级。

```javascript
// Fastify hooks 实战
fastify.addHook('onRequest', async (req, reply) => {
  req.traceId = req.headers['x-trace-id'] ?? newTraceId();    // trace 起点
  const user = await auth(req.headers.authorization);
  if (!user) return reply.code(401).send({ code: 'UNAUTH' }); // 提前响应：跳过后续 hook
  req.user = user;
});
fastify.addHook('preHandler', async (req) => {
  if (!requirePerm(req.user, req.routeOptions.config.perm))   // 路由级权限
    throw { statusCode: 403, code: 'PERM_DENIED' };           // 抛错 → error handler
});
fastify.addHook('onSend', async (req, reply, payload) => {
  reply.header('X-Trace-Id', req.traceId);                    // 响应头
  return payload;
});
fastify.addHook('onResponse', async (req, reply) => {
  perf.histogram('http', { route: req.routeOptions.url, ms: reply.elapsedTime });
});
```
