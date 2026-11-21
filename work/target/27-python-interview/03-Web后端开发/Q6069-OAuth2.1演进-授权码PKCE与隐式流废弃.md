---
title: [Q6069] OAuth 2.1 演进：PKCE 强制与隐式流废弃
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6069 · OAuth 2.1 演进：授权码 PKCE 强制与隐式流废弃

> 难度:★★★★ | 标签:版本演进, OAuth2.1, PKCE, 认证安全

**问**：老系统还在用"隐式流"（response_type=token 前端拿 access_token）和"资源属主密码流"（password grant）。OAuth 2.1 为什么把它们废弃了？PKCE 的 code_verifier 机制怎么防授权码拦截？服务端（Python 后端）在授权码流里的职责边界是什么？

**答**：演进脉络：OAuth 2.1（2.0 的最佳实践收敛版，draft RFC 6749bis）废弃两条流：a) **隐式流**：access_token 经 URL fragment 直接回前端——历史上是 SPA 无后端时的妥协，缺陷是 token 暴露在浏览器历史/Referer/日志、无法安全用 client_secret、被重定向劫持即丢 token；替代 = 授权码+PKCE（SPA 同样可用）。b) **密码流**：应用收集用户密码——教会整个生态"第三方替用户输入密码"这个反模式，无法接 MFA/SSO；替代 = 授权码流或客户端凭据流（机器对机器）。**PKCE 机制**：客户端先生成随机 `code_verifier`（高熵 43-128 字符），其 SHA256 = `code_challenge` 随授权请求发出；换 token 时必须出示原始 verifier，服务端验 hash——授权码即使被重定向劫持，攻击者没有 verifier 兑不了 token（防"授权码注入/拦截"攻击）。Python 后端职责边界：a) **我们是资源服务器时**：只验 access_token（JWT 验签或 introspection，见 Q6009），**不参与授权码交换**；b) **我们是客户端（接入第三方登录）时**：负责 code→token 的后端交换（code_verifier 保存方式：SPA 场景存 sessionStorage、有后端存 session/cookie），redirect_uri 严格注册；c) **我们是授权服务器时**：强制 PKCE（public client 一律 require），校验 redirect_uri 精确匹配（防开放重定向，与 Q6059 SSRF 同源的风险面）、state 防 CSRF。落地基线：authlib（OAuth client/server）、joserfc（JWT），Django/FastAPI 都有集成路径；缺库降级：PKCE 的 SHA256/S256 校验标准库 hashlib 即可实现。

```python
# file: code/03_Web后端开发/q6069_oauth_pkce.py
import base64, hashlib, hmac, secrets, urllib.parse

# 1) 客户端: 生成 verifier/challenge (PKCE S256)
def make_pkce():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    return verifier, challenge

verifier, challenge = make_pkce()
state = secrets.token_urlsafe(16)                    # CSRF 防 token
auth_url = ("https://auth.demo/authorize?" +
    urllib.parse.urlencode({
        "response_type": "code", "client_id": "app",
        "redirect_uri": "https://app.demo/cb",       # 严格注册, 精确匹配
        "scope": "openid", "state": state,
        "code_challenge": challenge, "code_challenge_method": "S256"}))
print("授权请求:", auth_url[:90], "...")

# 2) 授权服务器: 强制 public client 用 PKCE; 校验 + 颁发 code
codes = {}
def authorize(client_id, is_public, given_challenge, redirect_uri, session_user):
    assert redirect_uri == "https://app.demo/cb", "redirect_uri 精确匹配"
    if is_public:
        assert given_challenge, "public client 必须带 PKCE"
    code = secrets.token_urlsafe(24)
    codes[code] = {"client": client_id, "user": session_user,
                   "challenge": given_challenge, "used": False}
    return code

code = authorize("app", True, challenge, "https://app.demo/cb", "u42")

# 3) token 端点: 一次性 code + verifier hash 校验
def exchange_token(code, verifier, client_id):
    rec = codes.get(code)
    assert rec and not rec["used"], "code 无效或重放"     # 一次性, 防 code 重放
    codes[code]["used"] = True
    if rec["challenge"]:
        calc = base64.urlsafe_b64encode(
            hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
        assert hmac.compare_digest(calc, rec["challenge"]), "PKCE 校验失败(码被劫持也换不到)"
    return {"access_token": secrets.token_urlsafe(32), "token_type": "Bearer"}

tok = exchange_token(code, verifier, "app")
print("正常交换:", "access_token 已颁发")

# 4) 攻击演示: 劫持 code 但没有 verifier -> 换不到
try:
    exchange_token(code, "wrong-verifier-attacker-value", "app")
except AssertionError as e:
    print("劫持拦截:", e)

# 5) code 重放拦截
code2 = authorize("app", True, challenge, "https://app.demo/cb", "u42")
exchange_token(code2, verifier, "app")
try:
    exchange_token(code2, verifier, "app")
except AssertionError as e:
    print("重放拦截:", e)

print("废弃流: implicit(response_type=token) / password grant -> 一律授权码+PKCE")
```

**追问**：1) state 参数防什么、PKCE 防什么，两者重复吗？——不重复：state 防 **CSRF/会话固定**（回调必须与发起请求同会话绑定），PKCE 防**授权码被拦截后兑换**（码不绑定 verifier 无效）；生产两个都要，还常见 nonce（防 ID token 重放，OIDC 层）。2) 后端做 code 交换时 verifier 存哪最安全？——有后端的 Web 应用存服务端 session（HTTP-only cookie 关联），绝不下发浏览器；SPA+后端 BFF 模式把交换移到 BFF，token 不进浏览器（2.1 的推荐架构）；纯 SPA 无后端才用 sessionStorage+PKCE 兜底。3) 为什么 password grant 难以彻底清退？——存量客户端改造是成本大头：机器对机器换 client_credentials，用户场景换授权码流；迁移抓手是在授权服务器**先禁新接入、限期关旧流**并监控旧流调用方清单逐个迁移——技术以外是流程工程。

## 背诵要点
- OAuth 2.1 废弃隐式流（token 进 URL，暴露于历史/Referer/日志）与密码流（第三方收密码、不兼容 MFA），统一授权码+PKCE。
- PKCE：verifier（高熵 43-128）→ S256=challenge 随授权请求，换 token 验 hash；防授权码劫持；state 防 CSRF（不重复），code 一次性防重放。
- 职责边界：资源服务器只验 token；客户端后端做 code 交换（verifier 存服务端 session）；授权服务器强制 public client PKCE + redirect_uri 精确匹配。

## 复盘追问
- 你们还有没有 implicit/password grant 的存量接入？调用方清单梳理了吗？（提示：按禁新/限期关旧推进；监控旧流调用并逐个迁移）
- 接第三方登录的后端有没有严格校验 redirect_uri/state？code 是否一次性消费？（提示：对照本卡三道校验演练；考虑 BFF 架构把 token 挡在浏览器外）
