---
title: "[JA-154] 工程·LLM 依赖（熔断）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · LLM 依赖（熔断）

- **事实**：LLM 作为"下游依赖"纳入熔断：错误率/慢调用率超阈跳闸，降级到备模型或模板回复
- **原理**：把 AI 当新型 RPC 治理（AI-060 方法论），resilience4j/Sentinel 环绕 ChatClient 调用点，与 DF-022 熔断知识同构
- **常见误区**：
  1. LLM 调用不需要熔断（错）
  2. 熔断会阻止 AI 功能（错）
  3. 降级只有报错（错）
- **工程用法**：雪崩防护迁移
- **版本锚点**：实战共识
