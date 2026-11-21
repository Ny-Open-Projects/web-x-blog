---
title: [Q160] SQLAlchemy 2.x ORM 用法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q160 · SQLAlchemy 2.x ORM 用法

> 难度:★★★ | 标签:SQLAlchemy, ORM

**问**:用 ORM 建模并完成一次增查,2.x 的推荐写法是什么?

**答**:2.x 用 `DeclarativeBase` + `Mapped`/`mapped_column` 声明模型,类型注解驱动;写操作通过 `Session.add()` + `session.commit()`,查询用 `session.scalars(select(Model)...)` 返回对象列表。ORM 适合业务复杂、对象间有关联的场景,代价是学习成本和 N+1 风险(见 Q162)。

```python
# file: code/04_数据库与缓存/q160_sqlalchemy_orm.py
"""SQLAlchemy 2.x ORM 风格: DeclarativeBase + Mapped"""
from typing import Optional

try:
    from sqlalchemy import String, create_engine, select
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "orm_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32))
    age: Mapped[Optional[int]]

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name!r})"


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:            # 写: add + commit
        session.add_all([User(name="alice", age=30), User(name="bob", age=25)])
        session.commit()

    with Session(engine) as session:            # 读: select 表达式
        stmt = select(User).where(User.age >= 26).order_by(User.id)
        for user in session.scalars(stmt):
            print(user)
```

**追问**:
- `session.scalars` 和 `session.execute` 的区别?——scalars 直接取第一列并返回标量/对象,execute 返回 Row,需要 `row._mapping` 或下标取值。
- 模型里的 relationship 何时配置?——定义一对多/多对多关联与级联时,配合 `selectinload/joinedload` 控制加载方式。

---
