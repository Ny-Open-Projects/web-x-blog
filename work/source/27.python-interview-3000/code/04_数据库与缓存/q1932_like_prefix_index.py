"""LIKE 与索引: 通配符位置与 case_sensitive_like 的实测"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT)")
conn.executemany("INSERT INTO users(email) VALUES(?)",
                 [("user%05d@example.com" % i,) for i in range(50000)])
conn.execute("CREATE INDEX idx_email ON users(email)")
conn.commit()

def plan(sql):
    return " | ".join(r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql))

q_prefix = "SELECT id FROM users WHERE email LIKE 'user005%'"
q_suffix = "SELECT id FROM users WHERE email LIKE '%@example.com'"
print("默认设置 前缀 LIKE ->", plan(q_prefix))
print("默认设置 后缀 LIKE ->", plan(q_suffix))

# 默认 LIKE 对 ASCII 大小写不敏感, BINARY 索引帮不上忙; 打开开关后前缀 LIKE 才走索引
conn.execute("PRAGMA case_sensitive_like = ON")
print("开关打开 前缀 LIKE ->", plan(q_prefix))
print("开关打开 后缀 LIKE ->", plan(q_suffix))

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

print(f"前缀 LIKE 耗时 {timed(q_prefix):6.2f} ms vs 后缀 LIKE 耗时 {timed(q_suffix):6.2f} ms")

# 后缀需求的替代: 倒序串索引
conn.execute("CREATE TABLE rev(email TEXT, email_rev TEXT)")
conn.executemany("INSERT INTO rev VALUES(?,?)",
                 [(r[0], r[0][::-1]) for r in conn.execute("SELECT email FROM users")])
conn.execute("CREATE INDEX idx_rev ON rev(email_rev)")
print("倒序串查后缀计划   ->", plan("SELECT email FROM rev WHERE email_rev LIKE 'moc.elpmaxe%'"))
print("结论: abc% 可走索引, %abc 与 %abc% 只能全扫; 后缀需求用倒序串索引或全文索引")
