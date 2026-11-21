---
title: "题 5.2.3：redo log、undo log、binlog 各自的作用？两阶段提交是干什么的？"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 5.2.3：redo log、undo log、binlog 各自的作用？两阶段提交是干什么的？

**【参考回答（可背）】**
- **redo log**（InnoDB）：物理日志，"某页做了什么修改"，**循环写**，保证崩溃恢复（持久性）；WAL 思想：顺序写日志代替随机写页，MySQL 高写性能的基石。
- **undo log**：逻辑日志，反向操作（insert 的 undo 是 delete），保证原子性（回滚）+ MVCC 版本链。
- **binlog**（Server 层）：逻辑日志，语句/行/混合三种格式（**生产用 ROW**），追加写，用于**复制与恢复**。
- **两阶段提交（2PC，必背）**：update 语句的提交顺序：
  1. 写 redo log，置 **prepare** 状态；
  2. 写 binlog；
  3. redo log 置 **commit**。
  崩溃恢复规则：redo prepare 但未 commit → 查 binlog：binlog 完整则提交，不完整则回滚。
  **为什么必须两阶段**：保证 redo 与 binlog 的一致性——否则崩溃后"主库有数据从库没有"或反之，存在必然分叉的崩溃窗口（主库有数据从库没有或反之），复制与恢复必错。

**【追问链】**
1. redo 和 binlog 区别一句话？→ 层级（引擎/Server）、物理/逻辑、循环写/追加写、崩溃恢复/复制归档。
2. 组提交是什么？→ 多个事务的 redo/binlog 合并一次 fsync（binlog_group_commit_sync_delay 微调），高并发下把"每事务一刷盘"摊薄成"一批一刷盘"，TPS 显著提升——**高并发写优化的隐藏大招**。
3. innodb_flush_log_at_trx_commit 和 sync_binlog 怎么配？→ 双 1（1,1）：不丢数据但每事务两次 fsync，最安全最慢；金融必双 1，普通业务 (1,2) 或 (2,1) 换吞吐，接受宕机丢 1 秒。

**【P10 加分项】**
指出双 1 的真实代价与折中：组提交 + NVMe 盘 + RAID 卡 BBU 缓存后，双 1 的 TPS 并不灾难；"参数调优前先问业务能接受丢多少"——把存储参数翻译成业务风险语言。

---
