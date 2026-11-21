---
title: [Q913] lazy 策略谱系与 raiseload 防护
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q913 · lazy 策略谱系与 raiseload 防护

> 难度:★★★★ | 标签:SQLAlchemy, relationship

**问**:relationship 的 lazy 参数有哪些取值?怎么防止业务代码意外触发隐式查询?

**答**:lazy 决定"首次访问 relationship 属性时如何加载":默认 select(访问时单发一条,即 N+1 源头)、selectin/joined/subquery(首次访问用批量/连接方式)、raise/raise_on_sql(访问未加载属性直接抛异常,用于强制显式加载)、noload(永不加载)、dynamic(返回可继续过滤的查询,适合大集合)。工程价值:把核心 relationship 设为 `lazy="raise_on_sql"`,任何隐式懒加载都会在测试阶段爆炸式报错,逼团队显式写 options,这是根治 ORM 性能退化的有效纪律。异步框架下隐式懒加载会直接失败,raise 语义反而是常态。

```python
# file: code/04_数据库与缓存/q913_lazy_raise.py
"""lazy=raise_on_sql 演示: 未预加载就访问属性立即报错"""

try:
    from sqlalchemy import create_engine, ForeignKey, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                relationship, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user", lazy="raise_on_sql")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="orders")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(User(orders=[Order(), Order()]))
        s.commit()

        u = s.scalars(select(User).options(selectinload(User.orders))).one()
        print("预加载后访问:", len(u.orders), "个订单")

        u2 = s.scalars(select(User)).one()
        try:
            _ = u2.orders
        except Exception as e:
            print("未预加载访问被拦截:", type(e).__name__)
```

**追问**:
- dynamic lazy 为什么被 2.0 弃用提示?——它让"关系即查询"边界模糊且与异步/批量加载冲突,官方建议改为显式 select(Order).where(...)。
- noload 与 raiseload 区别?——noload 静默返回空,raiseload 显式报错;防护场景用 raise,确认永不使用的场景才用 noload。

---
