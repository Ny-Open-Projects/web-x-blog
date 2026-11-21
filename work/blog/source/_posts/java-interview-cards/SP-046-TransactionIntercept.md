---
title: "[SP-046] 事务·TransactionInterceptor（原理）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · TransactionInterceptor（原理）

- **事实**：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现
- **原理**：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析
- **常见误区**：
  1. @Transactional 是 JDBC 驱动实现（错）
  2. 事务与 AOP 无关（错）
  3. 开启事务会立即提交一次（错）
- **工程用法**：事务原理是 AOP 应用的最佳案例
- **版本锚点**：Spring 源码
