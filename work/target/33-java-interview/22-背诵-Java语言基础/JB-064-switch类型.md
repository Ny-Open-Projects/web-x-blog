---
title: "[JB-064] 语言杂项·switch类型（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 语言杂项 · switch类型（误用）

- **事实**：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。
- **原理**：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。
- **常见误区**：
  1. switch 支持 long 类型。（错）
  2. switch 支持 double 类型。（错）
  3. switch 从 Java 5 就支持 String。（错）
- **工程用法**：JDK14+ 的 switch 表达式（箭头语法）是新的考察点。
- **版本锚点**：JDK 7（String 支持）
