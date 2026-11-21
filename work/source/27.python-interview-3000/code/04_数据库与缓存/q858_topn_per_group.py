"""组内 TopN: 窗口函数编号 + 外层过滤, 并与自相关子查询对照"""
import sqlite3

DDL = """
CREATE TABLE goods (id INTEGER PRIMARY KEY, category TEXT, sales INT);
INSERT INTO goods (category, sales) VALUES
 ('book',100),('book',90),('book',90),('book',80),('book',70),
 ('toy',50),('toy',40),('toy',30);
"""

WINDOW_SQL = """
SELECT category, id, sales FROM (
  SELECT category, id, sales,
         ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC, id) AS rn
  FROM goods
) WHERE rn <= 3 ORDER BY category, rn
"""

SUBQ_SQL = """
SELECT g.category, g.id, g.sales
FROM goods g
WHERE (SELECT COUNT(*) FROM goods g2
       WHERE g2.category = g.category AND g2.sales > g.sales) < 2
ORDER BY g.category, g.sales DESC
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        print("窗口函数法:", conn.execute(WINDOW_SQL).fetchall())
        print("相关子查询:", conn.execute(SUBQ_SQL).fetchall())
