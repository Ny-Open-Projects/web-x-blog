---
title: [Q942] 异步 ORM: SQLAlchemy 2.0 asyncio 用法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q942 · 异步 ORM: SQLAlchemy 2.0 asyncio 用法

> 难度:★★★★ | 标签:SQLAlchemy, asyncio

**问**:异步 ORM 与同步的差异在哪?哪些坑最容易踩?

**答**:2.0 原生支持 asyncio:create_async_engine + AsyncSession,execute/commit 都是 await;底层依赖驱动(aiosqlite/asyncpg/aiomysql)。最容易踩的坑:懒加载在异步里不能隐式发生(没有隐式 IO),必须显式 await session.run_sync 或用 selectinload 预加载;AsyncSession 不是并发安全的,一个请求一个 session;阻塞调用(重计算、time.sleep)会卡死事件循环,要 run_in_executor。事务语义相同,commit/rollback 均为 await。另一个实践:同一个服务里同步异步 ORM 别混用连接池,账号与池参数独立管理。

```python
# file: code/04_数据库与缓存/q942_async_orm.py
"""SQLAlchemy 2.0 异步: create_async_engine + AsyncSession"""
import asyncio

try:
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column,
                                selectinload)
    from sqlalchemy import select, ForeignKey
    from sqlalchemy.orm import relationship
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0 aiosqlite,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="posts")

async def main():
    engine = create_async_engine("sqlite+aiosqlite://")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSession(engine) as s:
        s.add(User(name="a", posts=[Post(), Post()]))
        await s.commit()
        result = await s.execute(
            select(User).options(selectinload(User.posts)))
        u = result.scalars().first()
        print("异步取到:", u.name, len(u.posts), "posts")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- 为什么异步下懒加载直接失败?——隐式懒加载需要同步 IO,事件循环不允许未 await 的数据库访问,SQLAlchemy 抛 MissingGreenlet,解法是预加载或 await session.refresh。
- run_sync 是什么?——把同步函数包成在 greenlet 里执行的异步调用,用于复用同步 ORM 逻辑(如 create_all)。

---
