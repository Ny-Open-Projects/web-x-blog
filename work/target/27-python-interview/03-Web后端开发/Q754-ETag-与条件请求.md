---
title: [Q754] ETag 与条件请求
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q754 · ETag 与条件请求

> 难度:★★★☆ | 标签:FastAPI, HTTP 缓存

**问**:接口响应内容不常变,怎么利用 HTTP 缓存省带宽?ETag 的协商流程是什么?

**答**:服务端对响应内容算指纹作为 `ETag` 返回;客户端下次带 `If-None-Match`,内容没变就返回 **304 空体**,省掉响应体传输。配合 `Cache-Control` 控制是否走本地缓存,强缓存与协商缓存组合使用。ETag 计算要便宜(内容哈希或版本号),对高频大响应要权衡计算成本;数据可变性强的接口别乱加,缓存错误比慢更伤。

```python
# file: code/03_Web后端开发/q754_etag.py
import hashlib
try:
    from fastapi import FastAPI, Request, Response
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/report")
def report(request: Request):
    payload = b"report-version-7"
    etag = '"' + hashlib.md5(payload).hexdigest() + '"'
    if request.headers.get("if-none-match") == etag:
        return Response(status_code=304, headers={"ETag": etag})
    return Response(content=payload, media_type="text/plain", headers={"ETag": etag})

client = TestClient(app)
r1 = client.get("/report")
print(r1.status_code, r1.headers["etag"])
r2 = client.get("/report", headers={"If-None-Match": r1.headers["etag"]})
print(r2.status_code, len(r2.content))
```

**追问**:
- ETag 和 Last-Modified 选哪个?——ETag 更精确但要算;Last-Modified 秒级精度且免费,静态资源两者都给。
- 304 响应还带其他头吗?——应带 ETag 与缓存指令等元信息头,不带响应体。
