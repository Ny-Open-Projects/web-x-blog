---
title: "[AD-279] 手写·MCP（发现）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 手写 · MCP（发现）

- **事实**：MCP 动态工具发现的手写集成：连 server→listTools→转 ToolDefinition 注册（JA-186 桥接的手写面），变更通知刷新（JA-094）
- **原理**：手写版 MCP 集成验证理解（发现→转换→注册三步），通知刷新（工具热更新），与 MCP 客户端知识（AD-021）联动
- **常见误区**：
  1. MCP 工具不能手写集成（错）
  2. 发现一次永久（错）
  3. 刷新机制不必要（错）
- **工程用法**：MCP 手写集成
- **版本锚点**：实战共识
