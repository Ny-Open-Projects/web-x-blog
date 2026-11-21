"""演示累计求和与移动平均, 并对比 ROWS 与 RANGE 的差异"""
import sqlite3

DDL = """
CREATE TABLE daily (day TEXT, amount INT);
INSERT INTO daily VALUES
 ('d1',10),('d2',20),('d3',30),('d4',40),('d5',50);
"""

SQL = """
SELECT day, amount,
       SUM(amount) OVER (ORDER BY day) AS cum_sum,
       AVG(amount) OVER (ORDER BY day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3
FROM daily
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(DDL)
        print(f"{'day':<5}{'amount':<8}{'cum':<6}{'ma3':>6}")
        for day, amount, cum, ma3 in conn.execute(SQL):
            print(f"{day:<5}{amount:<8}{cum:<6}{ma3:>6.1f}")
