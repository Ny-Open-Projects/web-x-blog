---
title: [Q1370] Vary 头与压缩缓存的安全陷阱
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1370 · Vary 头与压缩缓存的安全陷阱

> 难度:★★ | 标签:缓存, 安全

**问**:开了压缩的接口,缓存层要加哪个头?BREACH 类攻击和压缩有什么关系?

**答**:响应被按 `Accept-Encoding` 区分内容(压缩版/原始版),缓存必须带 **`Vary: Accept-Encoding`**,否则 gzip 客户端可能命中为非压缩客户端缓存的条目,反之出现乱码。Vary 的语义是"这些请求头的不同取值是不同的缓存条目",写 `Vary: *` 等于禁缓存。安全侧:BREACH 类攻击利用"响应 = 静态模板 + 攻击者可注入的反射内容 + 压缩"的信息侧信道推断页面里的密钥,含敏感 token 的页面要么不压缩,要么保证无反射点并加随机填充。共享缓存(CDN/代理)对带 Authorization 的响应默认不缓存,别画蛇添足。

```python
# file: code/03_Web后端开发/q1370_vary_breach.py
"""Vary 头对缓存键的影响(纯标准库)。"""


def cache_key(url, vary_headers, request_headers):
    parts = [url]
    for h in vary_headers:
        parts.append(f"{h}={request_headers.get(h, '')}")
    return "|".join(parts)


def serve(url, vary_headers, request_headers, store):
    key = cache_key(url, vary_headers, request_headers)
    if key not in store:
        store[key] = f"content-for-{key}"
    return key


store = {}
k1 = serve("/api/list", ["Accept-Encoding"], {"Accept-Encoding": "gzip"}, store)
k2 = serve("/api/list", ["Accept-Encoding"], {"Accept-Encoding": "identity"}, store)
print(k1)
print(k2)
print("缓存条目数:", len(store), "—— 缺 Vary 时两者会共用一条并出错")
```

**追问**:
- 反射内容加多少随机填充才安全?——无法给出安全量,业界结论是"含密钥页面避免压缩或保证无反射点",填充只是缓解。
- Vary: User-Agent 合理吗?——历史上用于区分浏览器,现代做法是响应自适应 + 尽量别用 UA 做键,否则缓存命中率崩塌。
