"""大事务拆分实测: 写入与回滚代价随事务规模增长"""
import os
import sqlite3
import tempfile
import time

def fresh_db():
    path = os.path.join(tempfile.mkdtemp(), "t.sqlite")
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, payload TEXT)")
    return c

rows = [("p" * 40,) for _ in range(60000)]

def timed(label, fn):
    t0 = time.perf_counter()
    fn()
    print(f"{label}: {time.perf_counter() - t0:.2f} s")

# 方案 A: 六万行塞进一个事务
c = fresh_db()
timed("6 万行单事务写入", lambda: (c.executemany("INSERT INTO events(payload) VALUES(?)", rows), c.commit()))

t0 = time.perf_counter()
c.executemany("INSERT INTO events(payload) VALUES(?)", rows)
c.rollback()
print(f"6 万行单事务回滚: {time.perf_counter() - t0:.2f} s")
c.close()

# 方案 B: 每 5000 行提交一次
c2 = fresh_db()
def batched():
    batch = []
    for r in rows:
        batch.append(r)
        if len(batch) >= 5000:
            c2.executemany("INSERT INTO events(payload) VALUES(?)", batch)
            c2.commit()
            batch = []
    if batch:
        c2.executemany("INSERT INTO events(payload) VALUES(?)", batch)
        c2.commit()
timed("分批 5000 行写入  ", batched)

t0 = time.perf_counter()
c2.executemany("INSERT INTO events(payload) VALUES(?)", rows[:5000])
c2.rollback()
print(f"5000 行事务回滚  : {time.perf_counter() - t0:.3f} s  回滚代价近似与事务大小成正比")
c2.close()
print("结论: 大事务拉长锁持有 推高回滚日志 放大复制延迟 拆分按行数或时间片提交并保留断点与幂等")
