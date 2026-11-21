---
title: [Q1888] Vary 头与缓存的正确性
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1888 · Vary 头与缓存的正确性

> 难度:★★☆☆ | 标签:HTTP 缓存, CDN

**问**:为什么说忘写 Vary 是缓存事故的高发源头?缓存键应该怎么算?

**答**:缓存默认按 URL 键值存储,但同一 URL 会因请求头不同返回不同表示(Accept-Encoding 压缩档、Accept 格式、Cookie 登录态),Vary 响应头就是服务端声明的"这些请求头参与表示的区分"。正确实现是把 Vary 列出的头按字典序规范化后拼进缓存键,键不匹配即未命中回源;忘写 Vary 时,第一个请求的表示会被缓存并错误地发给所有客户端——压缩响应发给不支持 gzip 的爬虫、登录态页面泄漏给未登录用户,都是真实事故形态。Vary: * 表示任何头都可能影响表示,等价于共享缓存不可存。结论:写协商逻辑与写 Vary 必须是同一次提交,用契约测试锁住两者的一致性。

```python
# file: code/03_Web后端开发/q1888_vary_cache.py
"""Vary 头与缓存正确性: 协商字段落进缓存键才不会串档(纯标准库)。"""


class RespCache:
    """按 Vary 头构造二级键的最小响应缓存。"""

    def __init__(self):
        self.store = {}

    @staticmethod
    def cache_key(url, vary_fields, request_headers):
        """Vary 列出的每个头都按字典序拼进键; 未列出的协商头不参与。"""
        parts = [url]
        for field in sorted(vary_fields):
            parts.append("{}={}".format(field.lower(),
                                        request_headers.get(field.lower(), "")))
        return "|".join(parts)

    def put(self, url, vary_fields, request_headers, status, body):
        key = self.cache_key(url, vary_fields, request_headers)
        self.store[key] = (status, body, tuple(sorted(vary_fields)))

    def get(self, url, vary_fields, request_headers):
        return self.store.get(self.cache_key(url, vary_fields, request_headers))


cache = RespCache()
req_gzip = {"accept-encoding": "gzip"}
req_plain = {"accept-encoding": "identity"}
body = "<html>同一个 URL 的两种表示</html>"

# 正确姿势: 协商了 Accept-Encoding 就必须 Vary: Accept-Encoding
vary = ["Accept-Encoding"]
cache.put("/page", vary, req_gzip, 200, "<gzip 压缩表示>")
cache.put("/page", vary, req_plain, 200, body)
hit_gzip = cache.get("/page", vary, req_gzip)
hit_plain = cache.get("/page", vary, req_plain)
print("gzip 请求命中:", hit_gzip[1])
print("identity 请求命中:", hit_plain[1])
assert hit_gzip[1] != hit_plain[1], "不同编码档位不能串档"

# 反例: 服务端按头协商了却忘写 Vary, 代理缓存只按 URL 存一份
cache.put("/wrong", [], req_gzip, 200, "<gzip 压缩表示>")
wrong = cache.get("/wrong", [], req_plain)
print("忘写 Vary 时 identity 请求误命中 gzip 档:", wrong[1])
assert wrong is not None and "gzip" in wrong[1]

# Vary: * 表示每次都可能不同, 任何共享缓存都应放弃缓存该响应
print("Vary: * 的语义: 等价于不可缓存, 只允许私有/客户端侧决策")
print("要点: Vary 是协商响应的缓存正确性契约, 写协商逻辑时必须同步写 Vary")
```

**追问**:
- Vary 比较时大小写和顺序敏感吗?——头名大小写不敏感,列表也应规范化(小写、排序)后比较。
- 压缩为什么通常由代理层做?——Nginx/CDN 统一压缩并自动带 Vary,应用层不重复劳动、缓存键也统一。
