---
title: "[JA-129] Spring AI·Markdown（Reader）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Markdown（Reader）

- **事实**：spring-ai-markdown-document-reader 提供 Markdown 文档解析
- **原理**：知识库常用 Markdown（内网 wiki），解析保留标题结构利于切分语义，Tika 覆盖其余格式
- **常见误区**：
  1. Markdown 需手写解析（错）
  2. 所有格式只能用 Tika（错）
  3. 文档读取器只有一种（错）
- **工程用法**：RAG 入库格式覆盖
- **版本锚点**：Spring AI 1.0 GA
