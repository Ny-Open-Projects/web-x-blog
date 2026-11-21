"""浮点金额的脏数据修复: REAL 求和误差与迁移为整数分"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE pays(id INTEGER PRIMARY KEY, amount REAL)")
conn.executemany("INSERT INTO pays(amount) VALUES(?)", [(0.1,)] * 10)
s = conn.execute("SELECT SUM(amount) FROM pays").fetchone()[0]
print("REAL 求和:", repr(s), "偏差", abs(s - 1.0))

conn.execute("ALTER TABLE pays ADD COLUMN amount_fen INTEGER")
conn.execute("UPDATE pays SET amount_fen = CAST(ROUND(amount * 100) AS INTEGER)")
s2 = conn.execute("SELECT SUM(amount_fen) FROM pays").fetchone()[0]
print("整数分求和:", s2, "无误差; 迁移时 ROUND 是把二进制近似拉回正确值的关键")
