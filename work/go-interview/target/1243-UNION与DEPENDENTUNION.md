# 1243 UNION 与 DEPENDENT UNION：临时表与嵌套

> 分类：MySQL 调优 | 难度：中高 | 题型：原理 | 频率：中 | 关键词：**UNION、UNION RESULT、DEPENDENT UNION、临时表、去重**

> 原文锚点：第 96~109 段「union 的 select_type 取值、union result 临时表、子查询内 union 的 dependent union」

## 一句话总述
UNION 查询中：最左边的查询是 PRIMARY，其余是 UNION，去重所用临时表的结果行标记为 UNION RESULT（这就是 EXPLAIN 比表数多一条的原因）。若 UNION 出现在子查询内部，其右侧查询的 select_type 为 DEPENDENT UNION——表示它依赖外层、可能多次执行。UNION ALL 不去重，故不会生成临时表、记录数等于表数。

## 面试官视角
这是 select_type 的进阶分支。考官看你能不能说清：① UNION RESULT 来自「去重临时表」，UNION ALL 没有；② 记录数 = 表数 + 1（临时表）；③ DEPENDENT UNION 是「子查询里的 union」，受外层驱动、可能多次执行。能对比 UNION vs UNION ALL 的执行计划差异最稳。

## 主问答
**Q（面试官原话）：** UNION 的 EXPLAIN 为什么比表数多一条？DEPENDENT UNION 是什么？

1. **UNION RESULT 来历**：UNION 需对多表结果去重，去重借助生成的临时表，该临时表的结果行在计划中标记为 UNION RESULT。
2. **记录数 = 表数 + 1**：如 t1 UNION t2 → 三条记录（t1=PRIMARY、t2=UNION、临时表=UNION RESULT）。
3. **UNION ALL 无临时表**：不去重就不生成临时表，记录数 = 表数，效率通常更高。
4. **DEPENDENT UNION**：当 UNION 位于子查询内部时，其右侧查询 select_type 为 DEPENDENT UNION，依赖外层、可能随外层每行执行。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 多一条原因？ | 说不清临时表 |
| L2 | UNION ALL 差异？ | 说不清不去重 |
| L3 | DEPENDENT UNION？ | 说不清子查询内 union |
| L4 | 为何去重？ | 说不清临时表作用 |
| L5 | 效率建议？ | 说不清能 ALL 就 ALL |

## 版本与兼容性
| 写法 | 临时表 | 记录数 |
|------|--------|--------|
| UNION | 有（去重） | 表数+1 |
| UNION ALL | 无 | 表数 |

## 关键代码
```sql
SELECT * FROM t1 UNION SELECT * FROM t2;            -- 3 条（含 UNION RESULT）
SELECT * FROM t1 UNION ALL SELECT * FROM t2;        -- 2 条（无临时表）
```

## 总结与追问预判
核心：**UNION 因去重临时表多一条(UNION RESULT)；UNION ALL 无临时表；DEPENDENT UNION 是子查询内 union 受外层驱动**。追问可回「select_type 总谱系」（见 1243）。

## ⚠️ 原文纠错
1. 事实核校： [经验] UNION RESULT 来自去重临时表、记录数=表数+1、UNION ALL 无临时表、DEPENDENT UNION 为子查询内 union 受外层驱动——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/EXPLAIN/SELECT/SQL/union/子查询/临时表 等音译为多组崩坏词；本卡统一为规范术语。
