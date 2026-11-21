---
title: "[MY-044] DDL·online DDL（在线）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## DDL · online DDL（在线）

- **事实**：online DDL：INPLACE 算法大部分操作不锁表（加列 8.0 支持 INSTANT 秒级）
- **原理**：INSTANT 只改元数据（8.0.12+），INPLACE 重建表仍需时间且 MDL 短锁，COPY 全量拷贝最慢，DDL 前查支持算法
- **常见误区**：
  1. 加列必须重建全表（错）
  2. online DDL 完全不锁表（错）
  3. INSTANT 是 5.7 功能（错）
- **工程用法**：大表 DDL 先查算法支持表
- **版本锚点**：MySQL 8.0.12
