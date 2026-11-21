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
