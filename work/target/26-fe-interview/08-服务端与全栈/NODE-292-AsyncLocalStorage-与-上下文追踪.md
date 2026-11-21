---
title: [NODE-292] AsyncLocalStorage 与上下文追踪？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-292：AsyncLocalStorage 与上下文追踪？
**答**:
- ALS：异步上下文容器——als.run(store, fn) 内启动的所有异步链（await/回调/timer）都能 als.getStore() 拿到 store，天然穿透 async/await。
- 典型应用：traceId/userId/租户上下文跨层传递（NODE-256）、请求级缓存（随请求 GC NODE-278）、日志自动附 trace。
- 陷阱：als.run 之外创建的异步链拿不到 store（如全局 setInterval）；worker_threads 各自独立 ALS。
- 与 OTel 的关系：OTel 的 context 管理内部就用 ALS——理解 ALS 等于理解 OTel 链路不断的原因。

```javascript
import { AsyncLocalStorage } from 'node:async_hooks';
const als = new AsyncLocalStorage();
// 中间件
app.use((ctx, next) => als.run({ traceId: ctx.get('x-trace-id') ?? newTrace(), uid: ctx.state.user?.id }, next));
// 深层调用链（无参数传递）
async function orderService() {
  const { traceId, uid } = als.getStore()!;
  log.info({ traceId, uid }, 'creating order');       // 日志自动带上下文
  await db.query('...', { traceId });                 // DB 慢查询归因
}
// 陷阱：
setInterval(() => { als.getStore() === undefined; /* 定时器无 store */ }, 1000);
// 正解：定时任务里显式带上下文或创建根 store
```
