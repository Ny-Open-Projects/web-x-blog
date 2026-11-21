---
title: "[JB-036] HashMap·fail-fast（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## HashMap · fail-fast（误用）

- **事实**：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。
- **原理**：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。
- **常见误区**：
  1. 迭代中修改集合是完全安全的。（错）
  2. fail-fast 保证修改一定不生效。（错）
  3. ConcurrentModificationException 只在多线程出现。（错）
- **工程用法**：单线程迭代中修改同样抛 CME（本机实测）。
- **版本锚点**：Iterator javadoc（fail-fast 语义）
