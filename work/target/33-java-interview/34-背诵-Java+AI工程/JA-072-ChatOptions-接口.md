---
title: "[JA-072] Spring AI·ChatOptions 接口（选项）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ChatOptions 接口（选项）

- **事实**：ChatOptions 是通用选项接口（temperature/topP/maxTokens 等），各 provider 提供自己的 options 子类
- **原理**：业务代码面向 ChatOptions 编程，换 provider 不改选项传递结构，OpenAiChatOptions 只是其中实现
- **常见误区**：
  1. ChatOptions 是 OpenAI 专属（错）
  2. 选项字段各 provider 语义完全不同（错）
  3. 通用接口不能传（错）
- **工程用法**：跨 provider 选项抽象
- **版本锚点**：Spring AI 1.0 GA
