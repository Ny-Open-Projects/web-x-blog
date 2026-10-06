# 1244 特殊访问类型：ref_or_null / index_merge / unique_subquery

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：中 | 关键词：**ref_or_null、index_merge、unique_subquery、索引合并、子查询**

> 原文锚点：第 55~80 段「ref_or_null、index_merge 并集、unique_subquery 唯一索引关联」

## 一句话总述
ref_or_null 是 ref 的变体：普通二级索引等值匹配，且该列允许 NULL（既要匹配值又要找 NULL 行）。index_merge 在「多个 OR/AND 条件各自命中不同索引」时合并多个索引（union / intersection / sort-union）以减少回表。unique_subquery 是用唯一索引关联的子查询特例，避免全表扫描。

## 面试官视角
这三种是「进阶识别项」。考官若问到，重点在 index_merge：当 `WHERE k1 = ? OR k2 = ?` 且 k1、k2 各有索引时，优化器把两个索引的结果取并集再回表。能说出「union 取并集、intersection 取交集、sort-union 排序并集」就是加分项。unique_subquery 则体现「子查询用唯一键关联可免全扫」。

## 主问答
**Q（面试官原话）：** index_merge 是什么？什么时候出现？

1. **ref_or_null**：ref 场景下，索引列允许 NULL，需同时取「等值匹配行」与「NULL 行」；如默认值为 NULL 的字段等值查询。
2. **index_merge 触发**：一个查询的多个条件分别适用于不同索引（常见 OR 连接两个有索引的列），优化器合并使用。
3. **三种合并算法**：union（取并集，如 OR）、intersection（取交集，如 AND）、sort-union（先排序再并集，用于无法简单并的情况）。
4. **unique_subquery**：`IN (SELECT 唯一键 ...)` 这类子查询，用唯一索引做关联，避免对子查询表全表扫；EXPLAIN 中 ref 列显示 function。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | index_merge 是什么？ | 说不清多索引合并 |
| L2 | 哪三种算法？ | 说不清 union/intersection |
| L3 | 何时触发？ | 说不清 OR 多索引 |
| L4 | unique_subquery 作用？ | 说不清免全扫 |
| L5 | 怎么制造 index_merge？ | 说不清索引布局 |

## 版本与兼容性
| 类型 | 合并/关联方式 |
|------|--------------|
| ref_or_null | ref + 含 NULL 行 |
| index_merge | union/intersection/sort-union |
| unique_subquery | 唯一索引关联子查询 |

## 关键代码
```sql
-- k1、k2 各有索引
SELECT * FROM t WHERE k1 = 1 OR k2 = 2;     -- index_merge (union)
SELECT * FROM t1 WHERE id IN (SELECT id FROM t2); -- unique_subquery
```

## 总结与追问预判
核心：**ref_or_null=ref+NULL 行；index_merge=多索引合并（union/intersection/sort-union）；unique_subquery=唯一键关联免全扫**。追问常接「索引失效与合并的边界」（见 1244-range-index-all）。

## ⚠️ 原文纠错
1. 事实核校： [经验] ref_or_null 含 NULL 行、index_merge 三算法、unique_subquery 唯一键关联——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/索引/子查询 等音译为崩坏词，且把 union/intersection 等术语拆碎；本卡统一为规范术语。
