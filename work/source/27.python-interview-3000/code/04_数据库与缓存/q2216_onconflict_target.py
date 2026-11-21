"""ON CONFLICT 指定目标: 多个唯一约束时冲突到底命中谁"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE kv(a TEXT UNIQUE, b TEXT UNIQUE, n INTEGER DEFAULT 0)")
c.execute("INSERT INTO kv VALUES('x', 'y', 1)")

c.execute("INSERT INTO kv(a, b, n) VALUES('x', 'z', 5) "
          "ON CONFLICT(a) DO UPDATE SET n = n + 1")
print("冲突 a 走指定目标 upsert:", c.execute("SELECT * FROM kv").fetchall())

try:
    c.execute("INSERT INTO kv(a, b, n) VALUES('w', 'y', 9) "
              "ON CONFLICT(a) DO UPDATE SET n = n + 1")
except sqlite3.IntegrityError as e:
    print("冲突 b 但目标写了 a     :", str(e)[:44], "-> 不走 upsert 直接报错")

c.execute("INSERT INTO kv(a, b, n) VALUES('w', 'y', 9) ON CONFLICT DO NOTHING")
print("不带目标 DO NOTHING    :", c.execute("SELECT * FROM kv WHERE a='w'").fetchall(),
      " <- b 冲突被静默吞掉")
c.execute("INSERT INTO kv(a, b, n) VALUES('x', 'y', 99) ON CONFLICT DO UPDATE SET n = 99")
print("不带目标 DO UPDATE     :", c.execute("SELECT * FROM kv").fetchall())
