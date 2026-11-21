---
title: [Q924] 分表路由键设计: 按 user_id 取模与一致性哈希
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q924 · 分表路由键设计: 按 user_id 取模与一致性哈希

> 难度:★★★★ | 标签:分表, 路由

**问**:订单表按 user_id 分 16 张表,路由代码怎么写?选路由键要注意什么?

**答**:最简单是 hash 取模:`table = tables[hash(user_id) % N]`,路由层(Repository 或中间件)把写与查都映射到目标表。选键三原则:一、高频查询必须带路由键,否则退化成广播查询(扫 16 张表);二、避免热点倾斜,大卖家/大 V 会把某片打爆,可按"买家 id 分表、卖家查询走二级索引或异构表";三、扩容友好——取模扩容要迁移大量数据,一致性哈希或"按 id 范围分片"只动边界。SQLite 演示 16 张分表的路由与跨片查询兜底,生产用 ShardingSphere 类中间件做同样的事。

```python
# file: code/04_数据库与缓存/q924_shard_routing.py
"""按 user_id 取模路由到 16 张分表, 含跨片查询兜底"""
import sqlite3

N_SHARDS = 16

def shard_table(user_id):
    return f"orders_{user_id % N_SHARDS:02d}"

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    for i in range(N_SHARDS):
        conn.execute(f"""CREATE TABLE orders_{i:02d}
                         (id INTEGER PRIMARY KEY, user_id INT, amt REAL)""")
    rows = [(uid, amt) for uid in range(100) for amt in (10.0, 20.0)]
    for uid, amt in rows:
        conn.execute(f"INSERT INTO {shard_table(uid)} (user_id, amt) VALUES (?, ?)",
                     (uid, amt))

    uid = 77
    print(f"user {uid} 路由到 {shard_table(uid)}:",
          conn.execute(f"SELECT * FROM {shard_table(uid)} WHERE user_id = ?",
                       (uid,)).fetchall())

    # 跨片兜底: UNION ALL 视图思路(仅限低频管理查询)
    union_sql = " UNION ALL ".join(
        f"SELECT user_id, amt FROM orders_{i:02d}" for i in range(N_SHARDS))
    total = conn.execute(
        f"SELECT count(*) FROM ({union_sql}) WHERE user_id = ?", (uid,)).fetchone()[0]
    print("广播查询结果:", total, "<- 应避免, 业务设计保证带路由键")
```

**追问**:
- 订单号里嵌入分片信息有什么好处?——订单号直接携带分片位(如 user_id 后 4 位),按订单号查询免查路由表,一次定位到表。
- 扩容 16 到 32 片怎么办?——取模要迁移一半数据;用一致性哈希只迁移相邻区间,或预分 1024 个逻辑分片映射到物理机,扩容只改映射。

---
