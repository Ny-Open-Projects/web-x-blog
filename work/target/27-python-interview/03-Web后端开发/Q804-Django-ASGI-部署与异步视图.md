---
title: [Q804] Django ASGI 部署与异步视图
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q804 · Django ASGI 部署与异步视图

> 难度:★★★☆ | 标签:Django, ASGI

**问**:Django 跑在 ASGI 下和 WSGI 有什么区别?异步视图怎么写、什么场景值得?

**答**:ASGI 模式(asgi.py + uvicorn/daphne)支持 async 视图、Channels 的 WebSocket、长轮询;WSGI 只能同步。异步视图 `async def view(request)`,收益只在**视图内有真正异步 IO**(asyncpg、httpx 异步)时兑现;同步 ORM 调用塞进 async 视图反而要线程池转发。整个技术栈要一致:要么全异步(异步 ORM + 异步客户端),要么老实同步,混用是性能陷阱。

```python
# file: code/03_Web后端开发/q804_asgi_django.py
import asyncio
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    INSTALLED_APPS=[],
    ROOT_URLCONF="__main__",
    USE_TZ=True,
)
django.setup()

from django.http import HttpResponse

async def hello(request):
    return HttpResponse("async ok")

from django.urls import path

urlpatterns = [path("async-hello", hello)]

from django.core.asgi import get_asgi_application

application = get_asgi_application()   # 真实部署交给 uvicorn/daphne

async def call_once():
    async def receive():
        return {"type": "http.request", "body": b""}

    sent: list = []

    async def send(msg):
        sent.append(msg)

    scope = {
        "type": "http", "method": "GET", "path": "/async-hello",
        "headers": [], "query_string": b"",
    }
    await application(scope, receive, send)
    return sent

sent = asyncio.run(call_once())
print("ASGI 响应状态:", sent[0]["status"])
```

**追问**:
- 同步中间件在 ASGI 下还能用吗?——Django 会做适配,但同步中间件会把异步请求线程化,链路尽量统一。
- Channels 的定位?——在 ASGI 上加 channel layer 的 WebSocket/后台消费框架,现在推荐原生 AsyncConsumer 或 Starlette 方案按需选。
