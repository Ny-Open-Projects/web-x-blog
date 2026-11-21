---
title: [Q1942] upsert 分支统计: 哪些行走了 insert
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1942 · upsert 分支统计: 哪些行走了 insert

> 难度:★★★★ | 标签:SQL, upsert

**问**:一条批量 upsert 语句执行完, 怎么知道哪些键是新插入、哪些走了更新分支?这有什么用?

**答**:upsert 把 insert 与 update 合并成一条语句, 代价是丢掉了分支可见性:changes 只返回受影响总行数, 不告诉你各分支占比。两种实测归因办法:逐行 INSERT OR IGNORE 加 UPDATE, 用 total_changes 差值精确判定每一行的分支, 适合需要逐行审计的场景;批量 ON CONFLICT 语句则先查已存在键集, 再用总变更数减去新键数反推 update 行数。EXCLUDED 伪表引用本次候选值, 是 DO UPDATE 分支里做增量累加的关键。分支统计的用途很实际:监控新客占比与热键更新比、驱动对账、以及压测时确认批量语句真的命中了预期路径。

```python
# file: code/04_数据库与缓存/q1942_upsert_branch_stats.py
"""upsert 分支统计: 哪些行走了 insert 哪些走了 update"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE stock(sku TEXT PRIMARY KEY, qty INTEGER, updated INTEGER)")
conn.commit()

# 方案一: 逐行 INSERT OR IGNORE 加 UPDATE, 用 total_changes 差值精确归因
def upsert_with_stats(rows):
    ins, upd = [], []
    for sku, qty, ts in rows:
        before = conn.total_changes
        conn.execute("INSERT OR IGNORE INTO stock VALUES(?,?,?)", (sku, qty, ts))
        if conn.total_changes - before == 1:
            ins.append(sku)
        else:
            conn.execute("UPDATE stock SET qty = qty + ?, updated = ? WHERE sku = ?", (qty, ts, sku))
            upd.append(sku)
    return ins, upd

r1 = upsert_with_stats([("A1", 10, 1), ("A2", 5, 1)])
print("第一批 ->", "insert:", r1[0], "update:", r1[1])
r2 = upsert_with_stats([("A1", 3, 2), ("A3", 7, 2), ("A1", 1, 3)])
print("第二批 ->", "insert:", r2[0], "update:", r2[1])
print("表内容 ->", conn.execute("SELECT * FROM stock ORDER BY sku").fetchall())

# 方案二: 单条 ON CONFLICT 批量语句, EXCLUDED 引用本次候选值
# 分支归因: 先查已存在的键, 再用 total_changes 差值反推 update 行数
def upsert_bulk(rows):
    marks = ",".join("?" * len(rows))
    existing = {r[0] for r in conn.execute(
        "SELECT sku FROM stock WHERE sku IN (%s)" % marks, [r[0] for r in rows])}
    before = conn.total_changes
    conn.executemany("""
        INSERT INTO stock(sku, qty, updated) VALUES(?,?,?)
        ON CONFLICT(sku) DO UPDATE SET
            qty = qty + excluded.qty,
            updated = excluded.updated""", rows)
    changed = conn.total_changes - before
    n_ins = len([s for s, _, _ in rows if s not in existing])
    return n_ins, changed - n_ins

r3 = upsert_bulk([("A1", 2, 4), ("A4", 9, 4)])
print("批量 upsert ->", "insert:", r3[0], "update:", r3[1], " 与逐行法口径一致")
print("表终态 ->", conn.execute("SELECT * FROM stock ORDER BY sku").fetchall())
print("结论: changes 口径只给总行数 分支归因靠存在性预查或逐行计数 EXCLUDED 用于引用冲突候选行")
```

**追问**:
- RETURNING 子句能直接区分分支吗?—— SQLite 3.35 与 PG 都支持 RETURNING, 但返回的行不直接带分支标记, 仍要配合 EXCLUDED 或哑列技巧。
- 存在性预查会不会有竞态?—— 并发下预查结果可能过期, 归因用于统计而非业务决策即可, 业务判定仍以数据库唯一约束为准。

---
