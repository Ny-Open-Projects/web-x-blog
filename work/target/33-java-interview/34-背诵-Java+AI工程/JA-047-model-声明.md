---
title: "[JA-047] Spring AI·model 声明（多模型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · model 声明（多模型）

- **事实**：Spring AI 支持多 provider 共存：spring.ai.model.chat 指定生效的 chat provider（openai/ollama 等）
- **原理**：classpath 上多个 starter 并存时由该属性决定装配哪个，避免隐式冲突，多 provider 项目必知
- **常见误区**：
  1. 多个 starter 自动全装配（错）
  2. 该属性不存在（错）
  3. model 属性只管 embedding（错）
- **工程用法**：多模型项目配置
- **版本锚点**：Spring AI 1.0 GA
