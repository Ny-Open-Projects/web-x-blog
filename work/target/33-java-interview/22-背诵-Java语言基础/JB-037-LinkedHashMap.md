---
title: "[JB-037] HashMap·LinkedHashMap（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## HashMap · LinkedHashMap（语法语义）

- **事实**：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。
- **原理**：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。
- **常见误区**：
  1. LinkedHashMap 只能保持插入顺序。（错）
  2. LinkedHashMap 的 accessOrder 默认就是 true。（错）
  3. LinkedHashMap 与 HashMap 无继承关系。（错）
- **工程用法**：accessOrder=true + removeEldestEntry 即 LRU 缓存。
- **版本锚点**：JDK 8+ 源码
