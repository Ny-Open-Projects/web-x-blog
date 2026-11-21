---
title: [Q730] add_middleware 的注册顺序与洋葱方向
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q730 · add_middleware 的注册顺序与洋葱方向

> 难度:★★★☆ | 标签:FastAPI, 中间件

**问**:连续 add_middleware 三次,请求先经过哪个?想让日志中间件统计所有其他中间件的耗时,应该怎么排?

**答**:`add_middleware` 是**压栈**:后注册的包在最外层,请求先经过后注册者。所以"最外层"中间件要**最后**注册——日志/计时想覆盖全部耗时,它的 add 调用必须放在其他中间件之后。`@app.middleware("http")` 装饰器本质也是 add_middleware,按代码执行到那一行的顺序压栈。官方 CORS 中间件建议放到能覆盖所有响应的位置,正是这个规则的体现。

```python
# file: code/03_Web后端开发/q730_mw_order.py
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

trace = []
app = FastAPI()

class MarkA:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        trace.append("A-in")
        await self.app(scope, receive, send)
        trace.append("A-out")

class MarkB:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        trace.append("B-in")
        await self.app(scope, receive, send)
        trace.append("B-out")

app.add_middleware(MarkA)  # 先注册
app.add_middleware(MarkB)  # 后注册者在最外层

@app.get("/t")
def t():
    return {"ok": True}

client = TestClient(app)
client.get("/t")
print(trace)
```

**追问**:
- 输出顺序是什么?——B-in、A-in、A-out、B-out:B 最外层,A 的收尾代码先于 B 执行。
- 中间件顺序错了会有什么后果?——典型是把 GZip 放在计费/签名中间件内侧,导致统计的是压缩前体量或签名验到压缩后的数据。
