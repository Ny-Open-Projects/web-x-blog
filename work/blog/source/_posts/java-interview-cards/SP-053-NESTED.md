---
title: "[SP-053] 事务·NESTED（传播）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · NESTED（传播）

- **事实**：NESTED 在当前事务内建立保存点（savepoint）可部分回滚
- **原理**：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务
- **常见误区**：
  1. NESTED 开新物理事务（错）
  2. NESTED 与 REQUIRES_NEW 等价（错）
  3. 保存点是 MySQL 不支持的（错）
- **工程用法**：嵌套业务步骤部分失败继续执行
- **版本锚点**：Spring 文档
