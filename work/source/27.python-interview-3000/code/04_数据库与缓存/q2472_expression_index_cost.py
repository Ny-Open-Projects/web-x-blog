"""表达式索引的写代价: 读路径提速的账要从写路径扣"""
import sqlite3
import time

N = 30000

def build(label, ddl):
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
    if ddl:
        c.execute(ddl)
    rows = [(i, "User.%d@Example.COM" % i) for i in range(1, N + 1)]
    t0 = time.perf_counter()
    c.executemany("INSERT INTO users(id, email) VALUES(?,?)", rows)
    cost = (time.perf_counter() - t0) * 1000
    conn.close()
    return cost

t_plain = build("无函数索引", None)
t_normal = build("普通索引", "CREATE INDEX idx_email ON users(email)")
t_expr = build("表达式索引", "CREATE INDEX idx_email_lc ON users(lower(email))")
print("写入 %d 行耗时: 无索引 %.0f ms | 普通索引 %.0f ms | 表达式索引 %.0f ms"
      % (N, t_plain, t_normal, t_expr))
print("表达式索引每行写入多一次函数求值, 比普通索引慢的部分就是读路径省下的账")

# 读路径: 表达式索引让 lower 等值查询免于全表扫描
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
c.execute("CREATE INDEX idx_email_lc ON users(lower(email))")
c.executemany("INSERT INTO users VALUES(?,?)",
              [(i, "User.%d@Example.COM" % i) for i in range(1, 20001)])
sql = "SELECT id FROM users WHERE lower(email) = ?"
plan = " | ".join(r[3] for r in c.execute("EXPLAIN QUERY PLAN " + sql, ("user.42@example.com",)))
print("表达式索引上的查询计划: %s" % plan)
