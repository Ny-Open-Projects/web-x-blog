---
title: "[AI-001] LLM·token（基础）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LLM · token（基础）

- **事实**：LLM 按 token 处理文本：中文约 1 字≈1-2 token，英文 1 词≈1.3 token，计费与上下文都按 token
- **原理**：上下文窗口与费用都以 token 计，Prompt 长度预算与成本估算的基础单位，压缩提示（精简指令）直接省成本
- **常见误区**：
  1. token 就是单词（错）
  2. 中文与英文 token 消耗相同（错）
  3. 上下文无限（错）
- **工程用法**：成本与窗口预算的基础
- **版本锚点**：通用
