---
title: [Q6101] Host 头注入与密码重置投毒事故
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6101 · Host 头注入与密码重置投毒事故复盘

> 难度:★★★★☆ | 标签:事故复盘, Host 头, 安全

**问**:用户反馈收到的"密码重置邮件"链接指向钓鱼域名，怎么发生的？

**答**:结论：服务端用请求的 `Host` 头拼绝对 URL（重置链接、sitemap、重定向），而 Host 是客户端可控输入——攻击者发一个 `Host: evil.com` 的请求，服务端生成的链接就指向 evil.com，这叫 Host 头投毒；配合缓存命中可把毒链接扩散给其他用户。根因是"把入站头当可信配置"。修复优先级：① 配置层显式注入公网 baseURL（环境变量/配置中心），链接生成绝不读 Host；② 框架层设 ALLOWED_HOSTS（Django）或 host 校验中间件，不在白名单直接 400；③ 反代层固定 `server_name` 并丢弃未知 Host。实战校验：`curl -H "Host: evil.com" https://site/reset` 应得到 400 或使用配置域名。取舍：允许 Host 换环境部署的灵活性 vs 安全，用白名单兼得。

```python
from urllib.parse import urljoin

# 事故形态：从请求头取 Host 拼链接
def build_reset_link_vuln(host_header: str, token: str) -> str:
    return urljoin(f"https://{host_header}", f"/reset?token={token}")

# 修复形态：白名单 + 配置 baseURL 双保险
ALLOWED = {"api.example.com", "www.example.com"}
BASE_URL = "https://api.example.com"

def build_reset_link_fixed(host_header: str | None, token: str) -> str:
    if host_header is not None and host_header not in ALLOWED:
        raise ValueError("非法 Host")        # 反代已兜一层，这里是纵深
    return urljoin(BASE_URL, f"/reset?token={token}")

print(build_reset_link_vuln("evil.com", "t1"))     # https://evil.com/reset?token=t1 投毒成功
print(build_reset_link_fixed("evil.com", "t1") if False else build_reset_link_fixed(None, "t1"))
try:
    build_reset_link_fixed("evil.com", "t1")
except ValueError as e:
    print("拦截:", e)

# X-Forwarded-Host 同样是入站输入，白名单逻辑一致（信任链见 Q2186）
```

**追问一层**:为什么 Behind 反向代理时 `Host` 可能是内部地址？`Host` 与 `X-Forwarded-Host` 的取舍？
**追二层**:缓存层（CDN）如何放大 Host 投毒？哪些响应头组合会造成"污染他人"？

**背诵要点**
- Host 是客户端输入，拼绝对 URL 前必须白名单或改用配置 baseURL。
- 修复三层：配置注入、框架 ALLOWED_HOSTS、反代固定 server_name。
- 复盘用 `curl -H "Host: evil.com"` 复测，X-Forwarded-Host 同罪同罚。

**复盘追问**
- 密码重置链接投毒的实际危害链如何评估？提示：token 绑定一次 + 链接短时效。
- 邮件模板之外，还有哪些"服务端拼 URL"的出口需要排查？提示：sitemap、redirect、OAuth 回调。
