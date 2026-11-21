"""rowid 与 AUTOINCREMENT: 隐式主键与 ID 复用行为"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(name TEXT)")                                  # 隐式 rowid
conn.execute("CREATE TABLE a(id INTEGER PRIMARY KEY, name TEXT)")          # id 是 rowid 别名
conn.execute("CREATE TABLE s(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
conn.executemany("INSERT INTO t(name) VALUES(?)", ["x"] * 3)
conn.executemany("INSERT INTO a(name) VALUES(?)", ["x"] * 3)
conn.executemany("INSERT INTO s(name) VALUES(?)", ["x"] * 3)

print("t 的 rowid       ->", [r[0] for r in conn.execute("SELECT rowid FROM t")])
print("a 的 id 与 rowid ->", conn.execute("SELECT id, rowid FROM a").fetchall(),
      " INTEGER PRIMARY KEY 就是 rowid 的别名")

# 删掉最大 rowid 的行后, 新行会复用这个 id
conn.execute("DELETE FROM t WHERE rowid = 3")
conn.execute("INSERT INTO t(name) VALUES('new')")
print("普通表删尾再插   ->", [r[0] for r in conn.execute("SELECT rowid FROM t")], "(3 被复用)")

# AUTOINCREMENT 由 sqlite_sequence 记录历史最大值 保证永不复用
conn.execute("DELETE FROM s")
conn.execute("INSERT INTO s(name) VALUES('new')")
print("AUTOINCREMENT 清空再插 ->", [r[0] for r in conn.execute("SELECT id FROM s")], " 单调不复用")
print("sqlite_sequence  ->", conn.execute("SELECT * FROM sqlite_sequence").fetchall())
print("结论: 默认 rowid 是实现细节且会被复用, 对外暴露 ID 或有审计续号需求时才值得上 AUTOINCREMENT")
