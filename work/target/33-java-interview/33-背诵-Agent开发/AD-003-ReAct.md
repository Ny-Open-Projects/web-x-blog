---
title: "[AD-003] 模式·ReAct（ReAct）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 模式 · ReAct（ReAct）

- **事实**：ReAct 模式：Reason（推理该做什么）→Act（调工具）→Observe（观察结果）循环，是 Agent 最基础的执行模式
- **原理**：推理与行动交替让模型"边做边想"，观察结果反馈下一轮推理，是最易实现与调试的 Agent 模式
- **常见误区**：
  1. ReAct 是一次性规划（错）
  2. ReAct 不含工具调用（错）
  3. Observe 是用户观察（错）
- **工程用法**：Agent 执行模式起点
- **版本锚点**：2025 共识
