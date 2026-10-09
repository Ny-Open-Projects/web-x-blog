# 1240 锁信息从哪查：8.0 与 5.7 的视图切换

> 分类：数据库 / MySQL 锁 | 难度：L4 | 题型：记忆题 | 频率：高 | 关键词：**data_locks、data_lock_waits、metadata_locks、innodb_trx、performance_schema**

> 原文锚点：第 30~42 段「show open tables 有两个关键字段，一个是 In_use…Name_locked 一般发生在使用 drop 或者 rename 命令操作这张表的时候…8.0 之前需要查 information_schema 下的 innodb_locks，从 8.0 版本开始需要查 performance_schema 下面的 data_locks…通过 data_lock_waits 查看当前正在等待的锁…在 performance_schema 里面通过 metadata_locks 查看元数据锁」

## 一句话总述
查锁有五张「仪表盘」：`SHOW OPEN TABLES` 看表级占用、`SHOW ENGINE INNODB STATUS` 看死锁日志、`information_schema.INNODB_TRX` 看活跃事务、8.0 起用 `performance_schema.data_locks` / `data_lock_waits` 看行锁与等待、`metadata_locks` 看元数据锁。

## 面试官视角
P6 知道 `SHOW ENGINE INNODB STATUS`；P7 必须说清 **8.0 的视图迁移**——老的 `information_schema.INNODB_LOCKS` / `INNODB_LOCK_WAITS` 在 8.0 被 `performance_schema.data_locks` / `data_lock_waits` 取代，答错版本等于没答。

## 主问答
**Q（面试官原话）：** 我想知道现在谁锁了哪一行、谁在等谁，该查什么？

1. **表级占用**：`SHOW OPEN TABLES` 的 `In_use` 大于 0 表示表正被使用/锁定；`Name_locked` 表示表名被锁，常见于执行 DROP 或 RENAME 时 `[源码]`。
2. **死锁日志**：`SHOW ENGINE INNODB STATUS` 输出事务与日志信息，发生死锁后其中有**详细的死锁日志** `[源码]`。
3. **活跃事务**：`information_schema.INNODB_TRX` 可看到当前正在执行的事务 `[源码]`。
4. **行锁明细（8.0+）**：`performance_schema.data_locks` 显示**加锁类型、被锁的具体数据、加锁状态** `[源码]`。
5. **版本切换**：8.0 之前查 `information_schema.INNODB_LOCKS`；8.0 起查 `performance_schema.data_locks` `[源码]`。
6. **锁等待（8.0+）**：`performance_schema.data_lock_waits` 查看当前正在等待的锁，无等待则不输出；8.0 之前对应 `INNODB_LOCK_WAITS` `[源码]`。
7. **元数据锁**：`performance_schema.metadata_locks` 查看 MDL 的加锁对象，如表或函数 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 看表是否被锁用什么？ | 答不出 SHOW OPEN TABLES |
| L2 | 死锁日志在哪看？ | 答不出 SHOW ENGINE INNODB STATUS |
| L3 | 活跃事务查哪张表？ | 答不出 INNODB_TRX |
| L4 | 8.0 看行锁查什么？ | 答不出 data_locks |
| L5 | 8.0 之前呢？ | 答不出 INNODB_LOCKS |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 8.0 起 | 视图迁移 | 用 data_locks / data_lock_waits |
| 8.0 之前 | 仍用旧表 | information_schema.INNODB_LOCKS / INNODB_LOCK_WAITS |
| 5.7 起 | 部分迁 performance_schema | 需在 my.cnf 开启对应 consumer |
| 所有版本 | 死锁日志 | SHOW ENGINE INNODB STATUS 通用 |

## 关键代码
```sql
-- 表级占用：In_use>0 表示被使用，Name_locked 表示表名被锁（DROP/RENAME 场景）
SHOW OPEN TABLES WHERE In_use > 0;

-- 当前正在执行的事务
SELECT * FROM information_schema.INNODB_TRX\G

-- MySQL 8.0：行锁明细（加锁类型、被锁数据、状态）
SELECT * FROM performance_schema.data_locks\G

-- MySQL 8.0：谁在等谁
SELECT * FROM performance_schema.data_lock_waits\G

-- MySQL 8.0：元数据锁及加锁对象
SELECT * FROM performance_schema.metadata_locks\G

-- 死锁日志（含最近一次死锁详情）
SHOW ENGINE INNODB STATUS\G
```

## 总结与追问预判
**记牢一条主线：8.0 是分水岭，行锁相关视图从 information_schema 迁到 performance_schema**。面试官常追问「5.7 和 8.0 查锁语句有什么区别」，答出这对迁移即可拿满分。查到等待后如何优化，见同批 1240-lock-optimization。

## ⚠️ 原文纠错
1. 事实核校：In_use 与 Name_locked 含义、DROP/RENAME 触发表名锁、死锁日志位置、INNODB_TRX 查活跃事务、8.0 视图迁移与旧版对应关系——均与 MySQL 官方手册一致 `[经验]`。
2. 补充：8.0 的 performance_schema 相关表需要对应 consumer 处于开启状态才可采集，排查前应先确认配置，避免「查得到表但没数据」 `[经验]`。
3. 崩坏词归一：源码将系统库名、表名与锁类型关键字音译为多组崩坏词，本卡统一为规范写法 `[经验]`。
