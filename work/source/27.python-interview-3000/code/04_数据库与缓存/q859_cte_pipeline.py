"""多级 CTE 分步计算: 每类目平均分 -> 高于平均的学生 -> 类目排名"""
import sqlite3

DDL = """
CREATE TABLE stu (name TEXT, category TEXT, score INT);
INSERT INTO stu VALUES
 ('a','math',90),('b','math',70),('c','math',80),
 ('d','eng',60),('e','eng',75),('f','eng',85);
"""

SQL = """
WITH class_avg AS (
  SELECT category, AVG(score) AS avg_score FROM stu GROUP BY category
),
above_avg AS (
  SELECT s.name, s.category, s.score, c.avg_score
  FROM stu s JOIN class_avg c USING (category)
  WHERE s.score > c.avg_score
)
SELECT category, name, score FROM above_avg ORDER BY category, score DESC
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        for row in conn.execute(SQL):
            print(row)
