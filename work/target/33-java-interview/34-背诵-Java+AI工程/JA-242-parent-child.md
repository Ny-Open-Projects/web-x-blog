---
title: "[JA-242] RAG·parent-child（切分）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · parent-child（切分）

- **事实**：parent-child 切分：检索用小块（child 精度高）注入用大块（parent 上下文全），child 元数据记 parent id
- **原理**：小块召回准但上下文碎，映射回父块注入兼得两者，Java 侧自实现（切分时建映射）
- **常见误区**：
  1. child 就是注入单元（错）
  2. parent-child 是框架内置自动（错）
  3. 大块直接检索更好（错）
- **工程用法**：切分策略进阶
- **版本锚点**：实战共识
