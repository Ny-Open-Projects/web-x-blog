"""sqlite3 真实演示三种排序窗口函数在并列分时的差异"""
import sqlite3

DDL = """
CREATE TABLE score (name TEXT, class TEXT, score INT);
INSERT INTO score VALUES
 ('alice','A',95),('bob','A',92),('carol','A',92),('dave','A',88),
 ('erin','B',93),('frank','B',90);
"""

SQL = """
SELECT name, class, score,
       ROW_NUMBER() OVER (PARTITION BY class ORDER BY score DESC, name) AS rn,
       RANK()       OVER (PARTITION BY class ORDER BY score DESC)      AS rk,
       DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC)      AS drk
FROM score
ORDER BY class, rk
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        print("name  class score rn rk drk")
        for row in conn.execute(SQL):
            print(f"{row[0]:<6}{row[1]:<6}{row[2]:<6}{row[3]:<3}{row[4]:<3}{row[5]}")
