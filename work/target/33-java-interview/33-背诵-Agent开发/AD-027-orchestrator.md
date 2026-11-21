---
title: "[AD-027] 多Agent·orchestrator（主从）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 多Agent · orchestrator（主从）

- **事实**：主从模式（orchestrator-worker）：主 Agent 拆解分发任务，子 Agent 执行并汇报，主 Agent 聚合产出
- **原理**：最常用的多 Agent 模式（主控清晰/子 Agent 简单），主 Agent 是单点（其决策质量决定全局），与舱壁隔离（JA-373）配套
- **常见误区**：
  1. 多 Agent 必然自由协作（错）
  2. 主从模式过时（错）
  3. 主 Agent 不会成为瓶颈（错）
- **工程用法**：主从模式设计
- **版本锚点**：实战共识
