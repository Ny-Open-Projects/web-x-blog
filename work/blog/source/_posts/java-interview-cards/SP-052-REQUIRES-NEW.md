---
title: "[SP-052] 事务·REQUIRES_NEW（传播）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · REQUIRES_NEW（传播）

- **事实**：REQUIRES_NEW 挂起当前事务开独立新事务互不影响
- **原理**：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高
- **常见误区**：
  1. REQUIRES_NEW 加入外层事务（错）
  2. 内层回滚外层必然回滚（错）
  3. 它不会挂起当前事务（错）
- **工程用法**：操作日志/审计与主业务解耦
- **版本锚点**：Spring 文档
