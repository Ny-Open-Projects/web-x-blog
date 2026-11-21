---
title: "[JB-052] 异常·finally执行（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异常 · finally执行（语法语义）

- **事实**：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。
- **原理**：编译器把 finally 代码内联到所有出口路径。
- **常见误区**：
  1. finally 只在 try 正常结束时执行。（错）
  2. finally 中 return 后原异常仍会抛出。（错）
  3. finally 执行顺序不确定。（错）
- **工程用法**：阿里手册：禁止在 finally 中使用 return。
- **版本锚点**：JLS 14.20
