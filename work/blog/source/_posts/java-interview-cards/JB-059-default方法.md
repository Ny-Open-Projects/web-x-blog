---
title: "[JB-059] 接口·default方法（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 接口 · default方法（语法语义）

- **事实**：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。
- **原理**：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。
- **常见误区**：
  1. 接口实现类初始化永远不会触发任何接口的初始化。（错）
  2. default 方法只能在实现类中调用。（错）
  3. 接口的 default 方法破坏了接口不能有实现的规则因此被移除过。（错）
- **工程用法**：本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化。
- **版本锚点**：JDK8+
