"""sqlite3 演示唯一约束幂等: 重复请求返回首次结果"""
import sqlite3

SETUP = """
CREATE TABLE payment (
  id INTEGER PRIMARY KEY,
  idempotency_key TEXT NOT NULL UNIQUE,   -- 幂等唯一键
  order_no TEXT NOT NULL,
  amount INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'success'
)
"""


def pay(conn: sqlite3.Connection, key: str, order: str, amount: int) -> dict:
    try:
        conn.execute(
            "INSERT INTO payment(idempotency_key, order_no, amount) VALUES (?, ?, ?)",
            (key, order, amount),
        )
        conn.commit()
        return {"duplicated": False, "amount": amount}
    except sqlite3.IntegrityError:
        # MySQL 写法: INSERT ... ON DUPLICATE KEY UPDATE 或先 SELECT
        row = conn.execute(
            "SELECT amount, status FROM payment WHERE idempotency_key = ?", (key,)
        ).fetchone()
        return {"duplicated": True, "amount": row[0], "status": row[1]}


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute(SETUP)
    print("首次请求:", pay(conn, "k-1", "o-100", 9900))
    print("重复请求:", pay(conn, "k-1", "o-100", 9900))   # 不会重复扣款
    print("表内记录数:", conn.execute("SELECT COUNT(*) FROM payment").fetchone()[0])
