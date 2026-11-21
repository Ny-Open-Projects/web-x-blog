"""乐观并发: 条件 UPDATE 的 rowcount 才是冲突信号"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE stock(sku TEXT PRIMARY KEY, qty INTEGER, version INTEGER)")
c.execute("INSERT INTO stock VALUES('A1', 10, 3)")

s1 = conn.cursor()   # 会话一
s2 = conn.cursor()   # 会话二

v1 = s1.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
v2 = s2.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
print("两个会话都读到 qty=%d version=%d" % v1)

cur = s1.execute("UPDATE stock SET qty=qty-2, version=version+1 "
                 "WHERE sku='A1' AND version=?", (v1[1],))
print("会话一扣减 rowcount =", cur.rowcount)

cur = s2.execute("UPDATE stock SET qty=qty-3, version=version+1 "
                 "WHERE sku='A1' AND version=?", (v2[1],))
print("会话二扣减 rowcount =", cur.rowcount, "-> 0 即版本已变, 丢失更新被拦截")

if cur.rowcount == 0:
    nv = s2.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
    cur = s2.execute("UPDATE stock SET qty=qty-3, version=version+1 "
                     "WHERE sku='A1' AND version=?", (nv[1],))
    print("会话二重读重试 rowcount =", cur.rowcount)
print("最终状态:", c.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone())
print("rowcount 是并发下的冲突信号, 匹配行数与修改行数口径必须分清")
