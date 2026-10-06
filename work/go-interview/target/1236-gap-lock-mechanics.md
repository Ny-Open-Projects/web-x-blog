# 1236 间隙锁机制：不互斥与插入意向锁

> 分类：MySQL 锁 | 难度：L4 | 题型：机制题 | 频率：中 | 关键词：**间隙锁不互斥**/**Insert Intention**/**插入意向锁**/**整段锁定**/**开区间**
> 原文锚点：第 72~99 段「间隙锁特性与插入意向锁」

## 一句话总述
间隙锁有几个反直觉特性：**开区间不含边界**、**同一行可同时持有间隙 X 锁与间隙 S 锁（不互斥）**、**锁整段不锁部分**、向已锁间隙插入会出现 **Insert Intention（插入意向锁）** 等待。这些特性共同决定幻读防护的边界。

## 面试官视角
- 考察意图：是否掌握间隙锁「不互斥」这一最易错的点，以及插入意向锁的观察方式。
- 分档：P5 知间隙锁防插入；P6 知开区间、整段锁；P7 知 X/S 间隙锁不互斥、Insert Intention 等待。
- 红旗答案：以为间隙锁像记录锁一样 X/S 互斥；或不知道插入意向锁。
- 惊艳点：点出「同一行可既有间隙 X 又有间隙 S 锁，二者不冲突」的实验现象。

## 主问答
**Q（面试官原话）：** 间隙锁之间会互斥吗？插入被阻塞时怎么看？
**A：**
1. **开区间**：间隙锁不含左右边界记录，只锁断层区间。
2. **不互斥（关键）**：同一行可同时持有**间隙 X 锁**和**间隙 S 锁**——X gap 与 S gap 之间没有互斥关系。实验：事务 A 拿 X gap，事务 B 仍能拿 S gap。
3. **整段锁定**：间隙锁不会只锁一部分，它锁定出现断层的整个间隙（如 5~20 全部锁住，而非 5~10）。
4. **插入意向锁**：当向被锁间隙插入时，加锁信息里出现 `insert intention`（插入意向锁），表示已有插入在该间隙排队等待。
5. **观测手段**：`information_schema.innodb_trx` 看运行事务；`performance_schema.data_locks`（或老版 `show engine innodb status`）看具体锁与等待。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 间隙锁含边界吗？ | 基础 | 不含，开区间 | P5 |
| L2 | 间隙锁会互斥吗？ | 机制 | X/S 间隙锁不互斥 | P6 |
| L3 | 插入被阻塞看到啥？ | 观测 | insert intention 等待 | P6 |
| L4 | 为什么整段锁？ | 原理 | 防间隙内任意插入致幻读 | P7 |
| L5 | 怎么看当前锁？ | 工具 | data_locks / innodb_trx | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.6~8.0 | 5.7 起 data_locks 在 performance_schema | 8.0 用 performance_schema.data_locks；旧版用 show engine innodb status |

## 关键代码
```sql
-- 事务 A 持 X gap，事务 B 持 S gap（可共存），再插入触发 Insert Intention
-- 查看等待
SELECT * FROM performance_schema.data_locks
WHERE LOCK_TYPE='RECORD' AND LOCK_MODE LIKE '%GAP%'\G
-- 期望看到 INSERT_INTENTION 类型的等待记录
```

## 总结与追问预判
间隙锁的「不互斥 + 整段锁 + 插入意向锁」是 InnoDB 幻读防护的精妙处。配合前面等值/范围规则，可完整回答「一个 SQL 到底锁了哪些行」。

## ⚠️ 原文纠错
1. 事实核校： [经验] 间隙锁开区间、X/S 不互斥、整段锁定、Insert Intention 等待、data_locks/innodb_trx 观测——均正确。
2. 崩坏词归一：源码将 间隙锁 正确保留、插入意向锁 音译为 insertintention、意向锁 音译为 意向组、意向共享锁 音译为 读组/意向共享、读锁 音译为 读组、终端 音译为 终态/中单、information_schema.innodb_trx 音译为 schemlDBTRX；MySQL 音译为崩坏词（本卡统一为 MySQL）。
