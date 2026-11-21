---
title: [Q714] use_cache 与依赖的请求级缓存边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q714 · use_cache 与依赖的请求级缓存边界

> 难度:★★★★ | 标签:FastAPI, 依赖注入

**问**:依赖注入的缓存是什么粒度?`use_cache=False` 什么场景必须用?

**答**:依赖缓存粒度是**单次请求**:同一依赖在同一请求内只调用一次,多个引用共享同一返回对象;跨请求之间**绝不复用**,所以依赖不能当全局缓存用。需要每请求新实例的场景必须 `use_cache=False`,典型是数据库会话:两个依赖各自要独立事务时,共享同一个 session 会互相污染。缓存键是依赖可调用对象本身,所以参数化的工厂产物(闭包)每个都是独立键。

```python
# file: code/03_Web后端开发/q714_dep_cache.py
try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
ids = []

def shared_token():
    ids.append("shared")
    return object()

def per_call_token():
    ids.append("fresh")
    return object()

def cached(a=Depends(shared_token), b=Depends(shared_token)):
    return a is b

def uncached(x=Depends(per_call_token), y=Depends(per_call_token, use_cache=False)):
    return x is not y

@app.get("/cached")
def cached_ep(v: bool = Depends(cached)):
    return {"same_instance": v}

@app.get("/uncached")
def uncached_ep(v: bool = Depends(uncached)):
    return {"different_instance": v}

client = TestClient(app)
print(client.get("/cached").json())
print(client.get("/uncached").json())
print("依赖调用次数:", ids)
```

**追问**:
- 想做"请求内共享上下文"怎么办?——定义一个返回字典/数据类对象的依赖,其他依赖和 handler 都引用它,往里写即可。
- use_cache 对类依赖生效吗?——生效,同一个类对象在请求内只会实例化一次,除非显式关掉。
