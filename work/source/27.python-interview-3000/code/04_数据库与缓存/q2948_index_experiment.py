"""索引选择对比实验: 四种索引方案跑同一查询集, 读收益与写代价一起量"""
import sqlite3
import time

ROWS = [(i, i % 8000, ("paid", "pending", "refund")[i % 3],
         round((i % 90) + 0.5, 2)) for i in range(1, 100001)]
QUERIES = [
    ("点查uid",       "SELECT id FROM orders WHERE uid=?", (77,)),
    ("uid加status",   "SELECT id FROM orders WHERE uid=? AND status='paid'", (77,)),
    ("topN按uid序",   "SELECT id FROM orders ORDER BY uid LIMIT 5", ()),
    ("覆盖读amt",     "SELECT amt FROM orders WHERE uid=? AND status='paid'", (77,)),
]


def build(index_sql):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER,"
                 " status TEXT, amt REAL)")
    if index_sql:
        conn.execute(index_sql)          # 先建索引再灌数, 量的是写代价
    t0 = time.perf_counter()
    conn.executemany("INSERT INTO orders VALUES(?,?,?,?)", ROWS)
    conn.commit()
    return conn, (time.perf_counter() - t0) * 1000


def read_bench(conn, loop=15):
    total = 0.0
    for tag, sql, params in QUERIES:
        for _ in range(loop):
            t0 = time.perf_counter()
            conn.execute(sql, params).fetchall()
            total += (time.perf_counter() - t0) * 1000
    return total / loop     # 一轮查询集 4 条 SQL 的平均耗时


plans = [
    ("无索引",             None),
    ("idx_uid",            "CREATE INDEX i1 ON orders(uid)"),
    ("idx_uid_status",     "CREATE INDEX i2 ON orders(uid, status)"),
    ("idx_uid_status_amt", "CREATE INDEX i3 ON orders(uid, status, amt)"),
]
print("%-22s %14s %16s" % ("方案", "写10万行", "查询集一轮"))
for name, idx in plans:
    conn, w = build(idx)
    r = read_bench(conn)
    print("%-22s %11.0f ms %13.2f ms" % (name, w, r))
    conn.close()
print("注意: topN 按 uid 序在无索引时要全表排序, 是本轮差距的主要来源")
print("结论: 索引方案要对准查询集设计, 每多一个索引写路径就多一份维护费")
