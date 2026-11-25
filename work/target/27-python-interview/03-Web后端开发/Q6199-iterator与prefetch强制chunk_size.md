---
title: "[Q6199] iterator() 配 prefetch_related 必须给 chunk_size"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6199 · iterator() 配 prefetch_related 必须给 chunk_size

难度：P7 ｜ 标签：Django、iterator、chunk_size、prefetch_related、游标、内存

**问**：导出 200 万行数据，为了省内存把 `for obj in qs` 改成 `qs.iterator()`，结果直接抛 `ValueError: chunk_size must be provided when using QuerySet.iterator() after prefetch_related()`。为什么裸 `iterator()` 不行？`chunk_size` 到底控制什么？加了之后内存会不会又爆？迭代中修改数据会不会漏行？

**答**：
结论：`iterator()` 绕过 QuerySet 的结果缓存，用数据库游标逐行取，默认 `chunk_size=None` 意味着"服务端游标一次取一行"或"客户端缓冲全部"（取决于后端）。`prefetch_related` 需要"主查询的一批 id"才能发起 `IN (...)` 子查询，而"流式逐行"没有批次边界，所以 Django 4.1+ 强制要求 `iterator(chunk_size=N)`：按 N 行一批，既保留批量预取，又限制内存。`chunk_size` 控制的是**每次从游标取多少行 + 每批 prefetch 的规模**，不是"总行数"。

取舍：a) 纯扫描无需关联时直接 `iterator(chunk_size=2000)`，避免默认一次性缓冲；b) 需要 prefetch 时必须给 `chunk_size`，且它要与 prefetch 的子查询规模平衡（太小 → 子查询次数多；太大 → 单批内存高）；c) 只取需要的列（`values_list`/`only`）比调 chunk_size 更有效；d) 迭代中修改被扫描的表，游标行为依赖隔离级别与索引：PostgreSQL 的游标在事务内看到快照，MySQL 可能看到新行/漏行——导出类任务应在只读事务/快照里做，或用 `id > last_id` 的键集分页。

实战：事故形态是"报表导出加 `iterator()` 后报错，随手补了 `chunk_size=100000`，结果单批 prefetch 把内存打满；后来改成 1000 并只 `values_list` 三列，内存才稳定"。下面用游标模拟"分批取 + 每批 prefetch"的内存与查询次数，并复现 Django 的强制校验。

```python
import sqlite3


class QuerySet:
    def __init__(self, conn, prefetch=False):
        self.conn = conn
        self.prefetch = prefetch

    def iterator(self, chunk_size=None):
        if self.prefetch and chunk_size is None:
            raise ValueError(
                "chunk_size must be provided when using QuerySet.iterator() "
                "after prefetch_related()"
            )
        cur = self.conn.execute("select id, author, title from post order by id")
        size = chunk_size or 1
        while True:
            rows = cur.fetchmany(size)
            if not rows:
                break
            if self.prefetch:
                ids = [r[0] for r in rows]
                tags = self.conn.execute(
                    "select post_id, tag from tag where post_id in (%s)"
                    % ",".join("?" * len(ids)),
                    ids,
                ).fetchall()
                yield rows, tags
            else:
                yield rows


conn = sqlite3.connect(":memory:")
conn.execute("create table post(id integer primary key, author text, title text)")
conn.execute("create table tag(post_id integer, tag text)")
conn.executemany("insert into post values (?, ?, ?)",
                 [(i, "a%d" % (i % 5), "t%d" % i) for i in range(1, 11)])
conn.executemany("insert into tag values (?, ?)",
                 [(i, "hot") for i in range(1, 11)])

qs = QuerySet(conn, prefetch=True)
try:
    list(qs.iterator())
except ValueError as e:
    print("[1]", e)

batches = list(qs.iterator(chunk_size=4))
print("[2] 分 3 批:", [len(rows) for rows, _ in batches])
print("[3] 每批 prefetch 的 tag 数:", [len(tags) for _, tags in batches])

no_prefetch = list(QuerySet(conn).iterator(chunk_size=4))
print("[4] 无 prefetch 时只需 chunk_size 控制内存:", [len(b) for b in no_prefetch])

# 迭代中删除：游标看到的是执行计划决定的结果
conn.execute("delete from post where id = 5")
again = [row[0] for batch in QuerySet(conn).iterator(chunk_size=3) for row in batch]
print("[5] 迭代前已删除 5，结果:", again)

conn.close()
```

**追问一**：`iterator()` 期间能不能 `save()` 同一个对象？—— 不建议。`iterator()` 取出的对象不在 QuerySet 缓存里，但仍在 identity map 之外；如果你在循环里改字段并 `save()`，会与游标读取共享同一张表，可能触发锁等待（MySQL 的间隙锁）或让后续批次看到/看不到修改。导出/迁移类任务应"只读快照 + 另开连接写"，或分页键集（`filter(id__gt=last)`）处理。

**追问二**：为什么 `chunk_size` 太小反而慢？—— 每批都要发一次 `IN (...)` 的 prefetch 查询，批次越小，SQL 往返次数越多；同时数据库游标在网络往返上的固定开销被放大。经验值是让单批在"内存可控"（比如几 MB）与"往返次数可接受"之间平衡，常见 1000～5000；真正的优化顺序是"少选列 > 关掉不必要的 prefetch > 调 chunk_size"。

## 背诵要点
- `iterator()` 绕过结果缓存逐批取；`prefetch_related` 需要批次边界，Django 4.1+ 强制 `chunk_size`。
- `chunk_size` 控制每批取行数与 prefetch 规模，不是总量；太小增加 SQL 往返，太大涨内存。
- 迭代中改表会受隔离级别/游标影响；导出用只读快照或键集分页。

## 复盘追问
- 加 `iterator()` 后报 chunk_size 缺失，为什么 prefetch 需要批次？（`IN (...)` 的子查询边界）
- 200 万行导出如何把内存压到常数级？（少选列 + chunk_size + 只读事务/键集分页）
