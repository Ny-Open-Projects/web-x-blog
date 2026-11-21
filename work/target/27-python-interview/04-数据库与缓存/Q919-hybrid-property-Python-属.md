---
title: [Q919] hybrid_property: Python 属性与 SQL 表达式两栖
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q919 · hybrid_property: Python 属性与 SQL 表达式两栖

> 难度:★★★☆ | 标签:SQLAlchemy, 查询

**问**:普通 @property 与 hybrid_property 有什么区别?什么时候必须用后者?

**答**:@property 只在 Python 对象层工作,不能出现在 where/order_by 里——ORM 会因为不知道如何翻译成 SQL 而报错。hybrid_property 提供两栖定义:实例层用 Python 函数计算,类层默认同一函数被当作 SQL 表达式调用,复杂逻辑可用 @x.expression 自定义 SQL 版本。典型场景:全名字段 first+last、状态推导 is_expired、软删除过滤条件,这些既要读对象时算,又要进查询条件时翻译成 SQL,避免"写死在 SQL 里对象上没有"或反之的割裂。

```python
# file: code/04_数据库与缓存/q919_hybrid_property.py
"""hybrid_property 同时服务对象读取与 SQL 过滤"""

try:
    from sqlalchemy import create_engine, select
    from sqlalchemy.ext.hybrid import hybrid_property
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first: Mapped[str]
    last: Mapped[str]

    @hybrid_property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.expression
    def full_name(cls):
        return cls.first + " " + cls.last

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(first="Ada", last="Lovelace"),
                   User(first="Alan", last="Turing")])
        s.commit()
        print("对象层:", s.scalars(select(User)).first().full_name)
        print("SQL 层:", s.scalars(select(User)
              .where(User.full_name == "Alan Turing")).one().first)
```

**追问**:
- hybrid 和 column_property 怎么选?——column_property 在查询时作为列表达式一次性求值适合纯派生列;hybrid 强在"对象与查询两用"且可写 setter。
- 表达式层能用 Python 函数吗?——不能,必须翻译成 SQL 构造(如 func.lower),否则运行时无法编译成 SQL。

---
