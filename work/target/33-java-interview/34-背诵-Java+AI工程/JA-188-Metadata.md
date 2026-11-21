---
title: "[JA-188] LangChain4j·Metadata（元数据）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · Metadata（元数据）

- **事实**：LC4j 的 TextSegment 携带 Metadata 对象（put/get 键值），随向量入库
- **原理**：与 Spring AI Document.metadata 对等（JA-128），溯源/权限/增量全靠它
- **常见误区**：
  1. TextSegment 无元数据（错）
  2. Metadata 不参与存储（错）
  3. 元数据类型任意不受限（错）
- **工程用法**：RAG 数据结构对等
- **版本锚点**：LangChain4j 1.0
