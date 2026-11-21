---
title: "[JA-062] Spring AI·advisor 构建（RAG）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · advisor 构建（RAG）

- **事实**：QuestionAnswerAdvisor.builder(vectorStore).searchRequest(SearchRequest.builder().topK(5).build()).build() 精细配置检索
- **原理**：builder 暴露检索参数（topK/阈值/过滤），RAG 行为在装配期声明而非硬编码
- **常见误区**：
  1. QuestionAnswerAdvisor 只能默认构造（错）
  2. topK 在调用时随机（错）
  3. RAG 参数不可配置（错）
- **工程用法**：RAG 装配精调
- **版本锚点**：Spring AI 1.0 GA
