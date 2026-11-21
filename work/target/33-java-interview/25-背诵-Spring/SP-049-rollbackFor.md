---
title: "[SP-049] 事务·rollbackFor（回滚）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · rollbackFor（回滚）

- **事实**：@Transactional 默认只回滚 RuntimeException 与 Error
- **原理**：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款
- **常见误区**：
  1. 默认回滚所有异常（错）
  2. 默认回滚受检异常（错）
  3. Error 不触发回滚（错）
- **工程用法**：事务注解一律显式 rollbackFor
- **版本锚点**：阿里手册
