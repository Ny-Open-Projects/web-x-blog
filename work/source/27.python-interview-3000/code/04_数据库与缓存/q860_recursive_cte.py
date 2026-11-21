"""递归 CTE 沿 manager_id 展开组织树, 携带层级与路径"""
import sqlite3

DDL = """
CREATE TABLE emp (id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER);
INSERT INTO emp VALUES
 (1,'ceo',NULL),(2,'cto',1),(3,'cfo',1),
 (4,'dev1',2),(5,'dev2',2),(6,'qa1',2),(7,'acc1',3);
"""

SQL = """
WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, 1 AS depth, name AS path
  FROM emp WHERE name = 'ceo'
  UNION ALL
  SELECT e.id, e.name, e.manager_id, c.depth + 1, c.path || '->' || e.name
  FROM emp e JOIN chain c ON e.manager_id = c.id
)
SELECT depth, path FROM chain ORDER BY path
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        for depth, path in conn.execute(SQL):
            print(f"depth={depth}  {path}")
