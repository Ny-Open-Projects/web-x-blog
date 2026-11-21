---
title: "[JA-562] 工程·keep-alive（网络）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · keep-alive（网络）

- **事实**：连接复用与 keep-alive：LLM 长响应下连接复用策略（TLS 握手成本摊薄），池化配置（JA-467 前置知识）
- **原理**：TLS 握手是延迟大头（首次请求），连接池 keep-alive 复用 TLS 会话，与连接池调优（JA-167）联动
- **常见误区**：
  1. 每请求新建连接无妨（错）
  2. keep-alive 与 LLM 无关（错）
  3. TLS 握手成本可忽略（错）
- **工程用法**：连接管理
- **版本锚点**：实战共识
