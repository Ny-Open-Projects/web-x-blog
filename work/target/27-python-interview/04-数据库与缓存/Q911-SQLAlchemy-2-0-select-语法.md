---
title: [Q911] SQLAlchemy 2.0 select 语法入门
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q911 · SQLAlchemy 2.0 select 语法入门

> 难度:★★★☆ | 标签:SQLAlchemy, 查询

**问**:SQLAlchemy 2.0 的 select 写法和 1.x 的 query 有什么区别?执行结果怎么取?

**答**:2.0 统一了 ORM 与 Core:`select(User).where(User.id == 1)` 返回 Select 对象,通过 `session.execute()` 执行,ORM 实体用 `session.scalars()` 取标量行,列查询用 `.scalars()`/`.all()` 按列取。1.x 的 `session.query()` 风格在 2.0 属遗留,新代码统一 select 语法,好处是查询对象与 Core/异步完全一致、类型标注友好。常用形态:where 多条件用 & | 且要加括号、order_by、limit/offset、join、group_by,链式组装天然支持动态条件。

```python
# file: code/04_数据库与缓存/q911_select_20.py
"""SQLAlchemy 2.0 select 全家桶: where/order/limit/聚合"""
try:
    from sqlalchemy import create_engine, select, func
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(name=n, age=a) for n, a in
                   [("a", 20), ("b", 30), ("c", 30)]])
        s.commit()

        print(s.scalars(select(User).where(User.age == 30)).all())
        print(s.scalar(select(func.count()).select_from(User)))
        print(s.scalars(select(User).order_by(User.age.desc(), User.id)
                        .limit(2)).all())
```

**追问**:
- scalars 与 execute 的区别?——execute 返回 Row 元组集合,scalars 取每行第一列(常用于实体或单列),count 之类单值用 scalar。
- 动态条件怎么拼?——预先构造 `conds = []`,按需 append,最后 `select(User).where(*conds)`,空列表表示无条件。

---
