---
title: "[Q6197] distinct() 被 order_by 打回原形：跨表排序把去重搞丢"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6197 · distinct() 被 order_by 打回原形：跨表排序把去重搞丢

难度：P7 ｜ 标签：Django ORM、distinct、order_by、JOIN 放大、分页计数

**问**：列表页写 `Post.objects.filter(comments__isnull=False).distinct().order_by("-comment__created")`，一个帖子有 3 条评论就出现 3 次，`distinct()` 像没生效。为什么加了 distinct 还重复？生成的 SQL 里到底 DISTINCT 了什么？PostgreSQL 的 `distinct("field")` 能不能救？分页总数为什么也对不上？

**答**：
结论：SQL 的 `DISTINCT` 作用于**整个 SELECT 列表**，不是"我脑子里想的那一列"。`order_by("-comment__created")` 引用了关联表的列，Django 为了保证排序有确定结果，会把这列**加进 SELECT**，于是 SQL 变成 `SELECT DISTINCT post.id, post.title, ..., comment.created`——同一帖子的不同评论 `created` 不同，整行就不同，DISTINCT 自然去不掉。JOIN 放大（一篇文章 N 条评论 → N 行）叠加"排序列进 SELECT"，就是重复的直接原因。

取舍：a) 只需要"有评论的帖子"，用 `Exists`/子查询过滤，根本不 JOIN，从源头消灭多行：`Post.objects.filter(Exists(Comment.objects.filter(post=OuterRef("pk"))))`；b) 需要按"最新评论时间"排序，用 `annotate(last=Max("comment__created")).order_by("-last")`，聚合把每个帖子压成一行；c) PostgreSQL 可用 `distinct("post_id")`（DISTINCT ON），但 `order_by` 必须以 `post_id` 开头，且 SQLite/MySQL 不支持，跨库项目不能用；d) 分页的 `count()` 会基于同一 SQL 计算，JOIN 放大让总数虚高，必须用子查询/`Exists` 方案或单独写 count。

实战：事故形态是"帖子列表上线后同一帖子重复出现、翻页越翻越乱，前端按 id 去重后每页数量又不够"。下面用 sqlite3 直接对比"整行 DISTINCT + 关联排序"与"先聚合/先过滤再去重"的结果差异。

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("create table post(id integer primary key, title text)")
conn.execute("create table comment(id integer primary key, post_id integer, created text)")
conn.executemany("insert into post values (?, ?)", [(1, "p1"), (2, "p2")])
conn.executemany(
    "insert into comment values (?, ?, ?)",
    [(1, 1, "2026-01-01"), (2, 1, "2026-01-03"), (3, 1, "2026-01-02"), (4, 2, "2026-01-05")],
)

naive = """
select distinct p.id, p.title, c.created
from post p join comment c on c.post_id = p.id
order by c.created desc
"""
print("[1] 整行 DISTINCT + 关联排序（仍重复）:")
for row in conn.execute(naive):
    print("   ", row)

only_post = """
select distinct p.id, p.title
from post p join comment c on c.post_id = p.id
order by p.id
"""
print("[2] 只选帖子列，DISTINCT 才生效:")
for row in conn.execute(only_post):
    print("   ", row)

aggregated = """
select p.id, p.title, max(c.created) as last_created
from post p join comment c on c.post_id = p.id
group by p.id, p.title
order by last_created desc
"""
print("[3] 聚合到一行再排序:")
for row in conn.execute(aggregated):
    print("   ", row)

exists = """
select p.id, p.title
from post p
where exists (select 1 from comment c where c.post_id = p.id)
order by p.id
"""
print("[4] Exists 子查询，不产生多行:")
for row in conn.execute(exists):
    print("   ", row)

print("[5] 分页 count 若基于 [1]，总数会被 JOIN 放大:",
      conn.execute("select count(*) from (select distinct p.id, p.title, c.created from post p join comment c on c.post_id=p.id)").fetchone()[0],
      "vs 实际帖子数:",
      conn.execute("select count(*) from post").fetchone()[0])

conn.close()
```

**追问一**：为什么 Django 要把 `order_by` 的关联列塞进 SELECT？—— 因为 `ORDER BY` 一个不在 SELECT 里的列，在 `DISTINCT` 语义下是未定义的（数据库可能先 DISTINCT 再排序，排序键丢了）。Django 选择"把排序列一起选出来"来保证顺序确定，代价就是去重粒度被细化。要避免这个副作用，只能让排序键属于主表，或先用聚合/子查询把结果收敛成"一帖一行"。

**追问二**：`distinct()` 和 `annotate(Count(...))` 一起用为什么也容易错？—— `annotate(Count("comments"))` 本身就会 JOIN 并 GROUP BY，`distinct()` 再叠加通常没意义；如果同时 `annotate` 多个多值关联（评论数 + 标签数），JOIN 会笛卡尔放大，计数变成乘积。正确做法是每个聚合用子查询（`Subquery`/`Count` 独立），不要在一个查询里 join 两张多值表再计数。

## 背诵要点
- `DISTINCT` 作用于整个 SELECT 列表；`order_by` 关联字段会把该列加进 SELECT，从而使去重失效。
- 去重方案：`Exists` 子查询（不 JOIN）、`annotate(Max(...))` 聚合到一行、PG 的 `distinct("field")`（不可跨库）。
- JOIN 放大会同时污染 `count()` 与分页；多值关联聚合要用独立子查询，别叠加 join。

## 复盘追问
- 加了 `distinct()` 仍重复，如何从生成的 SQL 解释？（排序列被加入 SELECT，行不再相同）
- 列表页既要"最新评论排序"又要"一帖一行"，怎么写？（`annotate(Max(...))` 或 `Exists` + 子查询排序）
