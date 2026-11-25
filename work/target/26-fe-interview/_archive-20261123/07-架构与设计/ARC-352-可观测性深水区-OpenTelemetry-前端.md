---
title: [ARC-352] OpenTelemetry 在前端如何落地？与自研 SDK 怎么取舍？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-352：OpenTelemetry 在前端如何落地？与自研 SDK 怎么取舍？
**答**：
- OTel 提供统一的数据模型（Trace/Metrics/Logs 三信号）与 Provider/Exporter 抽象，前端用 @opentelemetry/sdk-trace-base + 自定义 WebTracerProvider。
- 落地要点：自动埋点（fetch/XHR、document load、user interaction 插件）+ 手动 span 包裹业务关键路径；通过 Baggage 传递业务维度（灰度桶、实验组）。
- 优势：与后端链路同构（traceparent 贯穿前后端），一次排障看全链路；Exporter 可切换（OTLP/Jaeger/自研网关）。
- 自研 SDK 更适合：包体敏感（OTel tree-shake 后仍不小）、上报协议自有、监控平台已定型。折中方案：自研 SDK 采用 OTel 数据模型但不引入完整 SDK。
- 决策公式：有自建监控平台且协议私有 → 自研；希望前后端链路打通且后端已上 OTel → 前端跟进。
```javascript
import { WebTracerProvider, BatchSpanProcessor } from '@opentelemetry/sdk-trace-web';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const provider = new WebTracerProvider();
provider.addSpanProcessor(new BatchSpanProcessor(
  new OTLPTraceExporter({ url: '/api/otel/v1/traces' }),  // 走同域网关转发
  { maxQueueSize: 500, scheduledDelayMillis: 5000 }        // 批量+上限防泄漏
));
provider.register();
// fetch 自动埋点插件为每次请求创建 span，w3c traceparent 头自动注入
```
