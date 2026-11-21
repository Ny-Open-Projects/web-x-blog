---
title: [Q2775] 表膨胀的估算与增量清理: freelist 算账 增量还页
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2775 · 表膨胀的估算与增量清理: freelist 算账 增量还页

> 难度:★★★☆ | 标签:运维, SQLite

**问**:表删了一半数据,文件一点没变小,怎么估算能回收多少、要不要清理?

**答**:先算账再动手。膨胀的账本在页统计里:page_count 是文件总页数,freelist_count 是已释放待复用的空页,空页占比就是可回收比例,乘以页大小得到可回收字节数——这个数决定值不值得安排清理窗口(占比低于一两成通常不值得)。清理方式看引擎:SQLite 全量 VACUUM 会重建整库、锁库且需要等量临时空间,大库不可控;开 auto_vacuum=INCREMENTAL 后用 PRAGMA incremental_vacuum(N) 每次只还 N 页,把一次性大 IO 拆成可控小批。预防比清理更省:批量删除本来就该配分批与定期,避免 freelist 长期高位。注意 MySQL 的表膨胀另有 optimize table 一套机制,思想相同:先估算,再分批,挑窗口。

```python
# file: code/04_数据库与缓存/q2775_bloat_estimate.py
"""表膨胀的估算与增量清理: freelist 算账, auto_vacuum 增量还页"""
import os
import sqlite3
import tempfile

dbpath = os.path.join(tempfile.mkdtemp(), "bloat.db")
conn = sqlite3.connect(dbpath, isolation_level=None)
conn.execute("PRAGMA page_size=4096")
conn.execute("PRAGMA auto_vacuum=INCREMENTAL")     # 必须在建表前设置
conn.execute("CREATE TABLE log (id INTEGER PRIMARY KEY, msg TEXT)")
conn.execute("BEGIN IMMEDIATE")
conn.executemany("INSERT INTO log VALUES(?,?)",
                 [(i, "m" * 100) for i in range(1, 20001)])
conn.execute("COMMIT")
before = conn.execute("PRAGMA page_count").fetchone()[0]
conn.execute("DELETE FROM log WHERE id % 2 = 0")   # 删一半: 空页留在 freelist, 文件不变小

pc = conn.execute("PRAGMA page_count").fetchone()[0]
fl = conn.execute("PRAGMA freelist_count").fetchone()[0]
print("删除一半后: page_count=%d, freelist=%d (%.0f%%), 可回收约 %.1f MB"
      % (pc, fl, fl * 100.0 / pc, fl * 4096 / 1048576.0))

conn.execute("PRAGMA incremental_vacuum(200)")     # 每次最多还 200 页, 控 IO 节奏
fl2 = conn.execute("PRAGMA freelist_count").fetchone()[0]
print("增量回收一批后 freelist=%d (还剩 %d 页待回收)" % (fl2, fl2))
conn.execute("PRAGMA incremental_vacuum")          # 不带参数 = 全部还清
fl3 = conn.execute("PRAGMA freelist_count").fetchone()[0]
pc3 = conn.execute("PRAGMA page_count").fetchone()[0]
print("全部还清: freelist=%d, page_count=%d, 文件缩小 %.1f MB"
      % (fl3, pc3, (before - pc3) * 4096 / 1048576.0))
conn.close()
```

**追问**:
- freelist 里的页会被新写入复用吗?—— 会,后续插入优先填 freelist,所以膨胀的害处是文件虚高与扫描 IO,不是空间永久流失。
- auto_vacuum 能在老库上补开吗?—— 需要一次 VACUUM 重建库才能生效,老库要评估清理窗口,和增量清理的成本一起算。

---
