"""主键迁移: 自增换雪花 ID 的在线切换"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders_old(id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL)")
conn.execute(
    "CREATE TABLE orders_new(id INTEGER PRIMARY KEY, old_id INTEGER UNIQUE, amount REAL)")
conn.executemany("INSERT INTO orders_old(amount) VALUES(?)", [(99.0,), (199.0,), (299.0,)])

machine_id = 1
seq = 0
def snowflake():
    global seq
    seq = (seq + 1) & 0xFFF
    return (int(time.time() * 1000) << 22) | (machine_id << 12) | seq

for oid, amt in conn.execute("SELECT id, amount FROM orders_old").fetchall():
    conn.execute("INSERT OR IGNORE INTO orders_new VALUES(?,?,?)", (snowflake(), oid, amt))
new_id = snowflake()                          # 双写期新订单: 两边落, 新主键用雪花
conn.execute("INSERT INTO orders_old(amount) VALUES(?)", (499.0,))
conn.execute("INSERT INTO orders_new VALUES(?,?,NULL)", (new_id, 499.0))
n_old = conn.execute("SELECT COUNT(*) FROM orders_old").fetchone()[0]
n_new = conn.execute("SELECT COUNT(*) FROM orders_new").fetchone()[0]
print(f"旧表 {n_old} 行, 新表 {n_new} 行(3 条迁移 + 1 条双写)")
ids = [r[0] for r in conn.execute("SELECT id FROM orders_new ORDER BY id")]
print("新主键样例:", ids[0], f"({len(str(ids[0]))} 位), 趋势递增且全局唯一")
print("unique(old_id) 让回填重跑幂等, 是切换安全的关键")
