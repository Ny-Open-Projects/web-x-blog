---
title: "[JV-021] 收集器·Region（G1）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 收集器 · Region（G1）

- **事实**：G1 把堆划分为多个等大 Region 逻辑分代停顿可预测
- **原理**：Region 大小 1-32MB（2 的幂自动选），Eden/Survivor/Old 是 Region 的角色标记而非物理连续区域，按停顿目标优先回收价值高的 Region（垃圾优先）
- **常见误区**：
  1. G1 的分代是物理连续的内存块（错）
  2. Region 大小固定 32MB（错）
  3. G1 只能整堆回收（错）
- **工程用法**：回答"G1 为什么叫 Garbage First"的标准点
- **版本锚点**：G1 论文
