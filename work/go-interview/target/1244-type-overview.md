# 1244 EXPLAIN type 列：访问方法谱系总览

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**EXPLAIN、type 列、访问方法、执行计划、const/ref/range**

> 原文锚点：第 1~14 段「select_type 与 type 列、system/const 初见」

## 一句话总述
EXPLAIN 的 type 列描述「单表访问方法」，从快到慢大致为 system > const > eq_ref > ref > range > index > ALL；越靠左，扫描行越少、性能越好。另有 fulltext、ref_or_null、index_merge、unique_subquery 等特殊类型。select_type 描述查询整体角色（primary 主查询 / derived 物化派生表等）。

## 面试官视角
type 列是执行计划调优的入口。考官看你能不能说出「const 是主键/唯一索引等值常量」「ref 是普通二级索引等值」「range 是索引范围」，并能判断某 SQL 大致落在哪一档。能结合索引设计解释为什么掉到 ALL，说明你真的会调优。

## 主问答
**Q（面试官原话）：** EXPLAIN 的 type 列是什么意思？常见取值怎么排序？

1. **含义**：type 列表示存储引擎对「单表」的访问方法（access method），决定一次查询大致扫描多少行。
2. **快→慢谱系**：system（表仅 1 行且统计精确）> const > eq_ref > ref > range > index > ALL（全表扫）。
3. **特殊类型**：fulltext（全文索引）、ref_or_null（ref 且列可 NULL）、index_merge（索引合并）、unique_subquery（唯一索引关联子查询）。
4. **select_type 另算**：primary 主查询、derived 物化子查询生成派生表、simple 被优化为 join 的查询——描述查询拓扑而非访问速度。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | type 是什么？ | 说不清访问方法 |
| L2 | 快→慢顺序？ | 排错顺序 |
| L3 | const 触发条件？ | 说不清主键/唯一等值 |
| L4 | index_merge 何时用？ | 说不清多索引合并 |
| L5 | 掉到 ALL 怎么救？ | 说不清加索引/覆盖 |

## 版本与兼容性
| 类型 | 出现场景 | MySQL 版本 |
|------|----------|------------|
| system | MyISAM/Memory 单行表 | 全版本 |
| index_merge | 多条件命中不同索引 | 5.0+ |
| fulltext | 全文索引匹配 | 5.6+（InnoDB） |

## 关键代码
```sql
EXPLAIN SELECT * FROM t WHERE id = 1;        -- 看 type 列
EXPLAIN SELECT * FROM t WHERE id IN (1,2,3); -- range
```

## 总结与追问预判
核心：**type 列由快到慢 system>const>eq_ref>ref>range>index>ALL，越左扫描越少**。追问常拐向「const 与 eq_ref 区别」（见 1244-const-system / 1244-eqref-ref）或「索引合并怎么触发」（见 1244-special-types）。

## ⚠️ 原文纠错
1. 事实核校： [经验] type 列谱系、select_type 角色（primary/derived/simple）、system 需统计精确存储引擎——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/InnoDB/索引/EXPLAIN 等音译为多组崩坏词，SQL 语句亦被拆碎；本卡统一为规范术语与可读 SQL。
