---
title: "[MY-036] 事务·ReadView（MVCC）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · ReadView（MVCC）

- **事实**：ReadView 包含活跃事务列表 m_ids、低水位 min_trx_id、高水位 max_trx_id 与 creator_trx_id
- **原理**：可见性判断：trx_id<min 可见；>=max 不可见；中间再看是否在 m_ids（未提交的不可见），不可见则沿版本链向前找
- **常见误区**：
  1. ReadView 记录所有历史版本（错）
  2. max_trx_id 是最大事务 ID 本身（是"下一个将分配的 ID"）（错）
  3. creator_trx_id 表示只读事务（错）
- **工程用法**：MVCC 可见性规则题的标准推导
- **版本锚点**：InnoDB 文档
