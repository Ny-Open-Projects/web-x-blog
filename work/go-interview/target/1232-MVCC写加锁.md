# 1232 MVCC + 写加锁：读写不冲突的方案

> 分类：数据库 / MySQL 锁 | 难度：L4 | 题型：原理题 | 频率：极高 | 关键词：**MVCC、readview、undo log、快照读、当前读、RC vs RR**

> 原文锚点：第 57~74 段「读用 MVCC 写加锁…readview 找可见版本，历史版本由 undo log 构建…活跃事务最小 ID 与行隐藏事务 ID 比较…RC 每次生成 readview、RR 首次生成复用」

## 一句话总述
更优方案是「读用 MVCC、写加锁」：读走快照（历史版本由 undo log 构建，不阻塞写），写加锁防脏写。快照可见性靠 readview 比对事务 ID 实现；RC 每次查询新建 readview，RR 复用首次的 readview。

## 面试官视角
P6 能说出 MVCC 读不阻塞写；P7 要讲清 readview 的生成时机差异（RC 每次 / RR 首次复用）正是「不可重复读」与「可重复读」的分界，以及快照读 vs 当前读。

## 主问答
**Q（面试官原话）：** 为什么 MVCC 下读写不冲突？RC 和 RR 区别？

1. **读写分离**：读走历史版本（undo log 构建），写改最新版，二者不冲突，只有写写仍需加锁 `[源码]`。
2. **可见性判据**：readview 记录活跃事务列表，比较行隐藏事务 ID 与活跃最小 ID 决定版本是否可见 `[源码]`。
3. **RC 每次新建**：读已提交每次查询都新建 readview，故能读到别的事务已提交的新值 → 不可重复读 `[源码]`。
4. **RR 复用**：可重复读只在首次查询建 readview 并复用，后续读到同一快照 → 可重复读 `[源码]`。
5. **快照读 vs 当前读**：普通 select 是快照读；`select ... for update` 是当前读，仍要加锁防幻读 `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 为何不冲突？ | 答不出快照/最新分离 |
| L2 | 可见性？ | 说不出 readview 比 ID |
| L3 | RC vs RR？ | 答不出 readview 时机 |
| L4 | 快照读定义？ | 答不出普通 select |
| L5 | 当前读？ | 答不出 for update 加锁 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| InnoDB 全版本 | MVCC 内置 | RR 默认开启 |
| MySQL 8.0 | 隐藏事务 ID | 行含 DB_TRX_ID |
| 任意版本 | 当前读加锁 | for update/lock in share |

## 关键代码
```sql
-- RR 下快照读（不阻塞写）
SELECT * FROM t WHERE id=1;
-- 当前读：加锁，防幻读/防改
SELECT * FROM t WHERE id=1 FOR UPDATE;
```

## 总结与追问预判
**MVCC 是「读写不冲突」的核心**。回到锁全景——见同批 1232-lock-types 与 1232-lock-structure。

## ⚠️ 原文纠错
1. 事实核校：MVCC 读写分离、readview 比对事务 ID、RC 每次建/RR 复用、快照读 vs 当前读——均准确 `[经验]`。
2. 补充：原文说 RR「避免幻读」，精确是 RR 快照读避免，但当前读（for update）才真正防幻读，间隙锁在下批 `[经验]`。
3. 崩坏词归一：源码将 MySQL、InnoDB、事务、MVCC、undo log、索引等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
