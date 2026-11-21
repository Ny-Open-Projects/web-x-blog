---
title: [Q921] Unit of Work: 谁来提交事务
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q921 · Unit of Work: 谁来提交事务

> 难度:★★★★ | 标签:架构, 事务

**问**:UnitOfWork 模式解决什么问题?和"每个方法自己 commit"比好在哪?

**答**:Unit of Work 把一次业务操作涉及的所有变更收集起来,在边界处一次性提交或整体回滚,核心诉求是原子性与事务边界的唯一归属。反模式是"每个 Repository 方法内部 commit"——跨仓储的业务动作(创建订单+扣库存+发券)被切成多个独立事务,中途失败留下半成品。SQLAlchemy 的 Session 本身就是 UoW:session.add/删除都是登记,commit 才落库;工程实现是提供 `with uow:` 上下文,退出时 commit/rollback,Repository 只登记不提交。注意 UoW 生命周期与请求绑定,不要进程级共享。

```python
# file: code/04_数据库与缓存/q921_unit_of_work.py
"""Unit of Work: 跨仓储操作一个事务, 失败整体回滚"""
import contextlib

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str]

class Stock(Base):
    __tablename__ = "stocks"
    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str]
    qty: Mapped[int]

class UoW:
    def __init__(self, engine):
        self.engine = engine
        self.session = None
    def __enter__(self):
        self.session = Session(self.engine)
        return self
    def __exit__(self, exc_type, *_):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

def place_order(uow, sku):
    stock = uow.session.get(Stock, 1)
    if stock.qty <= 0:
        raise ValueError("库存不足, 整体回滚")
    stock.qty -= 1
    uow.session.add(Order(sku=sku))

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(Stock(sku="x", qty=1)); s.commit()

    with UoW(engine) as uow:               # 成功: 两个表一起提交
        place_order(uow, "x")
    with Session(engine) as s:
        print("成功后库存:", s.get(Stock, 1).qty, "订单数:",
              len(s.query(Order).all()))

    try:
        with UoW(engine) as uow:           # 失败: 整体回滚
            place_order(uow, "x")
            raise ValueError("下游支付失败")
    except ValueError as e:
        print("失败:", e)
    with Session(engine) as s:
        print("回滚后库存:", s.get(Stock, 1).qty)
```

**追问**:
- UoW 与事务上下文是一回事吗?——UoW 还包括变更追踪与聚合提交语义,事务只是其实现载体;小项目用 session 上下文管理器即可,不必造类。
- 异步任务里怎么用?——每个任务函数开独立 UoW,重试粒度等于任务粒度,避免复用请求级 session 跨事件循环。

---
