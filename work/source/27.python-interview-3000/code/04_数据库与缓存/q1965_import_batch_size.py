"""批量导入批大小实测: 事务粒度与吞吐甜点区"""
import os
import sqlite3
import tempfile
import time

rows = [(i, "name-%d" % i) for i in range(8000)]

def bench(batch_size):
    path = os.path.join(tempfile.mkdtemp(), "b.sqlite")
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
    t0 = time.perf_counter()
    for i in range(0, len(rows), batch_size):
        c.executemany("INSERT INTO users VALUES(?,?)", rows[i:i + batch_size])
        c.commit()
    dt = time.perf_counter() - t0
    c.close()
    os.remove(path)
    return dt

print("批大小    总耗时    吞吐 行每秒")
for bs in [10, 100, 1000, 8000]:
    dt = bench(bs)
    print(f"{bs:7d} {dt:8.2f}s {len(rows) / dt:10.0f}")
print("结论: 批太小事务与 fsync 开销占主导 批太大单事务内存与回滚代价上升 甜点区通常在千行量级 实测为准")
