"""字符串聚合的次序敏感: group_concat 不保证顺序, 需要显式定序"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, user TEXT, event TEXT)")
c.executemany("INSERT INTO logs VALUES(?,?,?)",
              [(1, "u1", "login"), (2, "u1", "view"), (3, "u2", "login"),
               (4, "u1", "buy"), (5, "u2", "view"), (6, "u1", "logout")])

a = c.execute("SELECT group_concat(event, '->') FROM logs WHERE user='u1'").fetchone()[0]
b = c.execute("SELECT group_concat(event, '->') FROM "
              "(SELECT event FROM logs WHERE user='u1' ORDER BY id DESC)").fetchone()[0]
print("自然扫描顺序:", a)
print("倒序子查询  :", b, " <- 同一份数据两种串")

d1 = c.execute("SELECT group_concat(event, '->') FROM "
               "(SELECT event FROM logs WHERE user='u1' ORDER BY id)").fetchone()[0]
d2 = " -> ".join(r[0] for r in c.execute("SELECT event FROM logs WHERE user='u1' ORDER BY id"))
print("子查询正序  :", d1)
print("应用层聚合  :", d2)

try:
    c.execute("SELECT group_concat(event, '->' ORDER BY id) FROM logs WHERE user='u1'")
    print("聚合内 ORDER BY: 本机支持")
except sqlite3.OperationalError as e:
    print("聚合内 ORDER BY: 本机 SQLite 版本不支持 ->", e)
