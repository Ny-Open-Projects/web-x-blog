"""ORDER BY 走索引与 top-N 优先队列: sqlite EXPLAIN QUERY PLAN 验证"""
import math
import random
import sqlite3

random.seed(7)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, amount REAL)")
rows = [(i, round(random.uniform(1, 10000), 2)) for i in range(1, 100001)]
conn.executemany("INSERT INTO orders VALUES(?,?)", rows)

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

sql = "SELECT id, amount FROM orders ORDER BY amount DESC LIMIT 10"
print("无索引:", plan(sql))
conn.execute("CREATE INDEX idx_amount ON orders(amount)")
print("加 amount 索引:", plan(sql))

n, k = 100000, 10
print(f"无索引全排序约 {n * math.log2(n):.0f} 次比较")
print(f"top-N 优先队列约 {n * math.log2(k):.0f} 次比较, 排序缓冲只留 k 行")
