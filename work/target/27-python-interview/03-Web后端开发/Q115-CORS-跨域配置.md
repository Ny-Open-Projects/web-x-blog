---
title: [Q115] CORS 跨域配置
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q115 · CORS 跨域配置

> 难度:★★☆ | 标签:CORS, 安全

**问**:什么是 CORS?浏览器跨域请求为什么会失败?FastAPI 如何配置?

**答**:CORS 是浏览器的同源策略放行机制:跨域请求先发 OPTIONS 预检,服务端必须返回 `Access-Control-Allow-Origin` 等响应头,浏览器才放行实际请求;服务端到服务端调用不存在 CORS。FastAPI 用 `CORSMiddleware` 配置:`allow_origins` 必须写明确域名列表,不要用 `["*"]` 同时 `allow_credentials=True`——带 cookie 的请求该组合无效且不安全。

```python
# file: code/03_Web后端开发/q115_cors.py
try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://app.example.com'],  # 明确列出前端域名
    allow_credentials=True,                      # 允许携带 cookie
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Authorization', 'Content-Type'],
)

@app.get('/data')
def data():
    return {'ok': True}
```

**追问**:
- allow_origins=['*'] 加 credentials=True 会怎样?——规范禁止,浏览器拒绝带 cookie 的跨域响应;按域名白名单配置才是正解。
- 预检 OPTIONS 请求要过鉴权吗?——不要,预检本身无凭证;鉴权逻辑要放行 OPTIONS,否则跨域请求全卡在预检。
- 服务端到服务端需要 CORS 吗?——不需要,CORS 是浏览器同源策略的放行机制;curl/服务间调用不受它约束。
