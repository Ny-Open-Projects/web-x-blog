---
title: "[Q6148] CSRF 防护从 Token 到 SameSite 演进"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6148 · CSRF 防护从 Token 到 SameSite 演进

难度：P6 ｜ 标签：CSRF、SameSite、双提交 Cookie、安全演进

**问**：站点 Cookie 已设 `SameSite=Lax`，安全团队仍要求保留 CSRF token。CSRF 攻击在 SameSite 时代还成立吗？双层提交（double-submit）与同步器 token（synchronizer）怎么选？哪些请求形态是 Lax 保护不了的？

**答**：
结论：`SameSite=Lax` 只挡"**跨站请求带 Cookie 的部分形态**"——Lax 允许顶级导航 GET 带 Cookie，所以 `<a href>`/`window.location` 触发的 GET 仍会带上 Cookie；POST 表单跨站提交被 Lax 挡住，但攻击者可用"顶级 GET 导航 + 服务端把危险操作放在 GET"（错误实现）绕过。另外 SameSite 是**浏览器执行**的策略，老旧浏览器/非浏览器客户端（App 内嵌 WebView）支持参差——所以 token 仍是纵深防御层，两者互补：SameSite 在浏览器层把大部分跨站请求掐掉，token 在应用层对"服务端收到的每个变更请求"做来源验证。

取舍：同步器 token（服务端生成存 session、表单隐藏域回传比对）最强但要求会话存储与全表单改造；双提交 Cookie（token 同时放 Cookie 与请求头/表单，服务端比对两者相等）无状态、易落地，但要求站点无子域注入面（子域可写父域 Cookie 会伪造配对）；API 场景用自定义 header token（CORS 已限来源）+ 不用 Cookie 鉴权的纯 Bearer 天然免 CSRF。

实战：落地清单——① 变更类接口（POST/PUT/DELETE）强制 token，GET 保持只读（这是 Lax 契约的前提）；② Django 的 CsrfViewMiddleware 默认开启、Flask-WTF 显式启用，自研框架参考双提交；③ 豁免白名单（第三方 webhook 回调）必须"非 Cookie 鉴权"（签名校验）；④ 测试：用脚本模拟跨站表单提交断言 403。

```python
import hmac
import secrets

class CsrfGuard:
    """双提交 + 同步器混合演示：token 对比 + 来源校验"""

    def __init__(self):
        self.session_tokens: dict[str, str] = {}   # sid -> server-side token

    def issue(self, sid: str) -> str:
        tok = secrets.token_urlsafe(24)
        self.session_tokens[sid] = tok
        return tok                                 # 放入表单隐藏域 + Set-Cookie

    def verify(self, sid: str, submitted: str, cookie_token: str,
               origin: str | None, site_host: str = "shop.example") -> bool:
        if submitted != cookie_token:              # 双提交配对
            return False
        server = self.session_tokens.get(sid)
        if server is None or not hmac.compare_digest(server, submitted):  # 同步器比对
            return False
        if origin and not origin.endswith(f"https://{site_host}"):        # Origin 头兜底
            return False
        return True

guard = CsrfGuard()
sid = "sess-1"
tok = guard.issue(sid)

# 合法请求：表单 token == Cookie token == 服务端 token，Origin 同站
print("valid request:", guard.verify(sid, tok, tok, "https://shop.example/cart"))

# CSRF 攻击：攻击者站点提交的表单里 token 是自己伪造的（与服务端 token 不配对）
evil_tok = secrets.token_urlsafe(24)
print("csrf attempt  :", guard.verify(sid, evil_tok, evil_tok, "https://evil.example"))

# Origin 缺失的老客户端：仅剩 token 配对防线（Lax 也挡不住 GET 导航）
print("no-origin ok  :", guard.verify(sid, tok, tok, None))

# GET 只读契约被破坏时（危险操作放 GET），Lax 保护失效的演示说明：
print("rule: mutating endpoints must reject GET -- enforce in router layer")
```

**追问一**：`hmac.compare_digest` 为什么在这里重要？——token 比对若用 `==` 是逐字符短路比较，存在时序侧信道；恒时比较让比对耗时与内容无关，这是安全比对的标准姿势（用户密码校验同理）。

**追问二**：CORS 能替代 CSRF 防护吗？——不能：CORS 是"浏览器是否把响应交给 JS"的资源读取策略，简单请求（表单 POST）照样发出且响应不暴露给攻击者 JS；CSRF 的问题是"请求被执行"不是"响应被读"，两者互补不可替代。

**追问三**：SameSite=None + Secure 什么时候才需要？——跨站需要携带 Cookie 的场景（第三方支付跳回、iframe 嵌入的 SSO）；代价是放弃 SameSite 防线，此时 token 层必须顶上，并配合 Origin 校验。

## 背诵要点
- SameSite=Lax 挡跨站 POST 但允许顶级 GET 导航带 Cookie，且是浏览器层策略——token 仍是必要纵深层。
- 双提交（Cookie+表单配对）无状态易落地，前提无子域注入；同步器（服务端比对）最强；恒时比较防时序侧信道。
- 变更接口禁 GET 是 Lax 契约前提；webhook 豁免必须改签名鉴权，不能豁免 Cookie 鉴权。

## 复盘追问
- 站点有多个子域（a.example 写 Cookie 给 shop.example），双提交如何被伪造、怎么加固？（子域注入配对 Cookie；迁移到同步器 token + `__Host-` 前缀 Cookie，讨论与 Q6130 前缀语义的衔接）
- 灰度启用 CSRF 中间件时老客户端（无 Origin 的原生 WebView）被误杀，兼容策略怎么定？（token 配对为主要判据、Origin 缺失降级放行并打标观测，讨论放宽窗口与回滚指标）
