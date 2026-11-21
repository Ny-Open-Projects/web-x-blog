"""HAVING vs WHERE: 过滤时机 聚合语义与代价实测"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY, region TEXT, amount INTEGER)")
conn.executemany("INSERT INTO sales(region, amount) VALUES(?,?)",
                 [("r%d" % (i % 50), i % 100) for i in range(200000)])
conn.execute("CREATE INDEX idx_region ON sales(region)")
conn.commit()

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

q_where = "SELECT region, SUM(amount) FROM sales WHERE amount >= 50 GROUP BY region"
q_having = "SELECT region, SUM(amount) FROM sales GROUP BY region HAVING MIN(amount) >= 50"
print(f"WHERE 先过滤再聚合 : {timed(q_where):7.2f} ms  进入分组的行数 "
      f"{conn.execute('SELECT COUNT(*) FROM sales WHERE amount >= 50').fetchone()[0]}")
print(f"HAVING 聚合后再过滤: {timed(q_having):7.2f} ms  进入分组的是全量 20 万行")

# 只能写在 HAVING 的条件: 引用聚合结果
agg_only = conn.execute(
    "SELECT COUNT(*) FROM (SELECT region FROM sales GROUP BY region HAVING COUNT(*) > 4100)"
).fetchone()[0]
print("聚合条件必须 HAVING -> 超大分组数:", agg_only)

# 行级条件两种写法结果相同 但 WHERE 便宜: 一边先少算一半行
same_w = timed("SELECT COUNT(*) FROM (SELECT region FROM sales WHERE region = 'r1' GROUP BY region)")
same_h = timed("SELECT COUNT(*) FROM (SELECT region FROM sales GROUP BY region HAVING region = 'r1')")
print(f"同语义 WHERE {same_w:.2f} ms vs HAVING {same_h:.2f} ms")
print("结论: 行级条件一律 WHERE 让过滤发生在聚合之前 组级条件才用 HAVING 别把能提前的过滤拖到最后")
