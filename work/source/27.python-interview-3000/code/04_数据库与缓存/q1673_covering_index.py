"""covering index 实测: 覆盖索引消除回表 的计划与耗时对比"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, memo TEXT)")
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, i % 2000, (i % 97) * 1.5, "memo-%d" % i) for i in range(200000)])
conn.commit()
conn.execute("CREATE INDEX idx_user ON orders(user_id)")

sql = "SELECT SUM(amount) FROM orders WHERE user_id = ?"
print("普通索引计划:", [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql, (1,))])

t0 = time.perf_counter()
for u in range(2000):
    conn.execute(sql, (u,)).fetchone()
t_plain = (time.perf_counter() - t0) * 1000
print(f"普通索引 2000 次点查: {t_plain:.0f} ms (每查约 100 行, 全部要回表)")

conn.execute("CREATE INDEX idx_user_cover ON orders(user_id, amount)")
conn.execute("DROP INDEX idx_user")
conn.commit()
print("覆盖索引计划:", [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql, (1,))])

t0 = time.perf_counter()
for u in range(2000):
    conn.execute(sql, (u,)).fetchone()
t_cover = (time.perf_counter() - t0) * 1000
print(f"覆盖索引 2000 次点查: {t_cover:.0f} ms")
print("要点: 查询列全部落在索引内时 USING COVERING INDEX 免回表, 随机 IO 变顺序扫;")
print("      索引越宽越接近覆盖, 但写放大与空间同步上涨, 只对高频查询值得")
