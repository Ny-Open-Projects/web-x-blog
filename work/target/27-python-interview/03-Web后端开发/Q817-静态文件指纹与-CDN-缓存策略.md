---
title: [Q817] 静态文件指纹与 CDN 缓存策略
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q817 · 静态文件指纹与 CDN 缓存策略

> 难度:★★★☆ | 标签:CDN, 缓存

**问**:前端发新版本,用户还在用旧 JS 文件怎么办?静态资源的缓存头怎么配?

**答**:标准方案:**内容指纹文件名 + 永久强缓存**。构建产物带 hash(app.a1b2c3.js),`Cache-Control: public, max-age=31536000, immutable`——内容变了文件名就变,永远不存在新旧混淆;入口 HTML 用 `no-cache` 走协商缓存,保证引用到最新指纹。发布顺序:**先发静态资源(新指纹文件),再发引用它的 HTML**,反向顺序会让新 HTML 引用不存在的资源。注意 Cookie 不要带给静态域名,省流量也降安全面。

```python
# file: code/03_Web后端开发/q817_static_cache.py
import hashlib

def fingerprint(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()[:8]

def asset_url(name: str, content: bytes) -> str:
    return f"/static/{name}.{fingerprint(content)}.css"

def cache_headers(is_fingerprinted: bool) -> dict:
    if is_fingerprinted:
        return {"Cache-Control": "public, max-age=31536000, immutable"}
    return {"Cache-Control": "no-cache"}   # 入口 HTML 走协商缓存

print(asset_url("app", b"body{color:red}"))
print(cache_headers(True), cache_headers(False))
```

**追问**:
- immutable 是什么作用?——告诉浏览器该资源永不变化,连协商请求(304 往返)都省掉,除非文件名变化。
- CDN 缓存了错误版本怎么救?——源站修复后主动刷新 CDN(purge),并检查指纹机制是否失效——指纹正确时根本不该出现该问题。
