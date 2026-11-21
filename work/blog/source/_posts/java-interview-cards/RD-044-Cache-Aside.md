---
title: "[RD-044] 缓存·Cache Aside（一致性）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 缓存 · Cache Aside（一致性）

- **事实**：标准缓存模式 Cache Aside：读 miss 查库回填，写时先更新库再删除缓存
- **原理**：先删缓存后更库（并发读回填旧值概率高）与先更缓存（并发写乱序）都有问题，先库后删是最优实践（Martin Kleppmann 分析）
- **常见误区**：
  1. 写时应该先更新缓存（错）
  2. 先删缓存是标准做法（错）
  3. 缓存与库总能强一致（分布式下只能最终一致）（错）
- **工程用法**：缓存一致性八股主线
- **版本锚点**：实战共识
