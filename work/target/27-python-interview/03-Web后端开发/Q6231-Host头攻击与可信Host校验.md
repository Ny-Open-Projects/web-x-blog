---
title: "[Q6231] Host 头攻击与可信 Host 校验：从缓存投毒到链接注入"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6231 · Host 头攻击与可信 Host 校验：从缓存投毒到链接注入

难度：P6 ｜ 标签：Host 头攻击、可信 Host、缓存投毒、密码重置投毒、Django ALLOWED_HOSTS、Absolute URL、X-Forwarded-Host

**问**：服务端从哪里拿 Host 生成"绝对 URL"？攻击者伪造 `Host: evil.com` 会造成什么——密码重置投毒、缓存投毒、SEO 劫持的链路是什么？可信 Host 白名单该在哪一层校验、放行规则怎么写（端口/大小写/X-Forwarded-Host）？为什么"服务能跑"不等于"Host 校验已生效"？

**答**：
结论：Host 头是**客户端可任意控制的输入**，却被大量服务端逻辑当"我的域名"用——凡是拼绝对 URL 的地方（密码重置链接、邮件退订、OAuth 回调、sitemap、 canonical 标签、跳转 Location）都可能是注入点。攻击链：①**密码重置投毒**——攻击者请求 `/reset` 时带 `Host: evil.com`，服务端生成 `https://evil.com/reset?token=xxx` 发给受害者，受害者点开就把 token 送进攻击者日志；②**缓存投毒**——CDN/代理按 URL 缓存，页面内嵌 `Host` 生成的绝对链接被缓存后，**污染所有后续用户**的页面内容；③**SEO/劫持**——canonical 指向攻击者域，搜索引擎逐步把页面归属改写。防线是**可信 Host 白名单在入口处校验**：解析 Host 后与 allowlist 精确比对（协议+域名+可选端口语义统一），不匹配直接 400/444——Django 的 `ALLOWED_HOSTS`、Nginx 的 default_server 兜底、框架层的 middleware 三层里**至少一层必须强制**。三个易漏规则：①大小写与端口归一化（`Host: API.example.com:443`）；②`X-Forwarded-Host` 是**更危险的旁路**——有些代码先读 XFH，它比 Host 还好伪造，必须在白名单内接受而不是直接信任；③**多 Host 头**——HTTP 解析器差异导致部分代理会透传两个 Host，取值规则因解析器而异，网关层要显式拒绝重复头。

取舍：a) 校验层次：网关层（Nginx `server_name` + default 444）最彻底且保护所有后端；应用层 middleware 兜底框架内部生成 Absolute URL 的路径（Django ALLOWED_HOSTS 双保险）——两层都要，单层总有绕过；b) 白名单写法：精确域名列表优于通配符，`*.example.com` 会放行 `evil.example.com.attack.com` 式的解析歧义（子域枚举面自己评估）；c) 绝对 URL 生成：**不要从请求头拼**，从配置中心拿"对外基础域名"（BASE_URL）生成——Host 校验是防注入，BASE_URL 是根治"依赖不可信输入"；d) 缓存层：对含 Host 生成内容的页面开 Vary: Host，或直接不缓存 HTML——投毒的前提是缓存命中；e) 测试：把"伪造 Host/XFH 的用例"进契约测试（Q1624），防止未来重构把校验删了。

实战：事故形态是"渗透测试发现密码重置邮件可被投毒：请求带 `Host: attacker.io`，邮件链接变成 attacker.io/reset?token=…；根因是 Django 没配 ALLOWED_HOSTS（DEBUG=False 后框架不再兜底 Host，但业务代码自己用 request.get_host() 拼链接）——修复为 ALLOWED_HOSTS 强制 + 邮件链接改 BASE_URL 生成 + 网关 default_server 444 三层加固"。下面演示 Host 校验与投毒链路。

```python
# Host 头攻击与可信 Host 校验
TRUSTED_HOSTS = {"api.example.com", "www.example.com", "admin.example.com"}

def normalize_host(raw: str) -> str:
    """归一化: 去端口、小写、去尾点 (FQDN 写法)"""
    host = raw.strip().lower().rstrip(".")
    # 只保留默认端口内的域部分 (443/80 等默认端口不参与判定)
    if ":" in host and not host.startswith("["):           # IPv6 用方括号, 不切
        host = host.rsplit(":", 1)[0]
    return host

def check_host(headers: dict) -> tuple[bool, str]:
    """入口校验: Host 必须在白名单; X-Forwarded-Host 是旁路, 必须与 Host 一致才可信"""
    raw = headers.get("host", "")
    if headers.get("host", "").count(":") > 1 and not raw.startswith("["):
        return False, "multiple host headers rejected"     # 简化: 多值/歧义直接拒
    host = normalize_host(raw)
    if host not in TRUSTED_HOSTS:
        return False, f"untrusted host: {host!r}"
    xfh = headers.get("x-forwarded-host")
    if xfh and normalize_host(xfh) != host:
        return False, "x-forwarded-host mismatch"
    return True, host

print("[1] 正常请求: Host 在白名单, 放行")
for hdr in ({"host": "api.example.com"}, {"host": "API.example.com:443"},
            {"host": "api.example.com.", "x-forwarded-host": "api.example.com"}):
    ok, info = check_host(hdr)
    print(f"    {hdr} -> {'放行 ' + info if ok else '拒绝: ' + info}")

print("[2] 攻击面一: 伪造 Host -> 密码重置链接投毒")
bad = {"host": "attacker.io"}
ok, info = check_host(bad)
print(f"    {bad} -> {'拒绝: ' + info}")
print("    若不校验, 服务端会生成 https://attacker.io/reset?token=xxx 发给受害者")

print("[3] 攻击面二: X-Forwarded-Host 旁路 (比 Host 还好伪造)")
xfh_bad = {"host": "api.example.com", "x-forwarded-host": "attacker.io"}
ok, info = check_host(xfh_bad)
print(f"    {xfh_bad} -> {'拒绝: ' + info}")
print("    先读 XFH 再读 Host 的代码是投毒最短路径; XFH 只能由可信代理设置且需与 Host 核对")

print("[4] 攻击面三: 缓存投毒 -> 污染所有后续用户")
print("    页面内嵌 Host 生成的绝对链接 + CDN 按 URL 缓存 => 被污染内容进缓存")
print("    对策: Vary: Host 或 HTML 不缓存; 根治: 绝对链接从 BASE_URL 配置生成")

print("[5] 框架与网关双保险: Django ALLOWED_HOSTS / Nginx server_name + default_server 444")
print("    校验层次 >= 2 层; 白名单精确域名优先于通配符; 多 Host 头在网关显式拒绝")
print("[6] 回归: 伪造 Host/XFH 用例进契约测试, 防重构时把校验删掉")
```

**追问一**：Django 的 ALLOWED_HOSTS 是怎么工作的？为什么 DEBUG=False 时配错会直接 400，而 DEBUG=True 时框架却自动放行？—— `ALLOWED_HOSTS` 在框架层校验 `request.get_host()` 的结果：不在白名单的 Host 直接 SuspiciousOperation → 400 Bad Request，**所有依赖 get_host() 的下游逻辑（get_absolute_url、reverse 到绝对路径、CSRF 的 trusted origins 交叉检查）都被这层闸门保护**。DEBUG=True 时框架自动放行 `["localhost", "127.0.0.1", "[::1]"]` 并对其他值宽容——这是开发便利，但制造了"本地没问题、上线必炸/或上线忘了配"的经典部署陷阱：**DEBUG 切 False 后 ALLOWED_HOSTS 必须显式配置**，漏配就是全员 400（部署清单 Q803 的固定条目）。更深的坑：DEBUG=True + 公网可达（开发服务器暴露）时 Host 校验等于没有——攻击面与"框架替你兜底"的错觉是同一枚硬币的两面。

**追问二**：密码重置投毒与"重置 token 的一次性消费"（Q2453）是什么关系？为什么说 Host 校验防不了全部、还需要哪几层？—— 两者是不同层：Host 投毒攻击的是"**token 被送到哪**"（链接指向攻击者域），token 一次性消费防的是"**token 被用两次**"——投毒成功后受害者主动把 token 送上门，一次性消费根本拦不住（第一次使用就是攻击者）。所以防线必须前移：①Host/XFH 白名单（本文）阻断投毒源；②邮件链接一律从服务端配置的 BASE_URL 生成（不依赖请求上下文）——即使 Host 校验被绕过，链接域名也是固定值；③敏感令牌短时效 + 绑定 UA/IP 弱校验作为纵深；④对"点击重置链接的 Referer/到达路径"做异常检测（从攻击者域跳转过来的可标记）。安全工程的一般规律在这里复现：**单层防线挡一种攻击，投毒这类"借合法功能转运"的攻击要靠'输出域固定'根治**——校验是防线，配置化生成是免疫。

## 背诵要点
- Host 头是客户端可伪造输入；注入点 = 一切拼绝对 URL 的功能（重置邮件/OAuth 回调/canonical/sitemap）；攻击链 = 重置投毒/缓存投毒/SEO 劫持。
- 白名单校验 ≥2 层（网关 default_server 444 + 框架 ALLOWED_HOSTS）；归一化端口/大小写/尾点；X-Forwarded-Host 是旁路必须与 Host 核对。
- 根治 = 绝对 URL 从 BASE_URL 配置生成；HTML 不缓存或 Vary: Host 防投毒落地；伪造用例进契约测试防回归。

## 复盘追问
- 密码重置邮件链接被指向 attacker.io 怎么根治？（ALLOWED_HOSTS+网关校验挡注入；BASE_URL 生成链接免疫；一次性 token 防不了投毒）
- X-Forwarded-Host 为什么比 Host 更危险？（部分代码优先读 XFH 且默认信任；它只能由可信代理设置，应用侧必须与 Host 核对）
