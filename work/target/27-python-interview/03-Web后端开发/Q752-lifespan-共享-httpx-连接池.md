---
title: [Q752] lifespan 共享 httpx 连接池
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q752 · lifespan 共享 httpx 连接池

> 难度:★★★★ | 标签:FastAPI, httpx, 性能

**问**:每个请求新建 httpx 客户端调外部 API,有什么问题?正确的姿势是什么?

**答**:每请求新建 AsyncClient 会丢失**连接复用、DNS 缓存、TLS 会话复用**,高并发下 TIME_WAIT 堆积、延迟放大。正确做法:在 lifespan 里创建**一个共享的 AsyncClient**(配 timeout 与 Limits 连接池上限)挂到 `app.state`,所有请求复用,关闭时统一 aclose。连接池上限要协调:应用池 ≤ 下游可承受并发,否则会把下游打挂。超时要分层配置 connect/read/write/pool。

```mermaid
graph LR
    A[lifespan 启动] --> B[创建 AsyncClient 与连接池]
    B --> C[挂到 app.state]
    C --> D[所有请求复用连接]
    D --> E[关闭时 aclose 释放]
```

```python
# file: code/03_Web后端开发/q752_httpx_pool.py
from contextlib import asynccontextmanager
try:
    import httpx
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient(
        timeout=2.0, limits=httpx.Limits(max_connections=50)
    ) as client:
        app.state.http = client
        yield

app = FastAPI(lifespan=lifespan)

@app.get("/probe")
async def probe(request: Request):
    return {"has_client": hasattr(request.app.state, "http")}

with TestClient(app) as c:
    print(c.get("/probe").json())
```

**追问**:
- Limits 里 max_keepalive_connections 管什么?——空闲保持的连接数,调太小会频繁握手,太大占用下游连接。
- 单例客户端线程安全吗?——AsyncClient 设计为多协程共享,跨 worker 进程不共享,每个进程各有自己的池。
