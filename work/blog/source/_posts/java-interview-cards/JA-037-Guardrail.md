---
title: "[JA-037] LangChain4j·Guardrail（护栏）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · Guardrail（护栏）

- **事实**：LangChain4j 1.0 提供 InputGuardrail 与 OutputGuardrail 对输入输出做校验拦截
- **原理**：护栏在模型调用前后执行（可改写/拒绝），合规与安全需求以声明式挂载，与 Spring AI 的 advisor 异曲同工
- **常见误区**：
  1. LC4j 没有护栏能力（错）
  2. 护栏在模型服务端执行（错）
  3. 护栏只能拒绝不能改写（错）
- **工程用法**：输入输出合规落地
- **版本锚点**：LangChain4j 1.0
