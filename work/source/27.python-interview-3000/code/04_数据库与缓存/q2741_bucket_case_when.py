"""分桶统计: 一趟扫描用 CASE WHEN 算完所有桶, 对比多趟扫描的代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amt REAL)")
c.executemany("INSERT INTO orders(amt) VALUES(?)",
              [(round((i * 37) % 997 / 7.0, 2),) for i in range(1, 50001)])

one_pass = """
SELECT
  SUM(CASE WHEN amt < 20 THEN 1 ELSE 0 END)                AS bucket_0_20,
  SUM(CASE WHEN amt >= 20 AND amt < 50 THEN 1 ELSE 0 END)  AS bucket_20_50,
  SUM(CASE WHEN amt >= 50 AND amt < 100 THEN 1 ELSE 0 END) AS bucket_50_100,
  SUM(CASE WHEN amt >= 100 THEN 1 ELSE 0 END)              AS bucket_100_up,
  COUNT(*)                                                 AS total
FROM orders
"""
t0 = time.perf_counter()
b = c.execute(one_pass).fetchone()
t1 = (time.perf_counter() - t0) * 1000
print("一趟 CASE WHEN: 桶分布 %s, 合计 %d, 耗时 %.1f ms" % (tuple(b[:4]), b[4], t1))
assert sum(b[:4]) == b[4], "桶边界必须恰好切分值域, 不重不漏"

t0 = time.perf_counter()
multi = [c.execute("SELECT COUNT(*) FROM orders WHERE amt >= ? AND amt < ?",
                   (lo, hi)).fetchone()[0]
         for lo, hi in ((0, 20), (20, 50), (50, 100), (100, 1e9))]
t2 = (time.perf_counter() - t0) * 1000
print("四趟范围 COUNT: 结果 %s, 耗时 %.1f ms (每桶一次全表扫描)" % (tuple(multi), t2))
