---
title: "[SP-045] AOP·exposeProxy（实践）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · exposeProxy（实践）

- **事实**：AopContext.currentProxy 需要开启 exposeProxy=true 才能用
- **原理**：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身
- **常见误区**：
  1. exposeProxy 默认开启（错）
  2. currentProxy 无需任何开关（错）
  3. 它是推荐的解自调用方式（错）
- **工程用法**：理解自调用问题的备选解
- **版本锚点**：Spring 文档
