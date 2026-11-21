---
title: "D 卷 MySQL"
date: 2026-11-18
categories: [Java面试, 笔试]
tags: [Java面试, 笔试题, 33]
type: 笔试题
disableNunjucks: true
---

## D 卷 MySQL

**D-1（选择）** MySQL 8.0 默认隔离级别与 RR 下防幻读的机制？
A. RC / MVCC　B. RR / MVCC+Next-Key Lock　C. RR / 仅 MVCC　D. SERIALIZABLE / 表锁
**答案：B。** 快照读靠 MVCC，当前读靠间隙锁+记录锁（左开右闭）；快照读后紧跟当前读的混用仍有幻读。

**D-2（选择）** 联合索引 (a,b,c)，下列走索引的是？
A. `b=1`　B. `a=1 and c=3`（只用到 a）　C. `a=1 and b>2 and c=3`（a,b 用到，c 不走索引排序）　D. `c=3`
**答案：B、C（多选考法：问"哪些能用"，B/C 都能用但 C 的 c 不参与索引过滤/排序）**——最左前缀 + 范围后失效的经典组合。

**D-3（选择）** 两阶段提交的正确顺序？
A. binlog → redo prepare → redo commit　B. redo prepare → binlog → redo commit　C. redo commit → binlog　D. binlog prepare → redo
**答案：B。** 崩溃恢复规则：redo 处于 prepare 且 binlog 完整 → 提交；不完整 → 回滚。

**D-4（选择）** RR 下下列哪个操作不会加间隙锁？
A. `select * from t where id>10 for update`　B. `update t set x=1 where id=10`（id 为主键等值命中）　C. `select ... where id between 10 and 20 for update`　D. `select * from t where name='x' for update`（name 无索引）
**答案：B。** 主键等值命中退化为记录锁；A/C 是范围当前读（Next-Key），D 无索引全表扫加全表间隙锁。

**D-5（简答）** 主从延迟 30 分钟，业务"写后立读"怎么处理？
**答案**：治理（并行复制 writeset）+ 读策略（写后 N 秒/本会话强制走主；关键校验强制主库）+ 监控三级告警；GTID 必开。

**D-6（简答）** 一条 SQL 突然从 10ms 变 3s，排查路径？
**答案**：slow log 确认 → explain（type/key/rows/Extra）→ 统计信息过期（analyze table）→ 锁等待（sys.innodb_lock_waits）→ 优化器选错索引（force index 验证）→ 参数/资源（buffer pool 命中率）。

**D-7（简答）** 数据被误删一行，恢复流程？
**答案**：停写缩小影响面 → 最近全量（XtraBackup）恢复到临时实例 → binlog 回放到误删前一秒 → 按表导回 → 对账。预防：权限分级、高危 SQL 审批、延迟从库、恢复演练（没演练过的备份=没有备份）。

**D-8（简答）** 分库分表的分片键怎么选？订单维度查询怎么办？
**答案**：最高频查询条件（user_id）+ 分布均匀 + 避免跨片事务；订单号用**基因法**内嵌 user 分片位；非分片键查询走异构索引（ES）或二次路由。

---
