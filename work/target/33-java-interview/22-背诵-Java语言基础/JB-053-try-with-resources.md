---
title: "[JB-053] 异常·try-with-resources（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异常 · try-with-resources（语法语义）

- **事实**：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。
- **原理**：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。
- **常见误区**：
  1. try-with-resources 只支持 IO 流。（错）
  2. try-with-resources 会吞掉 try 块中的异常。（错）
  3. 资源 close 的顺序与声明顺序相同。（错）
- **工程用法**：自定义资源类实现 AutoCloseable 即可享受语法糖。
- **版本锚点**：JDK 7+（JLS 14.20.3）
