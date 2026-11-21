---
title: "[JA-034] LangChain4j·DocumentSplitters（切分）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · DocumentSplitters（切分）

- **事实**：LangChain4j 的文档切分：DocumentSplitters.recursive(段大小, 重叠) 把 Document 拆成 TextSegment
- **原理**：递归切分按段落优先保持语义边界，TextSegment 携带元数据进向量库，是 RAG 质量的第一决定因素
- **常见误区**：
  1. 切分器只支持固定长度（错）
  2. 切分与向量库无关（切分决定检索质量）（错）
  3. TextSegment 无元数据（错）
- **工程用法**：知识库切分策略
- **版本锚点**：LangChain4j 1.0
