"""EXISTS vs IN 实测: NULL 语义差异与四种写法的代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, vip INTEGER)")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(i, 1 if i % 10 == 0 else 0) for i in range(1, 100001)])
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(i, (i * 7) % 50000 + 1) for i in range(1, 150001)])
conn.execute("CREATE INDEX idx_o_user ON orders(user_id)")
conn.commit()

def timed(sql, n=3):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

q_in = ("SELECT COUNT(*) FROM users WHERE id IN "
        "(SELECT user_id FROM orders WHERE user_id <= 5000)")
q_exists = ("SELECT COUNT(*) FROM users u WHERE EXISTS "
            "(SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.user_id <= 5000)")
q_not_in = "SELECT COUNT(*) FROM users WHERE id NOT IN (SELECT user_id FROM orders)"
q_not_exists = ("SELECT COUNT(*) FROM users u WHERE NOT EXISTS "
                "(SELECT 1 FROM orders o WHERE o.user_id = u.id)")
print(f"IN       半连接  : {timed(q_in):8.2f} ms")
print(f"EXISTS   半连接  : {timed(q_exists):8.2f} ms")
print(f"NOT IN   反连接  : {timed(q_not_in):8.2f} ms")
print(f"NOT EXISTS 反连接: {timed(q_not_exists):8.2f} ms")

# NULL 语义差异: 子查询含 NULL 时 NOT IN 全空, NOT EXISTS 不受影响
conn.execute("INSERT INTO orders VALUES(999999, NULL)")
conn.commit()
print("子查询混入一个 NULL 后: NOT IN =", conn.execute(q_not_in).fetchone()[0],
      "  NOT EXISTS =", conn.execute(q_not_exists).fetchone()[0])
print("结论: 否定语义一律用 NOT EXISTS 免疫 NULL; 肯定语义 IN 与 EXISTS 现代优化器多可等价改写, 实测为准")
