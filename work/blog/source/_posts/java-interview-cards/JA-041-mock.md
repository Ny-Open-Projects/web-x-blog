---
title: "[JA-041] 工程·mock（测试）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · mock（测试）

- **事实**：LLM 应用可测性：ChatModel 是接口，单测注入 mock 实现（固定返回）隔离真实模型
- **原理**：AI 应用测试原则：业务逻辑用 mock 模型测（快且确定），模型质量用评估集测（AI-034），两者分开
- **常见误区**：
  1. LLM 应用无法测试（错）
  2. 单测必须连真实模型（错）
  3. mock 模型返回值不可控（错）
- **工程用法**：测试策略设计
- **版本锚点**：实战共识
