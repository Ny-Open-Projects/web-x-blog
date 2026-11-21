# 1208 binlog 格式、刷盘与主从架构深挖

## 思路与架构
binlog（二进制日志）是 MySQL server 层日志，记录所有更改数据的"事件"，用于**主从复制**与**时间点恢复（PITR）**，与引擎层的 redo log 正交。
- **三种格式**：STATEMENT（记 SQL 语句，SBR，轻量但遇非确定性函数/存储过程易不一致）、ROW（记行改动，RBR，最准但日志大，对应原文"肉格式"）、MIXED（混合，默认 STATEMENT，无法精确复制时自动转 ROW，即 MBR）。
- **刷盘时机（`sync_binlog`）**：0=交给 OS 缓存（最快、宕机可能丢）、1=每次事务提交 fsync（最安全）、N=每 N 个事务 fsync 一次。配合 `innodb_flush_log_at_trx_commit=1` 构成"双 1"不丢事务基线。
- **复制架构**：主库 binlog → Binlog Dump 线程 → 从库 IO 线程 → relay log → SQL 线程回放；5.7+ 可 `LOGICAL_CLOCK` 并行回放。

## 方案取舍
- **STATEMENT vs ROW**：STATEMENT 日志小、主从带宽省，但 `UUID()`/`NOW()` 等不确定函数、带 `LIMIT` 的 `DELETE` 在主从可能产生不同结果；ROW 规避不确定性但 `UPDATE` 全表会产生海量 binlog。生产常选 MIXED 或 ROW（数据一致性优先时）。
- **sync_binlog=1 vs 0**：1 安全但每次提交都 fsync，高并发写吞吐受限；0/N 提升吞吐但崩溃可能丢已提交事务的 binlog，破坏与主库数据一致性。双 1 是金融级不丢的代价。
- **半同步 vs 异步 vs 全同步**：异步吞吐最高、可能丢；半同步折中（至少一从 ACK，ACK 超时降级异步）；全同步最强一致但受最慢从库拖累。按业务一致性 SLA 选。

## 答题技巧
1. **先定性后定量**：先讲 binlog"是什么/干嘛用"（复制+PITR，server 层），再讲格式/刷盘/复制链路。
2. **格式三选一要带缩写**：SBR/STATEMENT、RBR/ROW、MBR/MIXED——原文把 MBR 写成"MML/MMR"是机翻崩坏，面试必须说"Mixed Based Replication=MBR"。
3. **刷盘回答钩子**：把 `sync_binlog` 与 redo 的 `innodb_flush_log_at_trx_commit` 绑成"双 1"，顺带引出两阶段提交为何需要 XID 关联。
4. **复制链路三线程两日志**：Binlog Dump/IO/SQL + binlog/relay log，点出 SQL 单线程是延迟根因。
5. **反直觉点**：① binlog 时间戳用主库时钟，**主从时钟不同步不导致复制延迟**；② 半同步 ACK 是"写入 relay log"不是"执行完"；③ 混合模式缩写是 MBR 不是 MMR。

## 细节与核心 API

**双 1 不丢事务基线（server 层 binlog + 引擎层 redo 配合）**：

```ini
sync_binlog = 1                          # 每次事务提交 fsync（0=交 OS 缓存最快/可能丢；N=每 N 事务 fsync）
innodb_flush_log_at_trx_commit = 1      # redo 每次提交 fsync
```

**binlog 三种格式**：

```text
STATEMENT(SBR) 记 SQL 语句，轻量；UUID()/NOW()/带 LIMIT 的 DELETE 在主从可能不一致
ROW(RBR)       记行改动，最准；全表 UPDATE 产生海量 binlog（日志大）
MIXED(MBR)     默认 STATEMENT，无法精确复制时自动转 ROW   ← 面试必须说 MBR，不是 MMR
```

**主从复制链路（三线程两日志）**：

```text
主库 binlog → Binlog Dump 线程 → 从库 IO 线程 → relay log → SQL 线程回放
  SQL 单线程回放是复制延迟根因；5.7+ LOGICAL_CLOCK 支持并行回放
  半同步 ACK = 已"写入 relay log" 而非 "已执行完"
```

> 边界：redo/undo 与两阶段提交见 1207；事务隔离与 MVCC 见 1230/1231；本卡只讲 binlog 格式、刷盘、主从复制。
