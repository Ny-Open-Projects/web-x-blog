"""对比随机主键与自增主键的批量插入耗时, 量化乱序插入代价"""
import random
import sqlite3
import time

def bench(conn, keys):
    t0 = time.perf_counter()
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
    conn.executemany("INSERT INTO t (id, v) VALUES (?, ?)",
                     [(k, "x" * 40) for k in keys])
    conn.commit()
    return (time.perf_counter() - t0) * 1000

if __name__ == "__main__":
    a = sqlite3.connect(":memory:")
    b = sqlite3.connect(":memory:")
    seq = list(range(100000))
    rnd = seq[:]
    random.seed(1)
    random.shuffle(rnd)
    print(f"自增顺序主键插入: {bench(a, seq):.0f} ms")
    print(f"随机主键插入:     {bench(b, rnd):.0f} ms")
    a.close(); b.close()
