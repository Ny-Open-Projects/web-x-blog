---
title: "[JA-005] Spring AI·advisor（Advisor）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · advisor（Advisor）

- **事实**：Spring AI 的 advisor 机制：.advisors(...) 挂载拦截链，请求在调用模型前后经过 advisor
- **原理**：RAG 检索、对话记忆、日志审计都以 advisor 实现，业务代码组合 advisor 即可叠加能力，是 Spring AI 的扩展主轴
- **常见误区**：
  1. advisor 只能有一个（错）
  2. advisor 在模型调用后失效（错）
  3. advisor 是过滤器别名（错）
- **工程用法**：RAG/记忆/审计组合装配
- **版本锚点**：Spring AI 1.0 GA
