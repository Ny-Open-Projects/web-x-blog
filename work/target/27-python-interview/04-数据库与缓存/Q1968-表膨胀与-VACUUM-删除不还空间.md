---
title: [Q1968] 表膨胀与 VACUUM: 删除不还空间
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1968 · 表膨胀与 VACUUM: 删除不还空间

> 难度:★★★☆ | 标签:运维, SQLite

**问**:删了一大堆数据文件为什么没变小?空间什么时候才还给操作系统?

**答**:删除只是把页标记为空闲放进 freelist, 文件并不缩小, 本文件实测删除七千行后 page_count 不变而 freelist 涨到一百九十一页。真正归还要靠 VACUUM:全量重建库文件把数据压实到前部再截断尾部, 实测文件从二点二 MB 缩到一点四五 MB, 代价是重建期间的高 IO 与等量临时空间, 必须低峰执行。常态化的删除型负载用 auto_vacuum 增量回收更合适, 每次回收少量页分多次跑, 实测一百九十一次增量回收把页数从五百四十六收到三百五十五, 全程不需要全量重建。设计启示:持续小批量删除优于偶发巨量清理;预估会大量删除的表, 建库时就打开 auto_vacuum。

```python
# file: code/04_数据库与缓存/q1968_bloat_vacuum.py
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
```

**追问**:
- PostgreSQL 的 vacuum 一样吗?—— 概念相似但机制不同, PG 的 dead tuple 靠 vacuum 回收, autovacuum 是后台进程, 膨胀治理思路相通。
- MySQL InnoDB 删除会还空间吗?—— 表空间内页会复用但文件默认不缩, 需要 OPTIMIZE TABLE 或 innodb_file_per_table 下的表重建。

---
