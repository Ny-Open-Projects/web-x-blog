---
title: "[JA-017] Spring AI·Ollama（本地模型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Ollama（本地模型）

- **事实**：Spring AI 经 spring-ai-ollama starter 接本地 Ollama，配置 spring.ai.ollama.base-url 指向本地服务
- **原理**：本地模型（隐私/成本）与云端 API 同一编程模型（ChatClient 不变），换 provider 只是换依赖与配置
- **常见误区**：
  1. Ollama 需要改业务代码适配（错）
  2. Ollama 只支持推理不支持嵌入（错）
  3. base-url 默认指向云端（错）
- **工程用法**：私有化部署接入
- **版本锚点**：Spring AI 1.0 GA
