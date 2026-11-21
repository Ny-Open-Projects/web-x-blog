---
title: [Q585] 异步 DNS 解析:getaddrinfo 并发与阻塞本质
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q585 · 异步 DNS 解析:getaddrinfo 并发与阻塞本质

> 难度:★★★☆ | 标签:DNS, asyncio, getaddrinfo

**问**:asyncio 里怎么并发解析大量域名?它真的是"异步"的吗?

**答**:`loop.getaddrinfo` 在默认事件循环里是把阻塞的 `socket.getaddrinfo` 丢进线程池执行的,所以并发靠的是线程池并行调用 libc 解析器,不是单线程 IO 复用。批量解析用 `asyncio.gather` 收集即可,吞吐受默认 executor 线程数(通常 min(32, cpu+4))限制,必要时换更大的 ThreadPoolExecutor。工程要点:解析结果自己做 TTL 缓存(getaddrinfo 本身通常不缓存);hostname 传 IP 字面量时 libc 快速返回不查 DNS;IPv6 环境下双栈解析可能拖慢,可指定 family=socket.AF_INET(注意 AF_INET 常量在 socket 模块,asyncio 里没有这个名字)。

```python
# file: code/02_并发与网络工程/q585_async_dns.py
import asyncio
import socket
import time

HOSTS = ["localhost"] * 8 + ["127.0.0.1"] * 8  # 本机可解析, 不依赖外网


async def resolve_all_sequential() -> None:
    loop = asyncio.get_running_loop()
    for host in HOSTS:
        await loop.getaddrinfo(host, 80, family=socket.AF_INET)


async def resolve_all_concurrent() -> None:
    loop = asyncio.get_running_loop()
    await asyncio.gather(
        *[loop.getaddrinfo(host, 80, family=socket.AF_INET) for host in HOSTS]
    )


async def inspect_result() -> None:
    loop = asyncio.get_running_loop()
    infos = await loop.getaddrinfo("localhost", 80, family=socket.AF_INET)
    print("getaddrinfo 返回结构示例:", infos[0])
    # (family, type, proto, canonname, sockaddr) — 建连接时直接喂给 open_connection


async def main() -> None:
    await inspect_result()
    t0 = time.perf_counter()
    await resolve_all_sequential()
    t_seq = time.perf_counter() - t0

    t0 = time.perf_counter()
    await resolve_all_concurrent()
    t_con = time.perf_counter() - t0
    print(f"串行 {len(HOSTS)} 次: {t_seq:.3f}s, 并发: {t_con:.3f}s")
    print("并发来自线程池中的并行 getaddrinfo, 而非单线程复用")


asyncio.run(main())
```

**追问**:1) 为什么解析 IP 字面量也要小心?——getaddrinfo 对 "127.0.0.1" 走快速路径,但带端口号的字符串或非法字面量仍会走到解析分支;热路径上应显式用 `family` + 数值化预处理。2) 异步 DNS 的本质?——asyncio 的 getaddrinfo 走线程池(run_in_executor),不是真异步;阻塞的是池线程不是循环,但池饱和会排队(Q599);真异步 DNS 要 aioredis 风格的专用解析库或 c-ares。3) 解析的工程优化?——TTL 缓存结果;并发预解析(Q585 本题);负缓存防解析风暴;上游 DNS 故障的降级(失败快、重试退避)。4) 生产陷阱?——以为 getaddrinfo 不阻塞;DNS 慢导致连接超时链放大(配 deadline,Q1285);每请求重复解析。

---
