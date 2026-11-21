"""笛卡尔积的意外来源: 忘写连接条件与重复键扇出"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
c.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amt REAL)")
c.executemany("INSERT INTO users VALUES(?,?)", [(1, "a"), (2, "b"), (3, "c")])
c.executemany("INSERT INTO orders VALUES(?,?,?)",
              [(10, 1, 50.0), (11, 1, 30.0), (12, 2, 20.0), (13, 2, 80.0)])

n = c.execute("SELECT count(*) FROM users, orders").fetchone()[0]
print("忘写连接条件 users, orders  ->", n, "行  3*4=12 的纯笛卡尔积")
n = c.execute("SELECT count(*) FROM users u JOIN orders o ON o.user_id=u.id").fetchone()[0]
print("正确的多对一内连接          ->", n, "行")
s = c.execute("SELECT sum(amt) FROM orders").fetchone()[0]
s2 = c.execute("SELECT sum(o.amt) FROM users u JOIN orders o ON o.user_id=u.id").fetchone()[0]
print("订单直接求和 %.0f, 连接用户后求和 %.0f -> 多对一不扇出, 金额安全" % (s, s2))

c.execute("CREATE TABLE tags(user_id INTEGER, tag TEXT)")
c.executemany("INSERT INTO tags VALUES(?,?)", [(1, "x"), (1, "y"), (2, "x")])
n = c.execute("SELECT count(*) FROM orders o JOIN tags t ON t.user_id=o.user_id").fetchone()[0]
s3 = c.execute("SELECT sum(o.amt) FROM orders o JOIN tags t ON t.user_id=o.user_id").fetchone()[0]
print("订单连标签 ->", n, "行, sum(amt)=%.0f, 虚增 %.0f <- 一对多扇出, 聚合已失真" % (s3, s3 - s))
