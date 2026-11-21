---
title: [Q188] fixture 的四种作用域
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q188 · fixture 的四种作用域

> 难度:★★☆ | 标签:pytest, fixture, scope

**问**:fixture 的 scope 分别是什么?什么时候该用 session 级?

**答**:scope 有四种:`function`(默认,每个测试函数一个)、`class`、`module`(每个文件一个)、`session`(整个测试进程一个)。**高作用域 fixture 会被低作用域测试复用**,适合昂贵且只读的资源:session 级建数据库连接池或下载测试数据,module 级起一个本地 mock server。关键规则:**高作用域 fixture 不能依赖低作用域 fixture**(session 依赖 function 会直接报错),因为 session 只实例化一次,无法跟随 function 重建。需要隔离写状态的资源时,坚持 function 级并在 yield 后清理。

```python
# file: code/05_数据分析与工程化/q188_fixture_scope.py
try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.fixture(scope="session")
def db_pool():
    # 整个测试会话只创建一次
    return {"connected": True}

@pytest.fixture(scope="function")
def fresh_user(db_pool):
    # function 级依赖 session 级:合法
    return {"name": "alice", "db": db_pool}

def test_a(fresh_user):
    assert fresh_user["db"]["connected"]

def test_b(fresh_user):
    # fresh_user 在每个测试中都是新实例,测试间互不污染
    fresh_user["name"] = "bob"
    assert fresh_user["name"] == "bob"

def test_c(fresh_user):
    assert fresh_user["name"] == "alice"
```

**追问**:
- 为什么 session 级 fixture 不能依赖 function 级?——session 只实例化一次,无法在 function 级测试间反复重建,pytest 直接报 ScopeMismatch;需要时把数据传参或在低作用域里取自 session 对象。
- 高作用域 fixture 里的可变状态怎么防污染?——只读资源放高作用域;要写就每测试重置(事务回滚/快照恢复),否则用例顺序影响结果。
- scope 怎么选?——问一句「这个资源能不能跨用例共享」:连接池、容器、下载的数据共享;临时表、文件、随机种子每次新建。
