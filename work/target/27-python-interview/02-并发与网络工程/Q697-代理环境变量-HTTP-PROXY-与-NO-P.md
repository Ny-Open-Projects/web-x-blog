---
title: [Q697] 代理环境变量:HTTP_PROXY 与 NO_PROXY 的语义
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q697 · 代理环境变量:HTTP_PROXY 与 NO_PROXY 的语义

> 难度:★★☆ | 标签:环境变量, NO_PROXY, urllib

**问**:HTTP_PROXY/NO_PROXY 的解析规则是什么?为什么"internal:8080"在 NO_PROXY 里行为有坑?

**答**:HTTP_PROXY/HTTPS_PROXY 定义代理 URL(注意 HTTPS_PROXY 大写优先,小写 http_proxy 在 CGI 环境有安全歧义),ALL_PROXY 兜底。NO_PROXY 是"例外清单",主流实现语义:逗号分隔;条目可以是主机名、.domain 后缀(匹配子域)、IP、CIDR(部分实现支持);带端口条目只匹配该端口——但"是否带端口匹配所有端口"各库实现不一致,历史上 requests/http.client 都踩过坑。防坑实践:内部域名统一用规范后缀形式(.svc.cluster.local),不依赖端口匹配;程序启动时打印 getproxies() 结果便于排障。

```python
# file: code/02_并发与网络工程/q697_proxy_env.py
import os
import urllib.request


def matches_no_proxy(host: str, port: int, no_proxy: str,
                     port_sensitive: bool = True) -> bool:
    """复刻 http.client 的 NO_PROXY 语义 (含端口敏感行为)。"""
    host = (host or "").lower()
    for entry in no_proxy.split(","):
        entry = entry.strip().lower()
        if not entry:
            continue
        if ":" in entry:  # 带端口: 仅匹配该端口
            ehost, eport = entry.rsplit(":", 1)
            if port_sensitive and str(port) != eport:
                continue
            entry_host = ehost
        else:
            entry_host = entry
        entry_host = entry_host.lstrip(".")
        if host == entry_host or host.endswith("." + entry_host):
            return True
        if entry_host == "*":  # 全部直连
            return True
    return False


if __name__ == "__main__":
    os.environ.update({
        "HTTP_PROXY": "http://proxy:3128",
        "HTTPS_PROXY": "http://proxy:3128",
        "NO_PROXY": "localhost,127.0.0.1,.internal,repo.corp:8080",
    })
    print("getproxies():", urllib.request.getproxies())
    print("\nNO_PROXY 匹配判定:")
    cases = [
        ("localhost", 80, True),
        ("db.prod.internal", 5432, True),     # .internal 后缀
        ("notinternal.example", 80, False),   # 后缀陷阱: 须是 .internal 子域
        ("repo.corp", 8080, True),            # 带端口条目命中
        ("repo.corp", 443, False),            # 端口不符 → 走代理
        ("127.0.0.1", 80, True),
    ]
    for host, port, expect in cases:
        got = matches_no_proxy(host, port, os.environ["NO_PROXY"])
        mark = "OK " if got == expect else "FAIL"
        print(f"  [{mark}] {host}:{port} → direct={got}")
        assert got == expect

    print("\n端口条目注意: 'repo.corp:8080' 只影响 8080 端口, 443 仍走代理")
    print("建议: 内网域名一律用后缀形式 (.internal), 避免依赖端口语义")
```

**追问**:1) urllib 对大小写 http_proxy 的处理?——getproxies_environment() 优先小写(POSIX 习惯)但 CGI 环境下小写 http_proxy 会被跳过(防请求走私);Windows 上读取注册表代理;程序内设置时直接改 os.environ 再取。2) 端口匹配的实现差异怎么防?——「带端口条目只匹配该端口」主流一致,但「不带端口是否匹配所有端口」各库历史行为不一致;防坑:内部域名用规范后缀(.svc.cluster.local)不带端口,不做端口级例外。3) 大小写与 CGI 歧义的根源?——CGI 环境下大写 HTTP_PROXY 会被当客户端伪造头,urllib 特意跳过;POSIX 习惯小写;Windows 读注册表;跨平台代码统一显式设 os.environ+getproxies() 验证。4) 生产陷阱?——NO_PROXY 写 host:8080 期望覆盖同主机全部端口(语义理解错);CIDR 条目部分库不支持,内网网段漏例外;容器镜像里继承的全局代理变量让不需要代理的组件全部绕行。

---
