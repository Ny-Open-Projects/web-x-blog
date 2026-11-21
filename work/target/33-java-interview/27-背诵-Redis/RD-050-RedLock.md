---
title: "[RD-050] 分布式锁·RedLock（争议）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分布式锁 · RedLock（争议）

- **事实**：RedLock（多节点多数派锁）有学术争议（Martin Kleppmann 质疑其安全性）
- **原理**：争议点：时钟跳变与 GC 停顿下锁的正确性，结论：Redis 锁适合"效率"（防重复执行）不适合"正确性"（强互斥），强互斥用 ZooKeeper/etcd 或 fencing token
- **常见误区**：
  1. RedLock 完全安全（有争议）（错）
  2. Redis 锁永远可靠（错）
  3. 争议已经解决（未解决，仍是设计权衡）（错）
- **工程用法**：锁选型的高级考点
- **版本锚点**：学术争议
