---
title: "[JA-002] Spring AI·stream（流式）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · stream（流式）

- **事实**：ChatClient 流式调用 .stream().content() 返回 Flux<String>（Reactor 类型）
- **原理**：流式走 SSE 推给前端需 WebFlux 或 SseEmitter 桥接，返回类型是 Reactor Flux 是响应式栈的标志
- **常见误区**：
  1. stream 返回 List<String>（错）
  2. stream 阻塞到全部生成完（错）
  3. Flux 是 Spring AI 自研类型（错）
- **工程用法**：WebFlux 技术栈对接 SSE
- **版本锚点**：Spring AI 1.0 GA
