"""普通视图实时计算 vs 汇总表定时刷新 两种形态对比"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amt REAL)")
        conn.executemany("INSERT INTO orders (user_id, amt) VALUES (?, ?)",
                         [(i % 50, i * 1.0) for i in range(5000)])

        # 形态一: 普通视图, 每次查询实时聚合
        conn.execute("""CREATE VIEW v_user_stat AS
                        SELECT user_id, COUNT(*) AS cnt, SUM(amt) AS total
                        FROM orders GROUP BY user_id""")
        print("视图查询:", conn.execute(
            "SELECT * FROM v_user_stat WHERE user_id = 3").fetchall())

        # 形态二: 汇总表(物化), 定时全量或增量刷新
        conn.execute("""CREATE TABLE user_stat AS
                        SELECT user_id, COUNT(*) AS cnt, SUM(amt) AS total
                        FROM orders GROUP BY user_id""")
        conn.execute("INSERT INTO orders (user_id, amt) VALUES (3, 999.0)")
        conn.execute("""DELETE FROM user_stat""")
        conn.execute("""INSERT INTO user_stat
                        SELECT user_id, COUNT(*), SUM(amt)
                        FROM orders GROUP BY user_id""")
        print("汇总表刷新后:", conn.execute(
            "SELECT * FROM user_stat WHERE user_id = 3").fetchall())
