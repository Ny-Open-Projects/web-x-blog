---
title: "[AD-280] 手写·Spring（集成）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 手写 · Spring（集成）

- **事实**：Agent 与 Spring 集成：AgentExecutor/Registry/ModelClient 为 bean（AD-070 Builder 类比），配置绑定（AD-277），生命周期由容器管理（AD-107）
- **原理**：Spring 集成让 Agent 工程化（依赖注入/生命周期/观测），bean 化后 AOP 观测（JA-019）自动，与 Spring 知识联动
- **常见误区**：
  1. 手写 Agent 不能进 Spring（错）
  2. bean 化是过度设计（错）
  3. 生命周期手写管理（错）
- **工程用法**：Spring 集成实现
- **版本锚点**：实战共识
