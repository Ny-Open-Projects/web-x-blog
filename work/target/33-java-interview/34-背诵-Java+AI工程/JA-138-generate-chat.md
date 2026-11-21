---
title: "[JA-138] LangChain4j·generate→chat（迁移）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · generate→chat（迁移）

- **事实**：LangChain4j 1.0 迁移：ChatLanguageModel 的 generate 系列方法统一为 chat 系列
- **原理**：旧教程代码 generate 需迁移（编译期可见），与 Spring AI functions→tools 迁移（JA-049）同为 1.0 主题
- **常见误区**：
  1. generate 与 chat 完全等价共存（错）
  2. 迁移无编译提示（错）
  3. 1.0 保留了 generate（错）
- **工程用法**：1.0 迁移清单
- **版本锚点**：LangChain4j 1.0
