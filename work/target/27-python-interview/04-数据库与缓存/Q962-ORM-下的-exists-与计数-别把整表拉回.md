---
title: [Q962] ORM 下的 exists 与计数: 别把整表拉回来
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q962 · ORM 下的 exists 与计数: 别把整表拉回来

> 难度:★★★☆ | 标签:SQLAlchemy, 性能

**问**:判断"用户是否有订单"和"统计订单数",ORM 怎么写才不浪费?

**答**:存在性判断用 EXISTS:`select(exists().where(Order.user_id == uid))` 或 `session.query(exists)`,数据库找到第一行即返回,永远比 `len(session.scalars(select(Order)).all()) == 0` 快——后者把所有行拉回 Python。计数用 `select(func.count()).select_from(Order).where(...)`,并确认走了覆盖索引(小索引计数更快);只需要"有没有"就别 count。常见反模式:对列表结果取 len(先查全部再数)、循环内逐条 exists(合并成一次 IN 查询)、大表精确 count(改估算或计数器表,Q872)。ORM 层封装 exists/count 两个 Repository 方法,业务禁用 len(query.all())。

```python
# file: code/04_数据库与缓存/q962_exists_count.py
"""exists 与 count 的正确写法 vs 反模式"""

try:
    from sqlalchemy import create_engine, select, func, exists
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Order(user_id=1) for _ in range(100)])
        s.commit()

        # 正确: exists 谓词, 找到一行即短路
        has = s.scalar(select(exists().where(Order.user_id == 1)))
        print("EXISTS 判存在:", has)

        # 正确: 数据库端 count
        n = s.scalar(select(func.count()).select_from(Order)
                     .where(Order.user_id == 1))
        print("COUNT:", n)

        # 反模式对照(仅演示, 禁止上线):
        rows = s.scalars(select(Order).where(Order.user_id == 1)).all()
        print("反模式 len(rows):", len(rows), "<- 拉回 100 行只为判断 0/1")
```

**追问**:
- exists 在 SQLite/MySQL 都会短路吗?——会,EXISTS 语义就是找到即真,优化器对它有专门路径,与 LIMIT 1 效果等价但意图更清晰。
- 为什么 count 也要挑索引?——count 是"数最小的树",覆盖索引比聚簇索引窄,扫描页数少;大表配合估算或计数器方案。

---
