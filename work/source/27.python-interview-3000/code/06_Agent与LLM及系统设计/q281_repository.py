from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    def add(self, user: User) -> None: ...


class InMemoryUserRepository(UserRepository):
    """测试用内存实现,接口与 SQL 版一致。"""
    def __init__(self):
        self._data: dict[str, User] = {}
        self._next_id = 1

    def get_by_email(self, email: str) -> User | None:
        return self._data.get(email)

    def add(self, user: User) -> None:
        self._data[user.email] = user


class SQLAlchemyUserRepository(UserRepository):
    """生产实现:模拟,不真正连库。"""
    def __init__(self):
        self._rows: dict[str, dict] = {}

    def get_by_email(self, email: str) -> User | None:
        row = self._rows.get(email)
        return User(**row) if row else None

    def add(self, user: User) -> None:
        self._rows[user.email] = {"id": user.id, "email": user.email}


def register(repo: UserRepository, email: str) -> User | None:
    if repo.get_by_email(email):
        return None
    user = User(id=1, email=email)
    repo.add(user)
    return user


if __name__ == "__main__":
    repo = InMemoryUserRepository()
    print(register(repo, "a@x.com"))
    print(register(repo, "a@x.com"))  # None 已存在
