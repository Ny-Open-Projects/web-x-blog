---
title: [Q2429] Cookie 的 SameSite 三值行为矩阵
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2429 · Cookie 的 SameSite 三值行为矩阵

> 难度:★★☆☆ | 标签:Cookie, SameSite, CSRF

**问**:SameSite 的 Strict、Lax、None 三种取值分别在什么请求下携带 Cookie?默认值是什么?

**答**:SameSite 管"跨站上下文里 Cookie 带不带",三种取值构成一张矩阵:Strict 除同站外全不带,连跨站顶层导航的 GET 也不带;Lax 放行跨站顶层导航的 GET(安全方法),挡掉跨站 POST 与 iframe 内一切请求;None 全部放行,但现代浏览器强制要求同时带 Secure,否则直接拒收。未显式声明时,主流浏览器默认按 Lax 处理,这也是"升级浏览器后第三方嵌入突然丢登录态"的常见事故来源。防 CSRF 的原理就藏在矩阵里:CSRF 攻击靠跨站 POST 自动带 Cookie,而 Lax 恰好挡住这条路径。要记住 None 是给第三方嵌入、跨站 SSO 跳转用的,普通会话 Cookie 用 Lax 即可,Strict 留给高敏感操作。

```python
# file: code/03_Web后端开发/q2429_samesite_matrix.py
"""Cookie 的 SameSite 三值行为矩阵(纯标准库)。"""

# 请求上下文 -> 是否跨站以及请求形态
CONTEXTS = [
    ("同站页面内子资源请求", "sub"),
    ("跨站 POST 表单提交", "cross_post"),
    ("跨站 GET 顶层导航", "top_nav_get"),
    ("第三方 iframe 内请求", "iframe"),
]

# SameSite 取值 -> 各上下文是否携带 Cookie
MATRIX = {
    "Strict": {"sub": True,  "cross_post": False, "top_nav_get": False, "iframe": False},
    "Lax":    {"sub": True,  "cross_post": False, "top_nav_get": True,  "iframe": False},
    "None":   {"sub": True,  "cross_post": True,  "top_nav_get": True,  "iframe": True},
}


def set_cookie_header(name, value, samesite, secure=True):
    """拼一个 Set-Cookie 响应头, SameSite=None 必须搭配 Secure。"""
    parts = ["{}={}".format(name, value), "Path=/", "SameSite={}".format(samesite)]
    if secure:
        parts.append("Secure")
    return "; ".join(parts)


def send_cookie(samesite, context_key):
    return MATRIX[samesite][context_key]


print("{:22s} {:>7s} {:>7s} {:>7s}".format("上下文", "Strict", "Lax", "None"))
for label, key in CONTEXTS:
    print("{:22s} {:>7s} {:>7s} {:>7s}".format(
        label, str(send_cookie("Strict", key)),
        str(send_cookie("Lax", key)), str(send_cookie("None", key))))

assert not send_cookie("Lax", "cross_post"), "Lax 正是靠挡跨站 POST 防 CSRF"
assert send_cookie("Lax", "top_nav_get"), "顶层导航 GET 要能带 Cookie, 否则外链登录态丢失"
assert send_cookie("None", "iframe"), "第三方嵌入场景只能用 None"

csrf = set_cookie_header("sid", "abc123", "Lax")
embed = set_cookie_header("sid", "abc123", "None")
assert "SameSite=Lax" in csrf and "Secure" in embed
print("普通会话:", csrf)
print("嵌入场景:", embed)
print("要点: None 必须配 Secure 否则现代浏览器直接拒收; "
      "未显式声明时浏览器默认按 Lax 处理, 跨站 POST 丢 Cookie 是最常见的线上事故")
```

**追问**:
- Strict 会不会把外链进站的用户登出?——会,外链跳转属于跨站顶层导航,Strict 不带 Cookie,通常配合一个中转页或落地页重登。
- SameSite 能完全替代 CSRF Token 吗?——不能,Lax 挡不住同站子域发起的请求与 GET 型副作用,敏感操作仍要 Token 或校验 Origin。
