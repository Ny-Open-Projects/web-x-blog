---
title: "[JA-296] 工程·trace 深度（观测）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · trace 深度（观测）

- **事实**：LLM 调用 trace 深度：一次用户请求的 span 树=网关→框架→供应商→工具子调用，全链路串联（AI-042 落地）
- **原理**：trace 树还原"慢在哪层"（DF-053），工具内嵌 RPC 也要子 span，与分布式追踪知识同构
- **常见误区**：
  1. LLM 调用无 span 树（错）
  2. 只记顶层一个 span（错）
  3. 工具调用独立无关联（错）
- **工程用法**：trace 树设计
- **版本锚点**：实战共识
