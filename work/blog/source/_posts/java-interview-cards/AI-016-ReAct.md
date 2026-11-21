---
title: "[AI-016] Agent·ReAct（循环）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · ReAct（循环）

- **事实**：ReAct 循环：Reason（推理）→Act（调工具）→Observation（观察结果）循环直到任务完成
- **原理**：工具结果反馈给模型迭代决策，循环上限（max iterations）防死循环，每轮都消耗 token（成本随步数线性），与单轮问答的本质区别
- **常见误区**：
  1. ReAct 是并行执行（错）
  2. 循环无上限（错）
  3. 工具失败自动重试无限次（错）
- **工程用法**：Agent 执行模型
- **版本锚点**：实战共识
