"""排序规则对索引的影响: 比较排序规则与索引排序规则不一致时无法 seek"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users_bin (name TEXT NOT NULL)")            # 默认 BINARY
c.execute("CREATE TABLE users_ci  (name TEXT COLLATE NOCASE NOT NULL)")
rows = [("Alice",), ("BOB",), ("bob",), ("Carol",)]
c.executemany("INSERT INTO users_bin VALUES(?)", rows)
c.executemany("INSERT INTO users_ci  VALUES(?)", rows)
c.execute("CREATE INDEX idx_bin ON users_bin(name)")
c.execute("CREATE INDEX idx_ci  ON users_ci(name)")

cases = [
    ("BINARY 列  name = 'BOB'",                "users_bin", "'BOB'"),
    ("NOCASE 列  name = 'BOB'",                "users_ci", "'BOB'"),
    ("NOCASE 列  加 COLLATE NOCASE 比较",       "users_ci", "'BOB' COLLATE NOCASE"),
    ("NOCASE 列  加 COLLATE BINARY 比较",       "users_ci", "'BOB' COLLATE BINARY"),
    ("BINARY 列  加 COLLATE NOCASE 比较",       "users_bin", "'BOB' COLLATE NOCASE"),
]
for label, table, rhs in cases:
    plan = c.execute("EXPLAIN QUERY PLAN SELECT * FROM %s WHERE name = %s" % (table, rhs)).fetchone()[3]
    print("%-28s -> %s" % (label, "用索引 " + plan if plan.startswith("SEARCH") else "全表扫描"))

print("NOCASE 列 WHERE name='bob' 命中:",
      [r[0] for r in c.execute("SELECT name FROM users_ci WHERE name='bob'")])
print("BINARY 列 套 NOCASE 比较命中:",
      [r[0] for r in c.execute("SELECT name FROM users_bin WHERE name='BOB' COLLATE NOCASE")])
print("结论: 索引键按列的 COLLATE 排序, 查询比较规则必须与之一致, 否则优化器放弃 seek")
