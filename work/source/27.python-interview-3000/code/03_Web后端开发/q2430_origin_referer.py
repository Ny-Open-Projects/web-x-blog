"""Origin 与 Referer 的语义差异与 CSRF 源校验(纯标准库)。"""
from urllib.parse import urlsplit


def site_of(url):
    """取 scheme://host:port 站点粒度, 不含路径与查询。"""
    parts = urlsplit(url)
    netloc = parts.netloc.lower()
    if parts.scheme == "https" and parts.port == 443:
        netloc = netloc.split(":")[0]          # 规范化默认端口
    if parts.scheme == "http" and parts.port == 80:
        netloc = netloc.split(":")[0]
    return "{}://{}".format(parts.scheme.lower(), netloc)


def check_csrf(headers, method, allowed_sites):
    """CSRF 敏感方法的源校验: 优先 Origin, 退而求 Referer, 都没有则拒绝。"""
    if method not in ("POST", "PUT", "PATCH", "DELETE"):
        return True, "安全方法不做源校验"
    if "Origin" in headers:
        src = "Origin"
        got = site_of(headers["Origin"])
    elif "Referer" in headers:
        src = "Referer"
        got = site_of(headers["Referer"])
    else:
        return False, "无源信息, 拒绝"
    if got in allowed_sites:
        return True, "{} 源 {} 在白名单".format(src, got)
    return False, "{} 源 {} 不在白名单".format(src, got)


ALLOWED = {"https://app.example.com", "https://www.example.com"}

cases = [
    # 请求头, 方法, 期望
    ({"Origin": "https://app.example.com"}, "POST", True),
    ({"Origin": "https://evil.example.com"}, "POST", False),
    ({"Referer": "https://www.example.com/account/settings?tab=2"}, "POST", True),
    ({"Referer": "http://www.example.com/x"}, "POST", False),          # scheme 不同
    ({}, "POST", False),                                               # 两者都没有
    ({}, "GET", True),
    ({"Origin": "https://www.example.com:443/x/y"}, "POST", True),     # Origin 带路径时只取站点
]
for headers, method, expect in cases:
    ok, why = check_csrf(headers, method, ALLOWED)
    print("{:<4} {:34s} -> {}".format(method, str(headers), why))
    assert ok == expect, (headers, method, ok, why)

# 语义差异要点
assert site_of("https://www.example.com/a/b?c=1") == "https://www.example.com"
print("要点: Origin 只有站点三元组且 CORS 与非 GET 请求必带; "
      "Referer 带完整路径可被 Referrer-Policy 剥掉, 所以安全校验优先信 Origin")
