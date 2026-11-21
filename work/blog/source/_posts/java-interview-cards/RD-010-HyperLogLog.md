---
title: "[RD-010] 扩展类型·HyperLogLog（统计）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展类型 · HyperLogLog（统计）

- **事实**：HyperLogLog 以 12KB 固定内存估算亿级基数误差 0.81%
- **原理**：概率算法（伯努利+调和平均），PFADD/PFCOUNT/PFMERGE，官方文档核对零差异（0.81% 与 12KB）
- **常见误区**：
  1. HyperLogLog 精确计数（错）
  2. 12KB 是每个元素的开销（错）
  3. 误差 1% 以上（错）
- **工程用法**：UV 统计标准方案
- **版本锚点**：官方文档核对
