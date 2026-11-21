---
title: "[JA-079] LangChain4j·ChatRequest（模型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ChatRequest（模型）

- **事实**：LangChain4j 显式对象调用：model.chat(ChatRequest) 返回 ChatResponse，metadata 含 tokenUsage 与 finishReason
- **原理**：需要 token 统计与结束原因时用显式对象而非便捷字符串重载，与 Spring AI 的 Usage 对等
- **常见误区**：
  1. chat 只接受 String（错）
  2. ChatResponse 无元数据（错）
  3. tokenUsage 是估算值（错）
- **工程用法**：细粒度调用控制
- **版本锚点**：LangChain4j 1.0
