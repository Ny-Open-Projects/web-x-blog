# 1243 EXPLAIN 各列总览

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**EXPLAIN、执行计划、id、select_type、type、key、rows、Extra**

> 原文锚点：第 1~19 段「EXPLAIN 输出各列含义一览」

## 一句话总述
EXPLAIN 在不执行 SQL 的情况下输出「执行计划」，各列含义：id（每个 SELECT 关键字的编号）、select_type（查询类型）、table（表名）、partitions（分区）、type（单表访问方法）、possible_keys（可能用到的索引）、key（实际用到的索引）、key_len（实际使用索引长度）、ref（与索引等值匹配的对象）、rows（预估读取行数）、filtered（过滤后剩余百分比）、Extra（额外信息）。

## 面试官视角
EXPLAIN 是调优第一工具。考官看你能不能把关键列串起来讲：id 看执行顺序、type 看访问方法快慢、key/possible_keys 看索引命中、rows 看扫描量、Extra 看是否用覆盖/临时表/文件排序。能点出「key_len 在多列索引下标识实际用到多长」是细节加分。

## 主问答
**Q（面试官原话）：** EXPLAIN 输出有哪些重要列？分别代表什么？

1. **id / select_type / table**：id 标识 SELECT 关键字；select_type 是查询类型（simple/primary/subquery…）；table 是涉及表。
2. **type / possible_keys / key**：type 是单表访问方法（越快越好）；possible_keys 是候选索引；key 是实际选用的索引。
3. **key_len / ref / rows**：key_len 标识实际用到的索引长度（多列索引下看命中几列）；ref 是与索引等值匹配的对象；rows 是预估读取行数。
4. **filtered / Extra**：filtered 是过滤后剩余记录百分比；Extra 是补充信息（如 Using index、Using temporary、Using filesort）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 有哪些列？ | 说不全关键列 |
| L2 | id 作用？ | 说不清执行顺序 |
| L3 | key_len 含义？ | 说不清索引长度 |
| L4 | rows 意义？ | 说不清预估行数 |
| L5 | Extra 看什么？ | 说不清覆盖/临时表 |

## 版本与兼容性
| 列 | 含义 |
|------|------|
| type | 单表访问方法 |
| key | 实际索引 |
| rows | 预估扫描行 |

## 关键代码
```sql
EXPLAIN SELECT * FROM t1 INNER JOIN t2 ON t1.id = t2.id;
```

## 总结与追问预判
核心：**EXPLAIN 关键列 = id(顺序)/type(访问方法)/key(实际索引)/rows(扫描量)/Extra(补充)**。追问常接「id 列怎么读」（见 1243-id-column）或「select_type 有哪些」（见 1243-select-type）。

## ⚠️ 原文纠错
1. 事实核校： [经验] EXPLAIN 各列含义（id/select_type/table/type/possible_keys/key/key_len/ref/rows/filtered/Extra）——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/索引/EXPLAIN/SELECT/SQL/子查询 等音译为多组崩坏词；本卡统一为规范术语。
