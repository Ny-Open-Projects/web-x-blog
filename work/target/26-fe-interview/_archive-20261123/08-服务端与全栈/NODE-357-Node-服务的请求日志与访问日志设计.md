---
title: [NODE-357] Node 服务的请求日志与结构化访问日志设计
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-357：结构化访问日志设计
**答**:
- 结构化 JSON 日志（一行一事件）：ts/level/traceId/reqId/method/path/status/durationMs/uid/client/ip/errName——可被采集器直接索引、可按 traceId 关联（NODE-291）。禁 console.log 散写（pino 统一出口，异步写入不阻塞）。
- 访问日志内容取舍：不打请求/响应体（体积与隐私——只打摘要字段白名单）；错误日志带 stack 归一化（指纹，ARC-406 同思想）。
- 分级采样：错误全量、慢请求（> P90）全量、常规访问采样 10%（Nginx/网关层先采样更好）。
- 关联：traceId 从请求头提取生成（W3C）、uid 脱敏（哈希化）进日志；日志字段 schema 版本化（字段变更要兼容采集端）。
- 落地：日志等级运行时可调（配置中心热更）、轮转与磁盘保护（防日志写满磁盘拖死服务）、采样与脱敏规则进 lint（禁 console）。
```javascript
// pino 中间件
app.use(async (ctx, next) => {
  const start = Date.now();
  try { await next(); } finally {
    if (ctx.status >= 500 || Date.now() - start > 500 || sampled())
      logger.info({ reqId: ctx.state.reqId, traceId: ctx.get('traceparent'),
        method: ctx.method, path: ctx.path, status: ctx.status,
        durationMs: Date.now() - start, uid: hashUid(ctx.state.user?.id) });
  }
});
```
