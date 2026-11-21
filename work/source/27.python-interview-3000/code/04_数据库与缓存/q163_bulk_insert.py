"""sqlite3 对比逐条插入与 executemany 的耗时"""
import sqlite3
import time

N = 20_000
CREATE = "CREATE TABLE t (id INTEGER, name TEXT)"


def bench(label: str, fn) -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute(CREATE)
    start = time.perf_counter()
    fn(conn)
    cost = time.perf_counter() - start
    print(f"{label}: {cost:.3f}s")
    conn.close()


def insert_one_by_one(conn: sqlite3.Connection) -> None:
    for i in range(N):
        conn.execute("INSERT INTO t VALUES (?, ?)", (i, f"name{i}"))
    conn.commit()                      # 全程一个大事务


def insert_executemany(conn: sqlite3.Connection) -> None:
    rows = [(i, f"name{i}") for i in range(N)]
    conn.executemany("INSERT INTO t VALUES (?, ?)", rows)  # 单条多值语句
    conn.commit()


if __name__ == "__main__":
    bench("逐条 execute", insert_one_by_one)
    bench("executemany", insert_executemany)
