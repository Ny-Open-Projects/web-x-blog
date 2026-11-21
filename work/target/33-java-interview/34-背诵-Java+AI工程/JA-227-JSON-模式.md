---
title: "[JA-227] LangChain4j·JSON 模式（结构化）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · JSON 模式（结构化）

- **事实**：LC4j 对 OpenAI 官方 JSON 模式/结构化输出的支持（response format 配置级）
- **原理**：提示词注入 schema 之外，供应商原生结构化输出更稳（支持时优先），与 JA-173 机制互补
- **常见误区**：
  1. LC4j 不支持原生 JSON 模式（错）
  2. 两种方式等价无差异（错）
  3. 原生模式更慢（错）
- **工程用法**：结构化方式选型
- **版本锚点**：LangChain4j 1.0
