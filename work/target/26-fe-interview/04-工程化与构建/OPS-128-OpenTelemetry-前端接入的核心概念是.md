---
title: [OPS-128] OpenTelemetry 前端接入的核心概念是什么？怎么让前端成为分布式追踪的起点？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-128：OpenTelemetry 前端接入的核心概念是什么？怎么让前端成为分布式追踪的起点？
**答**：
- 核心概念：Trace（一次用户会话/请求链）、Span（一段操作）、Context（跨 span 传播的上下文）；Web SDK 提供 DocumentLoad（页面加载）与 XHR/Fetch（接口）自动埋点。
- 关键配置 propagateTraceHeaderCorsUrls：让请求头携带 traceparent 传给 API 域名，后端 SDK 接续同一 trace，实现前后端串联。
- resource 属性写齐 service.name/version/environment，错误与链路按构建版本归因（配合灰度归因）。
- 导出走 BatchSpanProcessor 批量上报到自建/云端 Collector，Collector 再做采样、脱敏与转发，前端只发一次。
- 初始化要防雪崩：SDK 自身异常必须静默，上报接口失败丢弃而非重试轰炸。

```typescript
// OpenTelemetry Web SDK 接入：前端作为分布式追踪的第一个环节
import { WebTracerProvider } from '@opentelemetry/sdk-trace-web';
import { DocumentLoadInstrumentation } from '@opentelemetry/instrumentation-document-load';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { Resource } from '@opentelemetry/resources';
import { registerInstrumentations } from '@opentelemetry/instrumentation';

const provider = new WebTracerProvider({
  resource: new Resource({
    'service.name': 'web-frontend',
    'service.version': __BUILD_VERSION__,        // 构建期注入，错误按版本归因
    'deployment.environment': 'prod',
  }),
});

// 批量上报到 Collector：由 Collector 统一采样/脱敏/转发，前端只发一次
provider.addSpanProcessor(
  new BatchSpanProcessor(
    new OTLPTraceExporter({ url: 'https://otel-collector.example.com/v1/traces' }),
    { maxQueueSize: 2000, scheduledDelayMillis: 5000 },
  ),
);
provider.register();

registerInstrumentations({
  instrumentations: [
    new DocumentLoadInstrumentation(),            // 页面加载链路 span
    new FetchInstrumentation({
      // 关键：向 API 域名注入 traceparent 头，后端接续同一 trace
      propagateTraceHeaderCorsUrls: [/^https:\/\/api\.example\.com/],
    }),
  ],
});
```
