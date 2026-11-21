---
title: "[SP-094] 事务·TransactionSynchronization（连接）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · TransactionSynchronization（连接）

- **事实**：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）
- **原理**：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活
- **常见误区**：
  1. 同步回调默认异步执行（错）
  2. afterCommit 中事务仍可回滚（错）
  3. 注册回调必须手动开新事务才能写库（提交后阶段）（错）
- **工程用法**：精确控制事务生命周期
- **版本锚点**：Spring 源码
