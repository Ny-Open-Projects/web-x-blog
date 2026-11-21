"""对比 OFFSET 与 seek 两种深分页的耗时, 行数越大 seek 优势越明显"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, score INT)")
        conn.executemany("INSERT INTO t (score) VALUES (?)",
                         [(i % 10000,) for i in range(200000)])
        conn.execute("CREATE INDEX idx_score ON t (score, id)")

        t0 = time.perf_counter()
        conn.execute("SELECT * FROM t ORDER BY score DESC, id LIMIT 150000, 20").fetchall()
        t1 = time.perf_counter()

        row = conn.execute(
            "SELECT score, id FROM t ORDER BY score DESC, id LIMIT 1 OFFSET 149999"
        ).fetchone()
        cursor = conn.execute(
            "SELECT * FROM t WHERE (score, id) < (?, ?) "
            "ORDER BY score DESC, id LIMIT 20", (row[0], row[1]))
        seek_rows = cursor.fetchall()
        t2 = time.perf_counter()

        print(f"OFFSET 深分页: {(t1 - t0) * 1000:.1f} ms")
        print(f"seek 游标分页: {(t2 - t1) * 1000:.1f} ms, 取到 {len(seek_rows)} 行")
