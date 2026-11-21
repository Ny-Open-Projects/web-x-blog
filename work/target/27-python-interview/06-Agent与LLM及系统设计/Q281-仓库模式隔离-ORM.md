---
title: [Q281] 仓库模式隔离 ORM
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q281 · 仓库模式隔离 ORM
> 难度:★★★ | 标签:架构, ORM

**问**:为什么要把 SQL/ORM 查询封装到 Repository 层?Service 层直接写 ORM 有什么问题?

**答**:Repository 层负责把领域对象与存储细节隔离,Service 只面向领域语义调用 `user_repo.get_by_email`。好处:单测可用内存仓库替换、换存储引擎不动业务、查询逻辑集中可优化复用。代价是多一层抽象,简单 CRUD 项目不必上。

```python
# file: code/06_Agent与LLM及系统设计/q281_repository.py
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
```

**追问**:
- Repository 和 DAO 有何区别?——DAO 偏单表 CRUD,Repository 面向聚合根/领域语义,是 DDD 里的概念。
- Repository 怎么和 SQLAlchemy 配合?——Repo 封装 session 操作返回领域对象,事务边界留在 Service/UoW;别把 session 泄漏给业务层。
- 什么项目不必上 Repository?——简单 CRUD、ORM 即领域模型的小服务;多一层抽象只有成本没有收益。
- 查询逻辑集中在 Repo 的好处?——N+1、深分页这类调优只改一处;散落在各 Service 的查询无法统一治理。
