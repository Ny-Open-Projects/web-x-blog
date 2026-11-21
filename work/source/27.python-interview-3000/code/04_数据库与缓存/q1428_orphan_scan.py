"""软引用完整性: 无外键时的孤儿行扫描"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.executescript("""
CREATE TABLE users(id INTEGER PRIMARY KEY);
CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER);
CREATE TABLE pay_records(id INTEGER PRIMARY KEY, order_id INTEGER);
INSERT INTO users VALUES(1),(2);
INSERT INTO orders VALUES(1,1),(2,1),(3,99);
INSERT INTO pay_records VALUES(1,1),(2,33);
""")
ORPHAN_SQL = {
    "orders.uid 不在 users":
        "SELECT o.id FROM orders o LEFT JOIN users u ON o.uid=u.id WHERE u.id IS NULL",
    "pay_records.order_id 不在 orders":
        "SELECT p.id FROM pay_records p LEFT JOIN orders o ON p.order_id=o.id WHERE o.id IS NULL",
}
for name, sql in ORPHAN_SQL.items():
    bad = [r[0] for r in conn.execute(sql)]
    print(f"{name}: {bad if bad else '无孤儿'}")
print("处置: 能补的补挂真实主键, 确认废弃的移隔离区, 先修写入路径再清数据")
