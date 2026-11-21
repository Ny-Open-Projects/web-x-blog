---
title: [Q963] 批量更新: CASE WHEN 与 executemany 对比
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q963 · 批量更新: CASE WHEN 与 executemany 对比

> 难度:★★★☆ | 标签:SQLAlchemy, 批量

**问**:一次更新 5000 个商品的价格,逐条 UPDATE、executemany、CASE WHEN 三种写法怎么选?

**答**:逐条 UPDATE + 每条 commit 是最差路径:N 次往返 × N 个事务,网络与 fsync 都乘 N。executemany(参数数组)一次往返完成 N 行同构更新,是默认选择;各行更新表达式不同(如按 id 定价)时,SQLAlchemy 的 `update(Table).where(...), [{...}]` executemany 形态同样适用。CASE WHEN 单语句形态 `UPDATE t SET price = CASE id WHEN 1 THEN .. WHEN 2 THEN .. END WHERE id IN (..)` 适合极小批量且要求单语句原子;大批量 CASE 语句解析成本高、SQL 超长,不如 executemany。批量级数万行时再叠加分批提交(Q896)。MySQL 还可 INSERT..ON DUPLICATE KEY UPDATE 做批量 upsert。

```python
# file: code/04_数据库与缓存/q963_batch_update.py
"""三种批量更新路径的耗时对比"""
import sqlite3
import time

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, price REAL)")
    N = 5000
    conn.executemany("INSERT INTO goods (price) VALUES (?)",
                     [(i * 1.0,) for i in range(N)])

    def bench(label, fn):
        t0 = time.perf_counter()
        fn()
        print(f"{label}: {(time.perf_counter() - t0) * 1000:.0f} ms")

    def per_row():
        c = sqlite3.connect(":memory:")
        c.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, price REAL)")
        c.executemany("INSERT INTO goods (price) VALUES (?)",
                      [(i * 1.0,) for i in range(N)])
        for i in range(1, N + 1):
            c.execute("UPDATE goods SET price = price * 2 WHERE id = ?", (i,))
        c.commit()

    def executemany_style():
        data = [(i * 3.0, i) for i in range(1, N + 1)]
        conn.executemany("UPDATE goods SET price = ? WHERE id = ?", data)
        conn.commit()

    def case_when():
        ids = list(range(1, 101))               # 小批量示例
        whens = " ".join(f"WHEN {i} THEN {i * 9.0}" for i in ids)
        conn.execute(f"UPDATE goods SET price = CASE id {whens} END "
                     f"WHERE id IN ({','.join(map(str, ids))})")
        conn.commit()

    bench("逐条 UPDATE 含建库", per_row)
    bench("executemany 5000 行", executemany_style)
    bench("CASE WHEN 100 行", case_when)
```

**追问**:
- executemany 真的只发一条 SQL 吗?——协议上是一条语句复用 + N 组参数(SQLite/MySQL 批量绑定),省掉的是解析与往返,不是 N 次行写。
- 什么时候必须分批提交?——单批影响行数过大导致锁与 undo 堆积时(经验 1 万行级),批量内部再切片 commit。

---
