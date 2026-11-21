"""GROUP BY 的临时表代价: 索引序分组 vs 内部临时表"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, user_id INTEGER, kind TEXT)")
conn.execute("CREATE INDEX idx_user_kind ON events(user_id, kind)")
conn.executemany("INSERT INTO events VALUES(?,?,?)",
                 [(i, i % 500, "k%d" % (i % 4)) for i in range(5000)])

def plan(sql):
    print("SQL:", sql)
    for r in conn.execute("EXPLAIN QUERY PLAN " + sql):
        print("   ", r[3])

plan("SELECT user_id, COUNT(*) FROM events GROUP BY user_id")
plan("SELECT kind, COUNT(*) FROM events GROUP BY kind")
plan("SELECT user_id, kind, COUNT(*) FROM events GROUP BY user_id, kind")
print("结论: 分组列与索引前缀对齐则免临时表, 否则建内部临时表再聚合")
