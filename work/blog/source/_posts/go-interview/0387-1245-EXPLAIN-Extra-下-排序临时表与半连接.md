---
disableNunjucks: true
title: "1245 EXPLAIN Extra（下）：排序临时表与半连接"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：MySQL 调优 | 难度：中高 | 题型：原理 | 频率：中 | 关键词：**Using filesort、Using temporary、Using join buffer、FirstMatch、LooseScan、Materialize、DuplicateWeedout**

> 原文锚点：第 60~85 段「join buffer、filesort、temporary、FirstMatch/LooseScan/Materialize/DuplicateWeedout」

## 一句话总述
进阶 Extra 标记：`Using join buffer`（被驱动表无法有效用索引时，分配 join buffer 内存块加速）、`Using filesort`（排序无法用索引，在内存或磁盘中排序）、`Using temporary`（需建内部临时表完成 distinct/group by/union 等）。此外子查询可转为连接时会出现四种半连接策略：**FirstMatch**（内表找到首个匹配即停）、**LooseScan**（内表按索引分组后与外表匹配）、**Materialize**（子查询物化后连接）、**DuplicateWeedout**（借临时表唯一 id 去重，对应 Start/End temporary）。

## 面试官视角
这一组是「调优信号弹」。考官看你能不能把 `Using filesort` / `Using temporary` 识别为**需要加索引或改写 SQL** 的红灯，并说清 join buffer 的触发条件（被驱动表无有效索引）。半连接四种策略属加分项，能说出名字与作用即可。

## 主问答
**Q（面试官原话）：** Extra 里出现 Using filesort、Using temporary 说明什么？

1. **Using filesort**：排序无法利用索引，需在**内存**（记录少）或**磁盘**（记录多）中完成排序——提示该排序字段应考虑加索引。
2. **Using temporary**：需要建立**内部临时表**来完成操作，常见于 `DISTINCT`、`GROUP BY`、`UNION` 且无法使用索引的场景。
3. **Using join buffer**：连接查询时被驱动表不能有效利用索引加速，MySQL 分配一块 join buffer 内存来加速。
4. **半连接四策略**：子查询可转连接时出现 FirstMatch（内表首匹配即停）、LooseScan（内表分组后匹配）、Materialize（子查询物化后连接）、DuplicateWeedout（临时表唯一 id 去重，表现为 Start/End temporary）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | filesort 说明？ | 说不清排序无索引 |
| L2 | temporary 场景？ | 说不清 distinct/group by |
| L3 | join buffer 触发？ | 说不清被驱动表无索引 |
| L4 | 内存还是磁盘？ | 说不清按记录数 |
| L5 | 半连接策略？ | 说不清四种 |

## 版本与兼容性
| Extra | 触发 |
|------|------|
| Using filesort | 排序无法用索引 |
| Using temporary | distinct/group by/union 无索引 |
| Using join buffer | 被驱动表无有效索引 |

## 关键代码
```sql
-- name 无索引 → 排序走 filesort；加去重统计 → 再叠加 temporary
SELECT DISTINCT name FROM t ORDER BY name;
```

## 总结与追问预判
核心：**filesort/temporary 是「应加索引」的红灯；join buffer 因被驱动表无索引而起；半连接有 FirstMatch/LooseScan/Materialize/DuplicateWeedout 四种**。追问可回「Extra 常用标记」（见 1245）。

## ⚠️ 原文纠错
1. 事实核校： [经验] Using filesort（内存/磁盘按记录数）、Using temporary（distinct/group by/union）、Using join buffer（被驱动表无有效索引）、半连接四策略 FirstMatch/LooseScan/Materialize/DuplicateWeedout(Start/End temporary)——均正确，本卡为准。
2. 崩坏词归一：源码将 MySQL/EXPLAIN/索引/连接查询/子查询/物化 等音译为多组崩坏词；本卡统一为规范术语。
