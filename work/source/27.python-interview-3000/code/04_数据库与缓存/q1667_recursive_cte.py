"""层级查询实现一: 递归 CTE 展开组织树, 带深度上限与环防护"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE dept(id INTEGER PRIMARY KEY, name TEXT, parent_id INTEGER, headcount INTEGER);
INSERT INTO dept VALUES
 (1, '总公司', NULL, 0), (2, '研发部', 1, 80), (3, '市场部', 1, 30),
 (4, '后端组', 2, 45), (5, '前端组', 2, 35), (6, '增长组', 3, 12);
""")

# 递归部分: 锚点取根, 递归步按 parent_id 挂接, path 记录层级链
sql = """
WITH RECURSIVE tree(id, name, parent_id, depth, path, headcount) AS (
  SELECT id, name, parent_id, 0, CAST(id AS TEXT), headcount
  FROM dept WHERE parent_id IS NULL
  UNION ALL
  SELECT d.id, d.name, d.parent_id, t.depth + 1, t.path || '/' || d.id, d.headcount
  FROM dept d JOIN tree t ON d.parent_id = t.id
  WHERE t.depth < 20
)
SELECT t.depth, t.path,
       (SELECT SUM(s.headcount) FROM tree s
          WHERE s.id = t.id OR s.path LIKE t.path || '/%') AS sub_heads
FROM tree t ORDER BY t.path
"""
print("递归展开与子树人力汇总:")
for depth, path, heads in conn.execute(sql):
    print(f"  {'  ' * depth}{path}  子树人力 {heads}")

# 环防护: 数据出现环时, 深度上限防止无限递归
conn.execute("UPDATE dept SET parent_id = 6 WHERE id = 3")   # 制造环 3 -> 6 -> 3
conn.commit()
sql_cycle = """
WITH RECURSIVE loop(id, parent_id, depth) AS (
  SELECT id, parent_id, 0 FROM dept WHERE id = 3
  UNION ALL
  SELECT d.id, d.parent_id, l.depth + 1
  FROM dept d JOIN loop l ON d.parent_id = l.id
  WHERE l.depth < 20
)
SELECT MAX(depth) FROM loop
"""
print("环 3<->6 上的递归被深度上限截断在:", conn.execute(sql_cycle).fetchone()[0], "层")
print("要点: 递归 CTE 三要素 = 锚点 递归步 终止条件;")
print("      深度上限是最后防线, 更优雅的做法是在 WHERE 里限制 path 不重复经过同一节点")
