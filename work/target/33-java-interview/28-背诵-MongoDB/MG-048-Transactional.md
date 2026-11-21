---
title: "[MG-048] Java·@Transactional（事务）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Java · @Transactional（事务）

- **事实**：副本集下 Spring @Transactional 即可用（驱动自动 session 管理）
- **原理**：分片事务 4.2+，事务内读用 session 关联的 read concern，测试环境单机版不支持事务（需副本集模式）
- **常见误区**：
  1. 单机 MongoDB 支持事务（错）
  2. 事务需要手动创建 session（错）
  3. @Transactional 不支持 MongoDB（错）
- **工程用法**：Spring 集成事务
- **版本锚点**：Spring Data 文档
