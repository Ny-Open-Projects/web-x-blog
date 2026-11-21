---
title: [Q134] CSRF 原理与防护
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q134 · CSRF 原理与防护

> 难度:★★☆ | 标签:CSRF, 安全

**问**:CSRF 攻击的原理是什么?为什么 JWT 放 Header 就天然免疫?

**答**:CSRF 利用浏览器"自动携带 Cookie"的行为:恶意站点诱导已登录用户发起跨站请求,服务器误认为是用户本人操作。防护核心是"验证请求来自本站同源表单":Django 内置 CsrfViewMiddleware 校验表单/头部的 csrftoken 与 Cookie 双提交;SameSite=Lax 已挡住绝大多数跨站 POST;JWT 放在 Authorization 头由 JS 显式携带,浏览器不会自动附加,故免疫 CSRF——代价是 token 必须防 XSS 窃取。

```python
# file: code/03_Web后端开发/q134_csrf.py
import secrets

# Django 内置方案的双提交校验逻辑示意
SESSIONS: dict[str, str] = {}     # session_id -> csrf_token

def issue_token(session_id: str) -> str:
    token = secrets.token_urlsafe(32)
    SESSIONS[session_id] = token          # ① Cookie/Session 侧存一份
    return token                          # ② 表单 hidden 字段发一份

def verify(session_id: str, form_token: str) -> bool:
    expected = SESSIONS.get(session_id)
    return bool(expected) and secrets.compare_digest(expected, form_token)

# settings.py: MIDDLEWARE 需含 CsrfViewMiddleware
# 模板: <form>{% csrf_token %}</form>
# 前后端分离: 前端从 cookie 取 csrftoken 放入 X-CSRFToken 头

sid = 'sess-0001'
tok = issue_token(sid)
print(verify(sid, tok), verify(sid, 'evil-token'))
```

**追问**:
- 双提交 Cookie 的原理?——CSRF token 同时放 cookie 与表单/头,服务端比对一致才放行;攻击者跨站读不到本站 cookie 所以拼不出匹配值。
- 纯 API(JSON Token 头携带)还需要 CSRF 防护吗?——浏览器不会自动附 Authorization 头,天然免疫;但 token 存 cookie 的 SPA 仍要防。
- SameSite=Lax 放行了什么?——顶级导航的 GET(链接跳转);所以 GET 请求必须保持无副作用,否则 Lax 也防不住。
