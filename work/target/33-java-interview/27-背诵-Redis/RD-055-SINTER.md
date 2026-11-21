---
title: "[RD-055] 集合·SINTER（运算）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合 · SINTER（运算）

- **事实**：Set 交集并集差集（SINTER/SUNION/SDIFF）支撑共同好友/推荐标签
- **原理**：10 万级以下集合运算可用，大集合运算阻塞主线程（O(N)），大集合运算改业务侧或 ES
- **常见误区**：
  1. Set 运算无性能风险（错）
  2. 差集是交集的补集无独立用途（错）
  3. SDIFF 结果包含对方独有元素（错）
- **工程用法**：社交关系功能实现
- **版本锚点**：实战共识
