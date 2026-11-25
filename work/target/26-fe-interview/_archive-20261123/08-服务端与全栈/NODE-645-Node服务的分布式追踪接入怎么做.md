---
title: [NODE-645] Node 服务的分布式追踪接入怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-645：分布式追踪怎么接入？
**答**：
- OpenTelemetry 标准接入：traceId 贯穿（W3C Trace Context 头传播）→ span 覆盖（HTTP 入口/出站调用/DB/Redis/消息）→ 采样策略（头部采样 + 尾部采样——错误全保留）。
- 自动埋点 vs 手动：OTel 自动插桩（http/db 模块 hook——零代码覆盖主干）+ 手动 span 补业务语义（「聚合」「风控判定」节点）。
- 上下文传递的坑：异步边界（worker_threads/回调队列）丢 context——AsyncLocalStorage 保证请求上下文跨 await 不丢（SCN-ENG-250 AI 上下文同源意识）。
- 采样与成本：全量 trace 存储贵——头采样（1%~10%）+ 尾采样（错误/慢请求 100% 保留）兼顾成本与排障价值。
- 追问钩子：为什么「AsyncLocalStorage」是 Node 追踪的基石——JS 无线程局部存储，请求上下文（traceId/用户）在 async 链中会丢失（事件循环交错）；ALS 利用 async_hooks 在异步执行域中隐式传播上下文（零参数污染）——没有它，每个函数都要显式传 ctx，埋点成本不可接受。

```javascript
import { AsyncLocalStorage } from 'async_hooks';
const als = new AsyncLocalStorage();
app.use((req, res, next) => als.run({ traceId: req.headers.traceparent }, next));
db.query = withALS(db.query);                          // 深层代码 als.getStore() 取 traceId
// 出站传播
headers['traceparent'] = buildTraceparent(als.getStore().traceId);   // W3C 格式贯穿
```
