---
title: [NODE-133] 结构化日志规范如何设计（traceId 贯穿全链路）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-133：结构化日志规范如何设计（traceId 贯穿全链路）？
**答**：
- 三条铁律：**一行一事件 JSON**（禁止拼字符串）、固定维度字段全环境必打（traceId/uid/route/status/cost）、日志即数据（可进 ELK 检索聚合）。
- traceId 来源：优先取上游头 `x-trace-id`，无则生成；写入 ALS（NODE-106）后**任何深度异步**的日志都自动带上；响应头回写方便用户报障。
- pino 实践：`base` 放服务级固定字段，`child` 派生请求级 logger，避免每次序列化重复字段。
- 级别纪律：error 必须可行动（带 runbook/traceId），info 控制量（访问日志采样可选），debug 生产默认关。

```javascript
const { randomUUID } = require('crypto');
const pino = require('pino');

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  base: { service: 'bff', env: process.env.NODE_ENV },       // 服务级固定字段
  timestamp: pino.stdTimeFunctions.isoTime,
  formatters: { level: (l) => ({ level: l }) },
});

// 请求级：ALS 注入 traceId，全链路日志自动贯穿
app.use((ctx, next) => {
  const traceId = ctx.get('x-trace-id') || randomUUID();
  ctx.set('x-trace-id', traceId);                            // 回写响应头
  const start = Date.now();
  return als.run({ traceId, uid: ctx.state.uid }, async () => {
    const log = logger.child({ traceId, uid: ctx.state.uid }); // 请求级 logger
    try {
      await next();
      log.info({ route: ctx.path, status: ctx.status, cost: Date.now() - start }, 'access');
    } catch (err) {
      log.error({ route: ctx.path, stack: err.stack, cost: Date.now() - start }, 'error');
      throw err;
    }
  });
});
// 输出示例：{"level":30,"time":"...","service":"bff","traceId":"...","route":"/api/home","cost":86}
```
