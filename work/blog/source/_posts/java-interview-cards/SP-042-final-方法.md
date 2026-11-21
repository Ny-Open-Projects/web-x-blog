---
title: "[SP-042] AOP·final 方法（失效）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · final 方法（失效）

- **事实**：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效
- **原理**：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理
- **常见误区**：
  1. CGLIB 能代理 private 方法（错）
  2. final 方法切面正常工作（错）
  3. static 方法可以被切面增强（错）
- **工程用法**：注解方法避免 private/final/static
- **版本锚点**：CGLIB 限制
