"""报表 SQL 的三轮优化: 函数包列 -> 范围条件 -> 提前聚合"""
import random
import sqlite3
import time

random.seed(2)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, city TEXT)")
conn.execute(
    "CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, created TEXT)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(i, "city%d" % (i % 30)) for i in range(1, 50001)])
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, random.randrange(1, 50001), round(random.uniform(10, 500), 2),
                   "2024-06-%02d" % random.randrange(1, 29)) for i in range(1, 200001)])

def timed(sql):
    t0 = time.perf_counter()
    rows = conn.execute(sql).fetchall()
    return rows, (time.perf_counter() - t0) * 1000

v0, ms0 = timed(
    "SELECT u.city, SUM(o.amount) FROM orders o JOIN users u ON o.user_id = u.id "
    "WHERE substr(o.created, 1, 7) = '2024-06' GROUP BY u.city")
conn.execute("CREATE INDEX idx_created ON orders(created)")
v1, ms1 = timed(
    "SELECT u.city, SUM(o.amount) FROM orders o JOIN users u ON o.user_id = u.id "
    "WHERE o.created >= '2024-06-01' AND o.created < '2024-07-01' GROUP BY u.city")
v2, ms2 = timed(
    "SELECT u.city, SUM(t.total) FROM (SELECT user_id, SUM(amount) total FROM orders "
    "WHERE created >= '2024-06-01' AND created < '2024-07-01' GROUP BY user_id) t "
    "JOIN users u ON u.id = t.user_id GROUP BY u.city")
same = abs(sum(r[1] for r in v0) - sum(r[1] for r in v2)) < 0.01
print(f"v0 函数包列: {ms0:.1f} ms")
print(f"v1 范围条件+索引: {ms1:.1f} ms")
print(f"v2 先聚合再 join: {ms2:.1f} ms, 金额一致: {same}")
