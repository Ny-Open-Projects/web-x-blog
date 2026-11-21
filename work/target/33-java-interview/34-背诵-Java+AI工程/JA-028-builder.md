---
title: "[JA-028] LangChain4j·builder（构建）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · builder（构建）

- **事实**：LangChain4j 模型用 builder 构建：OpenAiChatModel.builder().apiKey(...).modelName(...).build()
- **原理**：无 Spring 自动装配时手动构建（纯 Java 应用），参数在 builder 上显式可见
- **常见误区**：
  1. LC4j 模型只能通过 Spring 注入（错）
  2. builder 无 apiKey 参数（错）
  3. 构建后模型不可复用（错）
- **工程用法**：纯 Java 应用接入
- **版本锚点**：LangChain4j 1.0
