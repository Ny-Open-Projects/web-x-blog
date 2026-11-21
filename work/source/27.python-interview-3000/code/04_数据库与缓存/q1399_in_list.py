"""IN 大列表的代价与替代: 大列表 vs 临时表 JOIN 的耗时对比"""
import random
import sqlite3
import time

random.seed(6)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER)")
conn.execute("CREATE INDEX idx_uid ON orders(user_id)")
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(i, i % 100000) for i in range(200000)])
ids = [random.randrange(100000) for _ in range(900)]

t0 = time.perf_counter()
q = "SELECT COUNT(*) FROM orders WHERE user_id IN (%s)" % ",".join("?" * 900)
n1 = conn.execute(q, ids).fetchone()[0]
t1 = time.perf_counter()

conn.execute("CREATE TEMP TABLE wanted(user_id INTEGER PRIMARY KEY)")
conn.executemany("INSERT OR IGNORE INTO wanted VALUES(?)", [(i,) for i in ids])
n2 = conn.execute(
    "SELECT COUNT(*) FROM orders o JOIN wanted w ON o.user_id = w.user_id").fetchone()[0]
t2 = time.perf_counter()

print(f"IN 900 值: {n1} 行, {(t1 - t0) * 1000:.1f} ms")
print(f"临时表 JOIN: {n2} 行, {(t2 - t1) * 1000:.1f} ms, 语义等价且计划更稳")
print("工程建议: 限制 IN 个数, 大集合改临时表 JOIN 或拆批")
