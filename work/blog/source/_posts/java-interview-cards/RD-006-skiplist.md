---
title: "[RD-006] ZSet·skiplist（编码）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ZSet · skiplist（编码）

- **事实**：ZSet 底层是 skiplist（按分数有序）+ dict（member 到 score 的映射）双结构
- **原理**：跳表支持范围查询与有序遍历 O(logN)，dict 支持按 member 查 score O(1)，空间换双向高效
- **常见误区**：
  1. ZSet 只用跳表一种结构（错）
  2. ZSet 用红黑树（错）
  3. dict 与 skiplist 各存一份是浪费设计缺陷（错）
- **工程用法**：排行榜/延迟队列场景
- **版本锚点**：源码实现
