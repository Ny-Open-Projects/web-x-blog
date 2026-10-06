# 1208 两阶段提交保证 redo 与 binlog 一致

> 分类：MySQL 内核 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**两阶段提交**/**redo log**/**binlog**
> 原文锚点：第 1~15 段「宕机场景推演…redo 与 binlog 一致性」

## 一句话总述
MySQL 用两阶段提交（2PC）对齐 redo log 与 binlog：prepare 阶段写 redo（含 XID）、commit 阶段先写 binlog 再写 redo 的 commit 标记；崩溃恢复时以 binlog 中是否存在该 XID 决定重放还是回滚，从而保证二者一致。

## 面试官视角
- 考察意图：是否真懂"为什么需要 2PC"以及崩溃恢复的判定逻辑。
- 分档：P5 知有 redo/binlog 两个日志；P6 懂 2PC 三步与 XID；P7 能讲清"恢复时以 binlog 为准"的判定。
- 红旗答案：以为 binlog 先于 redo 写；说不清崩溃后怎么决定提交还是回滚。
- 惊艳点：**恢复判据只看 binlog 是否含该事务 XID**——有则补 commit 重放，无则回滚，binlog 成为"真相源" `[经验]`。

## 主问答
**Q（面试官原话）：** 为什么 redo 和 binlog 要用两阶段提交？怎么保证一致？
**A：**
1. **结论**：redo 保证崩溃后 InnoDB 数据不丢，binlog 供主从复制与时间点恢复；二者必须一致，否则主库恢复后数据与从库/备份对不上，故用 2PC 协调。
2. **机制**：① prepare：写 redo（状态 prepare，带 XID）落盘；② write binlog：binlog（含同一 XID）落盘；③ commit：redo 写 commit 标记（end）。崩溃恢复时：若 redo 为 prepare 且 binlog 有该 XID → 提交重放；若 binlog 无该 XID → 回滚 `[经验]`。
3. **边界**：2PC 解决"两个日志都写或都不写"的原子性，不解决主从网络延迟；binlog 落盘时机由 `sync_binlog` 控制。

**加分层：** 这就是为什么 `innodb_flush_log_at_trx_commit=1` 且 `sync_binlog=1`（双 1）才能做到不丢事务——两者任一不 fsync 都可能丢。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | redo/binlog 区别？ | 基础 | 崩溃恢复 vs 复制 | P5 |
| L2 | 2PC 几步？ | 机制 | prepare→binlog→commit | P6 |
| L3 | XID 干嘛用？ | 关联 | 关联两日志的事务 | P6 |
| L4 | 崩溃怎么恢复？ | 判据 | 看 binlog 有无 XID | P7 |
| L5 | 双 1 是什么？ | 进阶 | 不丢事务的 fsync 配置 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.6+ | 早期无 XID 关联易不一致 | 答"prepare→binlog→commit，恢复以 binlog XID 为准" |

## 关键代码
```sql
-- 双 1 配置（事务不丢的基线）
SET GLOBAL innodb_flush_log_at_trx_commit = 1;  -- redo 每次提交 fsync
SET GLOBAL sync_binlog = 1;                     -- binlog 每次提交 fsync
```

## 总结与追问预判
2PC 用 XID 把 redo/binlog 绑成原子；恢复以 binlog 为准。追问接"binlog 三种格式与主从复制"。

## ⚠️ 原文纠错
1. 原文两阶段提交的推演与结论正确，但**全程使用机翻崩坏词**：如 `callme`→commit、`REOOG`/`readadlog`→redo log、`RBlog`/`beillog`/`billog`/`BEOOG`/`blogg`→binlog、`TSID`→事务 XID（trx_id）。本卡正文已归一为 redo log / binlog / XID，崩坏词为语音转写噪声，不影响事实正确性 `[经验]`。
