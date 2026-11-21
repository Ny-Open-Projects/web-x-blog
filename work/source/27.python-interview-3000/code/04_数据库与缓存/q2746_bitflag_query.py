"""位标志列的查询设计: 位与条件用不上索引, 拆列与 partial index 是出路"""
import sqlite3
import time

VIP, VERIFIED, BANNED = 1, 2, 4

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT, flags INTEGER)")
rows = []
for i in range(1, 30001):
    f = VIP
    if i % 3 == 0:
        f |= VERIFIED
    if i % 10 == 0:
        f |= BANNED
    rows.append((i, "u%d" % i, f))
c.executemany("INSERT INTO user VALUES(?,?,?)", rows)
c.execute("CREATE INDEX idx_flags ON user(flags)")

def plan(sql):
    return c.execute("EXPLAIN QUERY PLAN " + sql).fetchone()[3]

def timed(label, sql):
    t0 = time.perf_counter()
    n = len(c.execute(sql).fetchall())
    print("%s: %d 行, %.1f ms" % (label, n, (time.perf_counter() - t0) * 1000))

sql_bit = "SELECT id FROM user WHERE flags & 3 = 3"
print("位与查询计划:", plan(sql_bit))
timed("位与查询 包含 vip 与 verified", sql_bit)
sql_eq = "SELECT id FROM user WHERE flags = 3"
print("等值查询计划:", plan(sql_eq))
timed("等值查询 flags 恰好等于 3", sql_eq)

# 出路: 高频组合拆布尔列 + partial index
c.execute("""CREATE TABLE user2 (id INTEGER PRIMARY KEY, name TEXT,
             vip INTEGER, verified INTEGER, banned INTEGER)""")
c.executemany("INSERT INTO user2 VALUES(?,?,?,?,?)",
              [(i, n, 1 if f & VIP else 0, 1 if f & VERIFIED else 0, 1 if f & BANNED else 0)
               for i, n, f in rows])
c.execute("CREATE INDEX idx_vip ON user2(id) WHERE vip = 1 AND verified = 1")
sql_cols = "SELECT id FROM user2 WHERE vip = 1 AND verified = 1"
print("拆列 + partial index 计划:", plan(sql_cols))
timed("拆列查询 vip 且 verified", sql_cols)
