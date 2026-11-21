"""路径规范化先行: 点段与编码变形的绕过防护(纯标准库)。"""
import posixpath
import re
from urllib.parse import unquote

ADMIN_PREFIX = "/admin"


class BadPath(ValueError):
    """路径含非法字符或点段越界。"""


def normalize_path(raw):
    """规范化顺序固定: 先解码一次, 再拒绝点段, 最后合并斜杠。

    先解码再校验是硬顺序: %2e%2e 必须先变回 .. 才会被规则拦住;
    网关策略直接拒绝任何点段, 不替客户端做穿越归并, 语义最简单最稳。
    """
    path = unquote(raw)  # 解码永远只做一次
    if "\\" in path or "\x00" in path:
        raise BadPath("非法字符")
    if path == ".." or path.startswith("../") or path == "/.." or "/../" in path or path.endswith("/.."):
        raise BadPath("点段越界")
    path = re.sub(r"/{2,}", "/", path)  # 合并重复斜杠
    return posixpath.normpath(path)


def authorize(raw, is_admin):
    """授权只看规范化后的路径; 原始路径仅用于日志与告警。"""
    norm = normalize_path(raw)
    if norm == ADMIN_PREFIX or norm.startswith(ADMIN_PREFIX + "/"):
        return is_admin, norm
    return True, norm


CASES = [
    "/api/%2e%2e%2fadmin/secrets",  # 编码点段: naive 放行, 规范化后拒绝
    "/%61dmin/keys",                # 编码字母: 解码后才露出 /admin 前缀
    "/api//admin//keys",            # 重复斜杠: 合并后不在管理区
    "/admin/console",               # 明文管理路径
    "/public/info",
]
for raw in CASES:
    naive = raw.startswith(ADMIN_PREFIX)
    try:
        norm = normalize_path(raw)
        ok, _ = authorize(raw, is_admin=False)
        print("%-30s -> %-24s naive=%-5s strict=%s" % (raw, norm, naive, ok))
    except BadPath as e:
        print("%-30s -> 拒绝: %-12s  naive=%-5s strict=False" % (raw, e, naive))

assert normalize_path("/api//x//y") == "/api/x/y"
assert normalize_path("/%61dmin/keys") == "/admin/keys"
for bad in ("/api/admin/../admin/users", "/out/../../etc", "/a%00b", "/a\\b"):
    try:
        normalize_path(bad)
    except BadPath:
        print("拒绝:", bad)
