"""分批删除: 每批独立事务, 打印进度, 总耗时可控"""
import sqlite3
import time

def delete_in_batches(conn, day_threshold, batch=2000):
    total = 0
    while True:
        with conn:  # 独立事务
            cur = conn.execute(
                "DELETE FROM log WHERE id IN "
                "(SELECT id FROM log WHERE day < ? LIMIT ?)",
                (day_threshold, batch))
            n = cur.rowcount
        total += n
        if n == 0:
            break
        print(f"本批删除 {n} 行, 累计 {total}")
        time.sleep(0.01)  # 模拟批间让路, 生产中可观察主从延迟决定
    return total

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE log (id INTEGER PRIMARY KEY, day INT)")
        conn.executemany("INSERT INTO log (day) VALUES (?)",
                         [(i % 365,) for i in range(20000)])
        t0 = time.perf_counter()
        deleted = delete_in_batches(conn, 180)
        print(f"共删除 {deleted} 行, 耗时 {(time.perf_counter() - t0) * 1000:.0f} ms")
        print("剩余行数:", conn.execute("SELECT COUNT(*) FROM log").fetchone()[0])
