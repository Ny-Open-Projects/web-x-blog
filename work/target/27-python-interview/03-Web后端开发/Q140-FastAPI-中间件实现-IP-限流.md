---
title: [Q140] FastAPI 中间件实现 IP 限流
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q140 · FastAPI 中间件实现 IP 限流

> 难度:★★☆ | 标签:FastAPI, 限流

**问**:如何在 FastAPI 里实现一个简单的按 IP 限流中间件?分布式部署怎么改?

**答**:在中间件里取 `request.client.host` 作为键,配合 Q139 的计数器判断,超限直接返回 429 JSON 响应(不进入路由)。单机内存计数即可;多实例部署必须把计数器外移到 Redis(用 INCR + EXPIRE 的原子脚本),并注意经过 Nginx 后真实 IP 要从 `X-Forwarded-For` 解析,同时只信任可信代理头防伪造。

```python
# file: code/03_Web后端开发/q140_fastapi_ratelimit.py
import time
from collections import defaultdict, deque
try:
    from fastapi import FastAPI, Request, Response
    from fastapi.responses import JSONResponse
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
WINDOW = 10       # 秒
LIMIT = 5         # 每窗口最多 5 次
hits: dict[str, deque] = defaultdict(deque)

@app.middleware('http')
async def rate_limit(request: Request, call_next):
    # 生产: 真实 IP 从 X-Forwarded-For 解析且只信任可信代理
    ip = request.client.host if request.client else 'unknown'
    now = time.monotonic()
    q = hits[ip]
    while q and q[0] <= now - WINDOW:
        q.popleft()
    if len(q) >= LIMIT:
        return JSONResponse(status_code=429,
                            content={'detail': 'too many requests'})
    q.append(now)
    return await call_next(request)

@app.get('/ping')
def ping():
    return {'msg': 'pong'}
```

**追问**:
- 多实例部署限流计数放哪?——Redis INCR+EXPIRE 原子脚本,键含接口与窗口;进程内计数每实例各一份,总量失控。
- 从 X-Forwarded-For 取 IP 为什么有伪造风险?——该头可被客户端伪造追加,只能取「可信代理写入的最后一跳」;Uvicorn 用 --forwarded-allow-ip 白名单。
- 限流被触发后返回什么?——429 + Retry-After + 简洁 JSON;别让限流响应本身又很重。
