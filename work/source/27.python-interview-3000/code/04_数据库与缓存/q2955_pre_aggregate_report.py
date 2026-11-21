"""报表预聚合: 写时增量维护一张聚合表, 读快百倍且口径可控"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, day TEXT, region TEXT, amount REAL);
CREATE TABLE agg(day TEXT, region TEXT, cnt INTEGER, total REAL,
                 PRIMARY KEY(day, region)) WITHOUT ROWID;
""")
regions = ["north", "south", "east", "west", "mid"]

rows, agg_rows = [], {}
for i in range(1, 120001):
    d, r = "d%02d" % (i % 30), regions[(i // 30) % 5]   # 两个维度独立取模
    amt = round((i % 50) + 0.5, 2)
    rows.append((i, d, r, amt))
    k = (d, r)
    if k in agg_rows:
        c, t = agg_rows[k]
        agg_rows[k] = (c + 1, round(t + amt, 2))
    else:
        agg_rows[k] = (1, amt)
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)", rows)
conn.executemany("INSERT INTO agg VALUES(?,?,?,?)",
                 [(d, r, c, t) for (d, r), (c, t) in sorted(agg_rows.items())])
conn.commit()

Q = "SELECT cnt, total FROM agg WHERE day=? AND region=?"
Q_RAW = "SELECT COUNT(*), SUM(amount) FROM orders WHERE day=? AND region=?"

t0 = time.perf_counter()
for _ in range(200):
    conn.execute(Q, ("d07", "north")).fetchone()
agg_ms = (time.perf_counter() - t0) * 1000 / 200

t0 = time.perf_counter()
for _ in range(20):
    conn.execute(Q_RAW, ("d07", "north")).fetchone()
raw_ms = (time.perf_counter() - t0) * 1000 / 20

a = conn.execute(Q, ("d07", "north")).fetchone()
b = conn.execute(Q_RAW, ("d07", "north")).fetchone()
print("预聚合 %.3f ms/次 vs 实时聚合 %.2f ms/次, 快约 %.0f 倍"
      % (agg_ms, raw_ms, raw_ms / max(agg_ms, 1e-6)))
assert a[0] == b[0] and abs(a[1] - b[1]) < 0.01, "口径必须对得上"

# 写路径增量维护: 新订单进明细, 同事务 upsert 聚合行
conn.execute("BEGIN")
conn.execute("INSERT INTO orders(day, region, amount) VALUES('d07','north',9.9)")
conn.execute("INSERT INTO agg VALUES('d07','north',1,9.9) "
             "ON CONFLICT(day, region) DO UPDATE SET cnt=cnt+1, total=total+9.9")
conn.commit()
c = conn.execute(Q, ("d07", "north")).fetchone()
d = conn.execute(Q_RAW, ("d07", "north")).fetchone()
print("增量维护后 agg cnt=%d total=%.2f, 与明细实时聚合 cnt=%d total=%.2f 一致"
      % (c[0], c[1], d[0], d[1]))
assert c[0] == d[0] and abs(c[1] - d[1]) < 0.01
