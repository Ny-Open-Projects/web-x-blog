"""JSON 字段的生成列: VIRTUAL 算在读 STORED 算在写, STORED 加索引后查询走索引"""
import json
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
N = 20000
payloads = [json.dumps({"uid": i, "amt": (i % 90) + 10}) for i in range(1, N + 1)]

def build(kind):
    ddl = "CREATE TABLE t_%s (id INTEGER PRIMARY KEY, payload TEXT" % kind
    coltype = {"virt": "VIRTUAL", "stor": "STORED"}.get(kind)
    if coltype:
        ddl += ", amt INTEGER GENERATED ALWAYS AS (json_extract(payload,'$.amt')) %s" % coltype
    c.execute(ddl + ")")
    t0 = time.perf_counter()
    c.executemany("INSERT INTO t_%s VALUES(?,?)" % kind,
                  [(i, p) for i, p in enumerate(payloads, 1)])
    return (time.perf_counter() - t0) * 1000

def query(kind):
    where = ("json_extract(payload,'$.amt')" if kind == "raw" else "amt") + " BETWEEN 20 AND 30"
    sql = "SELECT COUNT(*) FROM t_%s WHERE %s" % (kind, where)
    t0 = time.perf_counter()
    for _ in range(5):
        n = c.execute(sql).fetchone()[0]
    return n, (time.perf_counter() - t0) * 1000 / 5

w_raw = build("raw")
n1, r_raw = query("raw")
w_virt = build("virt")
n2, r_virt = query("virt")
w_stor = build("stor")
c.execute("CREATE INDEX idx_amt ON t_stor(amt)")
n3, r_stor = query("stor")

print("写入: raw %.0f ms | virtual %.0f ms | stored %.0f ms (stored 写时求值最慢)"
      % (w_raw, w_virt, w_stor))
print("查询均值: raw %.1f ms | virtual %.1f ms | stored+索引 %.1f ms, 命中 %d/%d/%d 行"
      % (r_raw, r_virt, r_stor, n1, n2, n3))
print("stored+索引计划:", c.execute(
    "EXPLAIN QUERY PLAN SELECT COUNT(*) FROM t_stor WHERE amt BETWEEN 20 AND 30").fetchone()[3])
