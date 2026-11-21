---
title: [Q144] 接口自动化测试:pytest 与 TestClient
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q144 · 接口自动化测试:pytest 与 TestClient

> 难度:★★☆ | 标签:pytest, 测试

**问**:如何不启动真实服务器测试 FastAPI/Flask 接口?依赖如何 mock?

**答**:Starlette 的 `TestClient`(基于 httpx)在进程内直接调用 ASGI app,无需监听端口,可用 `with client` 触发 lifespan;Flask 对应 `app.test_client()`。依赖替换用 FastAPI 的 `app.dependency_overrides[原依赖] = 假依赖`,比 patch 更干净;fixture 管理测试数据与 app 生命周期,数据库用 SQLite 内存库或 testcontainers。断言覆盖状态码、响应结构与副作用。

```python
# file: code/03_Web后端开发/q144_pytest_testclient.py
try:
    from fastapi import FastAPI, Depends
    from fastapi.testclient import TestClient
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

def get_current_user():
    return {'user': 'real'}

@app.get('/me')
def me(user: dict = Depends(get_current_user)):
    return user

client = TestClient(app)

def test_me():
    resp = client.get('/me')
    assert resp.status_code == 200
    assert resp.json() == {'user': 'real'}

def test_me_mocked():
    app.dependency_overrides[get_current_user] = lambda: {'user': 'fake'}
    try:
        resp = client.get('/me')
        assert resp.json() == {'user': 'fake'}
    finally:
        app.dependency_overrides.clear()   # 用完清理,防止影响其他用例

test_me()
test_me_mocked()
print('all tests passed')
```

**追问**:
- TestClient 与真实服务的差别?——进程内调用,无网络栈与代理层;Header/Cookie/HTTPS 行为要单独验证,别把它当集成测试全覆盖。
- dependency_overrides 比 patch 好在哪?——类型安全、只替换 DI 层、随 app 生命周期管理;patch 全局对象容易串用例。
- 测试数据库怎么隔离?——每用例事务回滚或 testcontainers 独立实例;SQLite 与生产方言差异要心里有数,关键 SQL 用同库验证。
