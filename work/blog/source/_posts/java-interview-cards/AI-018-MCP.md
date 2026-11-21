---
title: "[AI-018] Agent·MCP（MCP）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · MCP（MCP）

- **事实**：MCP（Model Context Protocol）：工具/资源/提示三能力的开放协议（Anthropic 发起），标准化 Agent 与工具生态接入
- **原理**：解决 M×N 集成问题（每个 Agent 每个工具单独写），MCP server 一次实现多客户端复用（IDE/CLI/Agent 框架），Java 生态 Spring AI/MCP SDK 支持
- **常见误区**：
  1. MCP 是模型内部机制（错）
  2. MCP 替代 function calling（是传输与生态协议层）（错）
  3. MCP 只支持 Python（错）
- **工程用法**：Agent 工具生态标准化
- **版本锚点**：2024-2025
