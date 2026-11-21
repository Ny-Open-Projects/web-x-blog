"""验证覆盖索引: 建联合索引后观察 Extra 出现 Using index"""
import sqlite3  # 标准库即可演示同样的索引原理, MySQL 下用 EXPLAIN 观察同理

SETUP = [
    "CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, status TEXT, amount REAL)",
    "CREATE INDEX idx_user_status ON orders(user_id, status)",
]


def count_by_user(conn: sqlite3.Connection, user_id: int) -> int:
    """SELECT 只用 user_id/status/id, 全部可从索引取得 -> 覆盖索引"""
    sql = "SELECT COUNT(*) FROM orders WHERE user_id = ? AND status = 'paid'"
    row = conn.execute(sql, (user_id,)).fetchone()
    plan = conn.execute("EXPLAIN QUERY PLAN " + sql, (user_id,)).fetchall()
    return row[0], plan


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    for sql in SETUP:
        conn.execute(sql)
    conn.executemany(
        "INSERT INTO orders(user_id, status, amount) VALUES (?, ?, ?)",
        [(i % 100, "paid" if i % 3 else "new", 9.9) for i in range(1000)],
    )
    conn.commit()
    total, plan = count_by_user(conn, 7)
    print("user 7 已支付订单数:", total)
    for step in plan:
        print("执行计划:", step)  # SEARCH orders USING COVERING INDEX 说明无需回表
