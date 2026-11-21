---
title: [Q954] ORM 层的死锁防范: 统一更新顺序与短事务
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q954 · ORM 层的死锁防范: 统一更新顺序与短事务

> 难度:★★★★ | 标签:死锁, SQLAlchemy

**问**:ORM 批量更新购物车多行时怎么防死锁?SQLAlchemy 有什么坑?

**答**:死锁三源头在 ORM 语境下依旧成立:交叉顺序加锁、长事务、热点间隙。防线一:按稳定键(主键)排序后再逐条更新——`for obj in sorted(objects, key=lambda o: o.id)`;防线二:session 提交前才 flush,事务尽量短,锁内不做 IO;防线三:批量 UPDATE 用 executemany/单条 CASE 而不是"读-改-写"循环,把行锁获取压缩到一条语句。SQLAlchemy 特有坑:relationship 的级联 save-update 会让"看起来只改 A"实际按依赖顺序写多表,顺序不可控时对热点并发不友好;commit 后对象过期导致意外重查,也拉长持锁时间(expire_on_commit=False 有帮助)。

```python
# file: code/04_数据库与缓存/q954_orm_deadlock.py
"""排序后批量更新 vs 随机顺序: 演示统一加锁顺序"""
import random
import sqlite3
import threading

def update_cart(db, user_id, items, busy=400):
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute(f"PRAGMA busy_timeout={busy}")
    try:
        conn.execute("BEGIN IMMEDIATE")
        for sku in items:                       # 调用方决定顺序
            conn.execute(
                "UPDATE cart SET qty = qty + 1 WHERE user_id = ? AND sku = ?",
                (user_id, sku))
        conn.execute("COMMIT")
        return "ok"
    except sqlite3.OperationalError:
        conn.execute("ROLLBACK")
        return "busy"
    finally:
        conn.close()

if __name__ == "__main__":
    db = "q954.db"
    s = sqlite3.connect(db, isolation_level=None)
    s.execute("CREATE TABLE IF NOT EXISTS cart (user_id INT, sku TEXT, qty INT, "
              "PRIMARY KEY (user_id, sku))")
    s.execute("DELETE FROM cart")
    s.executemany("INSERT INTO cart VALUES (1, ?, 0)", [("a",), ("b",), ("c",)])
    s.close()

    random.seed(2)
    print("随机顺序:", update_cart(db, 1, random.sample(["a", "b", "c"], 3)))
    print("排序顺序:", update_cart(db, 1, sorted(["c", "a", "b"])))
    print("批量合并:", sqlite3.connect(db).execute(
        "SELECT sku, qty FROM cart ORDER BY sku").fetchall())
    print("结论: 多事务并发时必须统一按主键排序加锁, 否则循环等待")
```

**追问**:
- SQLAlchemy 的 unit of work 会自己排序吗?——flush 按表依赖拓扑排序 insert/update/delete,但"行级加锁顺序"由 WHERE 命中顺序决定,批量提交多行时仍需业务侧排序。
- 死锁重试在 ORM 里怎么落地?——捕获 OperationalError/StaleDataError,session.rollback() 后整体重试,注意重试范围是"整个用例"而不是单条语句。

---
