"""INNER JOIN 过滤位置: ON 与 WHERE 等价且计划相同"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE a(id INTEGER PRIMARY KEY, k INTEGER)")
conn.execute("CREATE TABLE b(id INTEGER PRIMARY KEY, a_id INTEGER, flag TEXT)")
conn.executemany("INSERT INTO a(k) VALUES(?)", [(i % 1000,) for i in range(100000)])
conn.executemany("INSERT INTO b(a_id, flag) VALUES(?,?)",
                 [((i * 3) % 100000 + 1, 'y' if i % 2 else 'n') for i in range(120000)])
conn.execute("CREATE INDEX idx_b_aid ON b(a_id)")
conn.commit()

sql_on = "SELECT COUNT(*) FROM a JOIN b ON a.id = b.a_id AND b.flag = 'y' WHERE a.k = 7"
sql_where = "SELECT COUNT(*) FROM a JOIN b ON a.id = b.a_id WHERE a.k = 7 AND b.flag = 'y'"
r1 = conn.execute(sql_on).fetchone()[0]
r2 = conn.execute(sql_where).fetchone()[0]
print("ON 混合条件结果:", r1, "  WHERE 混合条件结果:", r2, "  相同:", r1 == r2)

def plan(sql):
    return " | ".join(r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql))

print("ON    计划:", plan(sql_on))
print("WHERE 计划:", plan(sql_where))

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchone()
    return (time.perf_counter() - t0) / n * 1000

print(f"ON 耗时 {timed(sql_on):.2f} ms  WHERE 耗时 {timed(sql_where):.2f} ms")
print("结论: 内连接里 ON 与 WHERE 语义等价 计划与耗时相同; 位置差异只在外连接才有后果")
