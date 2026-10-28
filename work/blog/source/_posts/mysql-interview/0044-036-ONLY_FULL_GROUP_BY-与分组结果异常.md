---
disableNunjucks: true
title: "036 ONLY_FULL_GROUP_BY 与分组结果异常"
date: 2026-10-16 00:49:40
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：服务器配置 | 难度：L3 | 题型：排障题 | 频率：高 | 关键词：**ONLY_FULL_GROUP_BY** / **非聚合列** / **结果不确定**
> 原文锚点：第 23~39 段「这个 SQL 在其他关系型数据库如 SQL Server 中执行一定是不可能成功的…但是在 MySQL 中并没有报错」

## 一句话总述
关掉 `ONLY_FULL_GROUP_BY` 时，MySQL **允许 SELECT 出现不在 GROUP BY 里的非聚合列**，并**随便取一行**的值——语句不报错但结果是错的；开启后直接报语法错误。

## 面试官视角
- **考察意图**：给一张表 + 一条 SQL + 错误结果，看你能不能把锅甩回 `sql_mode`，这是本章开篇题。
- **P5** 知道 GROUP BY 要写完整。
- **P6** 能指出缺 `ONLY_FULL_GROUP_BY` 时非聚合列取值为**不确定**，并给出修复写法。
- **P7** 能说明 5.7 起该值已进默认集，升级后老 SQL 会集中报错，需要提前灰度排查。
- **红旗**：① 只说"SQL 写错了"讲不出配置因素；② 认为"取的是第一行"；③ 建议"关掉这个限制"来消错。
- **惊艳点**：非聚合列的取值是**不确定**而非"第一行"——优化器可能换索引就变 `[经验]` —— 验证：同一 SQL 前后加索引，观察该列返回值变化。

## 主问答
**Q（面试官原话）：** 这条统计 SQL 执行成功了，但仓库 ID 全被算到同一个仓库，为什么？

**A：**
1. **结论**：因为 `sql_mode` **没有开 `ONLY_FULL_GROUP_BY`**——SELECT 里 `warehouse_id` 没写进 GROUP BY，MySQL 不报错，而是**任取一个值**填进去。
2. **机制**：开启后，非聚合列若未出现在 GROUP BY（也不能被函数依赖推出），MySQL **直接报 ERROR 1055**，行为与 SQL Server、PostgreSQL 一致。
3. **边界**：修复的正解是**补全 GROUP BY 列**，不是关掉限制——关掉只是把错误从"报错"变成"静默给错数据"。

**加分层**：`ONLY_FULL_GROUP_BY` 自 **5.7 起进入默认 sql_mode**，5.6→5.7/8.0 升级时这类 SQL 会集中报错，升级前必须先扫一遍。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | GROUP BY 怎么写才对 | 概念 | 非聚合列都要写进 | 换题 → 不及格 |
| L2 | 少了列为什么没报错 | sql_mode | 缺 ONLY_FULL_GROUP_BY | 判 P5 |
| L3 | 取到的是什么值 | 机制细节 | 不确定值，非第一行 | 判 P6 |
| L4 | 开启后会怎样 | 版本行为 | 报 ERROR 1055 | 判 P6+ |
| L5 | 升级时怎么避免 | 工程实践 | 升级前扫 SQL 并灰度 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6 及之前 | 默认**不含** `ONLY_FULL_GROUP_BY` | 老版本会静默给错结果 |
| 5.7 / 8.0 | 默认**包含**该值，语义更严格 | 现在默认就会报错，按"补全 GROUP BY"答 |

## 关键代码
```sql
-- 问题 SQL：warehouse_id 未进 GROUP BY
SELECT product_id, warehouse_id, SUM(qty) FROM stock GROUP BY product_id;
SET SESSION sql_mode = CONCAT(@@sql_mode, ',ONLY_FULL_GROUP_BY');
-- 再执行 → ERROR 1055；正解是补列
SELECT product_id, warehouse_id, SUM(qty) FROM stock GROUP BY product_id, warehouse_id;
```

## ⚠️ 原文纠错
原文说"这时它会报 error 1055（原文读作 irver 幺零零五）"——错误号 **1055** 正确。原文称"只按 product_id 分组，warehouse 是随机取了一个"——更准确的说法是**取值不确定（indeterminate）**，不保证随机也不保证第一行，已按官方表述修正。

## 总结与追问预判
- 缺 `ONLY_FULL_GROUP_BY` → **不报错但结果错**；开启 → ERROR 1055。
- 修复靠**补全 GROUP BY**，不是关限制；5.7 起已默认开启。
- 下一题：见 035（sql_mode 总览）、044（5.6 默认值变更）。
