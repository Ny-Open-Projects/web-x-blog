"""sqlite 演示分批归档: 小事务搬运 + 事后对账"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript("""
            CREATE TABLE orders (id INTEGER PRIMARY KEY, day INT, amt REAL);
            CREATE TABLE orders_archive AS SELECT * FROM orders WHERE 0;
        """)
        conn.executemany("INSERT INTO orders (day, amt) VALUES (?, ?)",
                         [(i % 30, i * 1.0) for i in range(10000)])

        moved = 0
        while True:
            with conn:  # 每批独立事务, 控制锁持有时间
                cur = conn.execute(
                    "CREATE TEMP TABLE IF NOT EXISTS batch AS "
                    "SELECT id, day, amt FROM orders WHERE day < 10 LIMIT 1000")
                n = conn.execute("SELECT COUNT(*) FROM batch").fetchone()[0]
                if n == 0:
                    break
                conn.execute("INSERT INTO orders_archive SELECT * FROM batch")
                conn.execute("DELETE FROM orders WHERE id IN (SELECT id FROM batch)")
                moved += n
            conn.execute("DROP TABLE batch")

        hot = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        cold = conn.execute("SELECT COUNT(*) FROM orders_archive").fetchone()[0]
        print(f"已归档 {moved} 行, 热表 {hot}, 归档表 {cold}, 对账 {hot + cold == 10000}")
