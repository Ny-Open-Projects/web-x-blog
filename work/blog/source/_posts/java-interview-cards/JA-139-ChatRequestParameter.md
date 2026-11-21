---
title: "[JA-139] LangChain4j·ChatRequestParameters（参数）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ChatRequestParameters（参数）

- **事实**：1.0 的请求参数抽象 ChatRequestParameters 覆盖模型选择/温度/maxTokens 等
- **原理**：per-request 参数与模型 builder 默认参数分层覆盖，与 Spring AI 的 options 覆盖对等
- **常见误区**：
  1. 参数只能在 builder 配（错）
  2. per-request 无法覆盖（错）
  3. 参数与模型绑定不可分离（错）
- **工程用法**：运行时参数覆盖
- **版本锚点**：LangChain4j 1.0
