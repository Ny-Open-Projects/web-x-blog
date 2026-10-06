# 1245 EXPLAIN Extra（上）：常用标记

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**Extra、Using index、Using index condition、Using where、Impossible WHERE**

> 原文锚点：第 45~59 段「Extra 定义、No tables used、Impossible WHERE、Using index、ICP、Using where」

## 一句话总述
`Extra` 展示执行计划的补充信息，帮助理解 MySQL 究竟怎么执行。常用标记：`No tables used`（无 FROM 子句）、`Impossible WHERE`（WHERE 恒假，如 1=2）、`Using index`（覆盖索引，无需回表）、`Using index condition`（**索引下推 ICP**，5.6+，先用索引条件过滤再回表，减少回表次数）、`Using where`（server 层拿到记录后再按 WHERE 过滤）。

## 面试官视角
Extra 是调优实战的高频列。考官期待你讲清 `Using index`（覆盖）与 `Using index condition`（下推）的区别——前者完全不回表，后者先过滤再回表、减少回表量。能补「ICP 是 5.6 引入」和「Using where 只是提示会用 WHERE 过滤，常出现在无法走索引时」更完整。

## 主问答
**Q（面试官原话）：** Extra 里的 Using index 和 Using index condition 有什么区别？

1. **Using index（覆盖索引）**：查询列都在索引中，扫描索引即得结果，**完全无需回表**。
2. **Using index condition（索引下推 ICP）**：5.6 引入；先用索引中的条件过滤，再拿过滤后的结果回表取其他字段，**大幅减少回表次数**。
3. **Using where**：存储引擎返回记录后，server 层再用 WHERE 条件做后过滤；通常出现在不能走索引、或条件不在索引中的场景，只是提示性信息。
4. **其他两个**：`No tables used` 表示查询没有 FROM 子句；`Impossible WHERE` 表示 WHERE 条件恒不成立（如 `1=2`）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | Using index 含义？ | 说不清覆盖不回表 |
| L2 | ICP 是什么？ | 说不清先过滤后回表 |
| L3 | 两者区别？ | 混淆覆盖与下推 |
| L4 | ICP 哪个版本？ | 说不清 5.6 |
| L5 | Using where？ | 说不清 server 层后过滤 |

## 版本与兼容性
| Extra | 含义 |
|------|------|
| Using index | 覆盖索引，不回表 |
| Using index condition | ICP，5.6+ |
| Using where | server 层后过滤 |

## 关键代码
```sql
-- ICP：先按索引过滤 100<k2<200，再回表取其他字段
SELECT * FROM t WHERE k2 > 100 AND k2 < 200;
```

## 总结与追问预判
核心：**Using index=不回表；Using index condition=ICP 先过滤再回表(5.6+)；Using where=server 层后过滤**。追问常接「Extra 进阶标记」（见 1245-extra-advanced）。

## ⚠️ 原文纠错
1. 事实核校： [经验] Extra 各标记语义（No tables used / Impossible WHERE / Using index 覆盖 / Using index condition ICP 5.6+ / Using where 后过滤）——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/EXPLAIN/索引/回表/连接查询 等音译为多组崩坏词；本卡统一为规范术语。
