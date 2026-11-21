---
title: "[SP-058] 事务·@TransactionalEventListener（事件）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · @TransactionalEventListener（事件）

- **事实**：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）
- **原理**：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选
- **常见误区**：
  1. 默认在事务提交前执行（错）
  2. 它默认异步执行（错）
  3. 事务回滚后默认仍会执行（错）
- **工程用法**：提交后发 MQ/清缓存的标准姿势
- **版本锚点**：Spring 文档核对
