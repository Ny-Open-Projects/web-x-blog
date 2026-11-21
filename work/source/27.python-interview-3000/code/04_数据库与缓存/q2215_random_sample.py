"""随机抽样的代价: ORDER BY random() 全表排序 vs 蓄水池抽样"""
import random
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
c.executemany("INSERT INTO t VALUES(?,?)", [(i, "v%d" % i) for i in range(1, 50001)])

plan = " | ".join(r[3] for r in
                  c.execute("EXPLAIN QUERY PLAN SELECT id FROM t ORDER BY random() LIMIT 5"))
print("ORDER BY random() 计划:", plan)

t0 = time.perf_counter()
rows = c.execute("SELECT id FROM t ORDER BY random() LIMIT 5").fetchall()
print("全表排序取 5 条   : %6.1f ms, 样本 %s" % ((time.perf_counter() - t0) * 1000, [r[0] for r in rows]))

t0 = time.perf_counter()
rows2 = c.execute("SELECT id FROM t WHERE id >= (abs(random()) % 49996) + 1 "
                  "ORDER BY id LIMIT 5").fetchall()
print("随机起点区间      : %6.2f ms, 样本 %s 有偏" % ((time.perf_counter() - t0) * 1000, [r[0] for r in rows2]))

t0 = time.perf_counter()
sample, n = [], 0
for (rid,) in c.execute("SELECT id FROM t"):
    n += 1
    if len(sample) < 5:
        sample.append(rid)
    else:
        j = random.randrange(n)
        if j < 5:
            sample[j] = rid
print("蓄水池抽样 O N 一趟: %6.1f ms, 样本 %s 等概率" % ((time.perf_counter() - t0) * 1000, sorted(sample)))
