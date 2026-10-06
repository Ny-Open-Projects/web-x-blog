# 1231 ReadView 与 RC/RR 的生成时机差异

> 分类：MySQL 事务 | 难度：中高 | 题型：原理 | 频率：高 | 关键词：**ReadView、一致性视图、RC、RR、快照读、事务启动时机**

> 原文锚点：第 29~35 段、第 86~89 段「RC 每语句生成、RR 启动时生成一次、事务真正启动的两种方式」

## 一句话总述
读已提交（RC）与可重复读（RR）都靠一致性视图 ReadView 实现，**唯一区别是生成时机**：RC 在事务内**每条语句执行前**都重新生成一个 ReadView，故同一事务两次读可能不一致；RR 只在**事务启动时**生成一次并全程复用，故事务期间读到的数据恒为启动时刻的快照。

## 面试官视角
「RC 与 RR 的实现差异」是必考题，答案就是 ReadView 生成时机。高分还要补：**BEGIN/START TRANSACTION 并不立即启动事务**，要等到第一条操作 InnoDB 表的语句才真正启动；想立即启动需用 `START TRANSACTION WITH CONSISTENT SNAPSHOT`。

## 主问答
**Q（面试官原话）：** RC 和 RR 在 MVCC 实现上有什么区别？

1. **共同点**：两者都通过 ReadView（一致性视图）判断版本可见性，视图记录「当前所有活跃事务 ID 列表」。
2. **RC 时机**：事务中**每个 SQL 语句执行前**都重新生成一个 ReadView → 期间别的事务提交修改后，本事务再读会看到新数据（不可重复读）。
3. **RR 时机**：仅在**事务启动时**生成一个 ReadView，整个事务期间复用 → 事务内读到的一直是启动时刻的快照（可重复读）。
4. **启动事务的真正时机**：`BEGIN`/`START TRANSACTION` 本身**不启动事务**，要等第一条操作 InnoDB 表的语句；`START TRANSACTION WITH CONSISTENT SNAPSHOT` 才立即启动。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 两者差异？ | 说不清生成时机 |
| L2 | RC 几次生成？ | 说不清每语句 |
| L3 | RR 几次？ | 说不清一次 |
| L4 | BEGIN 即启动？ | 说不清延迟启动 |
| L5 | 立即启动方式？ | 说不清 WITH SNAPSHOT |

## 版本与兼容性
| 隔离级别 | ReadView 生成 |
|----------|---------------|
| RC | 每语句前重新生成 |
| RR | 事务启动时生成一次 |

## 关键代码
```sql
START TRANSACTION WITH CONSISTENT SNAPSHOT;  -- 立即启动事务并建 ReadView
```

## 总结与追问预判
核心：**RC 每语句新建 ReadView、RR 仅启动时建一次；BEGIN 不立即启动事务**。追问常接「可见性怎么判」（见 1231-visibility）。

## ⚠️ 原文纠错
1. 事实核校： [经验] RC/RR 均靠 ReadView、生成时机差异（每语句 vs 启动一次）、BEGIN 不立即启动事务需首条 InnoDB 语句、WITH CONSISTENT SNAPSHOT 立即启动——均正确，本卡为准。
2. 崩坏词归一：源码将 InnoDB/ReadView/事务/隔离级别/SQL 等音译为多组崩坏词；本卡统一为规范术语。
