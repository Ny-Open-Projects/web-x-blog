"""模拟零停机加列: 加可空列 -> 分批回填 -> 应用新列"""
import sqlite3

def backfill(conn, batch=3):
    total = 0
    while True:
        with conn:
            cur = conn.execute(
                "UPDATE orders SET region = 'cn' WHERE region IS NULL "
                "AND id IN (SELECT id FROM orders WHERE region IS NULL LIMIT ?)",
                (batch,))
            total += cur.rowcount
        if cur.rowcount == 0:
            break
    return total

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amt REAL)")
    conn.executemany("INSERT INTO orders (amt) VALUES (?)",
                     [(i * 1.0,) for i in range(10)])

    conn.execute("ALTER TABLE orders ADD COLUMN region TEXT")   # 可空列, 秒级
    print("扩展完成:", [c[1] for c in conn.execute("PRAGMA table_info(orders)")])

    n = backfill(conn)
    print(f"回填 {n} 行, 未回填:", conn.execute(
        "SELECT count(*) FROM orders WHERE region IS NULL").fetchone()[0])
    print("收缩: 应用确认全量写入带 region 后再收紧约束")
