---
title: [Q133] Cookie 安全属性
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q133 · Cookie 安全属性

> 难度:★★☆ | 标签:Cookie, 安全

**问**:HttpOnly、Secure、SameSite 分别防什么?如何组合设置一个登录 Cookie?

**答**:`HttpOnly` 禁止 JS 读取,防 XSS 窃取;`Secure` 仅 HTTPS 传输,防明文嗅探;`SameSite=Lax/Strict` 限制跨站携带,防 CSRF(Lax 允许顶级导航 GET,Strict 全禁,`None` 必须配 Secure);再加 `Path/Domain` 限定范围与 `Max-Age/Expires` 控制生命周期。登录态 Cookie 推荐组合:HttpOnly + Secure + SameSite=Lax + 合理过期时间;CSRF Token 作为纵深防御仍建议保留。

```python
# file: code/03_Web后端开发/q133_cookie_attrs.py
try:
    from fastapi import FastAPI, Response
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.post('/login')
def login(username: str, password: str, response: Response):
    # 实际:校验密码后签发 session id 或 JWT
    response.set_cookie(
        key='sessionid',
        value='fake-session-id',
        httponly=True,       # 防 XSS 读取
        secure=True,         # 仅 HTTPS
        samesite='lax',      # 防 CSRF,允许顶级导航
        max_age=3600,        # 1 小时
        path='/',
    )
    return {'msg': 'logged in'}

@app.post('/logout')
def logout(response: Response):
    response.delete_cookie('sessionid', path='/')
    return {'msg': 'logged out'}
```

**追问**:
- SameSite=None 什么时候用?——跨站场景(第三方嵌入、SSO 回跳)必须显式 None 且强制 Secure;默认 Lax 已挡大多数 CSRF。
- HttpOnly 挡得住 XSS 吗?——挡住 cookie 窃取,挡不住 XSS 本身;还能伪造请求(带 cookie 自动附上),CSRF token 与 CSP 仍要。
- Domain 属性设宽有什么风险?——`Domain=.example.com` 让所有子域可携带,任一子域 XSS 即波及全站;尽量不设 Domain。
