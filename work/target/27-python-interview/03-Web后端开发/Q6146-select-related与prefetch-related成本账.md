---
title: "[Q6146] select_related 与 prefetch_related 成本账"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6146 · select_related 与 prefetch_related 成本账（N+1 治理）

难度：P6 ｜ 标签：ORM、N+1、JOIN、容量规划

**问**：订单列表页 20 条数据发出 61 条 SQL。`select_related`（JOIN）与 `prefetch_related`（两次查询 + 内存拼接）各适合什么关系形态？滥用 prefetch 把整表拉进内存的容量账怎么算？

**答**：
结论：N+1 是"每访问一条关系再发一条 SQL"的惰性加载放大。两种标准解对应两种关系形态：**select_related**（SQL JOIN，一条 SQL）适合 ForeignKey/OneToOne 的**多对一**——每行只 JOIN 出一条关联行，结果集可控；**prefetch_related**（分两条 SQL + Python 内存按外键拼装）适合 **一对多/多对多**——JOIN 会导致关联行翻倍、去重开销与内存浪费。滥用 prefetch 的容量账：`prefetch_related('order_items')` 不带过滤会把**每个主对象的所有子行**全量拉回（20 个订单×每单 5000 明细 = 10 万行进内存），必须给 prefetch 加 QuerySet 过滤切片。

取舍：JOIN 结果集带宽 vs 两次查询的网络往返；关联行数 ≤3 时 prefetch 的第二条 SQL 也很快，两者差距不大——决策看**乘法系数**（关系基数），而不是感觉。Django 的 `Prefetch('items', queryset=Item.objects.filter(...))` 是带条件 prefetch 的唯一正解；SQLAlchemy 用 `selectinload`（对应 prefetch）/`joinedload`（对应 select_related），语义同构。

实战：治理手段——① 开发期 `django.db.connection` 记录查询数断言（pytest 计数 ≤N）或 `django-debug-toolbar`/`nplusone` 工具；② 只取需要的列（`only()/values()`）降低 JOIN 行宽；③ 列表页固定"主查询 + 显式 prefetch 白名单"，禁止模板里触发未声明的惰性加载。

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, total REAL)")
cur.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, order_id INT, sku TEXT)")
cur.executemany("INSERT INTO users VALUES (?,?)", [(i, f"user{i}") for i in range(50)])
cur.executemany("INSERT INTO orders VALUES (?,?,?)",
                [(i, i % 50, i * 2.0) for i in range(100)])
cur.executemany("INSERT INTO items VALUES (?,?,?)",
                [(i, i % 100, f"sku{i}") for i in range(500)])
conn.commit()

query_count = 0
def q(sql, params=()):
    global query_count
    query_count += 1
    return cur.execute(sql, params).fetchall()

# 反例：N+1 —— 1 次订单 + 每单一查 user + 每单一查 items
query_count = 0
orders = q("SELECT id, user_id, total FROM orders LIMIT 20")
for oid, uid, total in orders:
    q("SELECT name FROM users WHERE id=?", (uid,))
    q("SELECT sku FROM items WHERE order_id=?", (oid,))
print("N+1 query count:", query_count)               # 1 + 20 + 20 = 41

# select_related 等价：JOIN 一条 SQL（多对一）
query_count = 0
rows = q("SELECT o.id, u.name, o.total FROM orders o JOIN users u ON u.id=o.user_id LIMIT 20")
print("select_related (JOIN) count:", query_count, "rows:", len(rows))

# prefetch_related 等价：两条 SQL + 内存拼装（一对多）
query_count = 0
main = q("SELECT id, user_id FROM orders LIMIT 20")
all_items = q("SELECT order_id, sku FROM items WHERE order_id IN (%s)" %
              ",".join(str(o[0]) for o in main))
from collections import defaultdict
items_by_order: dict[int, list[str]] = defaultdict(list)
for oid, sku in all_items:
    items_by_order[oid].append(sku)
print("prefetch (2 SQL) count:", query_count, "joined in memory:",
      sum(len(items_by_order[o[0]]) for o in main))

# 滥用账：无过滤 prefetch 拉全表 500 行 vs 条件 prefetch 只拉需要的
n_all = cur.execute("SELECT count(*) FROM items").fetchone()[0]
n_need = len(all_items)
print(f"unfiltered prefetch would fetch {n_all} rows; filtered fetches {n_need}")
```

**追问一**：为什么一对多用 JOIN 反而差？——JOIN 使主表行按子行数复制（20 订单×25 明细 = 500 返回行），网络与去重（DISTINCT/内存合并）成本随基数放大；二次查询的行数恰是真实需要的子行数，线性可控。

**追问二**：`prefetch_related` 的内存峰值账公式？——峰值 ≈ 主对象数×子行平均数×行对象开销 + 拼装字典；带 `values()`/`only()` 可砍半；超过阈值（如单页 >5 万行对象）就该改聚合 SQL（子查询 count）而不是拉明细。

**追问三**：SQLAlchemy 2.0 的 `raiseload`/`lazy='raise'` 如何在架构上根治 N+1？——把"未声明的关系访问"变成运行时异常，强迫调用方显式声明加载策略；配合只读会话与 `selectinload` 白名单，比事后计数断言更早失败。

## 背诵要点
- N+1 = 惰性加载×循环访问；select_related（JOIN）对多对一，prefetch_related（2 SQL+内存拼）对一对多/多对多。
- 决策看关系基数乘法系数；prefetch 必须带条件（Prefetch/queryset 过滤），否则全量子行进内存。
- 治理三件套：测试内查询计数断言、列表页 prefetch 白名单、SQLAlchemy raiseload 让隐式加载直接报错。

## 复盘追问
- 列表页加了 prefetch 后接口耗时反而上升，如何定位 prefetch 过滤不足或行宽过大？（分步计时两条 SQL 与拼装耗时 + 行数打点，讨论阈值化监控）
- ORM 抽象与手写 SQL 的边界怎么定团队规范？（列表页聚合类允许手写 SQL + plan 审计，事务写入走 ORM，讨论可维护性折衷）
