---
title: "[Q6192] QuerySet.update() 不刷新实例：库改了、响应还是旧值"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6192 · QuerySet.update() 不刷新实例：库改了、响应还是旧值

难度：P6 ｜ 标签：Django、QuerySet.update、save、信号、auto_now、缓存一致性

**问**：批量改状态从 `for obj in qs: obj.save()` 优化成 `qs.update(status="done")`，QPS 上去了，但审计日志不再产生、`auto_now` 没更新、接口返回的对象还是旧状态。`update()` 到底做了什么、绕过了什么？为什么内存里的实例不会同步？什么时候必须回到逐条 `save()`？

**答**：
结论：`QuerySet.update()` 直接生成一条 `UPDATE ... WHERE ...` 的 SQL，**不实例化模型、不调用 `save()`、不触发 `pre_save`/`post_save` 信号、不更新 `auto_now`（除非你显式写进 SET）、也不刷新已加载的实例**。它的语义是"对数据库做一次集合更新"，而 `save()` 的语义是"保存一个模型实例"，两者不是同一层。已加载的 `obj` 仍持有旧字段值，`obj.status` 还是旧状态，直到 `refresh_from_db()`。

取舍：a) 纯批量、无需审计/信号/钩子时用 `update()`，性能最好；b) 需要信号或 `auto_now` 时，显式在 `update(...)` 里带上 `updated_at=timezone.now()`，并把审计下沉到"批量事件"（一次写一条 batch 日志），而不是假装每行都有信号；c) 强依赖 `post_save` 的副作用（缓存失效、搜索索引）时，只能逐条 `save()` 或引入 outbox/CDC；d) `update()` 返回受影响行数，**不返回对象**，别拿它当"批量保存并返回列表"用。

实战：事故形态是"订单批量关单改成 `update()` 后，风控的 `post_save` 钩子不再触发，风险名单没有同步；同时接口返回给前端的订单仍是 `paid`，用户刷新才变"。下面用 sqlite3 复现"库已改、内存仍旧、信号未发"三件事，并演示显式补 `updated_at`。

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("create table orders(id integer primary key, status text, updated_at text)")
conn.execute("insert into orders values (1, 'paid', 't0')")

signals = []


def fake_save(obj):
    """模拟 Model.save()：赋值 auto_now 并发信号。"""
    obj["updated_at"] = "t1"
    conn.execute("update orders set status=?, updated_at=? where id=?",
                 (obj["status"], obj["updated_at"], obj["id"]))
    signals.append(("post_save", obj["id"]))


row = conn.execute("select id, status, updated_at from orders where id=1").fetchone()
obj = {"id": row[0], "status": row[1], "updated_at": row[2]}

obj["status"] = "done"
fake_save(obj)
print("[1] save(): 信号", signals, "实例", obj)
print("    库:", conn.execute("select status, updated_at from orders where id=1").fetchone())

# 回到 paid，改用 QuerySet.update()
conn.execute("update orders set status='paid', updated_at='t0' where id=1")
obj = {"id": 1, "status": "paid", "updated_at": "t0"}
signals.clear()

cur = conn.execute("update orders set status='done' where id=1")   # 等价 qs.update(...)
print("[2] update() 受影响行数:", cur.rowcount, "信号:", signals)
print("[3] 库已改:", conn.execute("select status, updated_at from orders where id=1").fetchone())
print("[4] 内存实例仍是旧值:", obj)

# 正确姿势：显式带上 auto_now，并接受"没有 per-row 信号"
conn.execute("update orders set status='paid', updated_at='t0' where id=1")
cur = conn.execute("update orders set status='done', updated_at='t9' where id=1")
print("[5] 显式补时间戳:", conn.execute("select status, updated_at from orders where id=1").fetchone())

conn.close()
```

**追问一**：`update()` 能更新关联字段吗？—— 只能更新本表的列。`update(user__name=...)` 会抛 `FieldError`；要跨表改值得用 `Subquery` 或分两步（先查 id 再更新）。另外 `update()` 会立即执行，不受 `QuerySet` 惰性求值影响，也不支持 `select_related` 之类的加载优化——它根本不加载行。

**追问二**：既然 `update()` 不发信号，为什么很多项目还大量用它？—— 因为"每行信号"在批量场景本来就是错误的抽象：1 万行触发 1 万个钩子，每个钩子再查库/发消息，等于自造 N+1 和消息风暴。正确做法是把"批量变更"当成一个领域事件（一条 batch 消息，带 id 列表与变更前后摘要），由消费者统一处理缓存失效/索引更新。只有当副作用确实逐行不同（比如每行算法不同）时，才逐条 `save()`。

## 背诵要点
- `update()` 直接发 SQL：不实例化、不调 `save()`、不发信号、不自动更新 `auto_now`、不刷新已加载实例。
- 需要时间戳就显式写进 SET；需要逐行副作用只能逐条 `save()` 或改用 outbox/CDC。
- `update()` 返回受影响行数，立即执行，不能跨表更新关联字段。

## 复盘追问
- 批量关单后风控名单没同步、接口还返回旧状态，分别对应 `update()` 的哪两个语义？（信号缺失、实例未刷新）
- 万行批量更新既要审计又不能 N+1，怎么设计？（batch 事件 + 显式时间戳 + 缓存批量失效）
