# 1243 EXPLAIN 的 id 列：执行顺序怎么读

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**id 列、SELECT 关键字、驱动表、join、子查询、union**

> 原文锚点：第 20~65 段「建表造数、join 同 id、子查询异 id、子查询改 join、union 多一条临时表记录」

## 一句话总述
id 列给每个 SELECT 关键字编号：一条 SQL 只有一个 SELECT → 所有表同 id；join 查询涉及多表但同属一个 SELECT → 同 id、多条记录（前表驱动、后表被驱动）；含子查询且未被改写 → 多个 SELECT → 不同 id；union 因生成临时表会多一条记录（id 1,2,3…）。优化器也可能把子查询重写成 join，使原本不同的 id 变成相同。

## 面试官视角
id 列是理解「执行顺序」的钥匙。考官看你能不能说清：① 同 id 多记录 = 同一 SELECT 下的多表（join）；② 不同 id = 多个 SELECT（子查询/union）；③ union 比表面多一条（临时表）；④ 优化器可能把子查询改写成 join，让 id 合并。能举例 t1 join t2、union 三记录最稳。

## 主问答
**Q（面试官原话）：** EXPLAIN 的 id 列怎么看执行顺序？

1. **单 SELECT 同 id**：无论涉及多少表（join），只要一个 SELECT 关键字，id 全相同，每条表一条记录。
2. **多 SELECT 异 id**：子查询含多个 SELECT，主查询 id=1、子查询 id=2；id 越大越先执行（嵌套由内而外）。
3. **join 的驱动/被驱动**：同 id 时，记录靠前的表是驱动表，靠后的是被驱动表。
4. **union 多一条**：union 除各表外，还会生成临时表做去重，故记录数 = 表数 + 1（临时表行 id 递增）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | id 相同意味？ | 说不清同 SELECT |
| L2 | id 不同意味？ | 说不清多 SELECT |
| L3 | union 多一条？ | 说不清临时表 |
| L4 | 驱动表判定？ | 说不清记录顺序 |
| L5 | 子查询改 join？ | 说不清优化器改写 |

## 版本与兼容性
| 场景 | id 特征 |
|------|---------|
| join | 同 id 多记录 |
| 子查询 | 异 id |
| union | 表数+1 条 |

## 关键代码
```sql
EXPLAIN SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);  -- 子查询改写后同 id
EXPLAIN SELECT * FROM t1 UNION SELECT * FROM t2;            -- 3 条记录(含临时表)
```

## 总结与追问预判
核心：**id 同 = 同 SELECT 多表(join)；id 异 = 多 SELECT(子查询/union)；union 多一条临时表记录；优化器可改写子查询合并 id**。追问常接「select_type 怎么配合」（见 1243-select-type）。

## ⚠️ 原文纠错
1. 事实核校： [经验] id 标识 SELECT 关键字、join 同 id、子查询异 id、union 临时表多一条、优化器改写子查询合并 id——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/索引/EXPLAIN/SELECT/SQL/子查询/连接查询 等音译为多组崩坏词；本卡统一为规范术语。
