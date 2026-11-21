"""大 IN 列表改临时表: 交叉点实测"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
c.executemany("INSERT INTO t VALUES(?,?)", [(i, "v%d" % i) for i in range(1, 50001)])
ids = list(range(20000, 26000))   # 6000 个目标 id

ph = ",".join("?" * len(ids))
t0 = time.perf_counter()
n1 = c.execute("SELECT count(*) FROM t WHERE id IN (%s)" % ph, ids).fetchone()[0]
t_in = time.perf_counter() - t0

t0 = time.perf_counter()
c.execute("DROP TABLE IF EXISTS temp.want")
c.execute("CREATE TEMP TABLE want(id INTEGER PRIMARY KEY)")
c.executemany("INSERT INTO want VALUES(?)", [(i,) for i in ids])
n2 = c.execute("SELECT count(*) FROM t JOIN want ON want.id=t.id").fetchone()[0]
t_tmp = time.perf_counter() - t0
print("大 IN 6000 参数 : %d 行, %.1f ms" % (n1, t_in * 1000))
print("临时表 建表加查 : %d 行, %.1f ms" % (n2, t_tmp * 1000))

t0 = time.perf_counter()
for _ in range(5):
    c.execute("SELECT count(*) FROM t JOIN want ON want.id=t.id").fetchone()
t_reuse = (time.perf_counter() - t0) / 5
t0 = time.perf_counter()
for _ in range(5):
    c.execute("SELECT count(*) FROM t WHERE id IN (%s)" % ph, ids).fetchone()
t_in2 = (time.perf_counter() - t0) / 5
print("复用临时表再查 5 次平均 %.1f ms  vs  每次重发大 IN 平均 %.1f ms" % (t_reuse * 1000, t_in2 * 1000))
print("列表越大且查询越频繁, 临时表越划算; 一次性小列表直接 IN")
