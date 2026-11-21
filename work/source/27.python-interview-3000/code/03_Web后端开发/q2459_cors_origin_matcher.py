"""CORS 多域名白名单匹配器: 精确 通配子域与端口(纯标准库)。"""
from urllib.parse import urlsplit


def split_origin(origin):
    """origin 形如 https://app.example.com:8443, 返回 (scheme, host, port)。"""
    parts = urlsplit(origin)
    host = (parts.hostname or "").lower()
    scheme = (parts.scheme or "").lower()
    try:
        port = parts.port
    except ValueError:
        return None, None, None
    return scheme, host, port


def origin_allowed(origin, rules):
    """rules 为完整 origin 列表, 支持通配一层子域 https://*.example.com。"""
    if not origin or origin == "null":
        return False                              # 沙箱页面的 null origin 一律拒绝
    scheme, host, port = split_origin(origin)
    if not host:
        return False
    for rule in rules:
        r_scheme, _, r_rest = rule.partition("://")
        r_host, _, r_port = r_rest.partition(":")
        r_host = r_host.lower()
        if r_host.startswith("*."):
            suffix = r_host[1:]                   # .example.com
            if not host.endswith(suffix) or host == r_host[2:]:
                continue                          # 只匹配一层子域, 本域不算
            if "." in host[: -len(suffix)]:
                continue                          # a.b.example.com 深层不匹配
        elif host != r_host:
            continue
        if r_scheme and scheme != r_scheme:
            continue
        if r_port and port is not None and str(port) != r_port:
            continue
        return True
    return False


RULES = [
    "https://app.example.com",
    "https://*.example.com",
    "http://localhost:3000",
]

cases = [
    ("https://app.example.com", True),            # 精确命中
    ("https://api.example.com", True),            # 一层子域通配
    ("https://a.b.example.com", False),           # 深层子域不放行
    ("https://example.com", False),               # 本域不被 *.example.com 覆盖
    ("https://evilexample.com", False),           # 后缀拼接陷阱
    ("https://example.com.evil.com", False),      # 后缀拼接陷阱
    ("http://app.example.com", False),            # scheme 不同
    ("http://localhost:3000", True),
    ("http://localhost:4000", False),             # 端口不同
    ("null", False),
    ("", False),
]
for origin, expect in cases:
    got = origin_allowed(origin, RULES)
    print("{:30s} -> {}".format(origin or "(空)", "允许" if got else "拒绝"))
    assert got == expect, (origin, got, expect)

print("要点: 白名单匹配要同时锁 scheme host port 三元组; "
      "通配只放一层子域且不含本域, 拼接后缀与 null origin 是最常见的两类误放行")
