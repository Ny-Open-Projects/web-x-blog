"""尾斜杠规范化与 308 重定向: 让同一资源只有一个规范地址(纯标准库)。"""
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

CANONICAL = {"/api/users", "/api/users/{id}", "/api/orders"}


def normalize(path_with_query):
    """对多余尾斜杠做 308 规范重定向; 保留查询串, 不改变方法语义。"""
    parts = urlsplit(path_with_query)
    path = parts.path
    if len(path) > 1 and path.endswith("/"):
        stripped = path.rstrip("/") or "/"
        if stripped in CANONICAL:
            query = urlencode(parse_qsl(parts.query, keep_blank_values=True))
            location = urlunsplit(("", "", stripped, query, ""))
            return 308, location
    return 200, None      # 已是规范地址或确实以斜杠结尾的根路径


cases = [
    ("/api/users/", "应重定向"),
    ("/api/users/?page=2&size=10", "查询串必须保留"),
    ("/api/users", "规范地址直接 200"),
    ("/", "根路径不重定向"),
]
for url, note in cases:
    status, location = normalize(url)
    print("{:28s} -> {} {} ({})".format(url, status, location or "", note))

status, loc = normalize("/api/users/?page=2&size=10")
assert status == 308 and loc == "/api/users?page=2&size=10"
status, loc = normalize("/api/users")
assert status == 200 and loc is None

# 308 的意义: 浏览器与客户端会用同一方法重发请求, GET/POST 都不降级成 GET
print("要点: 尾斜杠重定向用 308 而不是 301, 保证 POST 不被改写成 GET; 查询串必须原样保留")
