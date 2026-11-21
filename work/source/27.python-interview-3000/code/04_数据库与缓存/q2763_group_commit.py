"""组提交的概念: 逐条提交与攒批提交的落盘次数与耗时对比"""
import os
import sqlite3
import tempfile
import time

d = tempfile.mkdtemp()

def run(label, per_commit, total=100):
    db = os.path.join(d, "gc_%s.db" % label)
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute("PRAGMA journal_mode=DELETE")   # 回滚日志模式, 每事务一次完整落盘
    conn.execute("PRAGMA synchronous=FULL")      # 每次提交强制 fsync
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v INTEGER)")
    t0 = time.perf_counter()
    done = 0
    commits = 0
    while done < total:
        conn.execute("BEGIN")
        for _ in range(min(per_commit, total - done)):
            done += 1
            conn.execute("INSERT INTO t VALUES(?,?)", (done, done))
        conn.execute("COMMIT")                   # 每个事务对应一次真正的落盘
        commits += 1
    cost = (time.perf_counter() - t0) * 1000
    conn.close()
    os.remove(db)
    return commits, cost

c1 = run("solo", 1)
c50 = run("group50", 50)
print("100 行: 逐条提交 %d 次落盘 耗时 %.0f ms | 攒 50 条一组 %d 次落盘 耗时 %.0f ms"
      % (c1[0], c1[1], c50[0], c50[1]))
print("组提交在数据库内部自动攒批, 并发越高, 单条均摊的落盘代价越低")
