"""代理键 + 业务键: 生成 order_no 并以此锚定 upsert"""
import secrets
import sqlite3
import time

def gen_order_no() -> str:
    ts = f"{int(time.time() * 1000) % 10**10:010d}"
    return f"PO{ts}{secrets.randbelow(10**4):04d}"     # 时间 + 随机, 不可猜测

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_no TEXT NOT NULL UNIQUE, amount INT)""")

    no = gen_order_no()
    for i in range(2):                     # 重复提交同一 order_no
        try:
            conn.execute("INSERT INTO orders (order_no, amount) VALUES (?, ?)",
                         (no, 9900))
            conn.commit()
            print(f"第{i + 1}次提交 {no}: 成功")
        except sqlite3.IntegrityError:
            conn.rollback()
            print(f"第{i + 1}次提交 {no}: 唯一冲突, 幂等返回")
    print("落库:", conn.execute("SELECT id, order_no FROM orders").fetchall())
