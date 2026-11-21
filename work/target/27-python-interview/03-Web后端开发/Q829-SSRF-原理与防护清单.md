---
title: [Q829] SSRF 原理与防护清单
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q829 · SSRF 原理与防护清单

> 难度:★★★★ | 标签:SSRF, 安全

**问**:服务端根据用户传的 URL 拉取资源,会有什么风险?防护清单是什么?

**答**:SSRF:攻击者让服务器去请求**内网地址**——云元数据服务(169.254.169.254 拿凭证)、内部管理接口、Redis/数据库端口。防护清单:协议白名单(仅 http/https,禁 file/gopher/dict);**解析后的 IP 校验**(拒绝环回、私网、链路本地段);禁用或逐跳校验**重定向**(302 跳内网是经典绕过);DNS rebinding 防御——校验和连接用同一份解析结果;出网走独立代理并隔离权限。核心原则:校验发生在**连接的目标 IP**上,不是域名上。

```python
# file: code/03_Web后端开发/q829_ssrf_guard.py
import ipaddress
from urllib.parse import urlparse

BLOCKED = [
    ipaddress.ip_network(n) for n in (
        "127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12",
        "192.168.0.0/16", "169.254.0.0/16", "0.0.0.0/8",
    )
]

def is_safe_url(raw: str, resolved_ips: list) -> bool:
    if urlparse(raw).scheme not in ("http", "https"):
        return False                     # 协议白名单
    for s in resolved_ips:               # 用解析后的 IP 判定
        ip = ipaddress.ip_address(s)
        if any(ip in net for net in BLOCKED):
            return False
    return True

print("公网 URL:", is_safe_url("https://api.example.com/x", ["93.184.216.34"]))
print("元数据服务:", is_safe_url("http://internal.local/x", ["169.254.169.254"]))
print("file 协议:", is_safe_url("file:///etc/passwd", []))
```

**追问**:
- 为什么校验域名不够?——域名解析可指向内网,且存在 DNS rebinding:校验时解析公网、连接时换内网,必须在连接时对 IP 校验。
- 元数据服务还有什么缓解手段?——云厂商支持元数据 v2(要求先取 session token),从根上挡住直接 GET。
