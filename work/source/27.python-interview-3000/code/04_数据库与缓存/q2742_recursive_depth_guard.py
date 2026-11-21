"""递归 CTE 的深度守卫: 层级上限与防环 path 检查双保险"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE node (id INTEGER PRIMARY KEY, parent INTEGER, name TEXT)")
c.executemany("INSERT INTO node VALUES(?,?,?)",
              [(1, None, "root"), (2, 1, "a"), (3, 2, "b"),
               (4, 3, "c"), (5, 4, "d"), (6, 3, "e")])

def subtree(root, max_depth):
    sql = """
    WITH RECURSIVE walk AS (
      SELECT id, parent, name, 0 AS depth, ',' || id || ',' AS path
      FROM node WHERE id = :root
      UNION ALL
      SELECT n.id, n.parent, n.name, w.depth + 1, w.path || n.id || ','
      FROM node n JOIN walk w ON n.parent = w.id
      WHERE w.depth < :max_depth AND w.path NOT LIKE '%,' || n.id || ',%'
    )
    SELECT id, name, depth FROM walk ORDER BY depth, id
    """
    return c.execute(sql, {"root": root, "max_depth": max_depth}).fetchall()

print("root=1 全量展开:", subtree(1, 6))
print("root=1 深度限制 2:", subtree(1, 2), "(超过两层的分支被截断)")

# 故意造环: 2 的父亲改成 5, 形成 2-3-4-5-2 的环, 无守卫的递归会无限转下去
c.execute("UPDATE node SET parent=5 WHERE id=2")
print("环数据 + 守卫 depth<3:", subtree(2, 3), "(守卫保证必停)")
