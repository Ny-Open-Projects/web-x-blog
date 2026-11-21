---
title: "[SP-012] IoC·request（作用域）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · request（作用域）

- **事实**：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理
- **原理**：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求
- **常见误区**：
  1. request 作用域在非 Web 环境也能用（错）
  2. 注入 request Bean 不需要任何处理（错）
  3. session 作用域线程安全无需代理（错）
- **工程用法**：每请求状态对象的标准做法
- **版本锚点**：Spring 文档
