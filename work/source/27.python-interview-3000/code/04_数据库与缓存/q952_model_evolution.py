"""状态字段演进: 读兼容映射 + 分批迁移 + 最终校验"""
import sqlite3

LEGACY_MAP = {0: "created", 1: "paid"}    # 旧值 -> 新状态机

def normalize(raw):
    if isinstance(raw, int):
        return LEGACY_MAP.get(raw, "unknown")
    return raw                            # 已是新语义

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT)")
    conn.executemany("INSERT INTO orders (status) VALUES (?)",
                     [("0",), ("1",), ("0",)])

    # 阶段一: 读兼容
    print("兼容读取:", [(i, normalize(s)) for i, s in
          conn.execute("SELECT id, status FROM orders")])

    # 阶段二: 分批把旧值改写为新语义
    while True:
        cur = conn.execute(
            "UPDATE orders SET status = 'created' "
            "WHERE status = '0' AND id IN "
            "(SELECT id FROM orders WHERE status = '0' LIMIT 2)")
        conn.commit()
        if cur.rowcount == 0:
            break
    conn.execute("UPDATE orders SET status='paid' WHERE status='1'")
    conn.commit()

    # 阶段三: 收紧约束
    conn.execute("""CREATE TABLE orders_new (id INTEGER PRIMARY KEY,
                    status TEXT CHECK (status IN ('created','paid')))""")
    conn.execute("INSERT INTO orders_new SELECT id, status FROM orders")
    print("迁移完成:", conn.execute("SELECT * FROM orders_new").fetchall())
