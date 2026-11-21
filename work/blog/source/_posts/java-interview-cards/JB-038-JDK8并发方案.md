---
title: "[JB-038] CHM·JDK8并发方案（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CHM · JDK8并发方案（语法语义）

- **事实**：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。
- **原理**：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。
- **常见误区**：
  1. JDK8 的 CHM 全表只有一把全局锁。（错）
  2. CHM 的所有读操作都需要加锁。（错）
  3. CHM 使用 ReentrantLock 锁定每个桶。（错）
- **工程用法**：JDK7 是 Segment 分段锁（默认 16 段），JDK8 彻底重构。
- **版本锚点**：JDK 8 源码
