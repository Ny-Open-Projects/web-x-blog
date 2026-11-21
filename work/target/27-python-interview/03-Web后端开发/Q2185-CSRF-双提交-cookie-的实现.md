---
title: [Q2185] CSRF 双提交 cookie 的实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2185 · CSRF 双提交 cookie 的实现

> 难度:★★★☆ | 标签:安全, CSRF

**问**:双提交 cookie 防 CSRF 的原理是什么?裸的双提交为什么不够?

**答**:原理是利用"浏览器会自动带 cookie,但攻击者站点读不到本域 cookie"的边界:服务端把随机 token 写入一个非 HttpOnly 的 cookie,同时要求前端脚本读取它并放进自定义请求头(X-CSRF-Token);校验时比对 cookie 值与请求头是否一致——跨站伪造请求只能自动带 cookie,读不到值,头对不上即拒绝。裸双提交的漏洞在于子域:任何能写主域 cookie 的子域 XSS 或子域接管,可以伪造一个自洽的 cookie 头对;所以生产实现必须给 token 加签名或与会话绑定(HMAC(session, nonce)),服务端验签,cookie 值就不再由客户端说了算。与 SameSite 的关系:SameSite=Lax 挡大部分 CSRF,双提交是纵深防御的第二层,跨浏览器兜底。

```python
# file: code/03_Web后端开发/q2185_csrf_double_submit.py
"""CSRF 双提交 cookie: cookie 与请求头成对校验加签名强化(纯标准库)。"""
import hmac
import secrets

KEY = b"csrf-signing-key"


def issue_pair(session_id):
    """签名的双提交令牌: nonce 绑定会话, 同时写入非 HttpOnly cookie 与页面。"""
    nonce = secrets.token_hex(16)
    mac = hmac.new(KEY, (session_id + ":" + nonce).encode(), "sha256").hexdigest()[:16]
    return "{}.{}".format(nonce, mac)


def verify(session_id, cookie_token, header_token):
    if not cookie_token or not header_token:
        return False, "缺少 cookie 或请求头"
    if not hmac.compare_digest(cookie_token, header_token):
        return False, "cookie 与请求头不一致"
    try:
        nonce, mac = cookie_token.split(".", 1)
    except ValueError:
        return False, "令牌格式错误"
    expect = hmac.new(KEY, (session_id + ":" + nonce).encode(), "sha256").hexdigest()[:16]
    if not hmac.compare_digest(mac, expect):
        return False, "签名不匹配, cookie 可能被子域注入"
    return True, "通过"


token = issue_pair("sess-1")
print("正常提交:", verify("sess-1", token, token))
print("头不匹配:", verify("sess-1", token, "attacker-value"))
forged = "deadbeef." + token.split(".", 1)[1]
print("子域伪造:", verify("sess-1", forged, forged))
assert verify("sess-1", token, token)[0]
assert not verify("sess-1", forged, forged)[0]
print("要点: 双提交把自动带 cookie 变成脚本主动回显; 加签名后才能扛住子域写 cookie 的变体")
```

**追问**:
- token 要每次请求轮换吗?——不必,会话级 token 足够,登录后必须轮换一次防会话固定。
- API 用 JWT 还有 CSRF 风险吗?——token 放 Authorization 头(而非 cookie)时无此风险;放 cookie 的 JWT 仍需 CSRF 防护。
