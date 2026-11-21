---
title: [Q2506] 加列默认值的 online 差异: 元数据与回填
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2506 · 加列默认值的 online 差异: 元数据与回填

> 难度:★★★★ | 标签:迁移, DDL

**问**:同样是加一列带默认值,为什么有的库秒级完成,有的整表重建?

**答**:取决于默认值是"元数据"还是"数据"。MySQL 8.0 的 INSTANT ADD COLUMN、PG 11+ 的 fast default、SQLite 的 ADD COLUMN,都只把默认值记在元数据里:历史行不重写,读取时按元数据补值,5 万行的表实测毫秒级完成。低版本 MySQL 会在数据行里回填默认值,等于整表重建加锁。表达式默认值(如当前时间戳)通常不被 instant 支持——它无法只存元数据。而"加列"秒级完成后,历史数据的业务化填充(如初始化状态)是另一笔账:走可空列 + 分批回填 + 收紧约束的三步,别指望一条 ALTER 同时干完。

```python
# file: code/04_数据库与缓存/q2506_add_column_default.py
"""加列默认值的 online 差异: 元数据秒加与数据回填是两件事"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amt INTEGER)")
c.executemany("INSERT INTO orders(amt) VALUES(?)", [(i,) for i in range(1, 50001)])
conn.commit()

# SQLite / MySQL 8 INSTANT / PG 11+ 这一类: 常量默认值只记元数据, 不改历史行
t0 = time.perf_counter()
c.execute("ALTER TABLE orders ADD COLUMN flag INTEGER NOT NULL DEFAULT 0")
ms_alter = (time.perf_counter() - t0) * 1000
t0 = time.perf_counter()
n = c.execute("SELECT COUNT(*) FROM orders WHERE flag = 0").fetchone()[0]
ms_read = (time.perf_counter() - t0) * 1000
print("5 万行表加列带默认值: ALTER 耗时 %.1f ms, 查询默认值命中 %d 行 耗时 %.1f ms"
      % (ms_alter, n, ms_read))
dflt = [r[4] for r in c.execute("PRAGMA table_info(orders)") if r[1] == "flag"][0]
print("table_info 里 flag 的 dflt_value=%r  <- 默认值存在元数据里, 历史行没被重写" % dflt)

# 表达式默认值在 ALTER ADD COLUMN 里不被允许 (常量才行)
try:
    c.execute("ALTER TABLE orders ADD COLUMN ts INTEGER DEFAULT (strftime('%s','now'))")
except sqlite3.OperationalError as e:
    print("表达式默认值被拒: %s" % e)

# 版本不支持 instant 的库/场景: 加可空列 + 分批回填 + 再收约束
t0 = time.perf_counter()
conn.execute("ALTER TABLE orders ADD COLUMN tag TEXT")
WINDOW, last = 10000, 0
batches = 0
while True:
    cur = conn.execute("SELECT id FROM orders WHERE id > ? AND tag IS NULL LIMIT ?",
                       (last, WINDOW))
    ids = [r[0] for r in cur.fetchall()]
    if not ids:
        break
    conn.execute("UPDATE orders SET tag='legacy' WHERE id IN (%s)"
                 % ",".join("?" * len(ids)), ids)
    conn.commit()
    last = ids[-1]
    batches += 1
ms_backfill = (time.perf_counter() - t0) * 1000
print("回填路线: 加可空列 + %d 个窗口分批 UPDATE, 总耗时 %.1f ms (每批独立提交可断点)"
      % (batches, ms_backfill))
print("结论: '加列'的代价取决于默认值是元数据还是数据; instant DDL 秒级完成,")
print("      回填是另一笔账, 任何库上大表都该走'可空列 -> 分批回填 -> 收紧约束'三步")
```

**追问**:
- instant 加列有什么限制?—— 只能加在末列、常量默认值、部分版本限制并发 DDL;中间插列会退化为重建。
- 默认值改了(SET DEFAULT)会重写数据吗?—— 不会,改的仍是元数据,只影响"未来插入的行",历史行保持原值。

---
