---
title: "[MY-028] 日志·redo log（redo）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 日志 · redo log（redo）

- **事实**：redo log 是 InnoDB 层物理日志 WAL 顺序循环写保证崩溃恢复
- **原理**：先写日志后刷数据页（WAL），随机写变顺序写提升性能，空间固定循环复用，8.0.30 起由 innodb_redo_log_capacity 统一控制
- **常见误区**：
  1. redo log 记录逻辑 SQL（错）
  2. redo 在 Server 层（错）
  3. redo log 无限增长（错）
- **工程用法**：WAL 是 InnoDB 性能的基石
- **版本锚点**：MySQL 8.0.30
