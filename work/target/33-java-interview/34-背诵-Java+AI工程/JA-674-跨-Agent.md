---
title: "[JA-674] Agent·跨 Agent（观测）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · 跨 Agent（观测）

- **事实**：跨 Agent trace 延续：父 Agent 调子 Agent 的 trace 串联（子 Agent span 挂父 span），多 Agent 全链路可追
- **原理**：多 Agent 观测（JA-258/373）：trace 树跨 Agent 边界延续（DF-053 分布式追踪思想），观测断裂=多 Agent 黑盒
- **常见误区**：
  1. 各 Agent trace 独立无法串（错）
  2. 跨 Agent 追踪不存在（错）
  3. 串联成本高无价值（错）
- **工程用法**：多 Agent 可观测
- **版本锚点**：实战共识
