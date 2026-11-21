---
title: "[JA-135] LangChain4j·@MemoryId（会话）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · @MemoryId（会话）

- **事实**：LC4j 用 @MemoryId 注解标记接口方法的会话标识参数，实现多用户记忆隔离
- **原理**：多用户并发场景每个 memoryId 独立窗口（JA-035），与 ToolContext 防串号（JA-097）同属租户红线
- **常见误区**：
  1. memoryId 可选不加（错）
  2. 所有用户共享一个记忆（错）
  3. 注解加在类上（错）
- **工程用法**：多用户隔离
- **版本锚点**：LangChain4j 1.0
