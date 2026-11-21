---
title: "[JB-095] 集合通用·Iterator契约（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合通用 · Iterator契约（语法语义）

- **事实**：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。
- **原理**：连续 remove 两次抛 IllegalStateException。
- **常见误区**：
  1. 可以在不调用 next 的情况下多次 remove。（错）
  2. Iterator 的 remove 与集合的 remove 等价且安全。（错）
  3. Iterator.remove 之后必须立即 next。（错）
- **工程用法**："为什么设计 next 后才能 remove"是理解迭代器状态的切入点。
- **版本锚点**：Iterator javadoc
