---
title: "[JB-050] 异常·Checked与Runtime（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异常 · Checked与Runtime（语法语义）

- **事实**：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。
- **原理**：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。
- **常见误区**：
  1. IOException 是 RuntimeException 的子类。（错）
  2. RuntimeException 不需要处理所以不算异常。（错）
  3. 所有异常都必须被捕获。（错）
- **工程用法**：自定义业务异常统一继承 RuntimeException 是主流实践。
- **版本锚点**：JLS 11.2
