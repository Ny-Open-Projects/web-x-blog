"""COLLATE 与大小写: 等值 排序与 LIKE 的三套规则"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(word TEXT COLLATE NOCASE)")
conn.executemany("INSERT INTO t VALUES(?)", [("Apple",), ("banana",), ("APPLE",), ("Banana",)])

# 列声明 NOCASE 后, 索引与等值比较都不区分大小写
n = conn.execute("SELECT COUNT(*) FROM t WHERE word = 'apple'").fetchone()[0]
print("NOCASE 列等值查 apple ->", n, "行")
b = conn.execute("SELECT COUNT(*) FROM t WHERE word = 'apple' COLLATE BINARY").fetchone()[0]
print("同查询表达式级 BINARY ->", b, "行  查询侧可覆盖列侧规则")

# 默认 BINARY 的表: 等值比较区分大小写
conn.execute("CREATE TABLE t2(word TEXT)")
conn.executemany("INSERT INTO t2 VALUES(?)", [("Apple",), ("apple",)])
c = conn.execute("SELECT COUNT(*) FROM t2 WHERE word = 'APPLE'").fetchone()[0]
print("BINARY 列等值查 APPLE ->", c, "行  大小写敏感")

# LIKE 在 SQLite 默认对 ASCII 不区分大小写, 与等值比较规则不同源
l = conn.execute("SELECT COUNT(*) FROM t2 WHERE word LIKE 'apple'").fetchone()[0]
print("BINARY 列 LIKE apple  ->", l, "行  LIKE 另有一套大小写规则")

# ORDER BY 的排序规则决定字典序
print("BINARY 排序:", [r[0] for r in conn.execute("SELECT word FROM t2 ORDER BY word COLLATE BINARY")])
print("NOCASE 排序:", [r[0] for r in conn.execute("SELECT word FROM t2 ORDER BY word COLLATE NOCASE")])
print("结论: 等值与排序行为由列或表达式的 COLLATE 决定, LIKE 的大小写行为独立一套, 混用必踩坑")
