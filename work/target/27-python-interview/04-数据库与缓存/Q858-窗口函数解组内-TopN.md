---
title: [Q858] 窗口函数解组内 TopN
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q858 · 窗口函数解组内 TopN

> 难度:★★★☆ | 标签:SQL, 窗口函数

**问**:写 SQL 取每个分类下销量前 3 的商品,如果不用窗口函数你会怎么写?为什么窗口函数更好?

**答**:经典解法是先 `ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC)` 编号,再外层过滤 `rn <= 3`。老写法是相关子查询"比该商品销量高的不超过 2 个",或者自 join 计数,数据量大时复杂度和重复扫描都很差,而且处理并列名次很啰嗦。窗口函数只扫一遍并按分区计算,语义清晰、可扩展(改成 Top10 只改一个数字)。注意取"第 N 名"用 ROW_NUMBER,"前 N 名含并列"用 `RANK() <= N` 或 DENSE_RANK 视业务而定。

```python
# file: code/04_数据库与缓存/q858_topn_per_group.py
"""组内 TopN: 窗口函数编号 + 外层过滤, 并与自相关子查询对照"""
import sqlite3

DDL = """
CREATE TABLE goods (id INTEGER PRIMARY KEY, category TEXT, sales INT);
INSERT INTO goods (category, sales) VALUES
 ('book',100),('book',90),('book',90),('book',80),('book',70),
 ('toy',50),('toy',40),('toy',30);
"""

WINDOW_SQL = """
SELECT category, id, sales FROM (
  SELECT category, id, sales,
         ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC, id) AS rn
  FROM goods
) WHERE rn <= 3 ORDER BY category, rn
"""

SUBQ_SQL = """
SELECT g.category, g.id, g.sales
FROM goods g
WHERE (SELECT COUNT(*) FROM goods g2
       WHERE g2.category = g.category AND g2.sales > g.sales) < 2
ORDER BY g.category, g.sales DESC
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        print("窗口函数法:", conn.execute(WINDOW_SQL).fetchall())
        print("相关子查询:", conn.execute(SUBQ_SQL).fetchall())
```

**追问**:
- TopN 想并列时都取到怎么办?——把 ROW_NUMBER 换成 DENSE_RANK 再过滤 `<= 3`,并列名次都会保留。
- 数据量大时编号前的排序怎么优化?——给 `(category, sales DESC, id)` 建联合索引,让分区排序直接走索引顺序。

---
