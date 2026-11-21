---
title: "[JB-054] 异常·多重catch（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异常 · 多重catch（语法语义）

- **事实**：JDK7+ 支持多类型 catch（catch (A 
- **原理**： B e)），但同族类型必须子类在前否则编译错误。
- **常见误区**：
  1. 多类型 catch 中 e 是隐式 final。（错）
  2. 多类型 catch 中 e 可以重新赋值。（错）
  3. 多类型 catch 的异常类型顺序随意。（错）
- **工程用法**：多类型 catch 是语法糖，反编译后是多个 catch 块。
- **版本锚点**：JDK 7+（JLS 14.20）
