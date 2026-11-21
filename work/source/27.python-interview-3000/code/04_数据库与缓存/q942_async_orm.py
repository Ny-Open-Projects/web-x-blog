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
