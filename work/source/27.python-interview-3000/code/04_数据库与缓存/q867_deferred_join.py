"""对比直接 LIMIT 深偏移 与 先取 id 再回表 两种写法的耗时"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE t (id INTEGER PRIMARY KEY,
                        user_id INT, payload TEXT)""")
        conn.executemany(
            "INSERT INTO t (user_id, payload) VALUES (?, ?)",
            [(i % 500, "x" * 50) for i in range(200000)])
        conn.execute("CREATE INDEX idx_user ON t (user_id, id)")

        off, size = 150000, 20

        t0 = time.perf_counter()
        direct = conn.execute(
            f"SELECT * FROM t WHERE user_id = 1 LIMIT {off}, {size}").fetchall()
        t1 = time.perf_counter()

        ids = [r[0] for r in conn.execute(
            f"SELECT id FROM t WHERE user_id = 1 ORDER BY id LIMIT {off}, {size}")]
        deferred = conn.execute(
            f"SELECT * FROM t WHERE id IN ({','.join(map(str, ids))})"
            f" ORDER BY id").fetchall()
        t2 = time.perf_counter()

        print(f"直接 LIMIT: {(t1 - t0) * 1000:.2f} ms, {len(direct)} 行")
        print(f"延迟关联: {(t2 - t1) * 1000:.2f} ms, {len(deferred)} 行")
