---
title: [Q106] FastAPI 中间件的编写与用途
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q106 · FastAPI 中间件的编写与用途

> 难度:★★☆ | 标签:FastAPI, 中间件

**问**:如何给 FastAPI 写自定义中间件?典型用途有哪些?

**答**:中间件通过 `@app.middleware('http')` 或 `app.add_middleware(SomeMiddleware)` 注册,包裹整个请求处理过程,典型用途:请求日志与耗时统计、统一响应头(如 Request-ID)、全局限流、异常兜底转 JSON。`@app.middleware('http')` 是函数式写法,`add_middleware` 是类式写法(支持构造参数),多个中间件按注册顺序反向包裹,构成洋葱模型。

```python
# file: code/03_Web后端开发/q106_middleware.py
import time
import uuid
try:
    from fastapi import FastAPI, Request
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.middleware('http')
async def add_request_id(request: Request, call_next):
    rid = request.headers.get('x-request-id', str(uuid.uuid4())[:8])
    start = time.perf_counter()
    response = await call_next(request)          # 交给内层处理
    cost = round((time.perf_counter() - start) * 1000, 2)
    response.headers['x-request-id'] = rid
    response.headers['x-cost-ms'] = str(cost)
    return response

@app.middleware('http')
async def log_requests(request: Request, call_next):
    print(f'-> {request.method} {request.url.path}')
    response = await call_next(request)
    print(f'<- {request.url.path} done')
    return response

@app.get('/')
def root():
    return {'msg': 'hello'}
```

**追问**:
- BaseHTTPMiddleware 的性能坑?——它为每个请求包一层任务与内存流,大并发下开销明显;纯 ASGI 函数式中间件更快。
- 中间件里能修改请求体吗?——能但要小心:读过的 body 要重新塞回 receive 通道,否则路由拿不到;常见于签名校验中间件。
- Request-ID 应该在哪一层生成?——最外层中间件生成并塞入日志上下文(contextvars)与响应头,下游服务透传,全链路可检索。
