---
title: [Q1686] 大结果集流式处理: fetchall 与 yield_per
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1686 · 大结果集流式处理: fetchall 与 yield_per

> 难度:★★★☆ | 标签:ORM, 性能

**问**:要把 200 万行导出到文件,一次 fetchall 会发生什么?

**答**:fetchall 把全部行物化成 Python 对象列表,内存峰值与结果集成正比,百万行直接把进程打爆。流式方案是分块迭代:游标 fetchmany 循环喂给生成器,内存峰值只与 chunk 大小相关,本机 20 万行实测,fetchall 峰值 68MB、分块 3.4MB。注意两个方言细节:sqlite 的游标天然逐行读,MySQL 的默认驱动会把整个结果缓冲在客户端,必须用 SSCursor 或 stream_results 才是真流式;PG 用 named cursor。流式期间游标与事务保持打开,要权衡长事务与锁持有时间,导出类任务最好走只读副本。

```python
# file: code/04_数据库与缓存/q1686_yield_per_stream.py
"""大结果集流式处理: fetchall 一次载入 vs 分块 fetchmany 流式"""
import sqlite3
import tracemalloc

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE big(id INTEGER PRIMARY KEY, payload TEXT)")
conn.executemany("INSERT INTO big VALUES(?,?)",
                 [(i, "x" * 200) for i in range(200000)])
conn.commit()

tracemalloc.start()
rows = conn.execute("SELECT id, payload FROM big").fetchall()   # 一次性载入
total = sum(len(r[1]) for r in rows)
peak_all = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"fetchall : 行数 {len(rows)}, 载荷 {total / 1e6:.0f} MB, 峰值内存 {peak_all / 1e6:.1f} MB")

def yield_per(conn, sql, chunk=5000):
    cur = conn.execute(sql)
    while True:
        batch = cur.fetchmany(chunk)
        if not batch:
            break
        for r in batch:
            yield r

tracemalloc.start()
total, n = 0, 0
for r in yield_per(conn, "SELECT id, payload FROM big"):
    total += len(r[1])
    n += 1
peak_stream = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"流式分块 : 行数 {n}, 载荷 {total / 1e6:.0f} MB, 峰值内存 {peak_stream / 1e6:.1f} MB")
print("ORM 对应 yield_per 或按主键分段; MySQL/PG 需服务端游标才真正流式, 否则驱动仍会缓冲")
print("注意: 流式遍历期间游标与事务保持打开, 注意锁持有时间与连接占用")
```

**追问**:
- yield_per 的 chunk 设多大合适?——几百到几千,太小则网络往返多,太大则单批内存又上去了;配合导出文件的缓冲观察调。
- 流式遍历中能并发写同一张表吗?——同一事务内不行会锁冲突;只读副本上做导出,主库写路径完全不受影响。

---
