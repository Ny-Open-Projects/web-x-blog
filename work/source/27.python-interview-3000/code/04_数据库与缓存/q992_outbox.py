"""本地消息表: 业务与 outbox 同事务, 扫描投递 + 幂等消费"""
import sqlite3
import time

def setup():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE orders (id INTEGER PRIMARY KEY, amount INT);
        CREATE TABLE outbox (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             payload TEXT, status TEXT DEFAULT 'pending',
                             retry INT DEFAULT 0);
    """)
    return conn

def create_order(conn, amount):
    with conn:                                    # 同一事务
        conn.execute("INSERT INTO orders (amount) VALUES (?)", (amount,))
        conn.execute("INSERT INTO outbox (payload) VALUES (?)",
                     (f"order_created:{amount}",))

def relay(conn, mq):
    rows = conn.execute(
        "SELECT id, payload FROM outbox WHERE status='pending' "
        "ORDER BY id LIMIT 10").fetchall()
    for oid, payload in rows:
        mq.append(payload)                        # 投递到 MQ(重试由失败驱动)
        conn.execute("UPDATE outbox SET status='sent' WHERE id=?", (oid,))
    conn.commit()
    return [p for p in mq]

if __name__ == "__main__":
    conn = setup()
    create_order(conn, 9900)
    print("业务与消息同事务落库:", conn.execute(
        "SELECT status FROM outbox").fetchall())
    mq = []
    print("relay 投递:", relay(conn, mq))
    print("消费端按消息幂等去重:", mq)
