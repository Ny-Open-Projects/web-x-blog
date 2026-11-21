---
title: [Q6526] SQLAlchemy 2.0 类型化声明映射迁移
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6526 · SQLAlchemy 2.0 类型化声明映射：Mapped/MappedColumn 与 1.x 的差异及迁移要点

> 难度:★★★ | 标签:SQLAlchemy, 类型检查, 迁移

**问**：老项目全是 `Column(Integer)` 风格，mypy 里模型属性全是 Any。SQLAlchemy 2.0 的类型化声明映射解决了什么？迁移时最常踩的坑是什么？

**答**：结论：2.0 的 `Mapped[...]` + `mapped_column()` 把列类型写进注解，静态检查器能推理出 `user.name` 是 `str` 而不是 Any，IDE 补全、重构安全性、relationship 的类型推断都受益。同时 2.0 强制 `DeclarativeBase` 基类，`query()` 时代 API 被 `select()` 统一，1.4 提供 future 模式作为过渡。迁移最大的坑不是语法而是**语义**：`Column` 默认 nullable、`Optional[int]` 的映射规则、以及老代码里"改属性不 commit 也能读旧值"的隐式行为差异。

机理与实战：
- 注解规则：`Mapped[int]` 映射 NOT NULL 列，`Mapped[Optional[int]]` 映射可空列；只写注解不给类型也能由 `mapped_column(Integer)` 推断，但**注解与列类型冲突时以注解为准**，这是最容易静默出错的点。
- relationship 类型化：`Mapped[List["Order"]] = relationship()` 让一对多完全静态可查；`back_populates` 在 2.0 下更强调显式双向声明，老式 `backref` 虽兼容但绕过类型检查。
- 迁移路径：先开 `future=True` 在 1.4 上兼容运行 → 批量把 `Column` 换 `mapped_column`（Alembic 无感知，纯 Python 层）→ 删除 `Query` 用法换 `select()`。`Session.execute(select(...)).scalars()` 的返回值语义要逐个核对，这是行为回归高发区。

```python
# 基线:Python 3.9+ / SQLAlchemy 2.0 ;缺库降级:纯标准库演示注解推断
try:
    from sqlalchemy import ForeignKey, String, create_engine, select
    from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column,
                                relationship, Session)
    HAS_SA = True
except ImportError:
    HAS_SA = False


def demo_sa() -> None:
    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__ = "user"
        id: Mapped[int] = mapped_column(primary_key=True)          # 注解推断 NOT NULL
        name: Mapped[str] = mapped_column(String(50))
        nickname: Mapped[str | None]                                # 可空列,连列类型都可省
        orders: Mapped[list["Order"]] = relationship(back_populates="user")

    class Order(Base):
        __tablename__ = "order"
        id: Mapped[int] = mapped_column(primary_key=True)
        user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
        user: Mapped["User"] = relationship(back_populates="orders")

    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        u = User(name="w", nickname=None, orders=[Order()])
        s.add(u)
        s.commit()
        # 静态检查视角:u.name 是 str,o.user 是 User,u.nickname 是 str|None
        stmt = select(User).where(User.name == "w")
        got = s.execute(stmt).scalar_one()
        assert got.orders[0].user is got
        print("类型化映射查询通过:", got.name, "orders:", len(got.orders))


def demo_stdlib() -> None:
    """缺库降级:用注解表模拟"Mapped[Optional] -> nullable"推断规则。"""
    from typing import get_type_hints
    hints = {"name": str, "nickname": str | None}
    for col, t in hints.items():
        nullable = type(None) in getattr(t, "__args__", ())
        print(f"{col}: nullable={nullable}")   # 注解即 schema 的核心思想


if HAS_SA:
    demo_sa()
else:
    demo_stdlib()
```

**追问一**：注解写 `str` 但 `mapped_column(String(50), nullable=True)` 冲突时谁赢？
答：注解赢，SQLAlchemy 以 `Mapped[str]` 推断 NOT NULL 并可能告警；但反过来注解 `Optional[str]` 配默认非空列也会被注解修正。团队规范应写明"注解是唯一事实源"，列参数只放索引/约束等非类型信息。

**追问二**：1.x 的 `Query` 时代代码不全量迁移行不行？
答：可以长期共存——2.0 保留 `Query` 兼容层（`legacy_query_y`），新代码用 `select()`。风险点是两者混用时 session 行为差异（`autobegin`、`get` 返回 Optional 语义），建议按模块灰度切换并补类型检查作为护栏。

**背诵要点**：
- `Mapped[...]` 注解决定 nullability 与静态类型，注解优先于列参数。
- relationship 双向显式 back_populates 才能全静态推断。
- 迁移路径：1.4 future=True → Column 换 mapped_column → Query 换 select，逐模块灰度。

**复盘追问**：
- `Mapped[str | None]` 在 Python 3.9 上怎么写（没有 | 语法）？
- 从 Query 迁到 select() 时哪些返回值语义最容易出回归？

## 背诵要点
- 类型化映射让模型属性获得静态类型，注解是 nullability 事实源。
- 2.0 select() 统一查询 API，Query 是兼容层可共存灰度迁移。
- 迁移高发回归点：execute().scalars() 返回语义与 autobegin 行为。

## 复盘追问
- 注解与列参数冲突时框架行为是什么，团队规范如何约定？
- relationship 的类型推断在循环引用下如何处理？
