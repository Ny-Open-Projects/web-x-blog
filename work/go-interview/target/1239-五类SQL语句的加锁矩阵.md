# 1239 五类 SQL 语句的加锁矩阵：从快照读到插入意向锁

> 分类：数据库 / MySQL 锁 | 难度：L4 | 题型：矩阵题 | 频率：高 | 关键词：**MVCC、快照读、IS、IX、S锁、X锁、临键锁、插入意向锁**

> 原文锚点：第 41~49 段「对于普通的 select 语句，InnoDB 引擎采用的是MVCC机制来实现非阻塞读的，所以对于普通的 select 语句 InnoDB 是不加锁的…select … lock in share mode 语句，首先会加表级别的 IS 锁，然后加行级别的共享锁 S，InnoDB 会使用临键锁进行处理，如果扫描发现唯一索引就可以降级为记录锁…select … for update 首先会加表级别的意向排他锁 IX，然后加行级别的排他锁…delete 语句首先会加表级别的 IS 锁，然后加行级别的排他锁…insert 首先会加表级别的 IS 锁，也就是表级别的意向排他锁，如果其他事务已经插入了相同的ID数据，还会加入插入意向锁」

## 一句话总述
五类语句的加锁可以归成一张矩阵：**普通 `SELECT` 靠 MVCC 不加锁**；`SELECT ... LOCK IN SHARE MODE` 加**表级 IS + 行级 S**；`SELECT ... FOR UPDATE` 加**表级 IX + 行级 X**；`DELETE` 加**表级 IX + 行级 X**；`INSERT` 加**表级 IX**，若其他事务已插入相同 ID 则再加**插入意向锁**。行级锁**默认都是临键锁**，**扫描到唯一索引时降级为记录锁**。

## 面试官视角
- 考察意图：能否把"读/写语句各自加什么锁"系统化，而不是孤立地背 `FOR UPDATE` 加 X 锁。
- 分档：P5 知道 `FOR UPDATE` 加排他锁；P6 能说清**表级意向锁 + 行级锁**两层；P7 能补上**普通 SELECT 走 MVCC 不加锁**、**行级默认临键锁遇唯一降级**，以及 **`DELETE` 配的是 IX 而不是 IS**。
- 红旗答案：说 `DELETE` 加 IS 锁——**排他锁对应的表级意向锁是 IX**，IS 只与共享锁配套。
- 惊艳点：**意向锁是"表级"的，但它不锁表**——它只是告诉其他事务"这张表里有行被锁了"，用来快速判断表级锁冲突 `[源码]`。

## 主问答
**Q（面试官原话）：** `SELECT`、`SELECT ... FOR UPDATE`、`DELETE`、`INSERT` 分别加什么锁？

1. **结论**：普通 `SELECT` **不加锁**（走 MVCC）；锁定读与写操作都是"**表级意向锁 + 行级锁**"两层结构，行级**默认临键锁**、**遇唯一索引降级为记录锁** `[源码]`。
2. **普通 `SELECT`**：对于普通 `SELECT` 语句，InnoDB 采用 **MVCC 机制实现非阻塞读**，所以**不加锁** `[源码]`。
3. **`SELECT ... LOCK IN SHARE MODE`**：首先加**表级别的 IS 锁（意向共享锁）**，然后加**行级别的共享锁 S**；InnoDB 会用**临键锁**处理，**若扫描发现唯一索引则可降级为记录锁** `[源码]`。（8.0 起等价写法为 `SELECT ... FOR SHARE`。）
4. **`SELECT ... FOR UPDATE`**：首先加**表级别的意向排他锁 IX**，然后加**行级别的排他锁 X**；行级排他锁**默认使用临键锁**，**扫描发现唯一索引也可降级为记录锁** `[源码]`。
5. **`DELETE`**：首先加**表级别的 IX 锁**（意向排他锁），然后加**行级别的排他锁**；同样**默认用临键锁加锁，遇唯一索引降级为记录锁** `[源码]`。
6. **`INSERT`**：加**表级别的 IX 锁**；**如果其他事务已经插入了相同的 ID 数据，还会加入插入意向锁** `[源码]`——插入意向锁是一种**间隙锁**，多个事务插入**不同**位置时可以并发，只有插入**同一间隙的同一位置**才冲突。

**加分层：** 记法——**共享 → IS，排他 → IX**；行级锁一律**先按临键锁给、再按唯一索引降级**。这样五类语句就只需记"表级意向 + 行级模式"两个维度。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 普通 SELECT 加锁吗？ | 答不出靠 MVCC 不加锁 |
| L2 | FOR UPDATE 加什么？ | 答不出 IX + X |
| L3 | LOCK IN SHARE MODE 呢？ | 答不出 IS + S |
| L4 | DELETE 的表级意向锁是？ | 答不出 IX（答 IS 即错） |
| L5 | INSERT 什么时候加插入意向锁？ | 答不出有相同 ID 已插入 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 8.0 起 | 新增 `FOR SHARE` | `LOCK IN SHARE MODE` 仍兼容，推荐 `FOR SHARE` |
| RR（默认） | 行级默认临键锁 | 遇唯一索引降级为记录锁 |
| RC | 无间隙锁 | 行级只剩记录锁 |
| 所有版本 | 意向锁为表级 | 只做冲突判定，不阻塞行 |

## 关键代码
```sql
-- 1) 普通 SELECT：MVCC 快照读，不加锁（RR 下）
START TRANSACTION;
SELECT * FROM userbig WHERE id = 10;              -- 无锁
-- performance_schema.data_locks 中不会出现对应行锁

-- 2) LOCK IN SHARE MODE：表级 IS + 行级 S（8.0 可用 FOR SHARE）
START TRANSACTION;
SELECT * FROM userbig WHERE id = 10 LOCK IN SHARE MODE;
-- lock_mode 期望：S, REC_NOT_GAP（唯一索引命中，降级）

-- 3) FOR UPDATE：表级 IX + 行级 X
START TRANSACTION;
SELECT * FROM userbig WHERE id = 10 FOR UPDATE;
-- lock_mode 期望：X, REC_NOT_GAP

-- 4) DELETE：表级 IX + 行级 X（不是 IS！）
START TRANSACTION;
DELETE FROM userbig WHERE id = 10;

-- 5) INSERT：表级 IX；同 ID 已存在时再加插入意向锁
START TRANSACTION;
INSERT INTO userbig (id, name) VALUES (10, 'name10');

-- 6) 观察当前加锁
SELECT object_name, index_name, lock_type, lock_mode, lock_data
FROM performance_schema.data_locks WHERE object_name = 'userbig'\G
```

## 总结与追问预判
**最常见的追问是"意向锁有什么用"**——它是**表级**标记，用于**快速判断表锁与行锁是否冲突**：事务想加表级 S/X 锁时，只需看表上有没有相斥的意向锁，不必逐行检查。因此 **IS 与 IX 之间互相兼容**（都只是"表内有行被锁"的声明），冲突只发生在**表级 S/X 与相斥意向锁**之间。追问常接"`DELETE` 的表级锁是 IS 还是 IX"——**是 IX**，因为行级加的是排他锁。

## ⚠️ 原文纠错
1. 事实核校：普通 SELECT 走 MVCC 不加锁、`LOCK IN SHARE MODE` 加表级 IS + 行级 S、`FOR UPDATE` 加表级 IX + 行级 X、`INSERT` 在已有相同 ID 时加插入意向锁、行级默认临键锁且遇唯一索引降级——均与 InnoDB 实现一致 `[经验]`。
2. 补充：**原文第 47 段称 `DELETE` "首先会加表级别的 IS 锁，然后加行级别的排他锁"，应为 IX（意向排他锁）**——排他锁对应的表级意向锁是 IX，IS 只与共享锁配套；**第 49 段称 `INSERT` 加"表级别的 IS 锁，也就是表级别的意向排他锁"自相矛盾，正确为 IX** `[经验]`。
3. 崩坏词归一：源码将意向锁、临键锁、排他锁、共享锁、MVCC、InnoDB 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
