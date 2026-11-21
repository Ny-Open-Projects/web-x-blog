---
title: [Q937] ORM 批量写入: executemany 与 insert().values 批量
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q937 · ORM 批量写入: executemany 与 insert().values 批量

> 难度:★★★☆ | 标签:SQLAlchemy, 批量

**问**:用 ORM 插 10 万行,怎么做才快?bulk_save_objects 为什么被弃用?

**答**:三条路径按快慢:一、Core 的 `session.execute(insert(User), [dicts])` —— executemany 批量绑定,2.0 官方推荐,可配合 INSERT..RETURNING 拿回主键;二、逐对象 add + 单次 commit,对象全程被追踪,慢在 ORM 实例化与脏检查;三、bulk_save_objects 2.0 已弃用——它跳过大量 ORM 特性(关系、事件)又不比 Core 方案快,定位尴尬。速度优化还有:关 autoflush、分批 commit 控制事务大小、SQLite 用 executemany 天生快、必要时直接 executemany 跳过 ORM。批量 UPDATE 同理:`session.execute(update(User).where(...), [{...}])` 的 executemany 形态。

```python
# file: code/04_数据库与缓存/q937_bulk_insert.py
"""对比逐对象 add 与 insert executemany 的耗时与 SQL 条数"""
import time

try:
    from sqlalchemy import create_engine, event, insert
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Row(Base):
    __tablename__ = "rows"
    id: Mapped[int] = mapped_column(primary_key=True)
    v: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    n_sql = {"c": 0}
    event.listen(engine, "before_cursor_execute",
                 lambda *a: n_sql.__setitem__("c", n_sql["c"] + 1))
    Base.metadata.create_all(engine)
    data = [{"v": i} for i in range(20000)]

    t0 = time.perf_counter()
    with Session(engine) as s:
        s.add_all([Row(**d) for d in data])
        s.commit()
    print(f"ORM add_all: {(time.perf_counter() - t0) * 1000:.0f} ms, SQL {n_sql['c']} 条")

    n_sql["c"] = 0
    t1 = time.perf_counter()
    with Session(engine) as s:
        s.execute(insert(Row), data)
        s.commit()
    print(f"executemany: {(time.perf_counter() - t1) * 1000:.0f} ms, SQL {n_sql['c']} 条")
```

**追问**:
- executemany 怎么拿到生成的主键?——配合 RETURNING(SQLAlchemy 2.0 在支持的方言上自动处理 executemany + returning),或改分批取回。
- 为什么 ORM 对象插入慢?——每个对象要经历状态机、事件、关系级联与脏检查,10 万次这些 Python 开销远超 SQL 本身。

---
