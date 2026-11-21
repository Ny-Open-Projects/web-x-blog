"""综合案例: 夜间巡检报告的自动生成, 检查 三色定级与行动清单"""
import os
import sqlite3
import tempfile
import time

dbpath = os.path.join(tempfile.mkdtemp(), "night.db")
conn = sqlite3.connect(dbpath, isolation_level=None)
conn.execute("PRAGMA page_size=4096")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("""CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER,
                amt REAL, created TEXT)""")
conn.execute("BEGIN IMMEDIATE")
conn.executemany("INSERT INTO users VALUES(?,?)", [(i, "u%d" % i) for i in range(1, 2001)])
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, (i % 2000) + 1, (i % 90) + 1.0, "2026-10-%02d" % ((i % 28) + 1))
                  for i in range(1, 12001)])
conn.execute("COMMIT")
conn.execute("DELETE FROM orders WHERE id % 3 = 0")          # 埋问题 1: 膨胀
conn.execute("DELETE FROM users WHERE id IN (5, 7, 9)")      # 埋问题 2: 孤儿订单

CHECKS = []
def check(name):
    def deco(fn):
        CHECKS.append((name, fn))
        return fn
    return deco

@check("库完整性")
def _(conn):
    r = conn.execute("PRAGMA quick_check").fetchone()[0]
    return ("PASS" if r == "ok" else "FAIL", r)

@check("表膨胀水位")
def _(conn):
    pc = conn.execute("PRAGMA page_count").fetchone()[0]
    fl = conn.execute("PRAGMA freelist_count").fetchone()[0]
    ratio = fl / max(1, pc)
    state = "RED" if ratio > 0.5 else ("YELLOW" if ratio > 0.2 else "GREEN")
    return (state, "freelist 占 %.0f%%, 可回收约 %.1f MB"
            % (ratio * 100, fl * 4096 / 1048576.0))

@check("孤儿订单")
def _(conn):
    n = conn.execute("""SELECT COUNT(*) FROM orders o
                        LEFT JOIN users u ON u.id = o.user_id
                        WHERE u.id IS NULL""").fetchone()[0]
    return ("YELLOW" if n else "GREEN", "%d 条订单指向不存在的用户, 需回溯删除路径" % n)

@check("热点查询计划")
def _(conn):
    sql = "SELECT COUNT(*) FROM orders WHERE created = '2026-10-03'"
    plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchone()[3]
    t0 = time.perf_counter()
    conn.execute(sql).fetchone()
    ms = (time.perf_counter() - t0) * 1000
    bad = "SCAN" in plan
    return ("YELLOW" if bad else "GREEN",
            "%s, %.1f ms%s" % (plan, ms, " -> 建议 created 建索引" if bad else ""))

@check("容量水位")
def _(conn):
    used_gb, cap_gb, growth = 17.0, 20.0, 1.0     # 用量 上限 日增速
    pct = used_gb / cap_gb * 100
    days_left = (cap_gb - used_gb) / growth
    state = "RED" if (pct >= 85 or days_left <= 7) else ("YELLOW" if pct >= 70 else "GREEN")
    return (state, "水位 %.0f%%, 按当前增速剩 %.0f 天, 建议本周走扩容变更" % (pct, days_left))

rank = {"GREEN": 0, "YELLOW": 1, "RED": 2}
report = []
overall = "GREEN"
for name, fn in CHECKS:
    state, detail = fn(conn)
    report.append((name, state, detail))
    color = {"PASS": "GREEN", "FAIL": "RED"}.get(state, state)
    if rank[color] > rank[overall]:
        overall = color

print("=" * 62)
print("夜间巡检报告  %s" % time.strftime("%Y-%m-%d %H:%M"))
print("=" * 62)
for name, state, detail in report:
    print("[%s] %-8s %s" % (state, name, detail))
print("-" * 62)
print("总体定级: %s" % overall)
if overall == "RED":
    print("行动清单: 通知值班; 磁盘扩容走变更单; 膨胀表预约清理窗口; 孤儿数据补修复任务")
elif overall == "YELLOW":
    print("行动清单: 各 WARN 项开工单, 纳入日跟进")
else:
    print("一切正常, 报告归档")
conn.close()
