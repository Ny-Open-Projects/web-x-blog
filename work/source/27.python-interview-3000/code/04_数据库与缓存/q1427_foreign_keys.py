"""外键取舍: 约束拦截 vs 应用层保证的对照实验"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY)")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, uid INTEGER)")
conn.execute("INSERT INTO users VALUES(1)")

conn.execute("PRAGMA foreign_keys=ON")
conn.execute("CREATE TABLE orders2(id INTEGER PRIMARY KEY, "
             "uid INTEGER REFERENCES users(id))")
try:
    conn.execute("INSERT INTO orders2 VALUES(1, 999)")
except sqlite3.IntegrityError as e:
    print("FK 开启: 引用完整性被数据库拦截 ->", e)

conn.execute("INSERT INTO orders(id, uid) VALUES(1, 999)")   # 无 FK 表: 孤儿直接入库
print("FK 关闭: 孤儿订单已入库 ->", conn.execute("SELECT * FROM orders").fetchall())
print("取舍: 约束买安心, 应用层买吞吐; 关键是别两头都不管")
