---
title: "[JA-081] LangChain4j·RetrievalAugmentor（高级 RAG）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · RetrievalAugmentor（高级 RAG）

- **事实**：LangChain4j 的高级 RAG 接口 RetrievalAugmentor：DefaultRetrievalAugmentor 组合查询改写/路由/聚合
- **原理**：简单 ContentRetriever 之上提供查询压缩、多路检索等编排（AI-045 自适应 RAG 思想），AiServices.retrievalAugmentor 挂载
- **常见误区**：
  1. LC4j 只有简单检索（错）
  2. RetrievalAugmentor 是文档读取器（错）
  3. 高级 RAG 不能组合（错）
- **工程用法**：RAG 架构进阶
- **版本锚点**：LangChain4j 1.0
