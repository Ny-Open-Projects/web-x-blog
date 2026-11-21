---
title: "[JA-426] 流式·SSE vs WS（选型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 流式 · SSE vs WS（选型）

- **事实**：SSE 与 WebSocket 选型：单向流式 SSE 足够（简单/自动重连/HTTP 生态），双向交互（打断/追问）才需 WS
- **原理**：多数 AI 流式是单向（模型→用户），WS 的双向能力常被高估，SSE 运维简单（JA-087 断线处理），按交互方向选
- **常见误区**：
  1. 必须用 WebSocket（错）
  2. 两者无差别（错）
  3. SSE 不能双向交互（追问走新请求即可）（错）
- **工程用法**：传输协议选型
- **版本锚点**：实战共识
