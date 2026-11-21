import sqlite3

DDL = """
CREATE TABLE IF NOT EXISTS idempotency (
    key TEXT PRIMARY KEY,
    status TEXT NOT NULL,
    result TEXT
)
"""


def process_callback(conn: sqlite3.Connection, idem_key: str, amount: int) -> str:
    """唯一主键是并发下的最终防线,业务执行与幂等记录同事务。"""
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO idempotency(key,status) VALUES(?,'processing')",
                    (idem_key,))
    except sqlite3.IntegrityError:
        row = conn.execute("SELECT status,result FROM idempotency WHERE key=?",
                           (idem_key,)).fetchone()
        return row[1] or "duplicated"

    # --- 真正的业务:入账 ---
    result = f"credited {amount}"
    conn.execute("UPDATE idempotency SET status='done',result=? WHERE key=?",
                 (result, idem_key))
    conn.commit()
    return result


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute(DDL)
    print(process_callback(conn, "pay:1001", 100))
    print(process_callback(conn, "pay:1001", 100))  # 重复回调,返回旧结果
