# 1244 EXPLAIN type 全谱系（深挖）

> 分类：MySQL 调优 | 难度：中高 | 题型：原理深挖 | 频率：高 | 关键词：**EXPLAIN、type 谱系、访问方法、索引选择、执行计划**

> 原文锚点：第 1~100 段「EXPLAIN type 列与 select_type 全集」

## 思路与架构
type 列本质是「单表访问方法的成本排序」，可分层理解：
- 常量级：system（单行精确表）、const（主键/唯一键等值常量）。
- 等值级：eq_ref（被驱动表唯一键等值）、ref（普通索引等值）。
- 范围级：range（索引范围）、ref_or_null（ref+NULL）。
- 扫描级：index（二级索引全扫/覆盖）、ALL（全表扫）。
- 特殊：fulltext、index_merge、unique_subquery、index_subquery。
配套看 select_type（primary/derived/simple）与 key/possible_keys，才能完整读懂执行计划。

## 方案取舍
- 追求 const/eq_ref：给 WHERE/JOIN 条件配主键或唯一索引，且比较对象是常量或已定值；避免函数包裹、避免 OR 接非索引列。
- range 够用就好：范围查询优先走索引范围，减少扫描行；IN 列表本质是离散 range。
- index_merge 是把双刃剑：能合并多索引救 OR 场景，但 union 后仍需回表，远不如一个「覆盖 + 复合索引」彻底；优先考虑建复合索引消除 merge。
- possible_keys 不是越多越好：候选多拖慢优化器选成本，删掉无用索引。

## 答题技巧
1. 先背谱系顺序：system > const > eq_ref > ref > range > index > ALL，特殊类型单列。
2. 用「索引是否唯一 / 是否等值 / 是否常量」三个问句区分 const、eq_ref、ref。
3. 被问「为什么慢」时，先 EXPLAIN 看 type 是否掉到 index/ALL，再查 key 是否为 NULL、是否索引失效。
4. 实战话术：「这条 SQL 走的是 ref，因为普通二级索引等值；如果要到 const，需要把条件改成唯一键等值常量。」
5. 收尾升华：执行计划调优的终点是「用最左匹配的复合索引覆盖查询，让 type 尽量靠左且 Extra 出现 Using index」。

## 细节与核心 API

**type 谱系（单表访问方法成本，左→右越优）**：

```text
system > const(主键/唯一键等值常量) > eq_ref(被驱动表唯一键等值)
  > ref(普通索引等值) > range(索引范围) > index(二级索引全扫/覆盖) > ALL(全表扫)
特殊：fulltext / index_merge / unique_subquery / index_subquery
```

```sql
-- 目标：用最左匹配的复合索引覆盖查询，让 type 尽量靠左且 Extra=Using index
-- 想升到 const：条件改唯一键等值常量；避免函数包裹、OR 接非索引列
EXPLAIN SELECT * FROM t WHERE a=1 OR b=1;  -- 可能 index_merge；建 (a,b) 复合索引更优（消除 merge）
-- index_merge 双刃剑：救 OR 但需回表，不如建复合索引彻底；possible_keys 多拖慢优化器
```

> 边界：EXPLAIN 列与拓扑见 1243；key_len/Extra 见 1245；本卡只讲 type 谱系。
