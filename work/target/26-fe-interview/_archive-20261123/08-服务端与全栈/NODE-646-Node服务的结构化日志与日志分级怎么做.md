---
title: [NODE-646] Node 服务的结构化日志与分级怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-646：结构化日志怎么做？
**答**：
- 结构化优先：JSON 行日志（traceId/level/模块/耗时/关键字段）——可检索可聚合，文本日志是排障负债。
- 分级纪律：error（需行动）/warn（需关注）/info（关键路径事件——低频）/debug（细节——生产关闭）；每级有明确语义（「warn 里没有需要立即行动的」），防级别通胀。
- 上下文注入：ALS 自动注入 traceId/userId（SCN-NODE-645）——日志与 trace 互查。
- 性能与采样：pino 异步写入（不阻塞事件循环——同步 console 在高并发下是 P99 杀手）；日志采样分级（错误全量/正常采样，SCN-SLA-724 同源）；敏感字段脱敏白名单（SCN-NODE-合规）。
- 追问钩子：为什么「同步 console.log」在高并发下是 P99 杀手——console 同步写 stdout（TTY/管道阻塞），每个日志调用阻塞事件循环几毫秒，QPS 1000 时每请求 10 条日志 = 每请求额外 30ms+ P99——pino 的异步 + sonic-boom 缓冲写是标准解法；「日志不能比业务慢」。

```javascript
const logger = pino({ level: 'info',
  redact: ['req.headers.authorization', '*.password'] },   // 脱敏白名单
  pino.destination({ sync: false }));                  // 异步写（sonic-boom）
logger.info({ traceId: als.getStore()?.traceId, ms: 42 }, 'order created');
```
