---
title: [Q912] relationship 加载策略: selectinload 与 joinedload
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q912 · relationship 加载策略: selectinload 与 joinedload

> 难度:★★★★ | 标签:SQLAlchemy, relationship

**问**:joinedload 和 selectinload 都能解决 N+1,该选哪个?它们的 SQL 形态差在哪?

**答**:joinedload 用 LEFT OUTER JOIN 一次性把主表与关联表连接取出,一条 SQL,但结果集是笛卡尔积——一对多取 100 个父带 10 子会返回 1000 行,父子还可能触发去重;selectinload 先查主表,再拿主表主键 `IN (...)` 批量查子表,两条 SQL,行数不膨胀,对一对多最稳。经验法则:多对一/一对一用 joinedload(天然无膨胀),一对多用 selectinload,深层集合链用 selectinload 嵌套;还可以配 `lazy="selectin"` 把策略写死在 relationship 上。二者都可用 `contains_eager` 借手写 JOIN 填充。

```python
# file: code/04_数据库与缓存/q912_selectin_vs_joined.py
"""统计两种加载策略的 SQL 条数, 直观对比 joinedload 与 selectinload"""

try:
    from sqlalchemy import create_engine, ForeignKey, select, event
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                                mapped_column, relationship, joinedload, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="orders")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    count = {"n": 0}

    @event.listens_for(engine, "before_cursor_execute")
    def _c(*a):
        count["n"] += 1

    Base.metadata.create_all(engine)
    with Session(engine) as s:
        for u in range(10):
            s.add(User(name=f"u{u}", orders=[Order() for _ in range(5)]))
        s.commit()

        for label, opt in (("joinedload", joinedload(User.orders)),
                           ("selectinload", selectinload(User.orders))):
            count["n"] = 0
            users = s.execute(select(User).options(opt)).unique().scalars().all()
            n_orders = sum(len(u.orders) for u in users)
            print(f"{label}: SQL {count['n']} 条, 取回 {n_orders} 个订单")
```

**追问**:
- 为什么 joinedload 对集合要加 distinct?——JOIN 使父行重复出现,SQLAlchemy 自动加 DISTINCT 去重(MySQL 8.0.2x 前用子查询),集合场景行数膨胀本质没变。
- contains_eager 什么时候用?——你已经手写 JOIN 做过滤/排序时,用 contains_eager 直接把连接结果填充进 relationship,避免再发一条查询。

---
