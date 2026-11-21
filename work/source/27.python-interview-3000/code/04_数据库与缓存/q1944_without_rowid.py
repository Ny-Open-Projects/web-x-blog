"""WITHOUT ROWID 表: 复合主键的另一种物理组织与实测"""
import sqlite3
import time

def build(without_rowid):
    c = sqlite3.connect(":memory:")
    tail = " WITHOUT ROWID" if without_rowid else ""
    c.execute("CREATE TABLE readings(dev_id INTEGER, ts INTEGER, value REAL, note TEXT, "
              "PRIMARY KEY(dev_id, ts))" + tail)
    c.executemany("INSERT INTO readings VALUES(?,?,?,?)",
                  [(i % 200, i, i * 0.5, "note-%d" % i) for i in range(50000)])
    c.commit()
    return c

a = build(False)
b = build(True)
print("rowid 表       page_count =", a.execute("PRAGMA page_count").fetchone()[0])
print("WITHOUT ROWID  page_count =", b.execute("PRAGMA page_count").fetchone()[0],
      "(数据本身聚簇在主键 B 树里 不再存一份主键索引)")

def plan(c, sql):
    return " | ".join(r[3] for r in c.execute("EXPLAIN QUERY PLAN " + sql))

q = "SELECT value FROM readings WHERE dev_id = 7 AND ts BETWEEN 1000 AND 1100"
print("rowid 表计划      ->", plan(a, q))
print("WITHOUT ROWID 计划 ->", plan(b, q))

def timed(c, sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        c.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

print(f"rowid 表耗时 {timed(a, q):.2f} ms  WITHOUT ROWID 耗时 {timed(b, q):.2f} ms")

# WITHOUT ROWID 的代价: 大字段被冗余进每一个二级索引
b.execute("CREATE INDEX idx_ts ON readings(ts)")
a.execute("CREATE INDEX idx_ts ON readings(ts)")
print("加二级索引后 WITHOUT ROWID page_count =", b.execute("PRAGMA page_count").fetchone()[0],
      "(二级索引要背全部主键列)")
print("结论: 以复合主键点查为主的窄行表适合 WITHOUT ROWID; 宽行 多二级索引或大 blob 慎用")
