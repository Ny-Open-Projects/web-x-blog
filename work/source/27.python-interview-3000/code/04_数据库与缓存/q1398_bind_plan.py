"""绑定变量与执行计划: sqlite prepare 一次多次执行, 计划不随参数改变"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, g INTEGER)")
conn.executemany("INSERT INTO t VALUES(?,?)", [(i, i % 3) for i in range(10000)])
conn.execute("CREATE INDEX idx_g ON t(g)")

sql = "SELECT * FROM t WHERE g = ?"
for v in (0, 1):
    p = tuple(r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN SELECT * FROM t WHERE g = %d" % v))
    print(f"g={v} 的计划:", p)

cur = conn.cursor()
cur.execute(sql, (0,))
r1 = len(cur.fetchall())
cur.execute(sql, (1,))
r2 = len(cur.fetchall())
print(f"同一 prepared statement 两次执行: 复用同一计划, g=0 得 {r1} 行, g=1 得 {r2} 行")
print("结论: 计划固定服务所有参数, 倾斜参数需要 hint 或字面量特判")
