"""多态关联 target_type + target_id 的查询代价: 正向好查 反向 join 必须 UNION"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE comment (
    id INTEGER PRIMARY KEY, target_type TEXT, target_id INTEGER, body TEXT)""")
rows = []
for i in range(1, 40001):
    rows.append((i, ("article", "video", "topic")[i % 3], i // 3, "c%d" % i))
c.executemany("INSERT INTO comment VALUES(?,?,?,?)", rows)

# 正向: 取一个对象的评论, 有无复合索引的差距
sql_fwd = "SELECT COUNT(*) FROM comment WHERE target_type=? AND target_id=?"
print("无索引计划:", c.execute("EXPLAIN QUERY PLAN " + sql_fwd, ("video", 100)).fetchone()[3])
t0 = time.perf_counter()
for _ in range(20):
    c.execute(sql_fwd, ("video", 100)).fetchone()
print("无索引 20 次查询 %.1f ms" % ((time.perf_counter() - t0) * 1000))

c.execute("CREATE INDEX idx_target ON comment(target_type, target_id)")
print("有索引计划:", c.execute("EXPLAIN QUERY PLAN " + sql_fwd, ("video", 100)).fetchone()[3])
t0 = time.perf_counter()
for _ in range(20):
    c.execute(sql_fwd, ("video", 100)).fetchone()
print("有索引 20 次查询 %.1f ms" % ((time.perf_counter() - t0) * 1000))

# 反向: 每篇文章的评论数。不同类型的 target_id 共用数值空间, 直接 join 会数进别的类型
c.execute("CREATE TABLE article (id INTEGER PRIMARY KEY, title TEXT)")
c.executemany("INSERT INTO article VALUES(?,?)", [(i, "a%d" % i) for i in range(1, 6)])
naive = c.execute("""
    SELECT COUNT(*) FROM article a JOIN comment cm ON cm.target_id = a.id
""").fetchone()[0]
correct = c.execute("""
    SELECT COUNT(*) FROM article a
    JOIN comment cm ON cm.target_type='article' AND cm.target_id = a.id
""").fetchone()[0]
print("按 target_id 直接 join 统计到 %d 条 (混入其他类型); 加类型条件后 %d 条 (正确)" % (naive, correct))
print("多类型反向汇总只能按类型 UNION ALL 或拆独立关联表, 这就是多态关联的反向税")
