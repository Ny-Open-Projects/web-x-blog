---
title: "[DF-057] SRE·MTTR（指标）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SRE · MTTR（指标）

- **事实**：MTBF（平均故障间隔）/MTTR（平均恢复时间）构成可用性方程：可用性∝MTBF/(MTBF+MTTR)
- **原理**：提升可用性两路：减少故障（MTBF↑）与快速恢复（MTTR↓），现代实践重 MTTR（故障不可避免，1 分钟恢复优于 1 月无故障+1 小时恢复）
- **常见误区**：
  1. MTTR 是修复时长（恢复时长）（错）
  2. 可用性只靠预防故障（错）
  3. MTBF 更重要（错）
- **工程用法**：稳定性方法论
- **版本锚点**：Google SRE
