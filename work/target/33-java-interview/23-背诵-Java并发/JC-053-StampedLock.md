---
title: "[JC-053] 显式锁·StampedLock（乐观读）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 显式锁 · StampedLock（乐观读）

- **事实**：StampedLock 提供乐观读：读时不加锁事后 validate 校验
- **原理**：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition
- **常见误区**：
  1. StampedLock 支持可重入（错）
  2. 乐观读失败会自动重试无需处理（错）
  3. StampedLock 完全替代 ReentrantReadWriteLock（错）
- **工程用法**：热点缓存读路径优化
- **版本锚点**：JDK 文档
