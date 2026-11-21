---
title: [Q1665] 字符串聚合: group_concat 的分隔符 顺序 与 去重
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1665 · 字符串聚合: group_concat 的分隔符 顺序 与 去重

> 难度:★★☆☆ | 标签:SQL, 聚合

**问**:group_concat 拼出来的顺序是乱的,想按业务顺序拼怎么办?有什么坑?

**答**:group_concat 文档明确不保证元素顺序,默认分隔符是逗号,第二个参数可自定义分隔符。要有序拼接的通行做法是先在子查询里 ORDER BY 再交给聚合,SQLite 与 MySQL 上实现确实按子查询序拼接,但这是实现细节而非语义保证,强顺序要求应放应用层。去重方面,DISTINCT 只能与单参数形式连用,要"去重加分隔符"就得先在子查询 DISTINCT。另一个必须知道的坑:MySQL 的 group_concat 默认受 group_concat_max_len 1024 字节截断,拼长内容会静默丢数据;SQLite 没有这个参数,受最大字符串长度约束。

```python
# file: code/04_数据库与缓存/q1665_group_concat.py
"""字符串聚合: group_concat 的分隔符 顺序 与 去重三件套"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE emp(dept TEXT, name TEXT, age INTEGER);
INSERT INTO emp VALUES
 ('dev',  'zhang', 30), ('dev',  'wang',  28), ('dev',  'li',    28),
 ('ops',  'zhao',  35), ('ops',  'qian',  31), ('test', 'sun',   26);
""")

# 默认分隔符是逗号, 且元素顺序不保证 -- 文档明确说 arbitrary
print("默认:", conn.execute(
    "SELECT dept, group_concat(name) FROM emp GROUP BY dept ORDER BY dept").fetchall())

# 第二个参数指定分隔符
print("分号:", conn.execute(
    "SELECT dept, group_concat(name, '; ') FROM emp GROUP BY dept ORDER BY dept").fetchall())

# 想要有序拼接: 在子查询里先排序, 再交给聚合(实现上按子查询序, 语义上无保证)
sql = """
SELECT dept, group_concat(name, ' / ') FROM (
  SELECT dept, name FROM emp ORDER BY dept, name
) GROUP BY dept ORDER BY dept
"""
print("有序:", conn.execute(sql).fetchall())

# 想要去重: DISTINCT 只能与单参数形式连用, 带分隔符的先在子查询去重
print("DISTINCT 年龄:", conn.execute("SELECT group_concat(DISTINCT age) FROM emp").fetchone()[0])
sql2 = """
SELECT group_concat(age, ',') FROM (SELECT DISTINCT age FROM emp ORDER BY age)
"""
print("去重加分隔:", conn.execute(sql2).fetchone()[0])
print("要点: MySQL 的同名函数受 group_concat_max_len 默认 1024 截断; SQLite 无此参数;")
print("      超长或顺序敏感的拼接建议放应用层, SQL 里的拼接适合调试与轻量报表")
```

**追问**:
- 报表导出大 JSON 用 group_concat 合适吗?——不合适,截断与顺序两个坑都在,应该由应用层查询后用 json 库组装。
- PG 里对应什么函数?——string_agg(expr, sep) 配 ORDER BY 子句,顺序是语义保证的,比 MySQL 安全。

---
