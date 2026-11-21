"""级联更新的牵动面实测与批次控制: 一条父更新牵动两万行, 分批拆短锁窗口"""
import os
import sqlite3
import tempfile
import time

dbpath = os.path.join(tempfile.mkdtemp(), "cascade.db")
conn = sqlite3.connect(dbpath, isolation_level=None)
conn.execute("PRAGMA foreign_keys=ON")
conn.execute("CREATE TABLE team (id INTEGER PRIMARY KEY, code TEXT UNIQUE)")
conn.execute("""CREATE TABLE member (
    id INTEGER PRIMARY KEY,
    team_code TEXT REFERENCES team(code) ON UPDATE CASCADE,
    name TEXT)""")
conn.execute("INSERT INTO team VALUES(1, 'T01')")
conn.execute("BEGIN IMMEDIATE")
conn.executemany("INSERT INTO member VALUES(?,?,?)",
                 [(i, "T01", "m%d" % i) for i in range(1, 20001)])
conn.execute("COMMIT")

t0 = time.perf_counter()
conn.execute("BEGIN IMMEDIATE")
conn.execute("UPDATE team SET code='T99' WHERE id=1")     # 一条父更新
conn.execute("COMMIT")
cost = (time.perf_counter() - t0) * 1000
n = conn.execute("SELECT COUNT(*) FROM member WHERE team_code='T99'").fetchone()[0]
print("一条父表 UPDATE 被 CASCADE 放大成 %d 行子表写入, 单事务耗时 %.0f ms" % (n, cost))

# 批次控制: 不用 CASCADE, 应用分批搬家, 每批一个短事务
conn.execute("INSERT INTO team VALUES(2, 'T02')")
conn.execute("BEGIN IMMEDIATE")
conn.executemany("INSERT INTO member VALUES(?,?,?)",
                 [(30000 + i, "T02", "m%d" % i) for i in range(1, 20001)])
conn.execute("COMMIT")
conn.execute("INSERT INTO team VALUES(3, 'T77')")         # 新码先落位
lo, hi_all, batch = 30001, 50000, 10000
while lo <= hi_all:
    hi = min(lo + batch - 1, hi_all)
    t0 = time.perf_counter()
    conn.execute("BEGIN IMMEDIATE")
    conn.execute("UPDATE member SET team_code='T77' WHERE id BETWEEN ? AND ?", (lo, hi))
    conn.execute("COMMIT")
    print("  批次 %d-%d 已搬, 本批锁窗口 %.0f ms" % (lo, hi, (time.perf_counter() - t0) * 1000))
    lo = hi + 1
conn.execute("BEGIN IMMEDIATE")
conn.execute("DELETE FROM team WHERE id=2")               # 旧码无子行引用后安全下线
conn.execute("COMMIT")
left = conn.execute("SELECT COUNT(*) FROM member WHERE team_code='T02'").fetchone()[0]
print("批次搬完后旧码残留 %d 行, 父表旧码行已下线" % left)
conn.close()
