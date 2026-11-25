---
title: [NODE-730] 笔试题——实现 ALS 上下文贯穿（含 worker/回调队列边界）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-730：手写 ALS 贯穿

**需求与边界**：
- 需求：请求上下文（traceId/tenant/gray）ALS 贯穿（SCN-NODE-645）——① 中间件注入；② 深层取用（零参数传播）；③ 边界处理——worker_threads 手动传递（ALS 不跨 worker）、MQ 消费手动重建（消息头 → 新 ALS 域）、定时任务（无请求上下文——系统上下文）。
- 边界：① ALS 存储不可变（改字段用 run 新域——防跨请求污染）；② 上下文丢失检测（深层取不到 store 时告警——链断裂哨兵）；③ 测试（ALS 在 async 链的正确传播用例）。

**答**：
```javascript
export const ctx = new AsyncLocalStorage();
app.use((req, res, next) => {
  ctx.run({ traceId: req.headers['traceparent'], tenant: req.headers['x-tenant'],
    gray: req.headers['x-gray-bucket'] }, next);
});
// 深层零参数取用
function anyDeep() { return ctx.getStore()?.traceId; }   // ALS 自动传播
// 边界 1：worker 手动传递（ALS 不跨线程）
worker.postMessage({ task, ctx: ctx.getStore() });       // 序列化传递
worker.onmessage = (m) => ctx.run(m.data.ctx, () => handle(m));
// 边界 2：MQ 消费重建（消息头 → 新域）
consumer.on('message', (m) => ctx.run({ traceId: m.headers.traceparent }, () => handle(m)));
// 丢失检测（哨兵）
function getCtx() {
  const s = ctx.getStore();
  if (!s) report({ type: 'CTX_LOST', stack: captureStack() });   // 链断裂哨兵
  return s;
}
```

**评分点**:
- ALS 三边界显式处理（worker/MQ/定时——SCN-NODE-645 的工程化闭环）。
- 不可变语义（run 新域——跨请求污染防御）。
- 上下文丢失哨兵（深层取不到告警——链断裂可检测）。
- 测试意识（async 链传播用例）。
