---
title: [Q159] SQLAlchemy 2.x Core 用法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q159 · SQLAlchemy 2.x Core 用法

> 难度:★★★ | 标签:SQLAlchemy, Core

**问**:SQLAlchemy 的 Core 和 ORM 有什么区别?什么时候选 Core?

**答**:Core 是"SQL 表达式语言",围绕 Table 对象构造 SQL,所见即所得、开销小、可控性强,适合批量处理、报表和性能敏感场景;ORM 在其上叠加对象关系映射与 Unit of Work,适合业务建模。2.x 统一了 API:用 `Engine` + `Connection` + `select()/insert()` 表达式,执行时通过 `connection.execute()`。

```python
# file: code/04_数据库与缓存/q159_sqlalchemy_core.py
"""SQLAlchemy 2.x Core 最小示例: sqlite3 可直接运行"""

try:
    from sqlalchemy import (
        create_engine, MetaData, Table, Column, Integer, String, insert, select,
    )
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(32), nullable=False),
    Column("age", Integer),
)

if __name__ == "__main__":
    metadata.create_all(engine)          # 建表
    with engine.begin() as conn:         # begin 自动提交事务
        conn.execute(insert(users), [
            {"name": "alice", "age": 30},
            {"name": "bob", "age": 25},
        ])

    stmt = select(users.c.name).where(users.c.age >= 26).order_by(users.c.name)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(dict(row._mapping))
```

**追问**:
- `engine.begin()` 与 `engine.connect()` 区别?——begin 包含事务并在退出时提交,connect 不自动提交,需手动 conn.commit()(2.0 风格)。
- Core 性能优于 ORM 的原因?——省去对象状态追踪与 Unit of Work 刷库,SQL 完全由你控制。

---
