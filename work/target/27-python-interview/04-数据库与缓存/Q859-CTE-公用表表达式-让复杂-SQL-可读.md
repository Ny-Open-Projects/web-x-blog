---
title: [Q859] CTE 公用表表达式: 让复杂 SQL 可读
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q859 · CTE 公用表表达式: 让复杂 SQL 可读

> 难度:★★☆☆ | 标签:SQL, CTE

**问**:WITH 子句是什么?和子查询相比有什么好处?CTE 会被优化器内联展开吗?

**答**:CTE(Common Table Expression)是 `WITH name AS (SELECT ...)` 定义的临时命名结果集,只在本条语句内有效,可定义多个并互相引用,把"一大坨嵌套"变成"分步流水线"。相比子查询,它消除重复代码、层次清晰、便于注释与调试(可单独跑每个 CTE)。在 MySQL 8/PostgreSQL 中普通 CTE 默认会被优化器内联(或可被物化),行为接近等价子查询;PostgreSQL 里可显式 `AS MATERIALIZED` 或 `AS NOT MATERIALIZED` 控制是否物化,MySQL 8.0 普通列 CTE 会物化一次供复用。面试要点:CTE 首要价值是可读性,其次才是复用。

```python
# file: code/04_数据库与缓存/q859_cte_pipeline.py
"""多级 CTE 分步计算: 每类目平均分 -> 高于平均的学生 -> 类目排名"""
import sqlite3

DDL = """
CREATE TABLE stu (name TEXT, category TEXT, score INT);
INSERT INTO stu VALUES
 ('a','math',90),('b','math',70),('c','math',80),
 ('d','eng',60),('e','eng',75),('f','eng',85);
"""

SQL = """
WITH class_avg AS (
  SELECT category, AVG(score) AS avg_score FROM stu GROUP BY category
),
above_avg AS (
  SELECT s.name, s.category, s.score, c.avg_score
  FROM stu s JOIN class_avg c USING (category)
  WHERE s.score > c.avg_score
)
SELECT category, name, score FROM above_avg ORDER BY category, score DESC
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        for row in conn.execute(SQL):
            print(row)
```

**追问**:
- 同一个子查询要引用两次怎么办?——不用复制两遍,定义一个 CTE,后面两处直接引用同一个名字。
- 递归 CTE 和普通 CTE 的区别?——递归 CTE 用 `WITH RECURSIVE`,锚点查询与递归查询用 UNION ALL 连接,反复执行直到不再产生新行。

---
