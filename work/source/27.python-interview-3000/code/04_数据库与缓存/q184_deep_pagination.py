"""sqlite3 对比 OFFSET 深分页与游标分页的扫描代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
conn.executemany("INSERT INTO t(val) VALUES (?)", [(f"v{i}",) for i in range(100_000)])
conn.commit()

OFFSET_PAGE, CURSOR_LAST, SIZE = 90_000, 90_000, 20


def bench(label: str, sql: str, params: tuple) -> None:
    start = time.perf_counter()
    rows = conn.execute(sql, params).fetchall()
    print(f"{label}: {time.perf_counter() - start:.4f}s 首行 {rows[0][0]}")


# 传统 OFFSET: 扫描 90020 行再丢弃前 9 万行
bench(
    "OFFSET 深分页",
    "SELECT id FROM t ORDER BY id LIMIT ? OFFSET ?",
    (SIZE, OFFSET_PAGE),
)

# 游标分页: 用主键定位, 恒定扫描 SIZE 行
bench(
    "游标分页 seek",
    "SELECT id FROM t WHERE id > ? ORDER BY id LIMIT ?",
    (CURSOR_LAST, SIZE),
)

# 延迟关联思路(需要二级索引, sqlite 用 EXPLAIN 观察同理)
bench(
    "延迟关联",
    "SELECT t.id FROM t JOIN (SELECT id FROM t ORDER BY id LIMIT ? OFFSET ?) p ON t.id = p.id",
    (SIZE, OFFSET_PAGE),
)
