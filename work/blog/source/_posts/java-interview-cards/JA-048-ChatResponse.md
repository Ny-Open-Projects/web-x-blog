---
title: "[JA-048] Spring AI·ChatResponse（类型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ChatResponse（类型）

- **事实**：Spring AI 底层类型链：Prompt（请求）→ ChatModel.call → ChatResponse（含 Generation 列表）
- **原理**：ChatClient 是门面，底层 call 返回 ChatResponse 可取 token usage 与 finishReason，需要细粒度信息时下沉到底层 API
- **常见误区**：
  1. ChatClient 是唯一入口无底层（错）
  2. ChatResponse 不含 token 数据（错）
  3. Generation 就是字符串（错）
- **工程用法**：底层类型理解与下沉场景
- **版本锚点**：Spring AI 1.0 GA
