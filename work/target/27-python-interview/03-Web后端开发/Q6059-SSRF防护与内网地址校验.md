---
title: [Q6059] SSRF 防护与内网地址校验
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6059 · SSRF 防护：用户提交 URL 的内网访问校验

> 难度:★★★★ | 标签:SSRF, ipaddress, DNS rebinding, 安全工程, webhook

**问**：一个"填 URL 就预览"的功能被安全团队通报 SSRF：攻击者填 `http://169.254.169.254/` 读到了云元数据（AK/SK）。SSRF 的攻击面有哪些？校验该在哪一层做？DNS rebinding 怎么防？

**答**：SSRF 的本质是**服务器替用户发请求**，攻击面按目标分四类：a) 云元数据 169.254.169.254（拿临时凭证，最高危）；b) 内网服务（10/172.16/192.168 网段的 Redis/管理后台，Redis 未授权写 shell 是经典链）；c) 本机回环（127.0.0.1、[::1]、0.0.0.0/8 的花式写法）；d) 协议面（gopher://、file://、dict:// 换协议绕过）。校验铁律：**校验"解析后的 IP"，不是 URL 字符串**——字符串黑名单（"169.254"）挡不住十进制 IP、八进制、`rebind.example.com` 解析到内网等变形。Python 落地：`urlparse` 收窄 scheme → `socket.getaddrinfo` 解析出**全部**地址 → `ipaddress` 逐个判 `is_private/is_loopback/is_link_local/is_reserved/is_multicast` → 拒绝任何内网地址。**DNS rebinding** 是进阶攻击：域名第一次解析返回公网 IP（过校验），TTL 过期后第二次解析返回内网 IP（发请求时）——防御是 **pin IP**：校验时解析到的 IP 直接用于连接（自定义 HTTPAdapter/connect 绑定 IP，Host 头保留原域名），并开启重定向**逐跳重校验**（requests 默认自动跟随重定向，每跳都是新的 SSRF 注入点）。纵深上再叠一层：给出网请求套独立出口（egress 代理/独立安全组），让"校验失误"也出不了网。

```python
# file: code/03_Web后端开发/q6059_ssrf.py
import ipaddress, socket as _s
from urllib.parse import urlparse

def check_url(raw):
    """返回 (放行与否, 原因)。校验解析后的 IP, 不看字符串。"""
    u = urlparse(raw)
    if u.scheme not in ("http", "https"):            # 收窄协议面: 拒 file/gopher/dict
        return False, f"scheme={u.scheme}"
    if not u.hostname:
        return False, "no-host"
    try:
        infos = _s.getaddrinfo(u.hostname, None)
    except OSError:
        return False, "dns-fail"
    seen = set()
    for fam, _, _, _, addr in infos:                 # 全部地址逐一校验
        ip = ipaddress.ip_address(addr[0])
        seen.add(str(ip))
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast):
            return False, f"内网地址 {ip}"
    return True, f"公网 {seen}"

for target in ["http://127.0.0.1:6379/",
               "http://169.254.169.254/latest/meta-data/",
               "http://10.0.0.5/",
               "file:///etc/passwd",
               "https://example.com/"]:
    ok, why = check_url(target)
    print(f"{target} -> {'放行' if ok else '拦截'} ({why})")

print("再挖一层: rebinding 要 pin IP 连接 + 重定向逐跳重校验 + egress 出口兜底")
# pin IP 实现: requests 自定义 adapter, 将 getaddrinfo 结果固定后连接, Host 头保留域名
```

**追问**：1) 为什么校验"全部"解析地址而不是第一个？——getaddrinfo 可返回多 A 记录，攻击者控制 DNS 时让第一条是公网、第二条是内网，只查第一条就是漏洞；`round-robin` 与轮询策略都会踩。2) 云上除了 IP 层还要做什么？——元数据服务开 V2（IMDSv2 要求 PUT 令牌头，SSRF 的 GET 无法预取令牌）、egress 安全组禁内网段、禁用 302 自动跟随或逐跳校验；三层里任何一层失效都不致命。3) webhook 接收"用户提供回调 URL"怎么设计才安全？——固定回调域名白名单 + 首次验证（owner 证明域名所有权）+ 出站走代理限定目标段；运行时仍按本题函数校验每跳。

## 背诵要点
- SSRF 校验"解析后 IP"而非 URL 字符串：getaddrinfo 全部地址逐一过 `is_private/is_loopback/is_link_local/is_reserved`；scheme 收窄拒 file/gopher。
- 云元数据 169.254.169.254 最高危：IMDSv2 PUT 令牌 + egress 安全组 + 应用层校验三层纵深。
- DNS rebinding：校验后二次解析换 IP——防御是 pin IP 连接 + Host 头保留 + 重定向逐跳重校验。

## 复盘追问
- 你们产品里有哪些"用户可控 URL"的功能（预览/webhook/拉取头像）？各自有出网校验吗？（提示：按功能盘点请求出口，标出无校验的）
- 出网流量有没有独立出口与审计？校验层失效时谁兜底？（提示：egress 代理 + 安全组禁内网 + 出网日志按目标 IP 审计，三层对账）
