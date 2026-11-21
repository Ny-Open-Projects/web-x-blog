---
title: "[SP-091] Boot·metrics（监控）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · metrics（监控）

- **事实**：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana
- **原理**：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标
- **常见误区**：
  1. Micrometer 是监控系统（错）
  2. 指标采集有显著性能开销（错）
  3. 业务指标不能自定义（错）
- **工程用法**：可观测性三支柱之一（metrics）
- **版本锚点**：Boot 文档
