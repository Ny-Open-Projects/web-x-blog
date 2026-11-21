---
title: "[AI-029] 应用·SSE（流式）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 应用 · SSE（流式）

- **事实**：流式输出（SSE）改善体验：token 逐段推送首字延迟从秒级到毫秒级
- **原理**：用户感知延迟由首字时间（TTFT）决定，SSE 是标准协议（Response stream），前端逐段渲染，Java 实现（WebFlux/SSE emitter）与超时管理
- **常见误区**：
  1. 流式改变生成内容（错）
  2. 流式只影响速度不影响质量（错）
  3. 流式必须用 WebSocket（错）
- **工程用法**：交互体验基础
- **版本锚点**：实战共识
