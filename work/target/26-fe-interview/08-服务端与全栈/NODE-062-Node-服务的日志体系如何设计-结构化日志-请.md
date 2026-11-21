---
title: [NODE-062] Node 服务的日志体系如何设计（结构化日志、请求日志、错误日志）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-062：Node 服务的日志体系如何设计（结构化日志、请求日志、错误日志）？
**答**：
- 三条铁律：① **结构化 JSON**（一行一对象，便于 ELK/Loki 解析，禁止拼字符串）；② **traceId 贯穿**（入口生成 → 中间件透传 → 所有日志与下游 header 带上，全链路可查）；③ **分级采样**（info 采样或按需开关，error 全量 + 告警）。
- 请求日志：method/url/status/耗时/uid/traceId/ip/UA，在中间件统一记录（`on-finished` 时机）。
- 错误日志：uncaught/unhandled 兜底 + 业务错误统一走 error 中间件；写入用 pino（异步、低开销），**不要用 console.log**（同步写 stdout 阻塞事件循环）。
- 敏感信息脱敏：password/token/手机号在序列化前清洗。

```javascript
const pino = require('pino');
const crypto = require('node:crypto');

// 1. logger 实例：异步写 + 脱敏 + 分级
const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  redact: { paths: ['req.headers.authorization', '*.password', '*.token', '*.phone'], censor: '[REDACTED]' },
  formatters: { level: (label) => ({ level: label }) },
});

// 2. 请求日志中间件（Koa）：traceId 贯穿
app.use(async (ctx, next) => {
  const traceId = ctx.get('x-trace-id') || crypto.randomUUID();
  ctx.set('x-trace-id', traceId);
  ctx.state.log = logger.child({ traceId, uid: ctx.state.user?.uid }); // 子 logger 自动带上下文
  const start = Date.now();
  ctx.state.log.info({ event: 'request_in', method: ctx.method, url: ctx.url });

  await next();

  const onfinish = () => {
    const level = ctx.status >= 500 ? 'error' : ctx.status >= 400 ? 'warn' : 'info';
    ctx.state.log[level]({
      event: 'request_out', method: ctx.method, url: ctx.url,
      status: ctx.status, cost: Date.now() - start, ip: ctx.ip,
    });
  };
  ctx.res.on('finish', onfinish);
  ctx.res.on('error', onfinish);
});

// 3. 错误兜底：进程级 + 全局 error 事件
process.on('uncaughtException', (err) => {
  logger.fatal({ event: 'uncaught', msg: err.message, stack: err.stack });
  shutdown('uncaughtException');        // 记完日志走优雅退出
});
process.on('unhandledRejection', (reason) => {
  logger.error({ event: 'unhandledRejection', msg: String(reason) });
});
app.on('error', (err, ctx) => {
  ctx?.state?.log?.error({ event: 'app_error', msg: err.message, stack: err.stack });
});
```

```bash
# 生产收集：stdout → 容器 stdout → DaemonSet/Filebeat → ES/Loki
# Docker 中绝不写文件，只写 stdout（12-factor 原则）
docker run --log-driver=json-file --log-opt max-size=100m bff-server
# 本地开发美化输出
node main.js | npx pino-pretty
```
