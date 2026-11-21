"""视图展开与谓词下推: 嵌套视图的代价实测"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, paid INTEGER)")
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, i % 1000, i % 500, 1 if i % 3 else 0) for i in range(100000)])
conn.execute("CREATE INDEX idx_o_user ON orders(user_id)")
conn.commit()

conn.executescript("""
CREATE VIEW v_paid AS SELECT id, user_id, amount FROM orders WHERE paid = 1;
CREATE VIEW v_big AS SELECT id, user_id, amount FROM v_paid WHERE amount >= 100;
CREATE VIEW v_user AS SELECT user_id, SUM(amount) AS total FROM v_big GROUP BY user_id;
""")

def plan(sql):
    return " | ".join(r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql))

q_direct = "SELECT SUM(amount) FROM orders WHERE paid = 1 AND amount >= 100 AND user_id = 107"
q_view = "SELECT total FROM v_user WHERE user_id = 107"
print("直写三条件 ->", plan(q_direct))
print("三层视图   ->", plan(q_view))
print("结果一致   ->", conn.execute(q_direct).fetchone()[0] == conn.execute(q_view).fetchone()[0])

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchone()
    return (time.perf_counter() - t0) / n * 1000

print(f"直写 {timed(q_direct):.2f} ms vs 三层视图 {timed(q_view):.2f} ms")

# 下推失灵的场景: 视图带 LIMIT, 外层条件不敢推进去
conn.execute("CREATE VIEW v_top AS SELECT id, user_id, amount FROM orders ORDER BY amount DESC LIMIT 100")
print("带 LIMIT 的视图 ->", plan("SELECT * FROM v_top WHERE user_id = 7"))
print("结论: 简单视图会被展开并下推谓词 代价近似直写; 含 LIMIT 或去重的视图是黑盒 外层条件只能在结果上过滤")
