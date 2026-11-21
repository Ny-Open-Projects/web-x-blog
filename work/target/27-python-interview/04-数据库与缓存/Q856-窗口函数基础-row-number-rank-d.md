---
title: [Q856] 窗口函数基础: row_number / rank / dense_rank
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q856 · 窗口函数基础: row_number / rank / dense_rank

> 难度:★★★☆ | 标签:SQL, 窗口函数

**问**:窗口函数 ROW_NUMBER、RANK、DENSE_RANK 有什么区别?并列名次时三者各返回什么?

**答**:三者都是"每行一个值"的排序窗口函数,区别只在并列值的处理。ROW_NUMBER 对每一行给唯一递增序号,并列也强行分先后;RANK 并列给相同名次,且跳过后续名次,如 1、2、2、4;DENSE_RANK 并列相同且不跳号,如 1、2、2、3。面试要点:需要"取每条第几名"用 ROW_NUMBER,需要"名次并列"语义用 RANK/DENSE_RANK;排序键不唯一时必须补 tie-breaker 列,否则 ROW_NUMBER 结果不稳定。

```python
# file: code/04_数据库与缓存/q856_window_rank.py
"""sqlite3 真实演示三种排序窗口函数在并列分时的差异"""
import sqlite3

DDL = """
CREATE TABLE score (name TEXT, class TEXT, score INT);
INSERT INTO score VALUES
 ('alice','A',95),('bob','A',92),('carol','A',92),('dave','A',88),
 ('erin','B',93),('frank','B',90);
"""

SQL = """
SELECT name, class, score,
       ROW_NUMBER() OVER (PARTITION BY class ORDER BY score DESC, name) AS rn,
       RANK()       OVER (PARTITION BY class ORDER BY score DESC)      AS rk,
       DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC)      AS drk
FROM score
ORDER BY class, rk
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        print("name  class score rn rk drk")
        for row in conn.execute(SQL):
            print(f"{row[0]:<6}{row[1]:<6}{row[2]:<6}{row[3]:<3}{row[4]:<3}{row[5]}")
```

**追问**:
- 想取每个班级分数第二高的学生怎么写?——把窗口结果包成子查询(或 CTE),外层过滤 `WHERE rn = 2`,SQLite/MySQL 8 也可用等价写法。
- ROW_NUMBER 的顺序会变吗?——会,排序键有并列时结果不保证稳定,必须追加唯一列(如 id)作为 tie-breaker。

---
