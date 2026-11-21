---
title: "[JA-302] 选型·RAG 装配差异（RAG 装配面）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 选型 · RAG 装配差异（RAG 装配面）

- **事实**：Spring AI 的 RAG 装配面是 advisor 链，LangChain4j 是 contentRetriever/retrievalAugmentor 参数
- **原理**：两种装配面语义对等（JA-051），Spring AI 的 advisor 更通用（RAG 只是用途之一），LC4j 的更专用清晰
- **常见误区**：
  1. RAG 装配两框架完全相同（错）
  2. advisor 不能做 RAG（错）
  3. 专用装配面是劣势（错）
- **工程用法**：RAG 装配对比
- **版本锚点**：实战共识
