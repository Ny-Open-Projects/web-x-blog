"""唯一约束实现幂等: 重复回调返回既有结果"""
import sqlite3

SCHEMA = """
CREATE TABLE payment (
    request_id TEXT PRIMARY KEY,     -- 外部流水号: 幂等键
    order_no  TEXT NOT NULL, amount INT NOT NULL, status TEXT NOT NULL
);
"""

def handle_callback(conn, request_id, order_no, amount):
    try:
        conn.execute(
            "INSERT INTO payment (request_id, order_no, amount, status) "
            "VALUES (?, ?, ?, 'paid')", (request_id, order_no, amount))
        conn.commit()
        return "首次处理"
    except sqlite3.IntegrityError:
        conn.rollback()
        return "重复请求, 返回既有结果"

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA)
    for i in range(3):                  # 模拟回调重试 3 次
        print(f"第{i + 1}次回调:", handle_callback(conn, "req-1", "O100", 9900))
    print("落库:", conn.execute("SELECT request_id, status FROM payment").fetchall())
