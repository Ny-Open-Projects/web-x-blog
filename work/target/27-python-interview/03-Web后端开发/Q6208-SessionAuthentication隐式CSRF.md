---
title: "[Q6208] 前后端分离：SessionAuthentication 的隐式 CSRF 与 JWT 的取舍"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6208 · 前后端分离：SessionAuthentication 的隐式 CSRF 与 JWT 的取舍

难度：P7 ｜ 标签：DRF、SessionAuthentication、CSRF、JWT、Cookie、SameSite

**问**：API 同时支持 Session 和 JWT：前端用 Cookie 调接口时，POST 总返回 "CSRF Failed: CSRF token missing"；换成 `Authorization: Bearer` 就正常。为什么 JWT 不需要 CSRF？如果把 JWT 放进 Cookie 呢？DRF 的 `SessionAuthentication` 到底在什么时候强制 CSRF？前后端分离该怎么选？

**答**：
结论：CSRF 的前提是"浏览器会**自动**带上凭证"——Cookie 满足这一点，所以基于 Cookie 的认证必须校验 CSRF token；`Authorization` 头不会被浏览器自动附加（恶意站点无法跨域读/写自定义头），所以纯 Header 的 JWT 天然不受 CSRF 影响。DRF 的 `SessionAuthentication.authenticate()` 在请求带有效 session 时，对**非安全方法**（POST/PUT/PATCH/DELETE）调用 `enforce_csrf()`，失败抛 `PermissionDenied`；GET/HEAD/OPTIONS 不校验。把 JWT 放进 Cookie，就重新变成"自动携带"，必须加 CSRF 防护，等于回到 Session 模式。

取舍：a) 同域/同站前后端，Session + CSRF + `SameSite=Lax` 简单可靠，注销/吊销容易；b) 跨域 SPA/移动端，Bearer JWT 放内存（不放 localStorage 更安全但刷新丢失）或短期 access + HttpOnly refresh cookie；c) 如果必须用 Cookie 存 JWT，配 `SameSite=None; Secure` + CSRF 双提交/同步令牌，并注意 CORS `allow_credentials=True` 不能配 `*`；d) JWT 无状态，吊销要靠短过期 + 黑名单/版本号；e) 别同时开 Session 和 Cookie-JWT 两套认证而不区分 CSRF 策略，容易出现"某条路径漏校验"。

实战：事故形态是"前端从 Session 迁到 JWT，但登录接口仍写 Session Cookie，DRF 默认认证顺序先命中 SessionAuthentication，所有写接口开始 403；把 JWT 认证放前面并移除 Session 写入后恢复"。下面用最小请求模型演示三种凭证的 CSRF 判定。

```python
SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}


class Request:
    def __init__(self, method, cookie=None, auth=None, csrf_header=None,
                 csrf_cookie=None):
        self.method = method
        self.cookie = cookie
        self.auth = auth
        self.csrf_header = csrf_header
        self.csrf_cookie = csrf_cookie


def session_auth(req):
    if not req.cookie:
        return None
    if req.method not in SAFE_METHODS:
        if not req.csrf_header or req.csrf_header != req.csrf_cookie:
            raise PermissionError("CSRF Failed: token missing or mismatched")
    return {"user": "alice", "via": "session"}


def jwt_auth(req):
    if not req.auth:
        return None
    if not req.auth.startswith("Bearer "):
        raise PermissionError("bad token")
    return {"user": "alice", "via": "jwt-header"}


print("[1] Cookie 认证 POST 缺 CSRF:", end=" ")
try:
    session_auth(Request("POST", cookie="sid=1"))
except PermissionError as e:
    print(e)

print("[2] Cookie 认证 POST 带双提交 token:",
      session_auth(Request("POST", cookie="sid=1",
                           csrf_header="t", csrf_cookie="t")))

print("[3] Bearer JWT POST 不需要 CSRF:",
      jwt_auth(Request("POST", auth="Bearer x")))

print("[4] Cookie 认证 GET 不校验 CSRF:",
      session_auth(Request("GET", cookie="sid=1")))

print("[5] JWT 放 Cookie 就等于回到 Session，必须加 CSRF")
```

**追问一**：`SameSite=Lax` 能替代 CSRF token 吗？—— 不能完全替代。`Lax` 会阻止大多数跨站 POST 携带 Cookie，但：a) 老浏览器不支持；b) 同站不同子域、开放重定向、GET 型副作用仍可能被利用；c) `SameSite=None` 的场景（跨域 SPA）直接失效。CSRF token 是"服务端可验证的一次性/随机值"，和 SameSite 是互补而非替代；高安全场景两者都要。

**追问二**：为什么 `Authorization` 头能躲过 CSRF？—— 浏览器发起跨站请求时，HTML 表单/图片/脚本只能设置有限的头，不能自定义 `Authorization`；要带这个头必须用 `fetch`/XHR，并触发 CORS 预检，服务端不授权就发不出去。所以攻击者无法让受害者浏览器"自动"带上 Bearer token。代价是 token 存在 JS 可读的地方，XSS 一旦发生就失守——CSRF 和 XSS 是两个方向的风险，不能互相替代。

## 背诵要点
- CSRF 的本质是"浏览器自动带凭证"；Cookie 认证必须校验 CSRF，Header Bearer JWT 不需要。
- DRF `SessionAuthentication` 对非安全方法强制 CSRF；JWT 放 Cookie 等于回到 Session 模式。
- SameSite 是纵深防御不是替代；Bearer token 要防 XSS，Cookie 方案要防 CSRF。

## 复盘追问
- 同一 API 用 Cookie 调 POST 报 CSRF Failed，怎么解释？（SessionAuthentication 强制校验）
- JWT 放 HttpOnly Cookie 后还需要 CSRF 吗？（需要，自动携带语义回来了）
