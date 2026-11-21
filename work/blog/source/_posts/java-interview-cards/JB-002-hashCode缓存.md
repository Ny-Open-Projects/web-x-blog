---
title: "[JB-002] String·hashCode缓存（内存）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · hashCode缓存（内存）

- **事实**：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。
- **原理**：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。
- **常见误区**：
  1. String 的 hashCode 每次调用都会重新计算。（错）
  2. String 的 hashCode 缓存需要手动开启。（错）
  3. String 缓存 hashCode 会导致内存泄漏。（错）
- **工程用法**：把不变对象作 HashMap key 的核心收益之一。
- **版本锚点**：JDK 8+ String 源码
