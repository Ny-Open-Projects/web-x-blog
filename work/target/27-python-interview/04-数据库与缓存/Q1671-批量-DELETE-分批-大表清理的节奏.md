---
title: [Q1671] 批量 DELETE 分批: 大表清理的节奏
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1671 · 批量 DELETE 分批: 大表清理的节奏

> 难度:★★★☆ | 标签:SQL 运维, 删除

**问**:要从几亿行的大表里删掉一半数据,一条 DELETE 为什么危险?怎么删?

**答**:一条巨型 DELETE 的危险在 undo/回滚量与锁持有时间不可控:主从延迟飙高、行锁或间隙锁长时间持有阻塞业务、失败后回滚同样要花几十分钟。正确做法是按主键分批:每批用 DELETE ... WHERE id IN (SELECT id ... LIMIT n) 删几千行立即提交,循环到删完;生产上再加批间 sleep 限速、按业务低峰执行、每批之间观察主从延迟。过滤列必须有索引,否则每一批的 SELECT 都退化成全表扫;SQLite 不支持 DELETE LIMIT 语法,用子查询间接实现,MySQL 可直接 DELETE ... LIMIT。

```python
# file: code/04_数据库与缓存/q1671_batch_delete.py
"""批量 DELETE 分批: 大表清理的分批提交与节奏控制"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, created INTEGER, expired INTEGER)")
conn.execute("CREATE INDEX idx_exp ON logs(expired)")
conn.executemany("INSERT INTO logs VALUES(?,?,?)",
                 [(i, i, 1 if i % 2 == 0 else 0) for i in range(120000)])
conn.commit()

BATCH = 5000
total = conn.execute("SELECT COUNT(*) FROM logs WHERE expired=1").fetchone()[0]
print(f"待删除 {total} 行, 每批 {BATCH} 行")

batch_no, total_ms = 0, 0.0
while True:
    t0 = time.perf_counter()
    cur = conn.execute(
        "DELETE FROM logs WHERE id IN "
        "(SELECT id FROM logs WHERE expired = 1 LIMIT ?)", (BATCH,))
    conn.commit()                      # 每批提交, 释放空间与锁
    ms = (time.perf_counter() - t0) * 1000
    total_ms += ms
    batch_no += 1
    if batch_no <= 3 or cur.rowcount == 0:
        print(f"  第 {batch_no} 批删 {cur.rowcount} 行, 耗时 {ms:.1f} ms")
    if cur.rowcount < BATCH:
        break

print(f"共 {batch_no} 批, 总耗时 {total_ms:.0f} ms")
print("剩余未过期行:", conn.execute("SELECT COUNT(*) FROM logs WHERE expired=0").fetchone()[0])
print("要点: 一条巨型 DELETE 的 undo 与锁持有时间不可控, 分批提交把影响切片;")
print("      生产再加批间 sleep 限速, 过滤列必须有索引否则每批都是全表扫")
```

**追问**:
- 删完的空间会还给操作系统吗?——InnoDB 表空间通常不收缩,大删除后要么 OPTIMIZE TABLE 重建要么在低峰 pt-osc;吞吐回收的是页内复用。
- 分批时主键断档会有影响吗?——没有,每批按过滤条件重查,断档只是让单批行数变少;用游标式 WHERE id > last 反而要处理断档。

---
