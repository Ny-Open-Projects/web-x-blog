---
title: "[JA-088] LangChain4j·AiMessage（消息）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · AiMessage（消息）

- **事实**：LC4j 消息抽象：UserMessage/AiMessage/SystemMessage，AiMessage 可携带 toolExecutionRequests
- **原理**：工具调用轮次中 AiMessage 携带调用意图，历史回放时保留该结构才能正确续轮，与 JA-010 链路对齐
- **常见误区**：
  1. AiMessage 只是文本容器（错）
  2. 工具意图存独立日志（错）
  3. 消息类型可混用（错）
- **工程用法**：工具轮次与历史回放
- **版本锚点**：LangChain4j 1.0
