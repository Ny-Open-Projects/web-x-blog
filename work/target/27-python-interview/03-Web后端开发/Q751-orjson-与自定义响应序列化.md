---
title: [Q751] orjson 与自定义响应序列化
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q751 · orjson 与自定义响应序列化

> 难度:★★★☆ | 标签:FastAPI, 性能, orjson

**问**:接口序列化开销大,换 orjson 能带来多少收益?怎么全局启用?

**答**:orjson 用 Rust 实现,序列化速度通常是标准 json 的数倍且直接输出 bytes。启用方式:`pip install orjson` 后把 `default_response_class=ORJSONResponse` 设到 FastAPI 实例(全局)或单路由。注意三点:orjson 原生支持 datetime/UUID/dataclass,不需要 default 钩子兜底;收益只在**大响应体、高 QPS**场景明显,先用 profile 确认序列化真是瓶颈;混合场景可用 default_response_class 配合个别路由的 JSONResponse 微调。

```python
# file: code/03_Web后端开发/q751_orjson.py
try:
    from fastapi import FastAPI
    from fastapi.responses import ORJSONResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install orjson fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI(default_response_class=ORJSONResponse)

@app.get("/big")
def big():
    return {"items": [{"id": i, "name": f"item-{i}"} for i in range(1000)]}

client = TestClient(app)
r = client.get("/big")
print(r.status_code, len(r.content))
```

**追问**:
- orjson 输出和标准库有差异吗?——是 bytes 不是 str、默认紧凑无空格、浮点格式化更精确,逐字节 diff 的用例要注意。
- 响应里要自定义类型怎么办?——用 ORJSONResponse 的 default 参数或在模型里转好基础类型,不要塞自定义对象到响应里。
