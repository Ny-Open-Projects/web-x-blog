---
title: "[JA-068] Spring AI·TokenTextSplitter（切分）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · TokenTextSplitter（切分）

- **事实**：TokenTextSplitter 按 token 粒度切分文档（chunk 大小与重叠可配）
- **原理**：按 token 切分与模型上下文计量对齐（比字符切分准确），切分参数决定检索粒度
- **常见误区**：
  1. TokenTextSplitter 按字符切（错）
  2. 切分参数不可调（错）
  3. 切分无需考虑重叠（错）
- **工程用法**：RAG 入库切分
- **版本锚点**：Spring AI 1.0 GA
