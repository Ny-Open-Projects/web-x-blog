---
title: [NODE-134] OpenTelemetry 在 Node 中如何接入？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-134：OpenTelemetry 在 Node 中如何接入？
**答**：
- 接入姿势：`NodeSDK` 在**入口文件第一行 require**（确保 instrumentation 钩住后续模块加载），auto-instrumentations 自动生成 http/mysql/redis 的 span。
- 核心概念：Trace 全链路 → Span 单次操作（含属性/状态/耗时）→ Exporter 推到 Collector → 后端（Jaeger/Tempo/SkyWalking）。
- 手动 span：业务关键路径（聚合、风控）用 `startActiveSpan` 命名，属性带业务维度（uid/skuId）。
- 采样策略：开发 100%；生产 head sampling 10% + 错误请求 tail 全采样；注意与日志 traceId 打通（NODE-136）。

```javascript
// tracing.js —— 必须 require 在入口第一行
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'bff',
    [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: process.env.NODE_ENV,
  }),
  traceExporter: new OTLPTraceExporter({ url: 'http://otel-collector:4318/v1/traces' }),
  instrumentations: [getNodeAutoInstrumentations({
    '@opentelemetry/instrumentation-fs': { enabled: false }, // 噪音大的关掉
  })],
});
sdk.start();

// 业务手动 span
const { trace } = require('@opentelemetry/api');
await trace.getTracer('bff').startActiveSpan('aggregate-home', async (span) => {
  span.setAttribute('user.id', uid);
  const data = await aggregateHome(uid); // 内部 http/db span 自动挂到当前 span 下
  span.end();
  return data;
});
// 启动：node -r ./tracing.js dist/server.js
```
