---
title: "[JA-006] Spring AI·QuestionAnswerAdvisor（RAG）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · QuestionAnswerAdvisor（RAG）

- **事实**：QuestionAnswerAdvisor 是向量库 RAG 开箱 advisor：检索相关文档并注入提示词
- **原理**：挂载后每次提问自动走"向量化→相似检索→上下文注入"，业务一行 advisor 即得 RAG 能力
- **常见误区**：
  1. RAG 必须手写检索代码（错）
  2. QuestionAnswerAdvisor 不需要 VectorStore（错）
  3. advisor 只注入固定文档（错）
- **工程用法**：RAG 管道快速落地
- **版本锚点**：Spring AI 1.0 GA
