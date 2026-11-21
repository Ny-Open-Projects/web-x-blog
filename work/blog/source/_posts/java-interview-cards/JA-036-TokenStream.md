---
title: "[JA-036] LangChain4j·TokenStream（流式）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · TokenStream（流式）

- **事实**：LangChain4j 流式：StreamingChatLanguageModel 或 AiServices 返回 TokenStream（onPartialResponse 逐段回调）
- **原理**：流式回调与 Reactor 无关（LC4j 自定义回调风格），SSE 输出需桥接，消费完 onCompleteResponse 收尾
- **常见误区**：
  1. TokenStream 返回完整字符串（错）
  2. 流式必须用 WebFlux（错）
  3. 回调是 Reactor Flux（错）
- **工程用法**：流式交互实现
- **版本锚点**：LangChain4j 1.0
