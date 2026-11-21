---
title: [Q719] mount 子应用与 include_router 的边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q719 · mount 子应用与 include_router 的边界

> 难度:★★★☆ | 标签:FastAPI, Starlette

**问**:include_router 和 mount 挂子应用有什么本质区别?什么时候必须用 mount?

**答**:`include_router` 是把路由**复制进主应用**,共享主应用的中间件、依赖、异常处理器和 OpenAPI 文档。`mount` 是挂一个**独立 ASGI 应用**:子应用有自己的生命周期、中间件栈、`/docs`,主应用按前缀转发,OpenAPI 默认**不合并**。需要独立技术栈(另一个 FastAPI 服务、静态目录、不同框架)、独立中间件或独立文档时用 mount;只是组织代码用 include_router。

```python
# file: code/03_Web后端开发/q719_mount_subapp.py
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

inner = FastAPI(title="inner")

@inner.get("/health")
def inner_health():
    return {"app": "inner"}

outer = FastAPI(title="outer")

@outer.get("/health")
def outer_health():
    return {"app": "outer"}

outer.mount("/sub", inner)

client = TestClient(outer)
print(client.get("/health").json())      # 命中 outer 自己的路由
print(client.get("/sub/health").json())  # 前缀转发给子应用
```

**追问**:
- 子应用的 Swagger 能出现在主应用文档里吗?——默认不能,需要手动聚合 OpenAPI 或在文档页里分别链接两个 docs。
- mount 之后子应用里的路径参数怎么解析?——前缀在 mount 层剥掉,子应用看到的是剥完前缀的 path,两边互不感知。
