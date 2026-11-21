"""多窗口叠加: 类目排名 + 类目占比 + 全表累计 一条 SQL 完成"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE sales (name TEXT, category TEXT, amt REAL, seq INT)")
        conn.executemany("INSERT INTO sales VALUES (?,?,?,?)", [
            ("A", "book", 100, 1), ("B", "book", 70, 2), ("C", "toy", 80, 3),
            ("D", "toy", 80, 4), ("E", "book", 30, 5)])

        sql = """
        SELECT name, category, amt,
               RANK() OVER (PARTITION BY category ORDER BY amt DESC) AS rk,
               ROUND(amt * 1.0 / SUM(amt) OVER (PARTITION BY category), 3) AS share,
               SUM(amt) OVER (ORDER BY seq ROWS UNBOUNDED PRECEDING) AS running
        FROM sales ORDER BY seq
        """
        print(f"{'name':<5}{'cat':<6}{'amt':<6}{'rk':<3}{'share':<7}{'running'}")
        for row in conn.execute(sql):
            print(f"{row[0]:<5}{row[1]:<6}{row[2]:<6.0f}{row[3]:<3}{row[4]:<7.3f}{row[5]:.0f}")
