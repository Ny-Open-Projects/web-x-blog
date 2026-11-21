"""EXCEPT 与 INTERSECT: 隐式 DISTINCT 的语义与 ALL 缺失的替代"""
import sqlite3
from collections import Counter

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE a(x INTEGER)")
c.execute("CREATE TABLE b(x INTEGER)")
c.executemany("INSERT INTO a VALUES(?)", [(1,), (1,), (2,), (2,), (3,)])
c.executemany("INSERT INTO b VALUES(?)", [(2,), (2,)])

def show(label, sql):
    print("%-30s -> %s" % (label, [r[0] for r in c.execute(sql)]))

show("A EXCEPT B", "SELECT x FROM a EXCEPT SELECT x FROM b")
show("A INTERSECT B", "SELECT x FROM a INTERSECT SELECT x FROM b")
show("A UNION B", "SELECT x FROM a UNION SELECT x FROM b")
show("等价改写 去重差集", "SELECT DISTINCT x FROM a "
                        "WHERE x NOT IN (SELECT DISTINCT x FROM b)")

ca = Counter(r[0] for r in c.execute("SELECT x FROM a"))
cb = Counter(r[0] for r in c.execute("SELECT x FROM b"))
print("EXCEPT ALL 语义 按次数相减 ->", sorted((ca - cb).elements()))
print("EXCEPT 自动去重, 要保留重复次数必须按计数手工模拟")
