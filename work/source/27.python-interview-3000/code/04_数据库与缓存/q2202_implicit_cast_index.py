"""隐式类型转换实测: SQLite 靠列亲和性兜底, 列被表达式包裹才会失效"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE sn_t (sn TEXT PRIMARY KEY, amt REAL) WITHOUT ROWID")
c.executemany("INSERT INTO sn_t VALUES(?,?)", [(str(i), float(i)) for i in range(1, 2001)])

for label, sql in [
    ("sn = '1000'              ", "SELECT amt FROM sn_t WHERE sn = '1000'"),
    ("sn = 1000   数字字面量     ", "SELECT amt FROM sn_t WHERE sn = 1000"),
    ("CAST(sn AS INTEGER) = 1000", "SELECT amt FROM sn_t WHERE CAST(sn AS INTEGER) = 1000"),
    ("sn + 0 = 1000 表达式包裹   ", "SELECT amt FROM sn_t WHERE sn + 0 = 1000"),
]:
    plan = c.execute("EXPLAIN QUERY PLAN " + sql).fetchone()[3]
    print("%-28s -> %s" % (label, plan))

print("sn = 1000    命中:", [r[0] for r in c.execute("SELECT amt FROM sn_t WHERE sn = 1000")])
print("sn = '01000' 命中:", [r[0] for r in c.execute("SELECT amt FROM sn_t WHERE sn = '01000'")])
print("结论: 字面量类型错了亲和性还能救, 列一被表达式包裹必 SCAN, MySQL 则连字面量这层兜底都没有")
