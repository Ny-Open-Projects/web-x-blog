---
title: "[SP-048] 事务·public（失效）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · public（失效）

- **事实**：Spring 6.0 之前 @Transactional 只对 public 方法生效
- **原理**：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效
- **常见误区**：
  1. protected 方法事务在所有版本生效（错）
  2. 非 public 加注解会启动报错（错）
  3. 接口默认方法的事务一定生效（错）
- **工程用法**：升级 Spring 6 才有非 public 事务支持
- **版本锚点**：Spring 6.0 release note
