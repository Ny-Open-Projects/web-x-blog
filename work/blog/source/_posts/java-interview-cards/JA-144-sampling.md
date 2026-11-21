---
title: "[JA-144] MCP·sampling（反向）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · sampling（反向）

- **事实**：MCP 支持 server 反向请求 client 的 LLM 采样（sampling 能力）：server 无模型也能完成 AI 步骤
- **原理**：反向能力让工具 server 复用宿主模型的配额与上下文，安全边界由宿主审批，是 Agent 架构的高级特性
- **常见误区**：
  1. server 必须自带模型（错）
  2. sampling 是单向的客户端请求（错）
  3. 反向能力不存在（错）
- **工程用法**：Agent 架构进阶
- **版本锚点**：MCP 规范
