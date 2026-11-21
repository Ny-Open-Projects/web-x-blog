---
title: [Q748] 自定义 APIRoute 注入通用逻辑
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q748 · 自定义 APIRoute 注入通用逻辑

> 难度:★★★★ | 标签:FastAPI, 路由, 源码

**问**:想给一组路由统一加签名校验、审计这类逻辑,除了中间件和依赖还有什么手段?

**答**:继承 `APIRoute` 重写 `get_route_handler`,在原始 handler 外包一层自定义处理,再通过 `APIRouter(route_class=SignedRoute)` 整组生效。它比中间件**更靠内**(能拿到路由参数、路径操作上下文),比依赖**更统一**(不用每个路由声明)。适合签名校验、请求重放保护、路由级审计。注意该方法返回的是 async 处理函数,异常要自己转响应。

```python
# file: code/03_Web后端开发/q748_custom_route.py
try:
    from fastapi import APIRouter, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

class SignedRoute(APIRoute):
    def get_route_handler(self):
        original = super().get_route_handler()

        async def custom_handler(request: Request) -> Response:
            if request.headers.get("x-signature") != "secret":
                return Response("bad signature", status_code=401)
            return await original(request)

        return custom_handler

app = FastAPI()
router = APIRouter(route_class=SignedRoute)

@router.get("/data")
def data():
    return {"ok": True}

app.include_router(router)

client = TestClient(app)
print(client.get("/data").status_code)
print(client.get("/data", headers={"x-signature": "secret"}).json())
```

**追问**:
- get_route_handler 什么时候被调用?——注册路由时调用一次并缓存 handler,不是每请求执行,包装逻辑零运行时开销。
- 它和依赖的执行顺序?——先走依赖解析,再进入 handler 包装层,所以签名校验发生在依赖之后,要前置校验就用依赖或中间件。
