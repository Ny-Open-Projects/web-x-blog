---
title: "[Q6175] WebSocket 跨站劫持与 Origin 校验缺失"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6175 · WebSocket 跨站劫持与 Origin 校验缺失

难度：P7 ｜ 标签：WebSocket、CSWSH、Origin、SameSite、Cookie 鉴权

**问**：一个聊天应用用 Cookie 鉴权 WebSocket，握手只校验 `Upgrade: websocket` 和 session。攻击者做一个恶意页面，里面 `new WebSocket("wss://chat.example.com/ws")`，为什么受害者的浏览器会带着他的 session 完成握手，攻击者随后能读消息？WebSocket 握手不是 HTTP 吗，CORS 为什么不管？`SameSite` 能挡住吗？本题与 Q2936（握手/帧解析）的边界在哪？只校验 `Origin` 够不够？

**答**：
结论：WebSocket 握手是一个 HTTP GET，浏览器会自动带上目标域的 Cookie（受 SameSite 约束），但**不会执行 CORS 预检/响应检查**——CORS 是 `fetch`/XHR 的规则，WebSocket 不在其列。服务端如果不校验 `Origin`，任何站点都能以受害者身份建立连接，这就是 Cross-Site WebSocket Hijacking（CSWSH）。`SameSite=Lax` 对跨站子资源请求不发送 Cookie，能缓解一部分；但 `SameSite=None`（跨站嵌入必需）、老浏览器、或攻击者用顶层导航/同站子域场景仍可能带上 Cookie，不能当唯一防线。服务端必须显式校验 `Origin` 白名单，最好再叠加握手时的短期 token/子协议令牌。

取舍：纯 Cookie 鉴权的 WS 天然受 CSWSH 威胁；改成"握手时带一次性 token（query/subprotocol/header）"能把 CSRF 面消掉，但要注意 token 别进 URL 日志/Referer。`Origin` 白名单要覆盖所有合法前端域名（含多环境、移动 WebView、桌面客户端），并且注意反向代理可能改写/剥离 `Origin`；对没有 `Origin` 的非浏览器客户端，要么拒绝，要么走独立 token 鉴权，不能"没 Origin 就放行"。

实战：事故形态是"安全扫描报告 CSWSH，开发复现时用 curl 手动连也能通，以为没问题"——curl 不带 Origin，恰好绕过了"只校验浏览器 Origin"的错误实现。下面模拟：只校验 Upgrade 时恶意 Origin 也 101；加白名单后 403；并展示"无 Origin 的原生客户端"与"浏览器必须带 Origin"两种策略的差异。

```python
def handshake(headers, allowed_origins, check_origin=True):
    if headers.get("upgrade", "").lower() != "websocket":
        return 400
    if not check_origin:
        return 101
    origin = headers.get("origin")
    if origin is None:
        return 403
    if origin not in allowed_origins:
        return 403
    return 101


evil = {
    "upgrade": "websocket",
    "cookie": "session=victim-session",
    "origin": "https://evil.example",
}

print("只校验 Upgrade（常见错误）:", handshake(evil, set(), check_origin=False))
print("加 Origin 白名单          :", handshake(evil, {"https://app.example"}))
print("正常同源                  :", handshake(
    {"upgrade": "websocket", "cookie": "session=x", "origin": "https://app.example"},
    {"https://app.example"}))
print("无 Origin 的浏览器请求     :", handshake({"upgrade": "websocket"}, {"https://app.example"}))
print("无 Origin 的原生客户端     :", handshake({"upgrade": "websocket"}, set(), check_origin=False))
```

**追问一**：为什么 CORS 不保护 WebSocket？——CORS 是浏览器对 `fetch`/XHR 的"读响应"限制：它允许跨站发请求，但阻止跨站读响应（除非服务器放行）。WebSocket 是另一种协议升级，握手后是双向帧通道，没有"响应读权限"这个概念；浏览器只会在握手请求里带 Cookie，不会因为目标没给 CORS 头就阻止连接。因此防 CSWSH 的责任完全在服务端：校验 `Origin`，或用不可被跨站自动携带的凭据（token）。

**追问二**：只校验 `Origin` 有哪些绕过/盲区？——a) 反向代理/网关把 `Origin` 改写或剥离，后端看到空值；b) 同源但存在 XSS 时，攻击者本来就能用受害者身份连；c) 移动 App/桌面客户端的 `Origin` 可能是 `null` 或自定义值；d) 子域被接管（`evil.example.com`）若白名单用后缀匹配会被绕过。所以 `Origin` 要做**精确匹配**（协议+主机+端口），不要用 `endswith`/正则模糊匹配；对 `null` 和无 Origin 的客户端走独立鉴权，并在网关层保证 `Origin` 不被客户端伪造覆盖。

## 背诵要点
- WebSocket 握手是带 Cookie 的 HTTP GET，但不受 CORS 约束；不校验 `Origin` 即 CSWSH。
- `SameSite` 只能缓解（`None` 无效、旧客户端例外），服务端必须精确匹配 `Origin` 白名单。
- 高安全场景叠加握手 token/子协议令牌；无 `Origin` 的原生客户端走独立鉴权，不能默认放行。

## 复盘追问
- 恶意页面能读受害者聊天消息，如何用 CSWSH 与 CORS 不适用解释？怎么修？（Origin 精确白名单、token 鉴权）
- `SameSite=Lax` 为什么不能作为唯一防线？只校验 Origin 还有哪些盲区？（None/旧客户端、代理改写、`null` Origin、子域接管）
