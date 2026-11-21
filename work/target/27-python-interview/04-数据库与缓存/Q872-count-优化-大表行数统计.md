---
title: [Q872] count 优化: 大表行数统计
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q872 · count 优化: 大表行数统计

> 难度:★★★☆ | 标签:聚合, 优化

**问**:MyISAM 不带 WHERE 的 count(*) 为什么快?InnoDB 下大表 count 慢怎么优化?

**答**:MyISAM 存了精确总行数变量,无 WHERE 时直接读;InnoDB 的 MVCC 下"每个事务看到的行数不同",必须实际扫描(小代价可走最小的索引)才能给出本事务可见的 count。优化路径:对"总数仅供参考"的场景用 `EXPLAIN` 的估算行数或 information_schema 统计;需要精确但允许秒级延迟时维护计数器表(在业务事务里 upsert加减),或用缓存/异步任务定期刷新;展示层直接砍掉总数,只给"下一页"。count(*) 与 count(1) 无性能差异,count(col) 会跳过 NULL,语义不同。

```python
# file: code/04_数据库与缓存/q872_counter_table.py
"""用计数器表替代全表 count: 事务内同步增减, 查询 O1"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript("""
            CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT);
            CREATE TABLE counter (name TEXT PRIMARY KEY, cnt INT);
            INSERT INTO counter VALUES ('paid_orders', 0);
        """)

        def create_order(cur, status):
            cur.execute("INSERT INTO orders (status) VALUES (?)", (status,))
            if status == "paid":
                cur.execute(
                    "INSERT INTO counter (name, cnt) VALUES ('paid_orders', 1) "
                    "ON CONFLICT (name) DO UPDATE SET cnt = cnt + 1")

        for i in range(1000):
            with conn:
                create_order(conn.cursor(), "paid" if i % 2 else "new")

        print("全表 count:", conn.execute(
            "SELECT COUNT(*) FROM orders WHERE status='paid'").fetchone()[0])
        print("计数器表:", conn.execute(
            "SELECT cnt FROM counter WHERE name='paid_orders'").fetchone()[0])
```

**追问**:
- 计数器表会不会成为热点?——会,单行高频更新有锁竞争,可拆成 N 行分片累加,读时求和,或改用 Redis 计数。
- count(*) 能走覆盖索引吗?——能,优化器会挑最小的索引来数行数,所以也不要给 count 查询用 SELECT 列。

---
