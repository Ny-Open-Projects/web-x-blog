---
title: [Q1669] 聚合与 NULL: COUNT 口径与 AVG/SUM 偏差
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1669 · 聚合与 NULL: COUNT 口径与 AVG/SUM 偏差

> 难度:★★☆☆ | 标签:SQL, NULL 语义

**问**:COUNT(*) 和 COUNT(col) 有什么区别?AVG 会对 NULL 怎么处理?

**答**:COUNT(*) 数行数,包含 NULL 行;COUNT(col) 只数该列非 NULL 的值,同一张表两者可以不同。聚合函数普遍忽略 NULL:AVG 只对非 NULL 求均值,缺考的 NULL 不参与分母,这是"平均分"口径争议的根源;SUM、MAX、MIN 同样忽略 NULL。关键差异在空集:对零行聚合,SUM 返回 NULL 而不是 0,直接输出到报表会显示空,必须 COALESCE 包一层。做统计前先和需求方确认口径——数行还是数有效值、缺考算不算分母、空集显示 0 还是不显示。

```python
# file: code/04_数据库与缓存/q1669_agg_null.py
"""聚合与 NULL: COUNT 三种口径 与 AVG/SUM 的隐性偏差"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE score(student TEXT, subject TEXT, val REAL)")
conn.executemany("INSERT INTO score VALUES(?,?,?)",
                 [("a", "math", 80), ("a", "eng", None), ("a", "phys", 90),
                  ("b", "math", None), ("b", "eng", None), ("b", "phys", None),
                  ("c", "math", 70), ("c", "eng", 60), ("c", "phys", 50)])
conn.commit()

def one(sql):
    return conn.execute(sql).fetchone()[0]

print("COUNT(*) =", one("SELECT COUNT(*) FROM score"), "     数行, 含 NULL")
print("COUNT(val) =", one("SELECT COUNT(val) FROM score"), "    只数非 NULL")
print("COUNT(DISTINCT val) =", one("SELECT COUNT(DISTINCT val) FROM score"))

# AVG 只对非 NULL 求均值: a 是 80 与 90 两门 -> 85, 不是 (80+90)/3 也不是 170/3 的误解
for stu in ("a", "b", "c"):
    avg = one("SELECT AVG(val) FROM score WHERE student='" + stu + "'")
    print(f"{stu}: AVG={avg}  (b 全 NULL -> AVG 是 NULL 而不是 0)")

print("空集 SUM:", one("SELECT SUM(val) FROM score WHERE student='zz'"),
      "-> 是 NULL 不是 0, 报表必须 COALESCE")
print("COALESCE 修正:", one("SELECT COALESCE(SUM(val), 0) FROM score WHERE student='zz'"))
print("结论: 每个统计先明确口径, 是数行还是数值, 空集想显示 0 还是不显示, 再写 SQL")
```

**追问**:
- 想让 NULL 按零参与 AVG 怎么写?——AVG(COALESCE(val, 0)),先定口径再聚合,两种写法结果完全不同。
- COUNT(DISTINCT 多列) 为什么报错?——标准 SQL 的 DISTINCT 聚合只收单表达式,多列用 COUNT(DISTINCT a || '-' || b) 或先子查询去重再数。

---
