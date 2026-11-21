---
title: "[JC-085] 并发容器·synchronizedMap（选型）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · synchronizedMap（选型）

- **事实**：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap
- **原理**：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM
- **常见误区**：
  1. synchronizedMap 与 CHM 性能相当（错）
  2. synchronizedMap 读也无需锁（错）
  3. CHM 不保证复合操作原子所以不如 synchronizedMap 安全（错）
- **工程用法**：老代码 review 时识别并替换
- **版本锚点**：JDK 文档
