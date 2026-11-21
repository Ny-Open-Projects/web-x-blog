---
title: "[JA-083] LangChain4j·retrievalAugmentor（装配）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · retrievalAugmentor（装配）

- **事实**：AiServices.retrievalAugmentor(...) 挂载高级 RAG（与 contentRetriever 二选一，augmentor 内部可含 retriever）
- **原理**：简单场景用 contentRetriever，需要查询改写/多路检索升级为 augmentor，渐进式增强不改业务接口
- **常见误区**：
  1. 两者必须同时挂（错）
  2. 挂载后每次调用才编译（错）
  3. augmentor 替代模型（错）
- **工程用法**：RAG 装配升级路径
- **版本锚点**：LangChain4j 1.0
