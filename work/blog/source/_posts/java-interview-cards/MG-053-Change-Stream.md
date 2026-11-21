---
title: "[MG-053] 变更·Change Stream（Change Stream）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 变更 · Change Stream（Change Stream）

- **事实**：Change Stream（3.6+）订阅数据变更事件（基于 oplog）
- **原理**：应用级 CDC：微服务间同步、实时索引（ES）、审计，比轮询高效比直接读 oplog 安全（官方 API）
- **常见误区**：
  1. Change Stream 是轮询实现（错）
  2. Change Stream 丢事件（断点 resumeToken 续传）（错）
  3. 需要 trigger 组件才能用（错）
- **工程用法**：实时同步方案
- **版本锚点**：官方文档
