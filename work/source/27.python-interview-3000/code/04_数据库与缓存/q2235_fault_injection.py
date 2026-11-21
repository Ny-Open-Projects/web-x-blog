"""故障注入演练: 在客户端与库之间插一层可编程故障"""
import sqlite3

class FaultInjector:
    """按第 N 次调用注入真实驱动形态的异常"""
    def __init__(self, target, schedule):
        self.target = target
        self.schedule = list(schedule)
        self.calls = 0

    def __call__(self, *args, **kw):
        self.calls += 1
        for n, exc in self.schedule:
            if n == self.calls:
                raise exc
        return self.target(*args, **kw)

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
conn.commit()

def raw_query(sql):
    return conn.execute(sql).fetchall()

query = FaultInjector(raw_query, [(1, sqlite3.OperationalError("database is locked")),
                                  (2, sqlite3.OperationalError("database is locked"))])

def retry(fn, tries=5):
    for i in range(1, tries + 1):
        try:
            return fn(), i
        except sqlite3.OperationalError:
            continue
    raise RuntimeError("重试耗尽")

rows, used = retry(lambda: query("SELECT count(*) FROM t"))
print("注入两次 locked, 第 %d 次成功, 结果 %s, 注入器拦截 %d 次调用" % (used, rows[0][0], query.calls))

def raw_write(v):
    conn.execute("INSERT INTO t(v) VALUES(?)", (v,))
    conn.commit()

write = FaultInjector(raw_write, [(1, sqlite3.OperationalError("disk I/O error"))])
_, used_w = retry(lambda: write("x1"))
print("写路径注入 disk I/O error, 第 %d 次成功, 终态行数 %d <- 数据一致无半提交"
      % (used_w, conn.execute("SELECT count(*) FROM t").fetchone()[0]))
