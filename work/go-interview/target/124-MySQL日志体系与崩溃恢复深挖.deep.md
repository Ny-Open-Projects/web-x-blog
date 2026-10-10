# 124 MySQL 日志体系与崩溃恢复深挖

## 思路与架构
MySQL 日志全景，按"层级 + 职责"两条线组织：
- **InnoDB 引擎层**：`redo log`（物理、循环写、崩溃恢复/持久性）、`undo log`（逻辑、回滚+MVCC、自身受 redo 保护）。
- **Server 层**：`binlog`（逻辑、追加写、PITR+主从复制、全引擎）、`relay log`（**中继日志**：从库把主库 binlog 拉过来存的副本，用于主从异步复制 + 从库崩溃恢复，断点续传）、`slow log`（慢查询日志，调优用）、`audit log`（审计日志，企业版/MariaDB 插件，生产多在业务层工单审批实现）。
- **两阶段提交(2PC)崩溃恢复**：`prepare`（写 redo 标记 prepare）→ 写 `binlog` → `commit`（redo 标记 commit）。重启扫描 redo：处于 prepare **且 binlog 完整** → 提交；prepare 但 **binlog 缺失/不完整** → 借助 undo 回滚。这保证 redo 与 binlog 的"已提交集合"一致，主从不分裂。

## 方案取舍
- **redo 循环写 vs binlog 追加写**：redo 省空间、只保"未刷盘的近期改动"；binlog 全量变更历史但占盘——按 `binlog_expire_logs_seconds` 权衡保留期。
- **"双 1"不丢基线**：`sync_binlog=1` + `innodb_flush_log_at_trx_commit=1`，每次事务提交都 fsync，金融级不丢，代价是吞吐受限。
- **slow/audit 日志**：高并发下记录大量日志会拖累性能、占盘；通常按需开启，审计多在业务层而非数据库层做。

## 答题技巧
1. **先分层**：开口即"引擎层(redo/undo) vs server 层(binlog/relay)"，建立结构感。
2. **物理 vs 逻辑**是高频对比点：redo 物理、binlog/undo 逻辑。
3. **必讲 2PC 崩溃恢复**：prepare + binlog 完整性判据，这是 redo/binlog 协同的硬核答案。
4. **反直觉点**：① redo 在事务**执行中持续写**，非"提交才写"；② MVCC 是快照读机制，**非乐观锁**；③ 自增 ID 断层源于**回滚不回收**已分配 ID；④ binlog **所有引擎都记**、redo **仅 InnoDB**；⑤ relay log 是从库的 binlog 副本。
5. **版本锚点**：InnoDB 8.0 把自增计数器持久化到**数据字典**，重启后断层减少，但已用 ID 仍不回退。

## 细节与核心 API

**日志层级与职责**：

```text
引擎层：redo log（物理/循环写/崩溃恢复+持久性）+ undo log（逻辑/回滚+MVCC，自身受 redo 保护）
server层：binlog（逻辑/追加写/PITR+主从复制/全引擎）+ relay log（从库 binlog 副本/断点续传）
        + slow log（调优）+ audit log（企业版/MariaDB 插件，生产多在业务层做）
```

**两阶段提交（2PC）崩溃恢复**：

```text
prepare（写 redo 标记 prepare）→ 写 binlog → commit（redo 标记 commit）
重启扫描 redo：prepare 且 binlog 完整 → 提交；prepare 但 binlog 缺失/不完整 → undo 回滚
→ 保证 redo 与 binlog「已提交集合」一致，主从不分裂
```

```ini
# 双 1 不丢基线
sync_binlog = 1
innodb_flush_log_at_trx_commit = 1   # 每次事务提交 fsync，金融级不丢，代价吞吐受限
# 反直觉：redo 在事务执行中持续写（非提交才写）；binlog 所有引擎都记、redo 仅 InnoDB
```

> 边界：binlog 格式/刷盘/主从见 1208；MVCC 见 1231；本卡只讲日志体系与崩溃恢复。
