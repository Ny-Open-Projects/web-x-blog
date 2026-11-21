"""订单状态机: 合法流转表 + 条件 UPDATE 的 CAS"""
import sqlite3
from dataclasses import dataclass

TRANSITIONS = {
    "created": {"paid", "cancelled"},
    "paid": {"shipped", "refunded"},
    "shipped": {"done"},
    "cancelled": set(),
    "refunded": set(),
    "done": set(),
}

@dataclass
class Order:
    id: int
    status: str

def transition(conn, order: Order, target: str) -> bool:
    if target not in TRANSITIONS[order.status]:
        return False
    cur = conn.execute(
        "UPDATE orders SET status = ? WHERE id = ? AND status = ?",
        (target, order.id, order.status))
    conn.commit()
    if cur.rowcount:
        order.status = target
    return cur.rowcount == 1

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT
                    CHECK (status IN ('created','paid','shipped','done','cancelled','refunded')))""")
    conn.execute("INSERT INTO orders VALUES (1, 'created')")
    o = Order(1, "created")

    print("created->paid:", transition(conn, o, "paid"))
    print("paid->shipped:", transition(conn, o, "shipped"))
    print("shipped->cancelled 非法:", transition(conn, o, "cancelled"))
    print("最终状态:", o.status)
