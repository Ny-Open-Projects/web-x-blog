---
title: [Q6057] WSGI 到 ASGI 的迁移演进
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6057 · WSGI 到 ASGI 的迁移演进

> 难度:★★★★ | 标签:WSGI, ASGI, lifespan, 异步, 版本演进

**问**：老 Flask 服务要加 WebSocket 和长轮询，团队在讨论"直接上 FastAPI"还是"Flask 包一层"。WSGI 和 ASGI 的本质差异是什么？同一个应用的最小两种实现长什么样？迁移的真实成本在哪？

**答**：本质差异是**调用模型**：WSGI 是一次同步函数调用——`app(environ, start_response)`，一请求一线程，框架读 body 是阻塞 IO，没有"请求结束后还能干活"的钩子（lifespan 是各家私有约定）；ASGI 是消息驱动的异步协议——`app(scope, receive, send)`，scope 描述连接类型（http/websocket/lifespan），body 和响应都是异步消息流，连接生命周期由协议事件表达，WebSocket/SSE/SSE 推送因此是"一等公民"。迁移成本不在改写路由（那是最简单的部分），在四处：a) **同步依赖桥**——同步 ORM/SDK 混进 async 路由会阻塞事件循环（Q6006 的线程池耗尽正是这个病的并发症），要么换异步版库，要么 run_in_executor + 池上限；b) **中间件语义**——WSGI 中间件是"调用包裹"，ASGI 是消息级包裹，所有自研中间件重写；c) **部署矩阵**——gunicorn+gevent → uvicorn/hypercorn + worker 配比重构；d) **全局假设**——线程本地存储、每请求单线程假设（threading.local 直接失效，见 Q5551）。务实路线：新服务直接 ASGI；老 Flask 服务若只是加推送，先在旁路起一个小 ASGI 服务（WebSocket 专用）共域共存，比"原地改写"风险小一个量级；Django 同理用 ASGI 入口渐进（ASGI handler + sync_to_async 桥）。

```python
# file: code/03_Web后端开发/q6057_wsgi_asgi.py
import threading, asyncio

# 1) WSGI 最小实现: 同步函数, 一请求一线程
from wsgiref.simple_server import make_server, WSGIRequestHandler
def wsgi_app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"wsgi-ok"]
class Quiet(WSGIRequestHandler):
    def log_message(self, *a): pass
srv = make_server("127.0.0.1", 0, wsgi_app, handler_class=Quiet)
port = srv.server_port
threading.Thread(target=srv.serve_forever, daemon=True).start()
import urllib.request
print("WSGI 同步调用:", urllib.request.urlopen(f"http://127.0.0.1:{port}").read())
srv.shutdown()

# 2) ASGI 最小实现: scope+receive+send 消息协议
async def asgi_app(scope, receive, send):
    body = b""
    while True:
        msg = await receive()                  # 请求体按消息流到达
        if msg["type"] == "http.request":
            body += msg.get("body", b"")
            if not msg.get("more_body"):
                break
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"text/plain")]})
    await send({"type": "http.response.body", "body": b"asgi-" + body})

async def main():
    async def receive():
        return {"type": "http.request", "body": b"ok", "more_body": False}
    sent = []
    async def send(msg): sent.append(msg)
    await asgi_app({"type": "http", "method": "GET"}, receive, send)
    print("ASGI 消息协议:", sent[-1]["body"])

asyncio.run(main())
print("演进: WSGI 一请求一线程/无 lifespan -> ASGI 消息驱动/http|websocket|lifespan 三类 scope")
```

**追问**：1) ASGI 的 lifespan 消息解决了什么？——启动/关闭事件成为协议一部分（startup/shutdown 消息），连接池预热、后台任务托管有标准位置，不再依赖框架私有的 `@app.on_event`；迁移时把启动逻辑搬到 lifespan 是必做项。2) WSGI 应用挂在 ASGI 服务器下跑（ASGI-to-WSGI 桥）可行吗？——可行（a2wgi/uvicorn 支持 WSGI middleware），线程池代理同步调用，作为过渡形态；但两套并发模型叠着，超时/取消语义会打折，长期要收敛。3) 为什么"async def 路由 + 同步 ORM"比纯同步更危险？——事件循环被阻塞时**所有**并发请求一起卡（sync 模式只是占一个 worker 线程），且线程池（anyio 默认 40）耗尽会引发不可预期的 503——异步框架对阻塞调用的纪律要求更高。

## 背诵要点
- WSGI=同步函数 `app(environ, start_response)` 一请求一线程无 lifespan；ASGI=`app(scope, receive, send)` 消息驱动，http/websocket/lifespan 三类 scope。
- 迁移真实成本：同步依赖桥（阻塞事件循环）、自研中间件重写、部署矩阵换 uvicorn、threading.local 失效。
- 务实路线：新服务直接 ASGI；老服务旁路起小 ASGI 处理推送类，共域共存过渡，比原地改写风险小。

## 复盘追问
- 你们的 ASGI 服务里有多少 async 路由在调用同步库？怎么系统性审计？（提示：py-spy 采 loop 线程看长帧；静态扫 async 函数内无 await 的同步 IO 调用）
- 老 Flask 服务加 WebSocket 的方案评审结论是什么？为什么选/不选原地改写？（提示：列出四项迁移成本清单打分；共存方案的中立性——跨域/鉴权对齐是它的新成本）
