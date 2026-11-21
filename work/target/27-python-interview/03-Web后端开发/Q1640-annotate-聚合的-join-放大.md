---
title: [Q1640] annotate 聚合的 join 放大
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1640 · annotate 聚合的 join 放大

> 难度:★★★★ | 标签:Django ORM, SQL

**问**:annotate 里同时 Count 两个反关系,数字为什么会变大?怎么修?

**答**:根因是 join 笛卡尔放大:一个作者 2 本书、3 个奖,LEFT JOIN books 再 LEFT JOIN awards 后行数变成书乘奖的展开(每本书的行重复其奖项数),COUNT(b.id) 数到的是书乘奖的行数而不是书的数量——两个 Count 互相污染,一个变多,另一个碰巧对也别信。修法是把 Count 改成 distinct:`Count("books", distinct=True)`,底层生成 COUNT(DISTINCT b.id),代价是去重开销;更彻底的方案是把互相独立的聚合拆成多个查询或改用 Subquery 先聚合再外连,大表下更可控。这类 bug 的隐蔽点在于小数据集肉眼核对碰巧正确,数据量一大才爆。

```python
# file: code/03_Web后端开发/q1640_annotate_join.py
"""annotate 聚合的 join 放大: 两个反关系计数互相污染(标准库 sqlite3)。"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE books (id INTEGER PRIMARY KEY, author_id INT, title TEXT);
CREATE TABLE awards (id INTEGER PRIMARY KEY, book_id INT, name TEXT);
INSERT INTO authors VALUES (1, '王工');
INSERT INTO books VALUES (11, 1, '书一'), (12, 1, '书二');
INSERT INTO awards VALUES (91, 11, '奖一'), (92, 12, '奖A'), (93, 12, '奖B');
""")

one_join = conn.execute(
    "SELECT a.name, COUNT(b.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id GROUP BY a.id").fetchall()
print("只 join books:", one_join)                       # 2 正确

two_joins = conn.execute(
    "SELECT a.name, COUNT(b.id), COUNT(w.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id "
    "LEFT JOIN awards w ON w.book_id = b.id GROUP BY a.id").fetchall()
print("同时 join books+awards:", two_joins)              # 行数相乘, 计数互相污染

distinct = conn.execute(
    "SELECT a.name, COUNT(DISTINCT b.id), COUNT(DISTINCT w.id) FROM authors a "
    "LEFT JOIN books b ON b.author_id = a.id "
    "LEFT JOIN awards w ON w.book_id = b.id GROUP BY a.id").fetchall()
print("DISTINCT 修正:", distinct)
print("Django 对应: Count('books') 与 Count('books__awards') 同 annotate 必须都加 distinct=True")
```

**追问**:
- 加了 distinct 一定对吗?——对计数成立;Sum 与 Avg 不适用,要改子查询先聚合再外连。
- annotate 结果还能再 filter 吗?——可以,但分清 filter 在 annotate 前是过滤参与聚合的行,在后是按聚合结果过滤生成 HAVING。
