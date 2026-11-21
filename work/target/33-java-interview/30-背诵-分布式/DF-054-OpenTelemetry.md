---
title: "[DF-054] 可观测·OpenTelemetry（标准）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可观测 · OpenTelemetry（标准）

- **事实**：OpenTelemetry（OTel）：统一 traces/metrics/logs 三支柱 API+SDK+Collector
- **原理**：厂商中立标准（对接 Jaeger/Prometheus 等），自动埋点（agent）+手动埋点互补，替代各厂商私有 SDK，云原生观测标准
- **常见误区**：
  1. OTel 是某厂商产品（错）
  2. 三支柱只能分开采集（错）
  3. OTel 只支持 traces（错）
- **工程用法**：观测体系标准化
- **版本锚点**：OTel 规范
