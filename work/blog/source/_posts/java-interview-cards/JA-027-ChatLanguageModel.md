---
title: "[JA-027] LangChain4j·ChatLanguageModel（模型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ChatLanguageModel（模型）

- **事实**：LangChain4j 的模型抽象是 ChatLanguageModel 接口，1.0 统一 chat 方法入口
- **原理**：各 provider（OpenAI/Ollama/Azure 等）提供实现，业务面向接口编程换 provider 不换代码
- **常见误区**：
  1. ChatLanguageModel 只支持 OpenAI（错）
  2. 接口方法是 generate（1.0 已统一为 chat）（错）
  3. 每个 provider 的调用方式完全不同（错）
- **工程用法**：模型抽象层理解
- **版本锚点**：LangChain4j 1.0
