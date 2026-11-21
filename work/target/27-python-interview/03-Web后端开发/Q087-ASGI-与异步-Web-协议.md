---
title: [Q087] ASGI 与异步 Web 协议
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q087 · ASGI 与异步 Web 协议

> 难度:★★☆ | 标签:ASGI, asyncio

**问**:ASGI 解决了 WSGI 的什么问题?它的接口签名是怎样的?

**答**:ASGI 是 WSGI 的异步扩展(规范由 uvicorn/django 团队维护),把应用变成一个接收 `scope`、`receive`、`send` 三个参数的协程:`scope` 是连接级元数据,`receive` 异步接收事件(如 http.request、websocket.connect),`send` 异步发送数据。它原生支持 WebSocket、HTTP/2、Server-Sent Events 和后台长任务,单个事件循环可托管成千上万并发连接。

```python
# file: code/03_Web后端开发/q087_asgi_app.py
async def app(scope, receive, send):
    if scope['type'] == 'http':
        await receive()  # 读取 request 事件,真实场景可分段读取 body
        await send({'type': 'http.response.start',
                    'status': 200,
                    'headers': [(b'content-type', b'text/plain')]})
        await send({'type': 'http.response.body', 'body': b'hello asgi'})

if __name__ == '__main__':
    try:
        import uvicorn
    except ImportError:
        print("该题演示需要第三方库 uvicorn:pip install uvicorn,原理见正文")
        raise SystemExit(0)
    uvicorn.run(app, host='127.0.0.1', port=8000)
```

**追问**:
- ASGI 能兼容 WSGI 应用吗?——可以通过 asgiref 提供的 `WSGIToASGI` 适配器包装,但不能享受异步收益。
- ASGI 的 receive/send 事件模型长什么样?——receive 收 http.request/websocket.connect 等事件字典,send 发 http.response.body 等事件;协议就是事件循环上的消息协议。
- 一个事件循环能扛多少连接?——取决于内存与文件描述符上限,数万长连接可行;瓶颈从线程数变成每个连接的状态大小。
- ASGI 里怎么跑后台任务?——lifespan 内启动 asyncio 任务或独立 worker;直接在请求协程里开火不再管会泄漏。
