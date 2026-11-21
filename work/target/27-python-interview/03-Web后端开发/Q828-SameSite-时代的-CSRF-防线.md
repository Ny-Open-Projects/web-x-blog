---
title: [Q828] SameSite 时代的 CSRF 防线
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q828 · SameSite 时代的 CSRF 防线

> 难度:★★★☆ | 标签:CSRF, SameSite

**问**:现代浏览器默认 SameSite=Lax 之后,CSRF token 还需要吗?API 场景呢?

**答**:SameSite=Lax 让跨站请求**不自动携带 Cookie**,挡住了绝大多数传统 CSRF(跨站 POST/表单)。但防线要纵深:老浏览器与 SameSite=None 的会话仍需 CSRF token;现代方案是**双提交 Cookie**(token 同时在 Cookie 与请求头,服务端比对)或 **Origin/Referer 校验**。纯 API 场景:Authorization 头不自动携带,天然免疫 CSRF;用 Cookie 认证的 SPA 仍要保留防线。另外 CSRF token 要与会话绑定,登录后轮换。

```python
# file: code/03_Web后端开发/q828_samesite_csrf.py
from __future__ import annotations

from typing import Optional

def cookie_policy(name: str, same_site: str, secure: bool) -> str:
    parts = [f"{name}=v", f"SameSite={same_site}"]
    if secure:
        parts.append("Secure")
    return "; ".join(parts)

def csrf_guard(same_site: str, origin_header: Optional[str], trusted: set) -> str:
    if same_site in ("Lax", "Strict"):
        return "SameSite 已挡住跨站写请求"
    if origin_header:
        host = origin_header.split("/")[2] if "/" in origin_header else origin_header
        if host not in trusted:
            return "Origin 不在白名单 拒绝"
    return "需要 CSRF token 校验"

print(cookie_policy("sid", "Lax", True))
print(csrf_guard("Lax", "https://evil.com", {"api.example.com"}))
print(csrf_guard("None", "https://api.example.com", {"api.example.com"}))
```

**追问**:
- Lax 放行哪些跨站请求?——顶层导航的安全方法(GET 链接跳转),POST/DELETE 等写方法一律不带 Cookie。
- 双提交为什么有效?——攻击者能诱导请求却读不到目标域的 Cookie,无法把 token 放进自定义头,比对必然失败。
