---
title: "[DF-014] 一致性·Quorum（NWR）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 一致性 · Quorum（NWR）

- **事实**：NWR：N 副本写 W 份读 R 份，W+R>N 保证读写不交错
- **原理**：Dynamo 风格：W=N R=1 强一致写、W=1 R=1 高性能可容忍不一致（读修复），可调旋钮
- **常见误区**：
  1. W+R>N 表示强一致（错）
  2. N 越大越好（错）
  3. W=1 时写已安全（错）
- **工程用法**：多副本可调一致性设计
- **版本锚点**：Dynamo 论文
