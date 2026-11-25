---
title: [Q5612] TLS SNI 缺失校验失败事故
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5612 · TLS SNI 缺失校验失败事故

> 难度:★★★★☆ | 标签:事故复盘, TLS, SNI

**问**:同一台网关后面用 SNI 挂了多个域名的证书。服务迁移后客户端报 `certificate verify failed: Hostname mismatch`，拿到的是别的域名的证书。SNI 是什么？Python 客户端什么写法会把它弄丢，怎么修？

**答**:结论：SNI（Server Name Indication）是 TLS ClientHello 里的扩展，客户端把"我要访问的域名"明文带给服务端，服务端据此**挑选对应域名的证书**——没有 SNI（或 SNI 与校验主机名不一致）时，共享网关只会返回默认证书，客户端按目标主机名校验自然失败。事故的三类根源：a) 客户端**按 IP 连接**再自己配 Host 头——TLS 层没有主机名，SNI 为空，拿到默认证书；b) 自建 socket 包装时 `ctx.wrap_socket(sock, server_hostname=...)` 忘传 `server_hostname`；c) 经代理 CONNECT 隧道时把 `server_hostname` 传成了代理地址而非目标域名。修复姿势：按域名连接（DNS 层解析，不直连 IP）；需要"IP 直连 + 证书校验"时显式传 `server_hostname=目标域名`；另一个常被忽视的点是 **SNI 是明文**——内网里它暴露访问目标，敏感链路要 ECH（Encrypted Client Hello）或内网直接用 IP + pinning。取舍：`ssl.SSLContext` 默认 `check_hostname=True` 且连接带主机名时自动发 SNI，"能连上"不等于"发对了 SNI"，排查时用 `openssl s_client -servername` 或抓 ClientHello 验证。

```python
import socket, ssl, sys

host, port = "www.python.org", 443

# 1) 标准姿势：create_default_context + 域名连接，SNI 自动携带
ctx = ssl.create_default_context()
try:
    with socket.create_connection((host, port), timeout=10) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as tls:
            cert = tls.getpeercert()
            print("对端证书主体:", dict(x[0] for x in cert["subject"]).get("commonName"))
            print("TLS 版本:", tls.version())
except OSError as e:
    # 环境缺根证书/网络受限时降级打印，不影响后续演示
    print("标准姿势握手失败（环境问题）:", type(e).__name__, str(e)[:80])

# 2) 事故重演：按 IP 连接且不传 server_hostname → 拿到错误/默认证书
ip = socket.gethostbyname(host)
try:
    with socket.create_connection((ip, port), timeout=10) as sock:
        no_sni = ctx.wrap_socket(sock)                    # 无 server_hostname
        print("不该成功:", no_sni.getpeercert())
except (ssl.SSLCertVerificationError, ValueError) as e:
    # 默认 ctx 下：无 server_hostname 先在客户端侧拒绝（check_hostname requires...）；
    # 若关掉校验，则会在服务端侧拿到错误的默认证书
    print("SNI 缺失被拦:", type(e).__name__, str(e)[:80])

# 3) 正确的"IP 直连 + 域名校验"：显式补 server_hostname
try:
    with socket.create_connection((ip, port), timeout=10) as sock:
        tls = ctx.wrap_socket(sock, server_hostname=host)
        print("IP 直连但 SNI 正确 → 校验通过:", tls.version())
except OSError as e:
    print("IP 直连失败（环境网络受限可忽略）:", type(e).__name__)

# 4) 观测侧：本机无 openssl 也能看 ClientHello 是否带 SNI —— 用 s_client 命令
#    openssl s_client -connect host:443 -servername host   <- 带 SNI
#    openssl s_client -connect host:443                    <- 不带，比对返回证书
print("排查命令对照: openssl s_client -connect {h}:{p} [-servername {h}]".format(h=host, p=port))
```

**追问一层**:`ssl.SSLContext` 什么时候会自动带 SNI？`server_hostname` 与 `check_hostname` 校验的对象是什么关系——SNI 决定服务端发哪张证书，谁决定客户端信不信它？
**追二层**:SNI 明文带来的隐私与合规问题在监管侧怎么落地？Python 的 ssl 栈对 ECH 的支持现状如何，短期内的替代方案是什么？

**背诵要点**
- SNI 是 ClientHello 里的明文域名扩展，共享网关靠它选证书；缺失/不一致 → 返回默认证书 → Hostname mismatch。
- 按域名连接时 ssl 自动发 SNI；IP 直连必须显式 `wrap_socket(..., server_hostname=域名)`。
- 排查用 `openssl s_client -servername` 对比有/无 SNI 的返回证书。

**复盘追问**
- 迁移事故里"拿错证书"但网关日志显示配置无误，中间差了哪一跳？提示：LB/代理把 SNI 丢弃或改写（如按 IP upstream 转发），逐跳核对 ClientHello。
- 内网服务之间要不要也全走域名 + SNI？取舍是什么？提示：内网可用 mTLS + pinning 省公网证书治理，但域名化便于网关路由。
