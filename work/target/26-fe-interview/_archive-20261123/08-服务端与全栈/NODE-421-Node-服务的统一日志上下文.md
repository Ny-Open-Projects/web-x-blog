---
title: [NODE-421] Node 服务的统一日志上下文（AsyncLocalStorage 深度应用）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-421：统一日志上下文深度应用
**答**:
- 问题：Node 异步链路中传 reqId/uid/租户靠层层参数传递（污染业务签名）或全局变量（串请求）。AsyncLocalStorage 提供请求级隐式上下文（NODE-292 深度篇）。
- 架构：入口中间件 run() 包装请求生命周期（ctx 保存 reqId/traceId/uid/tenantId/灰度标签）；logger 自动注入上下文（序列化时从 ALS 取——业务日志调用零参数带上下文）；service 层透明获取（tenantRepo 取租户 NODE-395）。
- 深度细节：ALS 跨 await 保持（Promise 链一致）；worker_threads 不共享 ALS（任务提交时显式序列化上下文）；回调风格的第三方库（事件监听器）可能丢上下文——入口注册时用 ALS.bind 包装回调。
- 上下文丢失检测：日志缺 reqId 的比例监控（丢失即排障黑洞 NODE-371）；开发模式断言关键日志必须带 reqId。
- 性能：ALS 开销极小（每请求 create 一次 store），高频热点路径避免频繁 run() 嵌套。
```javascript
const als = new AsyncLocalStorage();
app.use((req, res, next) => als.run({ reqId: genId(), uid: req.user?.id,
  tenant: req.tenant }, next));
const log = {
  info(o) { pino.info({ ...als.getStore(), ...o }); }           // 自动带上下文
};
// worker 任务提交：submit(task, ctx) → worker.postMessage({ task, ctx: als.getStore() })
```
