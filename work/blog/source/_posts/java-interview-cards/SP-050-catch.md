---
title: "[SP-050] 事务·catch（失效）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · catch（失效）

- **事实**：事务方法内异常被 try-catch 吞掉后事务照常提交
- **原理**：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()
- **常见误区**：
  1. catch 后事务自动回滚（错）
  2. setRollbackOnly 会抛异常（错）
  3. 吞异常是推荐的容错方式（错）
- **工程用法**：代码 review 必查事务内 catch
- **版本锚点**：实战共识
