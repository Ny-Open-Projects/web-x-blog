---
title: "[DF-053] 可观测·trace（追踪）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可观测 · trace（追踪）

- **事实**：分布式追踪：traceId 贯穿全链路，span 记录每跳（服务/耗时/状态），context 跨进程传播
- **原理**：span 树还原调用拓扑，异步/MQ 传播需显式处理（header/attachment），traceId 进日志（MDC）串联，排查"哪个服务慢了"的钥匙
- **常见误区**：
  1. traceId 每服务重新生成（错）
  2. span 与日志无关（错）
  3. MQ 自动传播 trace（错）
- **工程用法**：可观测性支柱一
- **版本锚点**：实战共识
