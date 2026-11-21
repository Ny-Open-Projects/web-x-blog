"""跨子域会话共享的 Domain 收敛: 给谁看就看谁(纯标准库)。"""


def cookie_scope(set_cookie_value):
    """解析 Set-Cookie 的作用域: 有 Domain 属性则含所有子域, 无则仅限精确主机。"""
    parts = [p.strip() for p in set_cookie_value.split(";")]
    name_value = parts[0]
    attrs = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            attrs[k.strip().lower()] = v.strip()
        else:
            attrs[p.strip().lower()] = True
    domain = attrs.get("domain")
    host_only = domain is None
    if domain:
        domain = domain.lstrip(".").lower()  # 前导点早已废弃, 兼容处理
    secure = "secure" in attrs
    httponly = "httponly" in attrs
    samesite = attrs.get("samesite", "Lax").capitalize()
    return {"name_value": name_value, "domain": domain, "host_only": host_only,
            "secure": secure, "httponly": httponly, "samesite": samesite}


def receives(cookie, host):
    """host 是否能收到该 Cookie: host-only 要求全等, 否则 host 是 domain 本身或其子域。"""
    if cookie["host_only"]:
        return host == cookie["domain"]
    return host == cookie["domain"] or host.endswith("." + cookie["domain"])


CASES = [
    ("sid=abc; Domain=example.com; Secure; HttpOnly; SameSite=Lax", "example.com"),
    ("sid=abc; Domain=example.com; Secure; HttpOnly; SameSite=Lax", "api.example.com"),
    ("sid=abc; Secure; HttpOnly; SameSite=Strict", "app.example.com"),
    ("sid=abc; Domain=example.com; Secure; HttpOnly; SameSite=Lax", "evil.example.com"),
]
for raw, host in CASES:
    c = cookie_scope(raw)
    label = "Domain=%s" % c["domain"] if c["domain"] else "host-only"
    print("%-14s %-22s <- %-18s 收到=%s" % (c["name_value"], label, host, receives(c, host)))

c_shared = cookie_scope("sid=abc; Domain=example.com; Secure; HttpOnly")
assert receives(c_shared, "example.com") and receives(c_shared, "api.example.com")
c_narrow = cookie_scope("sid=abc; Secure; HttpOnly; SameSite=Strict")
assert c_narrow["host_only"] and not receives(c_narrow, "api.example.com")
assert not receives(c_shared, "notexample.com"), "后缀匹配必须带点, notexample.com 不是 example.com 的子域"
print("收敛原则: 会话 Cookie 默认 host-only; 确需跨子域时 Domain 收到主域并全线 Secure")
