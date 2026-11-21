"""大表 join 的驱动序实测: CROSS JOIN 钉住顺序, 驱动侧与索引共同决定代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE big (id INTEGER PRIMARY KEY, k INTEGER)")
c.execute("CREATE TABLE small (id INTEGER PRIMARY KEY, tag TEXT)")
c.executemany("INSERT INTO big VALUES(?,?)", [(i, i % 1000) for i in range(1, 30001)])
c.executemany("INSERT INTO small VALUES(?,?)", [(i, "t%d" % i) for i in range(1, 101)])

def drive(label, sql):
    t0 = time.perf_counter()
    n = c.execute(sql).fetchone()[0]
    print("%s: %d 行, %.1f ms" % (label, n, (time.perf_counter() - t0) * 1000))

# 1) big 驱动: 3 万行先过滤 k<=100 再逐行探测 small 主键
drive("big 驱动, 过滤后探测 small",
      "SELECT COUNT(*) FROM big CROSS JOIN small WHERE big.k <= 100 AND small.id = big.k")
# 2) small 驱动, big.k 无索引: 100 行各触发一次 3 万行全扫
drive("small 驱动, big.k 无索引",
      "SELECT COUNT(*) FROM small CROSS JOIN big WHERE big.k = small.id")
# 3) small 驱动, big.k 有索引: 100 次索引探测
c.execute("CREATE INDEX idx_big_k ON big(k)")
drive("small 驱动, big.k 有索引",
      "SELECT COUNT(*) FROM small CROSS JOIN big WHERE big.k = small.id")
print("规律: 驱动序由过滤选择性与对侧索引共同决定, 优化器选错时用 CROSS JOIN 钉序保命")
