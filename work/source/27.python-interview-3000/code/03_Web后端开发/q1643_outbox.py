"""事务内发消息的坑与 Outbox 模式(标准库 sqlite3)。"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT);
CREATE TABLE outbox (id INTEGER PRIMARY KEY AUTOINCREMENT, event TEXT, sent INT DEFAULT 0);
""")


def place_order(status="paid"):
    """正确: 业务写与事件写放同一个事务, 提交后由 relay 投递。"""
    with conn:
        conn.execute("INSERT INTO orders (status) VALUES (?)", (status,))
        conn.execute("INSERT INTO outbox (event) VALUES (?)", (f"order.{status}",))
    return conn.execute("SELECT MAX(id) FROM outbox").fetchone()[0]


def relay():
    """投递中继: 只读未发送事件, 发送成功才置位; 至少一次投递 + 消费端幂等。"""
    rows = conn.execute("SELECT id, event FROM outbox WHERE sent = 0").fetchall()
    sent = []
    for oid, event in rows:
        sent.append(event)                       # 此处假装调用 broker
        conn.execute("UPDATE outbox SET sent = 1 WHERE id = ?", (oid,))
    conn.commit()
    return sent


place_order()
print("下单后 outbox:", conn.execute("SELECT id, event, sent FROM outbox").fetchall())
print("relay 投递:", relay())
print("投递后 outbox:", conn.execute("SELECT id, event, sent FROM outbox").fetchall())


def place_order_rollback():
    """反例: 业务失败回滚, 但事务内直接发的消息不会跟着回滚。"""
    ghost = []
    try:
        with conn:
            conn.execute("INSERT INTO orders (status) VALUES ('bad')")
            ghost.append("order.bad")            # 事务内直接调 broker 的效果
            raise RuntimeError("下游约束失败")
    except RuntimeError as e:
        print("回滚原因:", e)
    return ghost


ghost = place_order_rollback()
print("幽灵消息(业务回滚但消息已发):", ghost)
print("outbox 模式下 orders 行数:", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
