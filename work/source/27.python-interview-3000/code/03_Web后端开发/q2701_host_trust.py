"""主机头的信任边界: 白名单校验与链接生成(纯标准库)。"""
from urllib.parse import urlsplit

ALLOWED_HOSTS = {"www.example.com", "api.example.com"}
BASE_URL = "https://www.example.com"  # 生成对外链接永远用配置基址


def host_allowed(host_header):
    """Host 允许带端口且大小写不敏感; 只做整域精确匹配, 不做子串匹配。

    urlsplit 前补 // 让 'host:port' 能按 netloc 解析, 拿到的 hostname 已去端口并小写。
    """
    if not host_header:
        return False
    host = urlsplit("//" + host_header).hostname or ""
    return host in ALLOWED_HOSTS


def reset_link(host_header, token):
    """重置链接的域名取配置基址而非请求 Host, 防止 Host 注入投毒。

    即使 Host 合法, 链接也走 BASE_URL: 多域名接入时重置页只认主站域名。
    """
    if not host_allowed(host_header):
        raise ValueError("非法 Host")
    return BASE_URL + "/reset?token=" + token


cases = [
    ("www.example.com", True),
    ("WWW.EXAMPLE.COM:443", True),
    ("www.example.com.attacker.io", False),  # 子串匹配会放过它
    ("attacker.io", False),
    ("", False),
]
for host, want in cases:
    got = host_allowed(host)
    assert got == want, (host, got)
    print("%-30s allow=%s" % (repr(host), got))

print("合法 Host 重置链接:", reset_link("www.example.com", "t123"))
try:
    reset_link("attacker.io", "t123")
except ValueError as e:
    print("注入 Host 被拒:", e)
print("即使 Host 合法也走配置基址:", reset_link("api.example.com", "t123"))
