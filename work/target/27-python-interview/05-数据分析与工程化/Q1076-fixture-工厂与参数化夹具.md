---
title: [Q1076] fixture 工厂与参数化夹具
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1076 · fixture 工厂与参数化夹具

> 难度:★★★★ | 标签:pytest, fixture

**问**:一个测试要创建 5 个不同配置的用户,你不会写 5 个 fixture 吧?怎么设计?

**答**:用 fixture 工厂(fixture 返回一个创建函数):外层 fixture 负责共享资源与清理,内层闭包负责定制参数,测试里按需 `user = make_user(role="admin")`。好处是把"创建几个、什么配置"的决定权交给测试体,而清理逻辑仍由 yield fixture 统一兜底;工厂里维护一个 created 列表,teardown 时逐个回收。这是测试数据构造中最常用的模式,比"一个场景一个 fixture"的组合爆炸可维护得多。

```python
# file: code/05_数据分析与工程化/q1076_fixture_factory.py

class UserStore:
    def __init__(self):
        self.users = []

    def add(self, name):
        user = {"id": len(self.users) + 1, "name": name}
        self.users.append(user)
        return user

def make_user_fixture(store):
    """pytest 真实用法:conftest 里 yield 这个工厂,测试内按需调用"""
    created = []

    def _make(name="alice", role="member"):
        user = store.add(name)
        user["role"] = role
        created.append(user)
        return user

    _make.created = created
    return _make

if __name__ == "__main__":
    store = UserStore()
    new_user = make_user_fixture(store)
    u1 = new_user()
    u2 = new_user("bob", role="admin")
    print(u1, u2)
    print("本次测试创建:", new_user.created, "清理时逐个回收即可")
```

**追问**:
- 追问 1:工厂和 yield fixture 怎么配合清理?—— fixture 里 `yield make_user_fixture(store)`,yield 之后遍历 created 回收,测试体不需要感知清理。
- 追问 2:工厂创建的对象要进缓存复用怎么办?—— 工厂内部按参数做 memo,或结合 request.cache,避免同配置重复创建。
