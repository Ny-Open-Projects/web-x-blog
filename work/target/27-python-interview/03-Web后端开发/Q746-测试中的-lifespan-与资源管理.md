---
title: [Q746] 测试中的 lifespan 与资源管理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q746 · 测试中的 lifespan 与资源管理

> 难度:★★★☆ | 标签:FastAPI, 测试, lifespan

**问**:应用启动时建连接池,测试怎么保证它被正确初始化和销毁?

**答**:`TestClient(app)` 必须**用 with 语句**才会在进入时执行 lifespan(启动建池)、退出时执行清理,等价于 pytest fixture 的 setup/teardown。多个用例共享昂贵资源时,把"with TestClient(app)"放进 session 级 fixture,资源只建一次;单测要隔离状态就把 lifespan 里的资源做成可注入。断言清理逻辑(池是否关闭)可直接检查 lifespan 闭包维护的状态对象。

```python
# file: code/03_Web后端开发/q746_lifespan_fixture.py
from contextlib import asynccontextmanager
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    state["pool"] = "connection-pool"
    yield
    state.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/pool")
def pool():
    return {"pool": state.get("pool")}

with TestClient(app) as client:   # with 才触发 lifespan
    print(client.get("/pool").json())
print("退出后资源已清理:", state)
```

**追问**:
- 不用 with 直接 TestClient(app).get 会怎样?——lifespan 不执行,依赖池的接口直接 500,这是新手测试常见的坑。
- 测试里怎么模拟启动失败?——lifespan 里抛异常,断言 TestClient 进入时抛出,验证 fail-fast 行为。
