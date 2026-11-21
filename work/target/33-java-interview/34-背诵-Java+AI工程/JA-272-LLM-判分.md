---
title: "[JA-272] 工程·LLM 判分（评估）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · LLM 判分（评估）

- **事实**：评估自动判分：LLM-as-judge 按评分细则打分，judge 模型与被测模型分开（防偏袒），抽样人工校准
- **原理**：AI-069 的工程化：人工全评不可行，judge 是杠杆，judge 自身的偏差要校准（换 judge 跑分对比）
- **常见误区**：
  1. 自动判分不需要校准（错）
  2. judge 用同一个模型最公平（错）
  3. 判分完全客观（错）
- **工程用法**：评估自动化
- **版本锚点**：实战共识
