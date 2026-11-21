"""条件请求头的组合裁决: 304 与 412 的优先级(纯标准库)。"""
import email.utils


def parse_etag_list(value):
    """If-None-Match 的值可以是逗号分隔列表, 也可以是通配符 *。"""
    value = value.strip()
    if value == "*":
        return "*"
    return [item.strip() for item in value.split(",")]


def etag_match(candidate, current, weak_ok=True):
    """弱比较忽略 W/ 前缀, 用于 If-None-Match; 强比较要求逐字节一致。"""
    def strip(s):
        return s[2:] if s.startswith("W/") else s
    if weak_ok:
        return strip(candidate) == strip(current)
    return candidate == current


def evaluate(method, resource, headers):
    """按 RFC 7232 固定顺序裁决, 返回 (status, 理由)。"""
    if "If-Match" in headers:
        listed = parse_etag_list(headers["If-Match"])
        ok = listed == "*" or any(
            etag_match(c, resource["etag"], weak_ok=False) for c in listed)
        if not ok:
            return 412, "If-Match 不匹配, 资源已被他人修改"
    if "If-Unmodified-Since" in headers:
        since = email.utils.parsedate_to_datetime(headers["If-Unmodified-Since"]).timestamp()
        if resource["mtime"] > since:
            return 412, "资源在 If-Unmodified-Since 之后被修改"
    if "If-None-Match" in headers:
        listed = parse_etag_list(headers["If-None-Match"])
        hit = listed == "*" or any(
            etag_match(c, resource["etag"], weak_ok=True) for c in listed)
        if hit and method in ("GET", "HEAD"):
            return 304, "ETag 命中, 缓存副本仍然有效"
        if hit:
            return 412, "非安全方法不允许覆盖已存在的表示"
    elif "If-Modified-Since" in headers and method in ("GET", "HEAD"):
        since = email.utils.parsedate_to_datetime(headers["If-Modified-Since"]).timestamp()
        if resource["mtime"] <= since:
            return 304, "修改时间未变, 缓存副本仍然有效"
    return 200, "条件全部通过, 返回新表示"


res = {"etag": '"v3"', "mtime": 1735689600.0}
httpdate = email.utils.formatdate(res["mtime"], usegmt=True)
cases = [
    ("GET", {"If-None-Match": 'W/"v3"'}, 304),
    ("GET", {"If-None-Match": '"v2", "v3"'}, 304),
    ("GET", {"If-None-Match": '"v9"', "If-Modified-Since": httpdate}, 200),
    ("GET", {"If-Modified-Since": httpdate}, 304),
    ("PUT", {"If-Match": '"v2"'}, 412),
    ("PUT", {"If-Match": '"v3"'}, 200),
]
for method, headers, expect in cases:
    status, why = evaluate(method, res, headers)
    print("{} {:36s} -> {} {}".format(method, str(headers), status, why))
    assert status == expect, (method, headers, status, expect)
print("要点: 裁决顺序 If-Match -> If-Unmodified-Since -> If-None-Match -> If-Modified-Since, "
      "INM 出现时 IMS 整体失效, 304 永不带响应体")
