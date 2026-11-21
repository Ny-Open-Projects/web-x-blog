---
title: "[JA-137] LangChain4j·start（流式）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · start（流式）

- **事实**：TokenStream 构建 Lambda 链后必须 start() 才开始消费
- **原理**：与 Flux 订阅语义同源（JA-125），回调链（onPartialResponse/onCompleteResponse/onError）注册后显式启动
- **常见误区**：
  1. 链式注册即自动开始（错）
  2. start 可省略（错）
  3. TokenStream 是同步阻塞（错）
- **工程用法**：流式启动纪律
- **版本锚点**：LangChain4j 1.0
