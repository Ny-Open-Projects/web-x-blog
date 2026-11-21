---
title: "[JA-090] LangChain4j·ChatMemoryStore（记忆）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ChatMemoryStore（记忆）

- **事实**：LC4j 记忆持久化实现 ChatMemoryStore 接口（getMessages/updateMessages/deleteMessages）
- **原理**：自选存储（Redis/DB）实现三方法即可持久化记忆，与 Spring AI 的 repository 同思想
- **常见误区**：
  1. 记忆只能内存（错）
  2. 持久化接口不存在（错）
  3. 接口方法只有 get（错）
- **工程用法**：记忆持久化定制
- **版本锚点**：LangChain4j 1.0
