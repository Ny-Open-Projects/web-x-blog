---
title: "[JB-107] HashMap·initialCapacity（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## HashMap · initialCapacity（语法语义）

- **事实**：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。
- **原理**：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。
- **常见误区**：
  1. new HashMap<>(100) 的表长就是 100。（错）
  2. 传入的 initialCapacity 会被原样用作表长。（错）
  3. 传入 100 实际表长是 128 是因为内存对齐。（错）
- **工程用法**：本机实测：new HashMap<>(100) 首插后 table.length=128。
- **版本锚点**：JDK 文档
