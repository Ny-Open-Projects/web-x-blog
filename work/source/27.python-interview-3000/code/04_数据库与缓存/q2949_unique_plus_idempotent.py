"""唯一约束与业务幂等的组合: 预检挡常态 约束兜并发 三种结局"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE payment(order_no TEXT PRIMARY KEY, amount INTEGER, state TEXT);
CREATE TABLE dedup(pay_key TEXT PRIMARY KEY, seen_at TEXT);
""")


def create_payment(order_no, amount, now):
    # 第一道: 业务预检, 常态重复在这里被友好挡下
    if conn.execute("SELECT 1 FROM dedup WHERE pay_key=?",
                    ("pay:" + order_no,)).fetchone():
        return "duplicate"
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("INSERT INTO dedup VALUES(?,?)", ("pay:" + order_no, now))
        conn.execute("INSERT INTO payment VALUES(?,?,?)",
                     (order_no, amount, "created"))
        conn.commit()
        return "created"
    except sqlite3.IntegrityError:
        # 第二道: 预检与插入之间有并发窗口, 唯一约束兜底
        conn.rollback()
        return "race_duplicate"


print("首单:", create_payment("o1", 100, "t1"))
print("重放:", create_payment("o1", 100, "t2"))
# 模拟并发竞态: 预检通过之后, 另一请求已把 key 抢注
conn.execute("INSERT INTO dedup VALUES('pay:o2','tx')")
conn.commit()
print("竞态:", create_payment("o2", 200, "t3"))
print("payment 行数:", conn.execute("SELECT COUNT(*) FROM payment").fetchone()[0],
      "dedup 行数:", conn.execute("SELECT COUNT(*) FROM dedup").fetchone()[0])
assert conn.execute("SELECT COUNT(*) FROM payment").fetchone()[0] == 1
