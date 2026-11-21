---
title: "[SP-037] AOP·JDK vs CGLIB（代理）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · JDK vs CGLIB（代理）

- **事实**：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求
- **原理**：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理
- **常见误区**：
  1. JDK 代理性能永远更差（错）
  2. CGLIB 可以代理 final 类（错）
  3. 有接口时 CGLIB 不能用（错）
- **工程用法**：回答 AOP 代理选型
- **版本锚点**：Spring 文档
