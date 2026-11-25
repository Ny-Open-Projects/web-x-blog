---
title: "[Q6174] 缺失 X-Forwarded-Proto 导致 redirect_uri 与 secure 判定错误"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6174 · 缺失 X-Forwarded-Proto 导致 redirect_uri 与 secure 判定错误

难度：P6 ｜ 标签：反向代理、X-Forwarded-Proto、redirect_uri、OAuth、scheme

**问**：TLS 在 ALB 终止，ALB 用 HTTP 回源到 uvicorn。上线后 OAuth 登录只在生产失败：IdP 报 `redirect_uri_mismatch`，而本地/测试一切正常。抓包看应用生成的 `redirect_uri` 是 `http://app.example.com/oauth/callback`，可 IdP 注册的是 `https://...`。应用怎么知道外部是 https？`X-Forwarded-Proto` 谁该信任、谁该清洗？为什么"无条件信任"比"不信任"更危险？

**答**：
结论：TLS 在 LB 终止后，应用收到的 TCP 是明文 HTTP，ASGI 的 `scope["scheme"]` 就是 `http`；外部是 https 这一事实只能通过代理头 `X-Forwarded-Proto: https`（或 RFC 7239 的 `Forwarded: proto=https`）传进来。应用不读这个头，`request.url.scheme`、`url_for(..., _external=True)`、OAuth `redirect_uri`、cookie 的 `Secure` 判定、HSTS/绝对重定向全都会按 `http` 生成。Q6121 讲 X-Forwarded-* 的信任边界与多跳取值，本题专攻“scheme 错导致 OAuth redirect_uri/secure 判定错”的落地事故。修复不是改业务代码拼 `https://`，而是让 uvicorn/Starlette 的 `ProxyHeadersMiddleware` 在**可信代理**前提下把 `scope["scheme"]` 改写为 `https`。

取舍：只信任来自已知代理网段的头（uvicorn `--proxy-headers --forwarded-allow-ips=<LB CIDR>`，不要用 `*`）；边缘必须**剥掉/覆盖**客户端自带的 `X-Forwarded-*`，否则攻击者可以伪造 `https` 让应用生成 https 链接/设置 Secure cookie，或在日志/风控里伪造来源。另一种做法是让 LB 直接做 HTTP→HTTPS 重定向和 HSTS，应用只处理内部语义；但 OAuth 的 `redirect_uri` 仍需要正确 scheme，不能只靠 LB。

实战：事故形态是"只有生产环境的 OAuth 回调失败，错误是 redirect_uri 不匹配；本地因为直接 https 或 IdP 配了 http 所以复现不了"。下面模拟：不信任转发头时生成 `http://`，与 IdP 注册值不一致；开启 ProxyHeaders 后生成 `https://`，一致。注意这段代码只演示 scheme 选择，真实部署还要校验代理来源、剥离客户端伪造头。

```python
from urllib.parse import urlencode


def request_url(scope, headers, path, trust_forwarded=True):
    scheme = scope["scheme"]
    if trust_forwarded and "x-forwarded-proto" in headers:
        scheme = headers["x-forwarded-proto"]
    host = headers.get("host") or scope["server"][0]
    return f"{scheme}://{host}{path}"


scope = {"scheme": "http", "server": ("10.0.3.17", 8000)}
headers = {"host": "app.example.com", "x-forwarded-proto": "https"}

no_proxy = request_url(scope, headers, "/oauth/callback", trust_forwarded=False)
with_proxy = request_url(scope, headers, "/oauth/callback")

print("默认（不信任转发头）redirect_uri:", no_proxy)
print("开启 ProxyHeaders     redirect_uri:", with_proxy)

registered = "https://app.example.com/oauth/callback"
print("与 IdP 注册值一致:", with_proxy == registered)
print("不一致时 IdP 直接拒绝授权码请求")
print("授权码请求参数:", urlencode({"redirect_uri": no_proxy}))
```

**追问一**：为什么"无条件信任 X-Forwarded-Proto"更危险？——这个头是客户端可发的。如果应用直接采信，攻击者可以发 `X-Forwarded-Proto: https` 让应用以为连接是安全的：可能绕过"仅 https 才允许"的检查、生成 https 链接、设置 `Secure` cookie（在 http 下设置 Secure cookie 浏览器不会回传，造成登录态异常），甚至在日志/风控里伪装来源。正确做法是网络层保证只有 LB 能设置该头（安全组/边缘清洗），应用只信任 LB 网段。

**追问二**：`Forwarded`（RFC 7239）和 `X-Forwarded-*` 该用哪个？——`Forwarded` 是标准头，能表达 `for/proto/host` 且支持多跳；`X-Forwarded-*` 是事实标准、生态支持广。关键是**多跳时的取值**：每跳代理应追加而不是覆盖，应用要取"最靠近自己的可信代理写入的值"，而不是第一个（第一个可能是客户端伪造）。无论用哪个，都要维护"可信代理链"配置，不能靠头里的顺序猜。

## 背诵要点
- TLS 在 LB 终止 → 应用 `scope["scheme"]="http"`；靠可信的 `X-Forwarded-Proto` 还原 https，否则 redirect_uri/cookie/绝对 URL 全错。
- 只信任已知代理网段，边缘必须剥离客户端自带的 `X-Forwarded-*`；`*` 等于把 scheme 交给攻击者。
- 多跳取"最近可信代理"写入的值；`Forwarded` 标准头与 `X-Forwarded-*` 语义对应，别混用顺序猜。

## 复盘追问
- 生产 OAuth 报 redirect_uri_mismatch、本地正常，如何用 scheme 与代理头解释并修复？（TLS 终止、ProxyHeaders、可信代理）
- 为什么无条件信任 `X-Forwarded-Proto` 会引入安全漏洞？（客户端可伪造、Secure cookie/仅 https 检查被绕过）
