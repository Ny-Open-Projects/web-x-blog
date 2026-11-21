---
title: "[AD-412] 协作·跨 Agent（调试）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 协作 · 跨 Agent（调试）

- **事实**：跨 Agent 调试工作流：从父 Agent trace（JA-674）下钻到子 Agent 轨迹，调试界面按调用树展开（分布式调试思想）
- **原理**：跨 Agent 调试的工程化（JA-674 观测的调试面），调用树 UI 让协作问题可定位，与分布式排障（DF-053）联动
- **常见误区**：
  1. 跨 Agent 调试只能看日志（错）
  2. 调用树 UI 不必要（错）
  3. 调试按 Agent 隔离（错）
- **工程用法**：跨 Agent 调试
- **版本锚点**：实战共识
