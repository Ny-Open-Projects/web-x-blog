---
title: "[JB-089] String·substring（性能）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · substring（性能）

- **事实**：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。
- **原理**：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。
- **常见误区**：
  1. substring 从未有过内存泄漏风险。（错）
  2. substring 在所有 JDK 版本中都拷贝新数组。（错）
  3. substring 的实现与 JDK 版本无关。（错）
- **工程用法**：P10 面试常以"substring 与内存泄漏"考察对实现的版本敏感度。
- **版本锚点**：JDK7u6
