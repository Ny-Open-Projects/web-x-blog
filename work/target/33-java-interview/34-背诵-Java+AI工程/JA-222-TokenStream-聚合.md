---
title: "[JA-222] LangChain4j·TokenStream 聚合（聚合）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · TokenStream 聚合（聚合）

- **事实**：TokenStream 同样可聚合：onCompleteResponse 回调拿完整响应做校验/落库
- **原理**：与 JA-221 对等（框架差异在回调 vs Flux），设计模式一致：流给体验、聚合给工程
- **常见误区**：
  1. TokenStream 无法聚合（错）
  2. 聚合需重新生成（错）
  3. 回调拿不到完整内容（错）
- **工程用法**：流式聚合对等
- **版本锚点**：LangChain4j 1.0
