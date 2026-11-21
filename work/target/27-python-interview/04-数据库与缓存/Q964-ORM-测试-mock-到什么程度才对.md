---
title: [Q964] ORM 测试: mock 到什么程度才对
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q964 · ORM 测试: mock 到什么程度才对

> 难度:★★★☆ | 标签:测试, mock

**问**:单元测试该 mock 掉 Repository 还是连真库?两类测试的分工是什么?

**答**:分工:单元测试 mock Repository(Protocol 接口 + 内存假实现),验证业务逻辑分支,毫秒级、无 IO;集成测试连真库(SQLite 内存或容器化 MySQL)验证 SQL 正确性、约束、事务与迁移。错误方向一:全部 mock——SQL 拼错、约束失效、事务边界问题全测不出来;方向二:全部连真库——慢、数据残留、并发场景难构造。工程要点:Repository 用 Protocol 定义(Q947),测试替身注入;集成测试用事务回滚夹具(Q931)保干净;对"同一查询"在 SQLite 与生产库都要有冒烟(方言差异)。mock 的边界判断标准:被 mock 的对象是否是"你正在验证的行为"——验证业务规则时 DB 是边界,验证数据访问时 DB 是主体。

```python
# file: code/04_数据库与缓存/q964_mock_boundary.py
"""内存 Repository 替身 + 真库集成测试 双层验证"""
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    active: bool = True

class UserRepo(Protocol := object):            # 生产实现签名
    def add(self, u: User) -> None: ...
    def count_active(self) -> int: ...

class MemoryRepo:                              # 单测替身
    def __init__(self):
        self.data: list[User] = []
    def add(self, u):
        self.data.append(u)
    def count_active(self):
        return sum(1 for u in self.data if u.active)

class Business:
    def __init__(self, repo):
        self.repo = repo
    def register(self, name):
        u = User(name=name)
        self.repo.add(u)
        return self.repo.count_active()

def integration_test():
    """真库集成: 验证 SQL 与约束"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT PRIMARY KEY, active INT)")
    try:
        conn.execute("INSERT INTO users VALUES ('a', 1)")
        conn.execute("INSERT INTO users VALUES ('a', 1)")   # 唯一约束
    except sqlite3.IntegrityError:
        return "集成测试: 唯一约束生效, 重复插入被拒"
    return "集成测试: 通过"

if __name__ == "__main__":
    biz = Business(MemoryRepo())
    print("单测: 注册后活跃数 =", biz.register("alice"))
    print(integration_test())
```

**追问**:
- mock 和内存替身哪个好?——优先手写内存替身(行为稳定可复用),mock 框架适合验证"调用是否发生"这类交互断言,不要用 mock 复杂模拟 SQL 行为。
- 集成测试的库怎么起?——CI 用 testcontainers 起真 MySQL,本地单跑可用 SQLite 内存,两档配置由环境变量切换。

---
