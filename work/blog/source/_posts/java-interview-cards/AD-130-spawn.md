---
title: "[AD-130] 编排·spawn（动态）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 编排 · spawn（动态）

- **事实**：动态子 Agent 生成：按任务特征动态 spawn 子 Agent（数量与角色按需），与预定义子 Agent 对比
- **原理**：静态子 Agent 简单可控，动态 spawn 灵活但不可预测（资源与安全管控难），按任务开放度选（JA-368）
- **常见误区**：
  1. 子 Agent 数量固定（错）
  2. 动态 spawn 无风险（错）
  3. 动态与静态无区别（错）
- **工程用法**：动态 spawn 设计
- **版本锚点**：实战共识
