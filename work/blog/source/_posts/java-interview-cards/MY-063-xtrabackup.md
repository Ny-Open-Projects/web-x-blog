---
title: "[MY-063] 备份·xtrabackup（工具）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 备份 · xtrabackup（工具）

- **事实**：物理备份 xtrabackup（热备 InnoDB 文件级）优于 mysqldump（逻辑 SQL 重放慢）
- **原理**：xtrabackup 拷贝数据文件+备份期间增量日志，TB 级库恢复按小时计，mysqldump 适合小库与跨版本迁移
- **常见误区**：
  1. mysqldump 是生产备份首选（错）
  2. xtrabackup 只能冷备（错）
  3. 物理备份跨平台无损（错）
- **工程用法**：备份方案选型
- **版本锚点**：Percona 文档
