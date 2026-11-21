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
