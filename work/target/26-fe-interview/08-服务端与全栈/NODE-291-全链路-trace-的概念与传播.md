---
title: [NODE-291] 全链路 trace 的概念与传播？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-291：全链路 trace 的概念与传播？
**答**:
- 三元组：traceId（整条链）、spanId（一个服务/操作段）、parentSpanId（父子关系）——W3C Trace Context 头（traceparent: 00-traceId-spanId-flags）。
- 传播：前端生成（或网关）traceId → HTTP 头 → BFF → 下游服务 → MQ（消息头）→ 异步任务——跨进程跨异步都续链。
- Node 实现：OpenTelemetry SDK 自动埋点（http/pg/redis 插件）+ AsyncLocalStorage 保证异步链不断（NODE-256）。
- 采样：头部采样（入口决定）+ 尾部采样（错误/慢请求全留）——成本与可见性平衡。

```javascript
// OTel Node 初始化
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
const sdk = new NodeSDK({
  instrumentations: [getNodeAutoInstrumentations()],   // 自动：http/express/pg/redis/mongoose
  traceExporter: otlpExporter,
  sampler: parentBased(traceIdRatioBased(0.1)),        // 10% 采样；错误全留（尾部采样在 collector）
});
sdk.start();
// 前端：fetch 时带 traceparent 头（RUM SDK 生成）→ BFF 透传（洋葱中间件）
app.use((ctx, next) => {
  if (!ctx.get('traceparent')) ctx.set('traceparent', newTraceparent());
  await next();
});
```
