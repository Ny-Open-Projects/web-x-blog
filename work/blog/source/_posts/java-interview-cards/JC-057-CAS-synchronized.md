---
title: "[JC-057] 并发容器·CAS+synchronized（CHM）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · CAS+synchronized（CHM）

- **事实**：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写
- **原理**：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数
- **常见误区**：
  1. CHM 使用 ReentrantLock 分段锁（那是 JDK7）（错）
  2. CHM 全表一把锁（错）
  3. JDK8 的 CHM 锁粒度是 Segment（错）
- **工程用法**：回答 CHM 原理必须分 JDK 版本
- **版本锚点**：JDK8 源码
