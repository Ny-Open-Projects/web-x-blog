"""HAVING 的下推改写: 分组键条件搬进 WHERE, 聚合条件才留在 HAVING"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, region TEXT, amt REAL)")
rows = []
for i in range(1, 120001):
    rows.append((i, ("north", "south", "east", "west")[i % 4], (i % 300) + 0.5))
c.executemany("INSERT INTO orders VALUES(?,?,?)", rows)

slow_sql = """SELECT region, COUNT(*), SUM(amt) FROM orders
GROUP BY region
HAVING region = 'north' AND SUM(amt) > 100000"""
fast_sql = """SELECT region, COUNT(*), SUM(amt) FROM orders
WHERE region = 'north'
GROUP BY region
HAVING SUM(amt) > 100000"""

rs, rf = c.execute(slow_sql).fetchall(), c.execute(fast_sql).fetchall()
assert rs == rf, "下推改写必须等价"
print("两版结果一致:", rf)
print("改写前计划:", c.execute("EXPLAIN QUERY PLAN " + slow_sql).fetchall())
c.execute("CREATE INDEX idx_ra ON orders(region, amt)")
print("下推+覆盖索引计划:", c.execute("EXPLAIN QUERY PLAN " + fast_sql).fetchall())

def timed(sql):
    t0 = time.perf_counter()
    for _ in range(10):
        c.execute(sql).fetchall()
    return (time.perf_counter() - t0) * 1000 / 10

print("改写前每次 %.2f ms, 改写后每次 %.2f ms (聚合前先删行 免全量分组)"
      % (timed(slow_sql), timed(fast_sql)))
