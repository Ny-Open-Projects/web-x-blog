---
title: "[SP-092] 可观测·traceId（tracing）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可观测 · traceId（tracing）

- **事实**：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递
- **原理**：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志
- **常见误区**：
  1. traceId 由业务代码手动生成（错）
  2. 跨 MQ 传递自动完成（错）
  3. 每服务重新生成 traceId（错）
- **工程用法**：可观测性第二支柱（tracing）
- **版本锚点**：实战共识
