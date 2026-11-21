---
title: [Q744] httpx AsyncClient 与 ASGITransport 异步测试
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q744 · httpx AsyncClient 与 ASGITransport 异步测试

> 难度:★★★☆ | 标签:FastAPI, 测试, httpx

**问**:测试异步接口,httpx 的 ASGITransport 怎么用?它和 TestClient 的本质区别是什么?

**答**:`httpx.AsyncClient(transport=httpx.ASGITransport(app=app))` 在**进程内直接调用 ASGI 应用**,不经过网络,能测真正的 async 代码路径且运行在当前事件循环里。TestClient 是同步包装(内部起 portal 跑事件循环),用起来简单但测不到 async 特有的行为(如取消传播)。注意 ASGITransport **不会自动执行 lifespan**,需要 lifespan 的测试用 asgi-lifespan 的 LifespanManager。异步测试通常配 pytest-asyncio 的 `@pytest.mark.asyncio`。

```python
# file: code/03_Web后端开发/q744_async_test.py
import asyncio
try:
    import httpx
    from fastapi import FastAPI
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/async-hi")
async def hi():
    return {"hi": True}

async def main():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        r = await c.get("/async-hi")
        print(r.status_code, r.json())

asyncio.run(main())
```

**追问**:
- ASGITransport 会启动端口吗?——不会,请求直接在进程内交给应用,没有 TCP 开销,适合高频单元测试。
- 想测 lifespan 该怎么做?——用 asgi-lifespan 的 LifespanManager 包住 app,或继续用 TestClient 的 with 语法。
