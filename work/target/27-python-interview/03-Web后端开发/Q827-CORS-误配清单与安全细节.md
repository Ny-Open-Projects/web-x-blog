---
title: [Q827] CORS 误配清单与安全细节
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q827 · CORS 误配清单与安全细节

> 难度:★★★☆ | 标签:CORS, 安全

**问**:`allow_origins=["*"]` 配 credentials=true 会怎样?CORS 还有哪些高频误配?

**答**:规范禁止 `Access-Control-Allow-Origin: *` 与 `Allow-Credentials: true` 共存——等于向任意网站开放带 Cookie 的读写权限,是最危险的误配。正确做法:**Origin 白名单逐个匹配**并回显具体 Origin,凭证场景必须加 `Vary: Origin` 防止代理缓存串头。其他高频坑:预检 OPTIONS 被业务鉴权拦截(要放行)、通配子域正则过宽(https://*.example.com 匹配了 evil-example.com)、把 CORS 当鉴权用(CORS 只是浏览器约束,防不了 curl)。

```python
# file: code/03_Web后端开发/q827_cors_detail.py

def cors_headers(origin: str, allowlist: set, with_credentials: bool) -> dict:
    if origin in allowlist:
        h = {"Access-Control-Allow-Origin": origin}
        if with_credentials:
            h["Access-Control-Allow-Credentials"] = "true"
            h["Vary"] = "Origin"
        return h
    return {}   # 不命中白名单就不放行

print(cors_headers("https://app.example.com", {"https://app.example.com"}, True))
print(cors_headers("https://evil.example.net", {"https://app.example.com"}, True))
```

**追问**:
- CORS 防不住服务端到服务端的调用?——对,CORS 是浏览器执行的策略,服务器间调用与 curl 完全不受限,鉴权必须独立存在。
- 预检请求怎么处理才对?——中间件层直接应答 OPTIONS(带 Allow-Methods/Headers),不进入业务路由与认证。
