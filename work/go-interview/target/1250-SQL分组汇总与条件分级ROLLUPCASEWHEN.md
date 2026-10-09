# 1250 SQL 分组汇总与条件分级（ROLLUP / CASE WHEN）

> 分类：SQL 技巧 | 难度：L2 | 题型：实操题 | 频率：中 | 关键词：**GROUP BY**/**WITH ROLLUP**/**CASE WHEN**/**分级打标**
> 原文锚点：第 44~60 段「GROUP BY+ROLLUP 汇总 + CASE WHEN 分级」

## 一句话总述
「每个 X 的 Y 并汇总总计」用 `GROUP BY col` + `WITH ROLLUP`；「按阈值给行打等级」用 `CASE WHEN` 多分支。两者常组合做分组统计与分层报表。

## 面试官视角
- 考察意图：是否掌握分组聚合的进阶用法（超级累加行、条件分支），而非只会单表 GROUP BY。
- 分档：P5 能写出 GROUP BY + ROLLUP 出总计；P6 能用 CASE WHEN 做三段分级；P7 知 ROLLUP 产生的 NULL 小计行含义、知 CASE 无 ELSE 时未命中返回 NULL。
- 红旗答案：要总计却不会 ROLLUP，手写 UNION 汇总；CASE 漏 ELSE 导致分级出现 NULL 行。
- 惊艳点：ROLLUP 的超级累加行用 `GROUPING()` 函数区分（MySQL 8.0+），避免把 NULL 业务值误当小计 [经验]。

## 主问答
**Q（面试官原话）：** 怎么算每个商品的销售额并汇总总计？怎么按销售额分级？
**A：**
1. **GROUP BY + WITH ROLLUP（分组并出总计）**：订单表算「每个商品的销售额」并追加一行总计，先 `GROUP BY product_id` 算每组 `SUM(qty*price)`，再加 **`WITH ROLLUP`** 让 MySQL 额外生成一层全体汇总（最高层小计即总销售额）[经验]。
2. **CASE WHEN 分级打标**：把商品按销售额分「低/中/高」三档——`CASE WHEN sales < 100 THEN '低' WHEN sales < 200 THEN '中' ELSE '高' END AS level`；未命中任何分支且无 ELSE 时返回 NULL，生产建议补 ELSE 兜底 [经验]。
3. **ROLLUP 与 CASE 组合做分层报表**：先 `GROUP BY product_id WITH ROLLUP` 出每商品销售额+总计，再在外层用 `CASE WHEN` 对各行（含总计行）打档位，一张报表同时给出汇总与分级 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么出每商品+总计？ | 分组汇总 | GROUP BY product_id WITH ROLLUP | P5 |
| L2 | ROLLUP 的 NULL 行是？ | 语义理解 | 超级累加小计行 | P6 |
| L3 | CASE 分级怎么写？ | 条件分支 | WHEN 阈值 THEN 档 ELSE 兜底 | P6 |
| L4 | 怎么区分 NULL 业务值和小计？ | 进阶 | GROUPING() 函数（8.0+） | P7 |
| L5 | 多列 ROLLUP 行为？ | 上卷规则 | 按最左前缀逐层上卷 | P7+ |

## 版本与兼容性
- `WITH ROLLUP` 为 MySQL/SQL 标准扩展；`GROUPING()` 需 MySQL 8.0+。PostgreSQL 用 `GROUP BY ROLLUP(...)` 语法，SQL Server 用 `GROUP BY ... WITH ROLLUP`。

## 总结与追问预判
ROLLUP 与 CASE WHEN 是多维度报表基石。配合本波「去重聚合」「自定义排序」三张卡，面试常见 SQL 统计题基本覆盖。

## ⚠️ 原文纠错
1. 事实核校： [经验] ROLLUP 与 `GROUP BY ... WITH CUBE` 不同，ROLLUP 只按最左前缀上卷、CUBE 生成全组合，别混用——正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（分组、汇总、小计、分级、条件分支等）。

```sql
-- 每个商品销售额 + 总计（ROLLUP 追加超级累加行）
SELECT product_id, SUM(qty * price) AS sales
FROM orders
GROUP BY product_id WITH ROLLUP;

-- 按销售额分级打标（低/中/高）
SELECT product_id,
       SUM(qty * price) AS sales,
       CASE
         WHEN SUM(qty * price) < 100 THEN '低'
         WHEN SUM(qty * price) < 200 THEN '中'
         ELSE '高'
       END AS level
FROM orders
GROUP BY product_id;
```
