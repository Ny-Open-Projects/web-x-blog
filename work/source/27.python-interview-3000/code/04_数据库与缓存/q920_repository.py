"""Repository 模式: 接口 Protocol + SQLAlchemy 实现 + 业务服务"""
from __future__ import annotations
from typing import Protocol

try:
    from sqlalchemy import create_engine, select
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
    active: Mapped[bool] = mapped_column(default=True)

class UserRepository(Protocol):
    def get(self, id_: int) -> User | None: ...
    def add(self, user: User) -> None: ...
    def list_active(self) -> list[User]: ...

class SqlUserRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id_: int):
        return self.session.get(User, id_)
    def add(self, user):
        self.session.add(user)
    def list_active(self):
        return list(self.session.scalars(
            select(User).where(User.active == True)))  # noqa: E712

def register(repo: UserRepository, name: str) -> User:
    """业务层只依赖接口, 不知道 ORM 存在"""
    u = User(name=name)
    repo.add(u)
    return u

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        repo = SqlUserRepository(s)
        register(repo, "alice")
        register(repo, "bob")
        s.commit()
        print("活跃用户:", [u.name for u in repo.list_active()])
