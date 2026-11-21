---
title: "[DF-064] 事务·undo_log（AT）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · undo_log（AT）

- **事实**：Seata AT 模式：自动生成 undo_log（前后镜像）实现二阶段回滚
- **原理**：业务无侵入（自动代理 SQL），一阶段本地提交+undo_log 落库，二阶段异步删除（成功）或镜像回滚（失败），全局锁防脏写
- **常见误区**：
  1. AT 模式强一致（错）
  2. undo_log 不需要清理（错）
  3. AT 无全局锁（错）
- **工程用法**：低冲突场景的自动补偿
- **版本锚点**：Seata 文档
