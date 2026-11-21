"""导入遇主键冲突的降级: 跳过 覆盖 隔离三种策略与代价"""
import sqlite3

BATCH = [("A", 9.5), ("C", 30.0), ("B", 21.0), ("D", 40.0), ("C", 31.0), ("E", 12.0)]

def fresh():
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE sku(code TEXT PRIMARY KEY, price REAL)")
    c.execute("CREATE TABLE rejects(code TEXT, price REAL, reason TEXT)")
    c.executemany("INSERT INTO sku VALUES(?,?)", [("A", 10.0), ("B", 20.0)])   # 库内已有
    return c

def show(label, c):
    rows = c.execute("SELECT code, price FROM sku ORDER BY code").fetchall()
    rej = c.execute("SELECT count(*) FROM rejects").fetchone()[0]
    print("   %s -> 表内 %s 拒收 %d 条" % (label, rows, rej))

def p_skip(c, rows):
    ok = 0
    for r in rows:
        ok += c.execute("INSERT OR IGNORE INTO sku VALUES(?,?)", r).rowcount
    return ok

def p_overwrite(c, rows):
    for r in rows:
        c.execute("INSERT OR REPLACE INTO sku VALUES(?,?)", r)
    return len(rows)

def p_quarantine(c, rows):
    ok = 0
    for r in rows:
        try:
            c.execute("INSERT INTO sku VALUES(?,?)", r)
            ok += 1
        except sqlite3.IntegrityError:
            c.execute("INSERT INTO rejects VALUES(?,?,?)", (r[0], r[1], "dup-pk"))
    return ok

for name, fn in [("跳过", p_skip), ("覆盖", p_overwrite), ("隔离", p_quarantine)]:
    c = fresh()
    print("%s 策略 实际入库 %d 条" % (name, fn(c, BATCH)))
    show("结果", c)
print("口径先定: 跳过保旧值 覆盖保新值 隔离保审计, 批内重复的 C 在覆盖策略下以后到为准")
