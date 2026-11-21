---
title: [Q2722] 跨子域会话共享的 Domain 收敛
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2722 · 跨子域会话共享的 Domain 收敛

> 难度:★★★☆ | 标签:Cookie, 会话, 安全

**问**:多个子域应用要共享登录态,Cookie 的 Domain 怎么配才不引火烧身?

**答**:规则先记住:不写 Domain 属性的 Cookie 是 host-only,只有设置它的精确主机收到;写了 Domain=example.com,所有子域包括 evil.example.com 都收到。共享的代价因此明确:任何一个子域被 XSS 或供应链攻破,主域会话 Cookie 就裸奔,子域越多爆炸半径越大。收敛策略三步:默认 host-only;确需共享才把 Domain 收到主域,并全线 Secure 加 HttpOnly 加 SameSite;高敏感会话收敛到专用认证域,业务子域只持短期授权令牌。匹配校验时后缀必须带点,notexample.com 不是 example.com 的子域;前导点写法与不带点等价,新代码统一不带点。

```python
# file: code/03_Web后端开发/q2722_cookie_domain.py
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
```

**追问**:
- 子域被攻破能偷走主域 Cookie 吗?——Domain 收敛后能;HttpOnly 挡住 XSS 直接读,但挡不住网络层,所以高价值会话不做域级共享。
- Domain 能设成别的域吗?——不能,只能设当前主机或其父域,浏览器直接拒绝跨域 Set-Cookie。
