# 1243 EXPLAIN 的 select_type：查询类型谱系

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**select_type、simple、primary、subquery、union、derived、查询类型**

> 原文锚点：第 65~99 段「simple/primary/subquery/union/union result 等 select_type 取值」

## 一句话总述
select_type 描述「每个 SELECT 的类型」：SIMPLE（无 union/子查询）、PRIMARY（复杂查询最外层主查询）、SUBQUERY（子查询，可被物化）、DEPENDENT SUBQUERY（依赖外层、可能执行多次）、UNION（union 中除最左外的查询）、UNION RESULT（union 临时表结果行）、DERIVED（物化派生表）等。它配合 id 一起揭示查询拓扑。

## 面试官视角
select_type 与 id 是一对。考官期待你列出常见取值并讲清 PRIMARY/SUBQUERY/DEPENDENT SUBQUERY 的区别，以及 UNION RESULT 的来历。能补 DERIVED（物化子查询生成的派生表）说明你见过复杂 SQL 的执行计划。

## 主问答
**Q（面试官原话）：** select_type 有哪些常见值？分别代表什么？

1. **SIMPLE**：不含 union 也不含子查询的查询（单表或 join 都算 simple）。
2. **PRIMARY**：含 union/子查询的复杂查询中，最左边的主查询。
3. **SUBQUERY / DEPENDENT SUBQUERY**：SUBQUERY 指子查询可被物化（只执行一次）；DEPENDENT SUBQUERY 指非物化、依赖外层、可能每行执行一次。
4. **UNION / UNION RESULT**：union 中除最左外的查询为 UNION；union 去重用的临时表结果行标记为 UNION RESULT。
5. **DERIVED**：子查询被物化成派生表（FROM 子查询）时的类型。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 常见取值？ | 说不全 |
| L2 | PRIMARY 是谁？ | 说不清最左主查询 |
| L3 | SUBQUERY vs DEPENDENT？ | 说不清物化与否 |
| L4 | UNION RESULT？ | 说不清临时表 |
| L5 | DERIVED？ | 说不清派生表 |

## 版本与兼容性
| select_type | 含义 |
|------|------|
| SIMPLE | 无 union/子查询 |
| PRIMARY | 主查询 |
| SUBQUERY | 物化子查询 |
| DEPENDENT SUBQUERY | 非物化子查询 |
| UNION RESULT | union 临时表 |

## 关键代码
```sql
EXPLAIN SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);  -- 子查询改写后同 id
```

## 总结与追问预判
核心：**select_type 谱系：SIMPLE/PRIMARY/SUBQUERY(物化)/DEPENDENT SUBQUERY(非物化)/UNION/UNION RESULT/DERIVED，配合 id 读拓扑**。追问常接「物化子查询细节」（见 1243）。

## ⚠️ 原文纠错
1. 事实核校： [经验] select_type 各取值语义（SIMPLE/PRIMARY/SUBQUERY/DEPENDENT SUBQUERY/UNION/UNION RESULT/DERIVED）——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/EXPLAIN/SELECT/SQL/子查询/union/物化 等音译为多组崩坏词；本卡统一为规范术语。
