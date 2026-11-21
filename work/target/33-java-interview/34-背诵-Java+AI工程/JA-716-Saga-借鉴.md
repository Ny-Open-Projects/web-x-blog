---
title: "[JA-716] 工程·Saga 借鉴（架构）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · Saga 借鉴（架构）

- **事实**：Agent 多步任务的 Saga 借鉴：每步可回滚设计（工具操作前记录可逆状态），失败沿补偿链逆放
- **原理**：Agent 步骤与 Saga 事务同构（JA-505 补偿的架构化），可逆设计让失败恢复优雅，与分布式事务知识联动
- **常见误区**：
  1. Agent 步骤不可逆是必然（错）
  2. Saga 与 Agent 无关（错）
  3. 回滚不需要设计（错）
- **工程用法**：可逆架构
- **版本锚点**：实战共识
