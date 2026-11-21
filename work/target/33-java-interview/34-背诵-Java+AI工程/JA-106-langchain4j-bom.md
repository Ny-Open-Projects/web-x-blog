---
title: "[JA-106] 依赖·langchain4j-bom（BOM）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 依赖 · langchain4j-bom（BOM）

- **事实**：LangChain4j 同样提供 langchain4j-bom 统一模块版本
- **原理**：LC4j 模块众多（provider/store/工具），BOM 对齐防依赖冲突，与 JVM 依赖知识联动
- **常见误区**：
  1. LC4j 无 BOM（错）
  2. 模块版本可以随意混搭（错）
  3. BOM 是可选装饰（错）
- **工程用法**：依赖治理
- **版本锚点**：LangChain4j 1.0
