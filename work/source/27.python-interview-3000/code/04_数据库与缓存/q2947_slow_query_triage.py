"""慢查询定位全流程: 慢日志采样 计划解读 加索引 复测出报告"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER,"
             " status TEXT, amt REAL)")
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, i % 5000, ("paid", "pending", "refund")[i % 3],
                   round((i % 100) + 0.5, 2)) for i in range(1, 200001)])
conn.commit()

SLOW_MS = 10.0
slow_log = []


def run(tag, sql, params=()):
    t0 = time.perf_counter()
    out = conn.execute(sql, params).fetchall()
    ms = (time.perf_counter() - t0) * 1000
    if ms >= SLOW_MS:                        # 慢日志阈值 10ms
        slow_log.append("%s: %.1f ms" % (tag, ms))
    return out, ms


sql = "SELECT id, amt FROM orders WHERE uid=? AND status='paid'"
run("预热", sql, (42,))                      # 先跑一遍排除冷缓存干扰
_, ms1 = run("优化前 uid=42", sql, (42,))
plan1 = conn.execute("EXPLAIN QUERY PLAN " + sql, (42,)).fetchone()[3]
print("优化前 %.1f ms, 计划: %s" % (ms1, plan1))

# 定位: SCAN 全表 20 万行, 判定缺 (uid, status) 复合索引
conn.execute("CREATE INDEX idx_o_uid_status ON orders(uid, status)")
conn.commit()
plan2 = conn.execute("EXPLAIN QUERY PLAN " + sql, (42,)).fetchone()[3]
out, ms2 = run("优化后 uid=42", sql, (42,))
print("优化后 %.1f ms, 计划: %s" % (ms2, plan2))
print("命中 %d 行, 提速约 %.0f 倍" % (len(out), ms1 / max(ms2, 0.01)))
print("慢日志留存:", slow_log)
