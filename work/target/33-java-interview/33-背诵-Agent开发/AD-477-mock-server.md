---
title: "[AD-477] 工具·mock server（模拟）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工具 · mock server（模拟）

- **事实**：工具的 mock server：测试环境工具的模拟实现（返回 fixture 数据），Agent 全链测试免真实下游（AD-039 的服务化）
- **原理**：mock server 让集成测试无真实依赖（JA-203 分层），fixture 数据贴近真实分布（AD-169 保真），与测试基建联动
- **常见误区**：
  1. 测试直接调真实工具（错）
  2. mock server 是过度设计（错）
  3. fixture 随意造（保真设计）（错）
- **工程用法**：mock server
- **版本锚点**：实战共识
