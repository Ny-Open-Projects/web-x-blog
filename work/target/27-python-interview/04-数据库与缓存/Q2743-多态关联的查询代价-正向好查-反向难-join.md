---
title: [Q2743] 多态关联的查询代价: 正向好查 反向难 join
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2743 · 多态关联的查询代价: 正向好查 反向难 join

> 难度:★★★★ | 标签:建模, 索引

**问**:评论表用 target_type + target_id 挂在文章、视频、话题上,这种多态关联在查询上要付什么代价?

**答**:正向代价小:按 (target_type, target_id) 复合索引等值查一个对象的评论,和普通外键查询一样快;不加这个索引就是全表扫描,因为 target_id 单列的选择性被三种类型稀释了。反向代价大:想"列出每篇文章的评论数"时,数据库不知道 comment.target_id 该 join 谁的 id——video 和 topic 里同数值的 id 会混进来,把统计撑大;只能按类型分别 join 再 UNION ALL,或每类一张纯关联表。多态关联省了表数量,买的是:没有数据库级外键、反向 join 失效、类型枚举靠应用层自觉。读多写少且反向统计少时它划算,反向 join 密集的模型应该拆成独立关联表。

```python
# file: code/04_数据库与缓存/q2743_polymorphic_cost.py
"""多态关联 target_type + target_id 的查询代价: 正向好查 反向 join 必须 UNION"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE comment (
    id INTEGER PRIMARY KEY, target_type TEXT, target_id INTEGER, body TEXT)""")
rows = []
for i in range(1, 40001):
    rows.append((i, ("article", "video", "topic")[i % 3], i // 3, "c%d" % i))
c.executemany("INSERT INTO comment VALUES(?,?,?,?)", rows)

# 正向: 取一个对象的评论, 有无复合索引的差距
sql_fwd = "SELECT COUNT(*) FROM comment WHERE target_type=? AND target_id=?"
print("无索引计划:", c.execute("EXPLAIN QUERY PLAN " + sql_fwd, ("video", 100)).fetchone()[3])
t0 = time.perf_counter()
for _ in range(20):
    c.execute(sql_fwd, ("video", 100)).fetchone()
print("无索引 20 次查询 %.1f ms" % ((time.perf_counter() - t0) * 1000))

c.execute("CREATE INDEX idx_target ON comment(target_type, target_id)")
print("有索引计划:", c.execute("EXPLAIN QUERY PLAN " + sql_fwd, ("video", 100)).fetchone()[3])
t0 = time.perf_counter()
for _ in range(20):
    c.execute(sql_fwd, ("video", 100)).fetchone()
print("有索引 20 次查询 %.1f ms" % ((time.perf_counter() - t0) * 1000))

# 反向: 每篇文章的评论数。不同类型的 target_id 共用数值空间, 直接 join 会数进别的类型
c.execute("CREATE TABLE article (id INTEGER PRIMARY KEY, title TEXT)")
c.executemany("INSERT INTO article VALUES(?,?)", [(i, "a%d" % i) for i in range(1, 6)])
naive = c.execute("""
    SELECT COUNT(*) FROM article a JOIN comment cm ON cm.target_id = a.id
""").fetchone()[0]
correct = c.execute("""
    SELECT COUNT(*) FROM article a
    JOIN comment cm ON cm.target_type='article' AND cm.target_id = a.id
""").fetchone()[0]
print("按 target_id 直接 join 统计到 %d 条 (混入其他类型); 加类型条件后 %d 条 (正确)" % (naive, correct))
print("多类型反向汇总只能按类型 UNION ALL 或拆独立关联表, 这就是多态关联的反向税")
```

**追问**:
- 为什么单列索引 target_id 不够用?—— 三种类型共用 id 数值空间,单列选择性低,而且语义上必须先定类型再定对象。
- 多态关联怎么补完整性?—— 数据库层给不了外键,只能靠应用层双写校验加定时孤儿扫描兜底。

---
