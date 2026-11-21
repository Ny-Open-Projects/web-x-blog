"""表膨胀与 VACUUM: 删除不还空间的实测"""
import os
import sqlite3
import tempfile
import time

def make(auto_vacuum=False):
    path = os.path.join(tempfile.mkdtemp(), "b.sqlite")
    c = sqlite3.connect(path)
    if auto_vacuum:
        c.execute("PRAGMA auto_vacuum = INCREMENTAL")   # 建表前设置才生效
    c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, payload TEXT)")
    return c, path

def stats(c):
    return (c.execute("PRAGMA page_count").fetchone()[0],
            c.execute("PRAGMA freelist_count").fetchone()[0])

c, path = make()
c.executemany("INSERT INTO t(payload) VALUES(?)", [("x" * 100,) for _ in range(20000)])
c.commit()
print("灌 2 万行   page_count/freelist =", stats(c), " 文件", os.path.getsize(path), "字节")
c.execute("DELETE FROM t WHERE id > 13000")   # 连续删除尾部 整页腾空
c.commit()
print("删尾部 7 千 page_count/freelist =", stats(c), " 空页进了 freelist 文件不缩小")

t0 = time.perf_counter()
c.execute("VACUUM")
dt = time.perf_counter() - t0
print(f"VACUUM 之后 page_count/freelist =", stats(c), f" 耗时 {dt:.2f}s 文件 {os.path.getsize(path)} 字节")
c.close()

# 增量回收: auto_vacuum 模式下不必全量重建 每次收一点 分多次跑
c2, _ = make(auto_vacuum=True)
c2.executemany("INSERT INTO t(payload) VALUES(?)", [("y" * 100,) for _ in range(20000)])
c2.commit()
c2.execute("DELETE FROM t WHERE id > 13000")
c2.commit()
before = stats(c2)
rounds = 0
while c2.execute("PRAGMA freelist_count").fetchone()[0] > 0:
    c2.execute("PRAGMA incremental_vacuum(50)")
    c2.commit()
    rounds += 1
print("增量回收    page_count/freelist =", before, "->", stats(c2), f" 分 {rounds} 次回收 不需要全量重建")
print("结论: 删除只标空页 VACUUM 是全量重建要在低峰跑 auto_vacuum 增量回收适合常态化删除型负载")
