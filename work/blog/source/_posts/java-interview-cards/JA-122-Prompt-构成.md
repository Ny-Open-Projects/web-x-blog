---
title: "[JA-122] Spring AI·Prompt 构成（类型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Prompt 构成（类型）

- **事实**：Spring AI 的 Prompt 对象由消息列表与可选 ChatOptions 组成
- **原理**：门面之下一切调用最终收敛为 Prompt 传给 ChatModel，理解构成才能做精细组装
- **常见误区**：
  1. Prompt 只有字符串（错）
  2. options 是 Prompt 的一部分但可省略（错）
  3. 消息与选项互斥（错）
- **工程用法**：底层组装理解
- **版本锚点**：Spring AI 1.0 GA
