"""重定向目标解析的边界: 反斜杠、userinfo、scheme 与 CRLF(纯标准库)。"""
from urllib.parse import unquote, urlsplit

TRUSTED = {"www.example.com"}


def analyze(target):
    problems = []
    if "\\" in target:
        problems.append("反斜杠会被浏览器当斜杠, 绕过前缀检查")
    if "\r" in target or "\n" in target:
        problems.append("CRLF 可注入响应头")
    parts = urlsplit(target)
    if parts.scheme and parts.scheme.lower() not in ("http", "https"):
        problems.append(f"危险 scheme: {parts.scheme}")
    if parts.scheme in ("http", "https") and not parts.netloc:
        problems.append("特殊 scheme 缺主机, 浏览器会补全成外部地址")
    if parts.netloc:
        host = (parts.hostname or "").lower()
        userinfo, _, _ = parts.netloc.rpartition("@")
        if userinfo:
            problems.append(f"netloc 带 userinfo, 真实主机是 {host}")
        if host not in TRUSTED:
            problems.append(f"主机不在白名单: {host}")
    decoded = unquote(target)
    if decoded != target and ("//" in decoded or "\\" in decoded):
        problems.append(f"解码后出现路径分隔符: {decoded}")
    return problems


cases = [
    "/ok/path",
    "//evil.com",
    "/\\evil.com",
    "https://www.example.com@evil.com/",
    "https:evil.com",
    "javascript:alert(1)",
    "/redirect?url=%2F%2Fevil.com",
    "/a\r\nSet-Cookie: x=1",
]
for c in cases:
    print(f"{c!r:42} -> {analyze(c) or '通过'}")
print("要点: 校验必须基于 urlsplit 解析后的 netloc, 而不是字符串前缀; 先解码再判一次防绕过")
