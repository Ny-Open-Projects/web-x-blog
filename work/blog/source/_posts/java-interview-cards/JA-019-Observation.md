---
title: "[JA-019] Spring AI·Observation（可观测）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Observation（可观测）

- **事实**：Spring AI 集成 Micrometer Observation：ChatModel/ChatClient 调用产生 trace 与 metrics
- **原理**：每次 LLM 调用有观测数据（耗时/token），与业务 trace 同链路串联，生产排障与成本归集的基础
- **常见误区**：
  1. LLM 调用无法被追踪（错）
  2. Observation 默认关闭且不能开（错）
  3. metrics 不含 token 数（错）
- **工程用法**：LLM 调用监控落地
- **版本锚点**：Spring AI 1.0 GA
