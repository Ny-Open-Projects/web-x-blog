---
title: [Q716] Annotated 依赖与请求级上下文对象
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q716 · Annotated 依赖与请求级上下文对象

> 难度:★★★☆ | 标签:FastAPI, 依赖注入, Annotated

**问**:团队统一用 Annotated 写依赖有什么好处?多个依赖之间怎么共享数据?

**答**:`Annotated[类型, Depends(fn)]` 把类型和依赖绑定成**可复用的类型别名**,handler 签名只剩类型,干净且对 mypy 友好,这是 FastAPI 官方现在推荐的风格。依赖之间共享数据的标准做法是定义一个**请求级上下文对象依赖**:第一个依赖创建并挂到 `request.state`,其余依赖和 handler 引用同一个对象读写。中间件、异常处理器也能通过 `request.state` 读到同一份上下文。

```python
# file: code/03_Web后端开发/q716_annotated_ctx.py
try:
    from typing import Annotated
    from fastapi import Depends, FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("需要 Python 3.9+ 并 pip install fastapi httpx")
    raise SystemExit(0)

app = FastAPI()

class RequestCtx(dict):
    pass

def get_ctx(request: Request) -> RequestCtx:
    ctx = RequestCtx(path=request.url.path)
    request.state.ctx = ctx
    return ctx

Ctx = Annotated[RequestCtx, Depends(get_ctx)]

def add_user(ctx: Ctx) -> str:
    ctx["user"] = "alice"
    return ctx["user"]

@app.get("/me")
def me(ctx: Ctx, user: Annotated[str, Depends(add_user)]) -> dict:
    return {"path": ctx["path"], "user": user}

client = TestClient(app)
print(client.get("/me").json())
```

**追问**:
- Annotated 写法和默认值写法能混用吗?——语法上可以,但同一参数别混,团队统一选 Annotated。
- request.state 是什么?——Starlette 每请求的命名空间对象,默认为空,适合在中间件、依赖、异常处理器之间挂数据。
