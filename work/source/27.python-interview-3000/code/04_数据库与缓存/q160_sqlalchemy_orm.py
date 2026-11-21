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
