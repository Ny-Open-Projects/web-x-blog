---
title: [Q5508] HTTP/2 多路复用下的队头阻塞与 Python 客户端选型
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5508 · HTTP/2 多路复用下的队头阻塞与 Python 客户端选型

> 难度:★★★ | 标签:HTTP/2, 队头阻塞, 客户端选型

**问**：HTTP/2 的多路复用解决了 HTTP/1.1 的什么队头阻塞，又留下了什么？TCP 层丢包为什么会让所有 stream 卡住？Python 侧 httpx/httpcore、aiohttp、h2、grpc 对 HTTP/2 的支持矩阵怎么选？连接数该怎么配？

**答**：结论：HTTP/2 把 HTTP/1.1 的**应用层队头阻塞**解决了——一个连接上多个 stream 并行，慢响应不再堵住后面的请求（1.1 的 keep-alive 管线化必须按序返回）；但**传输层队头阻塞仍在**：所有 stream 共享一条 TCP 字节流，任何丢包触发重传+拥塞窗口收缩，窗口没恢复期间**全部 stream 一起等**——这是 HTTP/3（QUIC，流独立可靠传输）存在的理由。Python 选型矩阵：a) **httpx**（httpcore 后端）：HTTP/1.1 默认，HTTP/2 要 `httpx.HTTP2Transport`/`http2=True` 依赖 `h2` 包，API 统一、同步异步双模式，做客户端聚合首选；b) **aiohttp**：不直接支持 h2 客户端（服务端部分支持），快但协议栈窄；c) **裸 h2**：自己管连接状态机与 stream，适合做代理/网关这类协议级工作；d) **gRPC**：天然 HTTP/2，streaming 场景直接选它而不是自己拼 h2。连接数策略：HTTP/1.1 靠连接池扩大并发（每主机 6-8 条），HTTP/2 一条连接 + stream 并发即可，但要检查 **SETTINGS_MAX_CONCURRENT_STREAMS**（对端常限 100-128）并配合 `http2_keepalive`；一条连接也意味着单点——丢包重传影响面比 1.1 大，高丢包链路反而要「少复用、多连接」或上 HTTP/3。实战事故模式：客户端从 1.1 连接池切到 h2 单连接后，某上游抖动导致**所有下游请求同时超时**——这就是 TCP 队头阻塞从「每连接」升级成「每主机」的放大效应。

```python
# 基线:httpx[http2]==0.27+ (pip install "httpx[http2]")。
# 缺库降级:去 http2=True 用 HTTP/1.1 连接池并发,行为差异见注释。
import asyncio

async def fetch_all(urls: list[str]) -> list[str]:
    try:
        import httpx
        async with httpx.AsyncClient(http2=True, timeout=5) as client:
            # 单连接多 stream 并行;受对端 MAX_CONCURRENT_STREAMS 限制
            resp = await client.get(urls[0])
            print("http version:", resp.http_version)   # HTTP/2 需服务端支持
    except ImportError:
        # 降级:HTTP/1.1 用连接池并发弥补多路复用
        import httpx
        limits = httpx.Limits(max_connections=16)
        async with httpx.AsyncClient(limits=limits, timeout=5) as client:
            resp = await client.get(urls[0])
            print("http version:", resp.http_version)
    return [urls[0]]

async def main() -> None:
    # 本地无 h2 服务时仅演示连接建立;真实对比请对支持 h2 的端点跑
    await fetch_all(["https://example.com"])

asyncio.run(main())
```

**追问**：
1) 为什么 HTTP/2 服务端反而可能更慢？——队头阻塞从「请求级」变「连接级」：丢包时 1.1 只卡那条连接上的请求，h2 卡整个主机的全部请求；高丢包（跨境、弱网）环境 h2 单连接是负优化，要调大连接数或协商 HTTP/3。
2) 怎么探测上游支不支持 h2？——`curl -sI --http2 -o /dev/null -w '%{http_version}'` 或 httpx 响应 `resp.http_version`；还要看 ALPN 协商结果与 SETTINGS 帧的 MAX_CONCURRENT_STREAMS，两个数决定实际并发能力。
3) gRPC 与 REST over h2 怎么分工？——内部服务间高频调用、需要双向流/级联取消 → gRPC（协议层原生管理 stream、超时以 header 传递）；对外 API 与浏览器 → REST/JSON（h2 只当传输优化），别为了 h2 把对外协议也换成 gRPC-Web。
