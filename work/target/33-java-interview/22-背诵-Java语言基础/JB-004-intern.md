---
title: "[JB-004] String·intern（内存）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · intern（内存）

- **事实**：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。
- **原理**：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。
- **常见误区**：
  1. JDK7+ 的 intern() 一定会返回常量池中的新拷贝对象。（错）
  2. intern() 会创建一个新的 String 对象。（错）
  3. intern() 只对字面量有效，对拼接结果无效。（错）
- **工程用法**：海量重复字符串场景 intern 可显著省内存（需评估 GC 压力）。
- **版本锚点**：JDK7+
