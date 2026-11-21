---
title: "[JB-096] 集合通用·Deque双端（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合通用 · Deque双端（语法语义）

- **事实**：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。
- **原理**：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。
- **常见误区**：
  1. Stack 是 Java 中栈的推荐实现。（错）
  2. ArrayDeque 不支持栈操作。（错）
  3. ArrayDeque 底层是链表。（错）
- **工程用法**：ArrayDeque 底层是循环数组，无容量限制自动扩容。
- **版本锚点**：JDK 6+
