---
title: "[Q6196] SECURE_SSL_REDIRECT 加健康探针：无限 301 循环"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6196 · SECURE_SSL_REDIRECT 加健康探针：无限 301 循环

难度：P7 ｜ 标签：Django、SECURE_SSL_REDIRECT、X-Forwarded-Proto、健康检查、TLS 卸载

**问**：TLS 在负载均衡上终止，Django 开了 `SECURE_SSL_REDIRECT=True`，上线后所有请求 301 到 https，浏览器跳过去还是 301，最终 `ERR_TOO_MANY_REDIRECTS`；同时 LB 的 HTTP 健康检查也全挂，实例被摘除。为什么 Django 认为请求不安全？`X-Forwarded-Proto` 该不该信？健康检查怎么排除？

**答**：
结论：TLS 在 LB 终止时，Django 收到的是一条**明文 HTTP** 连接，`request.is_secure()` 为 False；`SecurityMiddleware` 看到 `SECURE_SSL_REDIRECT=True` 就 301 到 https。浏览器按 301 跳到 https，LB 再解密转成 http 给 Django，Django 又看到"不安全"，于是再次 301——循环。解法是让 Django 知道"原始协议"：设置 `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")`，前提是 LB **一定**会覆写这个头、且应用端口不对公网暴露；否则客户端可以自己伪造 `X-Forwarded-Proto: https` 绕过重定向。

取舍：a) 只在"可信代理"后面启用该 header，并在网络层禁止直连应用端口（安全组/NetworkPolicy）；b) 健康检查路径要么走 https 探针，要么在 `SecurityMiddleware` 之前短路（自定义中间件对 `/healthz` 直接返回 200），不要用 `SECURE_REDIRECT_EXEMPT` 正则去匹配一堆路径——那是维护负担；c) `SECURE_SSL_REDIRECT` 与 HSTS 要分阶段上：先重定向观察，再开 `SECURE_HSTS_SECONDS`，否则一个配置错误会被浏览器缓存成"永久只能 https"；d) 内网服务间调用如果走 http，也会被 301，要么单独端口/域名，要么在网关层处理。

实战：事故形态是"新集群开了强制 HTTPS，忘了配 `SECURE_PROXY_SSL_HEADER`，首页 301 循环；同时 LB 用 HTTP 探 `/healthz`，拿到 301 判定失败，所有实例被摘，整站 502"。下面模拟"缺 XFP → 循环"、"有 XFP → 正常"、"健康检查被重定向"三种路径。

```python
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
EXEMPT_PATHS = {"/healthz"}          # 仅在中间件里短路，不依赖正则


def is_secure(headers):
    key, value = SECURE_PROXY_SSL_HEADER
    return headers.get(key) == value


def view(path, headers):
    if path in EXEMPT_PATHS:
        return 200, "ok"
    if SECURE_SSL_REDIRECT and not is_secure(headers):
        return 301, "https://api.example.com" + path
    return 200, "ok"


def follow(path, headers, max_hops=4):
    hops = 0
    while hops < max_hops:
        status, _ = view(path, headers)
        hops += 1
        if status == 200:
            return "ok", hops
    return "redirect-loop", hops


print("[1] 缺 X-Forwarded-Proto:", follow("/api/me", {}))
print("[2] LB 注入 X-Forwarded-Proto:", follow("/api/me", {"HTTP_X_FORWARDED_PROTO": "https"}))
print("[3] 健康检查已短路:", view("/healthz", {}))
print("[4] 伪造头直连应用（危险）:", view("/api/me", {"HTTP_X_FORWARDED_PROTO": "https"}))

# 修正：健康检查在中间件层短路，不参与重定向
def view_fixed(path, headers):
    if path.startswith("/healthz"):
        return 200, "ok"
    return view(path, headers)


print("[5] 修复后健康检查:", view_fixed("/healthz", {}))
print("[6] 修复后业务请求仍走重定向:", view_fixed("/api/me", {})[0])
```

**追问一**：`SECURE_PROXY_SSL_HEADER` 能被客户端伪造吗？—— 能，只要请求能直达应用。所以它必须与网络隔离配套：安全组只允许 LB 网段访问应用端口、LB 负责**删除并重写**客户端传来的 `X-Forwarded-Proto`（而不是追加）。如果 LB 只是透传，攻击者发 `X-Forwarded-Proto: https` 就能让 Django 认为连接安全，绕过重定向，甚至影响 `request.is_secure()` 相关的 cookie `Secure` 属性判断。

**追问二**：为什么健康检查不走 https？—— 很多 LB 的健康检查是"明文 + 内网"，配置 https 探针要额外信任内部 CA、还要处理 SNI，运维成本高；于是应用必须让健康路径"不参与业务安全策略"。这不是"给健康检查开后门"，而是把"存活/就绪"与"业务访问"分开：探针只回答"进程能不能服务"，不应被重定向、鉴权、限流影响。

## 背诵要点
- TLS 卸载后 Django 看到的是 http，`SECURE_SSL_REDIRECT` 会 301；没有 `X-Forwarded-Proto` 就是无限循环。
- `SECURE_PROXY_SSL_HEADER` 只在可信代理 + 应用端口不可直连时启用；LB 必须覆写该头。
- 健康检查在中间件层短路（或走 https 探针），不要用豁免正则堆路径。

## 复盘追问
- 开强制 HTTPS 后浏览器无限 301、LB 探针全挂，如何一步步定位？（is_secure、XFP、探针路径）
- 为什么"信任 X-Forwarded-Proto"必须和网络隔离绑定？（头可伪造 → 绕过重定向与 Secure cookie）
