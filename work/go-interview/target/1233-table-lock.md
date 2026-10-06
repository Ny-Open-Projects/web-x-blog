# 1233 表锁（Table Lock）

> 分类：MySQL 锁 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**LOCK TABLES**/**UNLOCK TABLES**/**metadata_locks**
> 原文锚点：第 41~79 段「表锁机制与查看」

## 一句话总述
表锁是 MySQL 最基础、开销最小的锁，锁定整张表；InnoDB 中手动 `LOCK TABLES` 是 server 层锁，会阻塞行锁，应尽量避免。

## 面试官视角
- 考察意图：常问"表锁怎么加、怎么看、和行锁怎么互相影响"。
- 分档：P5 知 LOCK TABLES 整表锁；P6 知 SHOW OPEN TABLES 只看是否锁；P7 知 metadata_locks 看类型。
- 红旗答案：以为表锁和行锁互不干扰。
- 惊艳点：点出 InnoDB 上表锁会阻塞行锁、降并发。

## 主问答
**Q（面试官原话）：** 怎么给表加锁、怎么看锁状态？
**A：**
1. **加/解锁**：`LOCK TABLES t READ`（共享读锁）、`LOCK TABLES t WRITE`（排他写锁）；`UNLOCK TABLES` 释放全部表锁；会话退出自动释放。
2. **READ LOCAL 变体**：写锁队列与读锁队列分离，写队列优先级绝对高于读，支持特定并发读写。
3. **查看锁状态**：`SHOW OPEN TABLES LIKE 't'` 的 `In_use=1` 仅表示"已上锁"，**不能看类型**；类型查 `performance_schema.metadata_locks`（8.0）或 `information_schema`（低版本），如 `SHARED_READ_ONLY`。
4. **与行锁互斥**：表锁 S 阻塞表锁 X 与行锁 S/X；表锁 X 阻塞行锁 S/X 且阻塞当前事务后续读写——InnoDB 表少用 `LOCK TABLES`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么加读/写锁？ | 基础 | LOCK TABLES t READ / WRITE | P5 |
| L2 | In_use=1 说明什么？ | 细节 | 仅"已上锁"不含类型 | P6 |
| L3 | 看锁类型查哪？ | 工具 | performance_schema.metadata_locks（8.0） | P7 |
| L4 | 表锁影响行锁吗？ | 区分 | 会，表锁阻塞行锁 S/X | P7 |
| L5 | InnoDB 为何少用 LOCK TABLES？ | 权衡 | 阻塞行锁、降并发 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.5+ | 8.0 锁信息移至 performance_schema | 8.0 查 performance_schema.metadata_locks；低版本查 information_schema |

## 关键代码
```sql
LOCK TABLES t READ;
SHOW OPEN TABLES LIKE 't';   -- In_use=1 表示已锁
UNLOCK TABLES;
```

## 总结与追问预判
表锁整表锁定、开销小但并发低；`SHOW OPEN TABLES` 只看是否锁、`metadata_locks` 看类型；InnoDB 上行锁与表锁互斥，慎用 `LOCK TABLES`。

## ⚠️ 原文纠错
1. 事实核校： [经验]LOCK TABLES READ/WRITE、UNLOCK 释放、会话退出自动释放、SHOW OPEN TABLES 的 In_use 不看类型、8.0 查 performance_schema.metadata_locks，均正确。
2. 崩坏词归一：soopentableslike→SHOW OPEN TABLES LIKE、performancescheml/performancedemo→performance_schema、MADAAAOS→metadata_locks、looktype→lock_type、shareadonly→SHARED_READ_ONLY、inuse→In_use、logtables→LOCK TABLES、绘画推出→会话退出、指印→（代词）。
