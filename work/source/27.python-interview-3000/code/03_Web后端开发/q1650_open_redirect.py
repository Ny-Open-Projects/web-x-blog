"""开放重定向防护: 相对路径优先 + 受信主机白名单(纯标准库)。"""
from urllib.parse import urlsplit

TRUSTED_HOSTS = {"www.example.com", "example.com"}
DEFAULT = "/dashboard"


def safe_redirect(target):
    if not target:
        return DEFAULT
    if "\\" in target:                     # 浏览器把 \ 当 /, 必须先归一化拦截
        return DEFAULT
    parts = urlsplit(target)
    if parts.scheme and parts.scheme.lower() not in ("http", "https"):
        return DEFAULT                     # javascript: data: 一律拒
    if parts.netloc:
        host = (parts.hostname or "").lower()
        return target if host in TRUSTED_HOSTS else DEFAULT
    if not target.startswith("/") or target.startswith("//"):
        return DEFAULT                     # //evil.com 是协议相对地址, 会跳外域
    return target


cases = ["/orders?tab=1", "https://www.example.com/help",
         "https://evil.example.net/phish", "//evil.com/x",
         "javascript:alert(1)", "", "/\\evil.com"]
for c in cases:
    print(f"{c!r:36} -> {safe_redirect(c)}")
print("要点: 默认拒绝, 白名单放行; 一律优先用站内相对路径, 绝不拼接用户输入")
