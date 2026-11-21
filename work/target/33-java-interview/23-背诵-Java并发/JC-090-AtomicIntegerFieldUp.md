---
title: "[JC-090] 原子类·AtomicIntegerFieldUpdater（字段更新）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 原子类 · AtomicIntegerFieldUpdater（字段更新）

- **事实**：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作
- **原理**：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存
- **常见误区**：
  1. 它能把普通字段变成原子字段无需 volatile（错）
  2. private 字段也能更新（错）
  3. 它比 AtomicReference 更慢（错）
- **工程用法**：海量小对象内字段原子更新
- **版本锚点**：JDK 文档
