---
title: "[JA-389] LangChain4j·usage（流式）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · usage（流式）

- **事实**：流式调用的 token 用量聚合：分片各自带 usage 或完成回调聚合（LC4j onCompleteResponse 元数据）
- **原理**：流式的成本归集（JA-065 同步版的流式版），聚合点在完成回调，与 JA-222 聚合知识联动
- **常见误区**：
  1. 流式无法统计 token（错）
  2. usage 只有同步有（错）
  3. 聚合在客户端拼（错）
- **工程用法**：流式成本归集
- **版本锚点**：LangChain4j 1.0
