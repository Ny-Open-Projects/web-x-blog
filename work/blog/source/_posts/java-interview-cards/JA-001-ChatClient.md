---
title: "[JA-001] Spring AI·ChatClient（ChatClient）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ChatClient（ChatClient）

- **事实**：Spring AI 的核心高层 API 是 ChatClient：ChatClient.create(chatModel) 构建，.prompt().user(...).call().content() 返回字符串
- **原理**：ChatClient 是流式链式门面，屏蔽底层 ChatModel 差异，业务代码面向它编程则换模型不改代码
- **常见误区**：
  1. ChatClient 由 new 直接构造（错）
  2. ChatClient 直接返回 ChatResponse 对象（错）
  3. call 与 stream 是同一个方法的不同参数（错）
- **工程用法**：业务层统一入口，模型层可替换
- **版本锚点**：Spring AI 1.0 GA
