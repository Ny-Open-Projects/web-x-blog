"""UNION 与 UNION ALL 分页: 去重要先物化整个结果集, LIMIT 救不了"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE hot(id INTEGER PRIMARY KEY, tag TEXT)")
c.execute("CREATE TABLE cold(id INTEGER PRIMARY KEY, tag TEXT)")
c.executemany("INSERT INTO hot VALUES(?,?)",
              [(i, "t%d" % (i % 97)) for i in range(1, 20001)])
c.executemany("INSERT INTO cold VALUES(?,?)",
              [(i, "t%d" % (i % 97)) for i in range(1, 20001)])

for label, sql in [
    ("UNION     + LIMIT 10", "SELECT id FROM hot UNION SELECT id FROM cold LIMIT 10"),
    ("UNION ALL + LIMIT 10", "SELECT id FROM hot UNION ALL SELECT id FROM cold LIMIT 10"),
]:
    plan = " | ".join(r[3] for r in c.execute("EXPLAIN QUERY PLAN " + sql))
    t0 = time.perf_counter()
    n = len(c.execute(sql).fetchall())
    ms = (time.perf_counter() - t0) * 1000
    print("%s -> %5d 行 %6.1f ms | %s" % (label, n, ms, plan))
print("计划可见: UNION 带 USE TEMP B-TREE FOR UNION, 先全量去重; UNION ALL 无临时结构, 提前终止")
