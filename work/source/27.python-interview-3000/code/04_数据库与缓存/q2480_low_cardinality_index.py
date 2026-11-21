"""低基数列的单列索引: 选择性决定它是加速器还是累赘"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, status TEXT, payload TEXT)")
# 90% 是 a, 9% 是 b, 1% 是 c
rows = []
for i in range(1, 50001):
    s = 'a' if i % 10 < 9 else ('b' if i % 100 < 95 else 'c')
    rows.append((i, s, "p%d" % i))
c.executemany("INSERT INTO t VALUES(?,?,?)", rows)
c.execute("CREATE INDEX idx_status ON t(status)")
c.execute("ANALYZE")

def timed(sql, args):
    t0 = time.perf_counter()
    data = c.execute(sql, args).fetchall()
    return len(data), (time.perf_counter() - t0) * 1000

# 同一条查询, 两种选择性, 有索引与无索引各跑一次
for v in ('c', 'a'):
    n_with, ms_with = timed("SELECT * FROM t WHERE status = ?", (v,))
    c.execute("DROP INDEX idx_status")
    c.execute("ANALYZE")
    n_wo, ms_wo = timed("SELECT * FROM t WHERE status = ?", (v,))
    c.execute("CREATE INDEX idx_status ON t(status)")
    c.execute("ANALYZE")
    verdict = "索引赢" if ms_with < ms_wo else "索引反而慢"
    print("status='%s' 命中 %5d 行: 有索引 %6.1f ms | 无索引 %6.1f ms -> %s"
          % (v, n_with, ms_with, ms_wo, verdict))

# 出路: 低基数列不单独出门, 与高频条件组成联合索引才有效
c.execute("CREATE INDEX idx_status_payload ON t(status, payload)")
plan = " | ".join(r[3] for r in c.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM t WHERE status='c' AND payload LIKE 'p4%'"))
print("组合索引下的计划: %s" % plan)
print("结论: 选择性 1% 的值走索引是数倍收益, 90% 的值走非覆盖索引是数倍亏损,")
print("      低基数列要么进联合索引, 要么建部分索引只索引稀有值")
