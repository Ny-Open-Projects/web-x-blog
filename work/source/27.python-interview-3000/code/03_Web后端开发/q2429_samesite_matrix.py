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
