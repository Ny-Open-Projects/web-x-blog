"""百分位统计: NTILE 分桶与手写分位的口径对齐"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE resp (id INTEGER PRIMARY KEY, ms REAL)")
c.executemany("INSERT INTO resp VALUES(?,?)",
              [(i, 10 + (i * 13) % 90 + ((i % 50) == 0) * 400) for i in range(1, 2001)])

rows = c.execute("""
  SELECT bucket, COUNT(*), MIN(ms), MAX(ms) FROM (
    SELECT ms, NTILE(4) OVER (ORDER BY ms) AS bucket FROM resp
  ) GROUP BY bucket ORDER BY bucket""").fetchall()
for b, n, lo, hi in rows:
    print("Q%d: %d 个样本, 区间 [%.0f, %.0f] ms" % (b, n, lo, hi))

allms = sorted(r[0] for r in c.execute("SELECT ms FROM resp"))
def pct(p):
    k = max(0, min(len(allms) - 1, int(round(p / 100.0 * (len(allms) - 1)))))
    return allms[k]
print("手写分位: P50=%.0f P95=%.0f P99=%.0f ms" % (pct(50), pct(95), pct(99)))
print("NTILE 顶桶的上界 %.0f ms 是 Q3 不是 P95, 口径不同不能互换" % rows[-1][3])
