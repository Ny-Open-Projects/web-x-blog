# 1251 面试 SQL（二）：CTE 两步统计与子查询取交集差集

> 分类：MySQL/SQL | 难度：L3 | 题型：方案题 | 频率：高 | 关键词：**CTE**/**WITH**/**两步统计**/**子查询IN**/**NOT IN差集**
> 原文锚点：第 1~29 段「CTE 统计每用户订单数/商品数/销售额(ordersummary)关联 user 表 + 子查询买101且102没买103(含 CTE 改写 a/b/c 三表)」

## 一句话总述
复杂统计常需**两步**：先用 CTE（WITH）按 `userID` 分组算出每用户的订单数/商品数/销售额生成 `ordersummary`，再关联 `user` 表取用户名。「买 101 且买 102 但没买 103 的用户」可用**子查询 + IN/NOT IN** 表达交集与差集，也可改写为多个 CTE（a=买101、b=买102、c=买103）再做 `IN a AND IN b AND NOT IN c`。

## 面试官视角
- 考察意图：能否把多步统计拆成 CTE + 关联，并用 IN/NOT IN 表达「交集 + 差集」语义。
- 分档：P5 知子查询；P6 能写 CTE 两步统计 + IN/NOT IN；P7 知 CTE 改写可读性、IN 子查询空值陷阱。
- 红旗答案：把「没买 103」写成 `= 103` 而非 `NOT IN`；忽略关联 user 表取用户名这一步。
- 惊艳点：点出「NOT IN 右表含 NULL 会全失配、改用 NOT EXISTS 更稳」，以及「CTE 改写多子查询提升可读性」 [经验]。

## 主问答
**Q（面试官原话）：** 统计每用户订单/商品/销售额并关联用户名？找出买 101 且 102 但没买 103 的用户？
**A：**
1. **CTE 两步统计**：先用 `WITH ordersummary AS (SELECT userID, COUNT 订单, SUM 商品, SUM 销售额 GROUP BY userID)` 算聚合，再 `JOIN user` 取用户名 [经验]。
2. **子查询取交集差集**：`WHERE userID IN (买101) AND userID IN (买102) AND userID NOT IN (买103)` 表达「买前两者、没买后者」 [经验]。
3. **CTE 改写可读性**：把三个条件各写成 CTE（a/b/c），主查询 `IN a AND IN b AND NOT IN c`，比嵌套子查询更清晰 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 多步统计？ | 思路 | CTE+JOIN | P5 |
| L2 | 差集？ | 语义 | NOT IN | P6 |
| L3 | 空值？ | 陷阱 | NOT IN 遇 NULL | P7 |
| L4 | 改写？ | 可读 | CTE a/b/c | P7 |
| L5 | 性能？ | 优化 | 索引/物化 | P7+ |

## 版本与兼容性
- 本卡只讲 CTE 统计与 IN/NOT IN；GROUP_CONCAT/HAVING 见 `1251-groupconcat-having`、排名技巧见 `1251-rank-second` [边界]。
- 同系列 SQL 写法（FIELD/ROLLUP/CASE）见 `1250-*`；MySQL 执行流/优化器见 `1210-*`、`1243-*`(EXPLAIN)——本卡只引不重述 [边界]。

## 总结与追问预判
CTE + 关联 + IN/NOT IN 是多步聚合与集合运算的趁手组合。面试常追问「NOT IN 空值陷阱」→ 答「改 NOT EXISTS 或确保右表非空」。

## ⚠️ 原文纠错
1. 事实核校： [经验] CTE 两步统计、IN/NOT IN 交集差集、CTE 改写 a/b/c——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（CTE、子查询、关联、订单、销售额、交集、差集等）。

```sql
-- ① CTE 两步统计每用户订单/商品/销售额，再关联 user 取用户名
WITH ordersummary AS (
  SELECT userID,
         COUNT(*)            AS order_cnt,
         SUM(item_cnt)       AS item_cnt,
         SUM(amount)         AS sales
  FROM   orders GROUP BY userID
)
SELECT u.userID, u.user_name, o.order_cnt, o.item_cnt, o.sales
FROM   ordersummary o JOIN user u ON u.userID = o.userID;

-- ② 买 101 且 102 但没买 103 的用户（交集 + 差集）
SELECT DISTINCT userID FROM orders
WHERE  userID IN  (SELECT userID FROM orders WHERE productID = 101)
  AND  userID IN  (SELECT userID FROM orders WHERE productID = 102)
  AND  userID NOT IN (SELECT userID FROM orders WHERE productID = 103);
-- 注：NOT IN 右表含 NULL 会全失配，生产改 NOT EXISTS 更稳
```
