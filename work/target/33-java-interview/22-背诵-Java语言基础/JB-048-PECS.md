---
title: "[JB-048] 泛型·PECS（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 泛型 · PECS（语法语义）

- **事实**：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。
- **原理**：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。
- **常见误区**：
  1. extends 与 super 在泛型里可以随意互换。（错）
  2. PECS 只适用于数组。（错）
  3. 通配符列表可以任意 add 任意类型。（错）
- **工程用法**：JDK 源码 Collections.copy 就是 PECS 的标准示范（src extends, dest super）。
- **版本锚点**：Effective Java Item 31
