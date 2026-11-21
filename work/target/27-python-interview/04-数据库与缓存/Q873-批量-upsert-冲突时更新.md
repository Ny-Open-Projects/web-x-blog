---
title: [Q873] 批量 upsert: 冲突时更新
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q873 · 批量 upsert: 冲突时更新

> 难度:★★★☆ | 标签:upsert, 批量

**问**:批量导入数据且可能主键冲突,怎么做?MySQL 与 SQLite 语法有什么差异?

**答**:标准做法是 `INSERT ... ON CONFLICT(唯一键) DO UPDATE`(SQLite/PostgreSQL)或 `INSERT ... ON DUPLICATE KEY UPDATE`(MySQL,0 行判断按全部唯一键),一条语句内由数据库原子地"存在则更新、不存在则插入",避免应用层先查后插的竞态。批量写用 executemany 一批提交,而不是逐行逐事务。注意:MySQL 的 ON DUPLICATE KEY UPDATE 会消耗自增 id 并可能带来主备 gap;SQLite 必须显式给冲突目标列。若"冲突就跳过",用 DO NOTHING / INSERT IGNORE。

```python
# file: code/04_数据库与缓存/q873_batch_upsert.py
"""sqlite3 演示批量 upsert: executemany + ON CONFLICT DO UPDATE"""
import sqlite3

UPSERT = """
INSERT INTO stock (sku, qty) VALUES (?, ?)
ON CONFLICT (sku) DO UPDATE SET qty = qty + excluded.qty
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INT)")
        batches = [
            [("A1", 10), ("A2", 5)],
            [("A1", 3), ("A3", 8)],   # A1 冲突, 应累加而非报错
        ]
        for batch in batches:
            with conn:
                conn.executemany(UPSERT, batch)

        for sku, qty in conn.execute("SELECT sku, qty FROM stock ORDER BY sku"):
            print(sku, qty)
```

**追问**:
- excluded 是什么?——SQLite/PG 里代表"本次试图插入的那行",可引用其列值参与更新计算。
- upsert 和"先 SELECT 再决定"错在哪?——两个事务并发时都查到不存在然后都插入,除非再加锁,upsert 把判断下沉到数据库的原子操作里。

---
