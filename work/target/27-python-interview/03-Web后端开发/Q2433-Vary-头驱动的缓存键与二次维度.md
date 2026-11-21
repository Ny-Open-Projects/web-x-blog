---
title: [Q2433] Vary 头驱动的缓存键与二次维度
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2433 · Vary 头驱动的缓存键与二次维度

> 难度:★★★☆ | 标签:HTTP, 缓存, Vary

**问**:Vary 头在缓存里起什么作用?漏写或写错会出什么事故?

**答**:Vary 声明"这份表示会随哪些请求头变化",缓存据此把缓存键从 URL 扩展成"URL + Vary 列出的头值"——同一个 URL 可以同时存 gzip 与 identity 两个变体,互不覆盖。漏写的代价是缓存串味:接口对桌面与移动端返回不同内容却没写 Vary: User-Agent,CDN 会把移动端副本发给桌面用户;Accept-Encoding 忘写则可能把压缩体发给不解压的客户端。写错也一样致命:Vary: * 表示表示随任意因素变化,等价于每次都不命中,命中率直接归零。工程实践是让框架按响应内容自动推导 Vary(内容协商自动加 Accept,压缩中间件自动加 Accept-Encoding),并定期审计"同一 URL 多副本"的膨胀问题。

```python
# file: code/03_Web后端开发/q2433_vary_cache_key.py
"""Vary 头驱动的缓存键: 同一 URL 的多表示共存(纯标准库)。"""


def cache_key(url, request_headers, vary):
    """缓存键 = URL + 按 Vary 列出的请求头值; Vary 为空则仅 URL。"""
    lowered = {k.lower(): v for k, v in request_headers.items()}
    parts = [url]
    for name in sorted(h.lower() for h in (vary or [])):
        parts.append("{}={}".format(name, lowered.get(name, "")))
    return "|".join(parts)


class VaryCache:
    def __init__(self):
        self.store = {}

    def put(self, url, vary, req_headers, body):
        self.store[cache_key(url, req_headers, vary)] = body

    def get(self, url, vary, req_headers):
        return self.store.get(cache_key(url, req_headers, vary))


cache = VaryCache()

# 场景一: 同一 URL 因 Accept-Encoding 不同存两份表示
vary = ["Accept-Encoding"]
cache.put("/api/report", vary, {"Accept-Encoding": "gzip"}, b"\x1f\x8b-gz-body")
cache.put("/api/report", vary, {"Accept-Encoding": "identity"}, b"plain-body")
assert cache.get("/api/report", vary, {"Accept-Encoding": "gzip"}) == b"\x1f\x8b-gz-body"
assert cache.get("/api/report", vary, {"Accept-Encoding": "identity"}) == b"plain-body"
assert cache.get("/api/report", vary, {"Accept-Encoding": "br"}) is None   # 未缓存过的变体
print("场景一: Vary: Accept-Encoding 时 gzip 与 identity 是两个键, 互不覆盖")

# 场景二: 忘写 Vary 导致 UA 差异被吞掉
cache.put("/page", None, {"User-Agent": "Mobile"}, b"mobile-html")
hit = cache.get("/page", None, {"User-Agent": "Desktop"})
assert hit == b"mobile-html"
print("场景二: 无 Vary 时桌面请求命中了移动端副本, 这就是缓存串味的根源")

# 场景三: Vary 列举的顺序不影响键
cache.put("/p2", ["Accept", "Accept-Language"], {"Accept": "a", "Accept-Language": "zh"}, b"x")
hit2 = cache.get("/p2", ["Accept-Language", "Accept"], {"Accept": "a", "Accept-Language": "zh"})
assert hit2 == b"x"
print("要点: Vary 决定缓存键的二次维度, 少写一个头就会串味, "
      "带 Vary: * 则等价于每次都不命中")
```

**追问**:
- Vary 与 304 条件请求如何配合?——304 必须回填 Vary,否则客户端不知道这份 200 副本该按哪些头区分。
- 缓存键里要不要包含 Cookie?——包含会撕裂命中率,通常只包含会话级差异真正影响内容的少数头,并配合 Cache-Control: private。
