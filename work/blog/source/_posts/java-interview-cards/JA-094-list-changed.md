---
title: "[JA-094] MCP·list_changed（通知）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · list_changed（通知）

- **事实**：MCP 服务端工具清单变更时发送通知（tools/list_changed），客户端重新 listTools
- **原理**：工具热更新协议化（新增工具无需重启客户端），客户端要处理通知刷新缓存，动态工具生态基础
- **常见误区**：
  1. 工具清单固定不可变（错）
  2. 变更必须重启服务（错）
  3. 客户端自动感知无需处理（错）
- **工程用法**：动态工具治理
- **版本锚点**：MCP 规范
