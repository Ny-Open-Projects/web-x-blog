---
title: "[AD-037] 可靠性·checkpoint（恢复）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可靠性 · checkpoint（恢复）

- **事实**：Agent checkpoint：每步后持久化状态（消息序列+任务状态），失败从最近 checkpoint 恢复（JA-021/505 落地）
- **原理**：长任务不 checkpoint=从头再来（成本浪费），checkpoint 频率与粒度权衡（每步 vs 阶段），与状态显式化（AD-021）配套
- **常见误区**：
  1. checkpoint 可选（错）
  2. 恢复自动完美（需要设计）（错）
  3. 粒度越细越好（存储代价权衡）（错）
- **工程用法**：checkpoint 设计
- **版本锚点**：实战共识
