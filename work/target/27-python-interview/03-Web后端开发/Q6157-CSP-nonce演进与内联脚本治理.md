---
title: "[Q6157] CSP nonce 演进与内联脚本治理"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6157 · CSP nonce 演进与内联脚本治理

难度：P6 ｜ 标签：CSP、nonce、XSS、安全头、版本演进

**问**：CSP 从 `unsafe-inline` 白名单时代到 nonce/hash 模式解决了什么？`script-src 'nonce-xxx'` 的 nonce 生成、注入与复用规则是什么？为什么 CSP 对"事件属性内联（onclick）"与"src 外链"的防护边界不同？Python 后端在模板渲染管线里怎么落地并渐进灰度（Report-Only → 强制）？

**答**：
结论：CSP 早期方案是域白名单（`script-src 'self' cdn.example.com`），但 `unsafe-inline` 与 JSONP/开放重定向会架空它——白名单域名下的任何脚本执行都被放行。**nonce 模式**（CSP2）改为"本次响应随机令牌"：响应头 `Content-Security-Policy: script-src 'nonce-R4nd0m'`，页面里每个合法 `<script nonce="R4nd0m">` 与令牌匹配才执行；攻击者注入的脚本没有 nonce，即使注入进 DOM 也不执行——防护从"信任来源"变为"信任本次响应的产物"。规则细节：nonce 必须**每响应随机**（≥128 bit，密码学随机，绝不能缓存复用——缓存页面的 nonce 复用等于白名单化）、必须加 `'strict-dynamic'` 才能覆盖第三方脚本动态注入加载（否则 script 注入 DOM 后再加载子脚本被拦）；事件属性（`onclick=...`）在 nonce 模式下**默认仍被禁**（`unsafe-hashes` 是受控例外），因为 nonce 无法保护行内属性。

取舍：落地难点全在存量改造：模板里散落的内联脚本、第三方 SDK（广告/统计）动态注入、以及**页面被 CDN/代理缓存**时 nonce 不可缓存——要么这些页面走 no-store，要么改用 hash 模式（内容固定的脚本用其摘要 `'sha256-...'`，可缓存）。灰度路径是标准三步：`Content-Security-Policy-Report-Only` 收违例报告（report-uri/csp-report）→ 修复全部合法路径 → 切强制头并保留上报观察。

实战：后端管线：中间件生成 `secrets.token_urlsafe(16)` 放进 request 上下文，模板引擎全局替换（如 Jinja 全局变量 `csp_nonce`），响应头与标签同源同值；对 API-only 服务 CSP 主要防 HTML 注入面，同样建议加 `object-src 'none'; base-uri 'none'; frame-ancestors 'none'` 三件套。

```python
import secrets
from jinja2 import Environment            # 基线：Jinja2 3.x；缺库降级用 str.format

def build_csp_header(nonce: str, report_only: bool = False) -> str:
    policy = (
        f"default-src 'self'; "
        f"script-src 'nonce-{nonce}' 'strict-dynamic' https:; "
        f"style-src 'self'; object-src 'none'; base-uri 'none'; "
        f"frame-ancestors 'none'; report-uri /csp-report"
    )
    return ("Content-Security-Policy-Report-Only" if report_only
            else "Content-Security-Policy"), policy

def render_page(template: str, nonce: str) -> str:
    env = Environment(autoescape=True)
    return env.from_string(template).render(csp_nonce=nonce)

nonce = secrets.token_urlsafe(16)          # 每响应随机 ≥128bit
tpl = ("<script nonce='{{ csp_nonce }}'>init();</script>"
       "<script>alert('injected without nonce');</script>")
name, policy = build_csp_header(nonce, report_only=True)   # 灰度第一步
print(name + ":", policy[:80] + "...")
html = render_page(tpl, nonce)
print("nonce script matches header nonce:", f"nonce='{nonce}'" in html or f'nonce="{nonce}"' in html)
print("injected script has nonce       :", "alert('injected" in html and f"nonce='{nonce}'" not in html.split("alert")[0])

# nonce 不可复用：连续两次请求令牌必须不同
n2 = secrets.token_urlsafe(16)
print("nonce rotates per response:", nonce != n2)

# hash 模式：内容固定的脚本可缓存（nonce 换 hash）
import hashlib, base64
fixed_js = b"init();"
digest = base64.b64encode(hashlib.sha256(fixed_js).digest()).decode()
print("hash directive:", f"script-src 'sha256-{digest}'")
```

**追问一**：`strict-dynamic` 为什么必须和 nonce 一起用、它放开了什么？——合法脚本运行后动态创建的 `<script src>`（第三方 SDK 的 loader）会继承信任；单用 nonce 时这些动态加载全被拦（接入率低的主因），单用 strict-dynamic 而无 nonce/hash 锚点则没有任何初始信任源。它同时**使旧白名单失效**（规范明确忽略并列的 host-source），防止新旧混用留下后门。

**追问二**：为什么 CDN 缓存页面与 nonce 天然冲突、hash 模式在什么条件下可行？——缓存的页面带着旧 nonce，新响应头换了 nonce，比对失败全部脚本被拦（整站白屏事故形态）；hash 模式的摘要是脚本内容的函数，与响应无关，可缓存——前提是脚本内容固定（构建产物带 hash 文件名的场景刚好匹配）。

## 背诵要点
- CSP2 nonce 模式：每响应密码学随机 ≥128bit、头与标签同源同值、禁缓存复用（复用=白名单化）。
- `strict-dynamic` 与 nonce 搭配覆盖第三方动态加载，且使并列 host 白名单失效；事件属性内联默认仍禁。
- 灰度三步：Report-Only 收违例 → 修复 → 强制；可缓存页面用 hash 模式替代 nonce。

## 复盘追问
- 灰度切强制后部分页面白屏，如何从 csp-report 快速归类是"动态加载缺失 strict-dynamic"还是"缓存 nonce 失配"？（违例报告的 directive 与 URL 分布，讨论缓存页面剔除策略）
- 为什么" nonce 每响应随机"与"页面进 CDN 缓存"二选一？给出架构判断框架。（可缓存内容用 hash/外链、动态个人化页面 no-store+nonce，讨论收益矩阵）
