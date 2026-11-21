---
title: "[JB-034] HashMap·JDK7头插（版本）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## HashMap · JDK7头插（版本）

- **事实**：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。
- **原理**：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。
- **常见误区**：
  1. JDK7 与 JDK8 的插入策略相同。（错）
  2. JDK7 并发扩容只会丢数据不会死循环。（错）
  3. 头插法在任何场景都比尾插快因此被保留。（错）
- **工程用法**："HashMap 并发死循环 CPU 100%"是真实生产事故类型。
- **版本锚点**：JDK 7→8 版本史
