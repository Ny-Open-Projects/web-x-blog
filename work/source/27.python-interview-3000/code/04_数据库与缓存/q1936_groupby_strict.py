"""GROUP BY 严格模式: ONLY_FULL_GROUP_BY 与裸列的任意性"""
import re
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE scores(id INTEGER PRIMARY KEY, class TEXT, name TEXT, score INTEGER)")
conn.executemany("INSERT INTO scores VALUES(?,?,?,?)", [
    (1, 'A', 'alice', 90), (2, 'A', 'amber', 85), (3, 'B', 'bob', 77), (4, 'B', 'bella', 92)])

# 宽松模式: name 不在 GROUP BY 也不聚合, SQLite 允许但值来自组内任意一行
rows = conn.execute("SELECT class, name, MAX(score) FROM scores GROUP BY class").fetchall()
print("SQLite 宽松模式 ->", rows, "(name 来自组内任意一行 不可依赖)")

# SQLite 特例: 裸列与 min/max 同用时, 裸列取自命中 min/max 的那一行
hi = conn.execute("SELECT class, name, MAX(score) FROM scores GROUP BY class").fetchall()
lo = conn.execute("SELECT class, name, MIN(score) FROM scores GROUP BY class").fetchall()
print("MAX 同用裸列    ->", hi, "(与最高分同行)")
print("MIN 同用裸列    ->", lo, "(与最低分同行)")

# 严格模式等价写法: 裸列进 GROUP BY 或用聚合与子查询明确定义
strict = conn.execute("""
SELECT s.class, s.name, s.score FROM scores s
JOIN (SELECT class, MAX(score) AS m FROM scores GROUP BY class) t
  ON s.class = t.class AND s.score = t.m""").fetchall()
print("严格模式等价写法 ->", strict, "(MySQL ONLY_FULL_GROUP_BY 下必须写清这种语义)")

# 模拟严格模式检查器: 找出 SELECT 里既不在 GROUP BY 也不在聚合里的裸列
def strict_check(sql):
    m = re.search(r"SELECT (.+?) FROM", sql, re.I)
    cols = [c.strip() for c in m.group(1).split(",")]
    g = re.search(r"GROUP BY (.+?)\s*(?:HAVING|$)", sql, re.I)
    allowed = set(c.strip() for c in g.group(1).split(",")) if g else set()
    agg = re.compile(r"(MAX|MIN|SUM|COUNT|AVG)\s*\(", re.I)
    return [c for c in cols if c not in allowed and not agg.search(c)]

print("宽松 SQL 的裸列  ->", strict_check("SELECT class, name, MAX(score) FROM scores GROUP BY class"))
print("严格 SQL 的裸列  ->", strict_check("SELECT class, MAX(score) FROM scores GROUP BY class"))
print("结论: 宽松模式的裸列值不确定 严格模式逼你把语义写进 GROUP BY 或聚合 可移植性更好")
