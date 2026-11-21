---
title: [Q729] 纯 ASGI 中间件与 BaseHTTPMiddleware
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q729 · 纯 ASGI 中间件与 BaseHTTPMiddleware

> 难度:★★★★ | 标签:FastAPI, 中间件, ASGI

**问**:自定义中间件该继承 BaseHTTPMiddleware 还是写纯 ASGI 类?各自代价是什么?

**答**:BaseHTTPMiddleware 写起来像 async 函数(`dispatch(request, call_next)`),直观但有历史包袱:它把下游包成独立 task,曾带来 contextvars 不下传、后台任务异常难传播、性能开销等问题(新版本已大幅缓解)。纯 ASGI 中间件直接操作 `scope/receive/send`,零包装、行为最透明,适合计时、改响应头、限流这类横切逻辑。原则:**能用纯 ASGI 就用纯 ASGI**,需要读改请求体或复杂分支才考虑 BaseHTTPMiddleware。

```python
# file: code/03_Web后端开发/q729_asgi_mw.py
import time
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        start = time.perf_counter()

        async def send_wrapped(message):
            if message["type"] == "http.response.start":
                ms = int((time.perf_counter() - start) * 1000)
                headers = list(message.get("headers", []))
                headers.append((b"x-process-ms", str(ms).encode()))
                message = {**message, "headers": headers}
            await send(message)

        await self.app(scope, receive, send_wrapped)

app = FastAPI()

@app.get("/hi")
def hi():
    return {"hi": True}

app.add_middleware(TimingMiddleware)

client = TestClient(app)
r = client.get("/hi")
print(r.json(), r.headers.get("x-process-ms") is not None)
```

**追问**:
- BaseHTTPMiddleware 的 contextvars 问题是什么?——下游在独立 task 里跑,任务内 set 的 contextvar 不回传到外层,日志过滤器可能拿不到请求级变量。
- 纯 ASGI 中间件怎么传配置?——`add_middleware(Cls, key=value)`,构造函数以关键字参数接收。
