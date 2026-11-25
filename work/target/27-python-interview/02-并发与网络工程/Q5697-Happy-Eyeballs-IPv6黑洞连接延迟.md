---
title: "[Q5697] Happy Eyeballs：IPv6 黑洞让连接建立慢 5 秒"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5697 · Happy Eyeballs：IPv6 黑洞让连接建立慢 5 秒

难度：P7 ｜ 标签：asyncio、happy_eyeballs_delay、getaddrinfo、IPv6、连接延迟

**问**：同一域名，容器里 `curl` 秒开，Python asyncio 客户端却每次卡 5 秒才连上。抓包发现客户端先试了 AAAA 记录里的 IPv6 地址，超时后才回退 IPv4。`asyncio.open_connection` 不是会自己尝试多个地址吗？`happy_eyeballs_delay` 是什么？默认不传会怎样？

**答**：
结论：`getaddrinfo` 返回的地址列表是"按优先级排序"的（通常 AAAA 在前），`create_connection` 默认**串行**尝试：第一个地址连不上就等它超时（受内核 `connect` 超时或 `syn` 重试影响，常见 5～20 秒），再试下一个。如果环境通告了 IPv6 但没有实际路由（典型容器/双栈配置错误），第一个 AAAA 就是个"黑洞"，整个连接被拖慢。3.8 起 `create_connection` 支持 `happy_eyeballs_delay`（RFC 8305）：先连第一个地址，若 `delay` 秒内没成功就**并行**发起下一个族的连接，谁先成功用谁。

取舍：a) 生产客户端显式传 `happy_eyeballs_delay=0.25`（`open_connection` 同样支持），把"协议族回退"从秒级降到百毫秒级；b) 更彻底的是修网络：容器里没有 IPv6 路由就不要通告 AAAA（`AI_ADDRCONFIG` 或 DNS 侧治理），否则每个新连接都交一次"黑洞税"；c) 连接池复用能掩盖问题，但冷启动/扩缩容时仍会集中爆发；d) 不要用 `socket.create_connection`（同步）在协程里，它没有 happy eyeballs 的并行回退，还阻塞事件循环。

实战：事故形态是"服务扩容后新 Pod 首次请求 P99 飙到 5s，稳定后又恢复——因为连接池建好了；滚动发布期间每个新实例都要付一次 IPv6 黑洞的代价"。下面演示 `getaddrinfo` 返回的协议族、带 `happy_eyeballs_delay` 的连接耗时，以及不传参数时行为差异。注意本机 `localhost` 只解析出 A 记录，双栈环境才会看到 AAAA 排在前面的情况。

```python
import asyncio
import socket
import time


async def main():
    server = await asyncio.start_server(lambda r, w: w.close(), "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    loop = asyncio.get_running_loop()

    infos = await loop.getaddrinfo("localhost", port, type=socket.SOCK_STREAM)
    families = sorted({info[0].name for info in infos})
    print("[1] getaddrinfo 返回的协议族:", families)
    print("[2] 地址顺序:", [info[4][0] for info in infos])

    t0 = time.monotonic()
    reader, writer = await asyncio.open_connection("localhost", port)
    print("[3] 默认连接耗时: %.3fs" % (time.monotonic() - t0))
    writer.close()
    await writer.wait_closed()

    t0 = time.monotonic()
    reader, writer = await asyncio.open_connection(
        "localhost", port, happy_eyeballs_delay=0.25, interleave=1
    )
    print("[4] Happy Eyeballs 连接耗时: %.3fs" % (time.monotonic() - t0))
    writer.close()
    await writer.wait_closed()

    server.close()
    await server.wait_closed()
    print("[5] delay 越小越激进：0.25s 后即并行尝试下一族")


asyncio.run(main())
```

**追问一**：`happy_eyeballs_delay=None` 与不传有区别吗？—— 没有，`None` 就是关闭（默认），走"串行尝试所有地址"。传 `0` 也不是"立刻并行"的魔法值，语义上要求正数延迟；实现里 `0` 会被当作"立即启动下一个"，可能变成对 DNS 结果的全量并发，反而放大握手风暴。工程上 `0.25` 是 RFC 8305 推荐的起点。

**追问二**：为什么 `curl` 快、Python 慢？—— `curl` 默认启用 Happy Eyeballs（`--happy-eyeballs-timeout-ms` 默认 200ms），而 `asyncio.open_connection` 默认关闭，Go 的 `net.Dialer` 也是默认开启（300ms）。这不是 Python "性能差"，而是默认策略不同：标准库选择保守（不额外建连），把选择权交给应用。跨语言对比连接延迟时，先确认双方的 Eyeballs 配置，否则会得出错误结论。

## 背诵要点
- `getaddrinfo` 常把 AAAA 排在前面，默认串行连接会吃满第一个地址的超时（可达数秒）。
- `happy_eyeballs_delay=0.25`（RFC 8305）让协议族回退并行化，`open_connection`/`create_connection` 都支持。
- 根治是网络侧不通告不可达的 AAAA；连接池只是掩盖冷启动问题。

## 复盘追问
- 新 Pod 首请求 5s、稳定后恢复正常，如何定位到 IPv6 黑洞？（getaddrinfo 顺序、connect 超时、池预热）
- Happy Eyeballs 的 delay 设太小有什么副作用？（并发握手放大、服务端 SYN 压力）
