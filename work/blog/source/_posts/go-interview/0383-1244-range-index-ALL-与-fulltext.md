---
disableNunjucks: true
title: "1244 range、index、ALL 与 fulltext"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：MySQL 调优 | 难度：中 | 题型：原理 | 频率：高 | 关键词：**range、index、ALL、fulltext、覆盖索引、全表扫描**

> 原文锚点：第 44~95 段「ref 普通等值、fulltext 全文、ref_or_null、index、ALL、possible_keys/key」

## 一句话总述
range 用索引取一个范围内的记录（如 `>`、`IN`、`BETWEEN`）。index 是「二级索引全扫」，通常因覆盖索引而比 ALL 便宜。ALL 是整表逐行扫描，最慢。fulltext 走全文索引。possible_keys 是候选、key 是实际选用——候选多反而拖慢优化器选型。

## 面试官视角
range/index/ALL 是「退化链」的三档。考官看你能解释：为什么有时明明有索引却走 ALL（如对索引列用函数/OR 非索引列导致失效）；为什么 index 比 ALL 快（扫更小的二级索引树 + 覆盖）。能提「possible_keys 不是越多越好」说明你懂优化器成本。

## 主问答
**Q（面试官原话）：** range、index、ALL 分别代表什么？为什么有索引还会 ALL？

1. **range**：通过索引取到「连续/离散范围区间」的记录，如 `id > 1`、`id IN (1,2,3)`。
2. **index**：按二级索引做「全索引扫描」，常见于覆盖索引——只查索引列，扫更小的索引树而非聚簇表。
3. **ALL**：全表扫描，逐行判断；当索引失效（对列用函数、OR 接非索引列、类型隐式转换）时出现。
4. **fulltext / 候选集**：fulltext 走全文索引；possible_keys 是优化器候选、key 是实际用到的——候选越多优化器算成本越久，故建议删无用索引。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | range 是什么？ | 说不清索引范围 |
| L2 | index 为何比 ALL 快？ | 说不清覆盖/小树 |
| L3 | 为什么掉 ALL？ | 说不清索引失效 |
| L4 | possible_keys 含义？ | 说不清候选集 |
| L5 | 怎么避免全表扫？ | 说不清索引设计 |

## 版本与兼容性
| type | 扫描对象 | 典型场景 |
|------|----------|----------|
| range | 索引范围 | > / IN / BETWEEN |
| index | 整棵二级索引 | 覆盖索引 |
| ALL | 整张表 | 索引失效 |

## 关键代码
```sql
EXPLAIN SELECT * FROM t WHERE id > 1;        -- range
EXPLAIN SELECT b FROM t;                     -- 联合索引覆盖 → index
EXPLAIN SELECT * FROM t WHERE k1 = k1 OR k3; -- 索引失效 → ALL
```

## 总结与追问预判
核心：**range 索引范围、index 二级索引全扫（常因覆盖）、ALL 全表扫；possible_keys 是候选非实际**。追问常接「索引什么时候失效」（见 1244）或「eq_ref/ref 怎么来」（见 1244）。

## ⚠️ 原文纠错
1. 事实核校： [经验] range/index/ALL 语义、覆盖索引使 index 优于 ALL、possible_keys 与 key 区别——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/索引/EXPLAIN 等音译为崩坏词；本卡统一为规范术语。
