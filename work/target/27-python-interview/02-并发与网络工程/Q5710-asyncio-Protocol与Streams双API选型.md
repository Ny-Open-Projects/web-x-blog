---
title: "[Q5710] asyncio 双 API：Protocol/Transport 与 Streams 怎么选"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5710 · asyncio 双 API：Protocol/Transport 与 Streams 怎么选

难度：P7 ｜ 标签：asyncio.Protocol、StreamReader、StreamWriter、回调用、帧解析、背压

**问**：同一个 echo 服务，`asyncio.start_server` + `reader.readline()` 一套，`loop.create_server` + `Protocol.data_received` 又一套，都能跑。Streams 和 Protocol/Transport 两套 API 的分层关系是什么？各自把什么控制权交给了你？为什么高性能帧解析器（长连接网关、代理）几乎都用 Protocol 写？半包缓冲在两套 API 里分别由谁负责？

**答**：
结论：Streams 是 Protocol/Transport 之上的**封装层**：`StreamReader` 内置缓冲与 `readline/readuntil` 等便捷方法，`await` 风格好写好读，代价是默认 64KB 行长限制（超限抛 `LimitOverrunError`）、每读一次要过一层封装、背压要显式 `drain()`。Protocol/Transport 是**回调式底层**：`data_received` 直接收到原始字节流，缓冲与帧解析（半包聚合、粘包拆分）完全由你自己实现，`transport.write` 是投递无阻塞（写缓冲满了有 `pause_writing` 回调通知），没有 read 限制——这正是高性能网关选它的原因：少一层封装、按自己的帧协议精确控制内存与解析状态机。

取舍：a) 请求-响应型、行/分隔符协议、开发效率优先：Streams（`start_server` 一行起服务）；b) 自定义二进制协议、万级长连接、需要精确背压与零拷贝（`memoryview` + `write`）：Protocol；c) 两套可混用：`loop.connect_read_pipe`/底层 fd 可以各自包装，同一进程内不同连接用不同 API 完全合法；d) Streams 的 `drain()` 是唯一背压点，忘了调 `drain()` 就会把内核写缓冲和 Python 侧缓冲一起堆满，Protocol 则用 `pause_writing/resume_writing` 回调强制你面对水位；e) 无论哪套，半包缓冲都要自己处理帧边界——Streams 的 `readline` 帮你处理了 `\n` 分帧，但自定义帧协议它无能为力。

实战：事故形态是"长连接网关用 Streams `readline` 接自定义帧，某客户端发出 128KB 的超长行（帧里没有换行），`LimitOverrunError` 未处理，连接被读协程异常静默断开，重连风暴放大；迁移到 Protocol + 手写缓冲状态机，帧长度上限自定（1MB）、超限主动踢连接并打审计日志"。下面两套 API 各实现一个 echo，验证行为等价。

```python
import asyncio


class ProtoEcho(asyncio.Protocol):
    def __init__(self, peers):
        self.peers = peers
        self.buf = b""
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        self.peers.add(self)

    def data_received(self, data):
        self.buf += data
        while b"\n" in self.buf:
            line, self.buf = self.buf.split(b"\n", 1)
            self.transport.write(line + b"\n")

    def connection_lost(self, exc):
        self.peers.discard(self)


async def stream_echo(reader, writer):
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            writer.write(data)
            await writer.drain()
    finally:
        writer.close()


async def probe(port):
    r, w = await asyncio.open_connection("127.0.0.1", port)
    w.write(b"hi\n")
    await w.drain()
    resp = await asyncio.wait_for(r.readline(), timeout=2)
    w.close()
    try:
        await w.wait_closed()
    except Exception:
        pass
    return resp


async def main():
    peers = set()
    s1 = await asyncio.start_server(stream_echo, "127.0.0.1", 0)
    s2 = await asyncio.get_running_loop().create_server(
        lambda: ProtoEcho(peers), "127.0.0.1", 0
    )
    r1 = await probe(s1.sockets[0].getsockname()[1])
    r2 = await probe(s2.sockets[0].getsockname()[1])
    print("[1] Streams 版回显:", r1)
    print("[2] Protocol 版回显:", r2)
    s1.close()
    await s1.wait_closed()
    s2.close()
    await s2.wait_closed()


asyncio.run(main())
```

**追问一**：为什么高并发长连接下 Protocol 的内存账更好？—— Streams 每个连接固定挂一对 StreamReader/Writer，内部缓冲按需增长但封装层额外对象多（buffer 对象、异常包装、drain 状态）；Protocol 自己管理 `buf`，可以按帧协议预分配、用 `memoryview` 零拷贝切帧、超限立即丢弃——"每连接常驻内存"从封装层的隐式预算变成状态机的显式预算。万级连接时这两者的差距是 GB 级 vs MB 级。另外 Streams 的 `readline` 每次调用要经过封装层的状态查询，Protocol 的 `data_received` 是一次回调直达解析器。

**追问二**：Streams 的 `drain()` 和 Protocol 的 `pause_writing` 分别怎么表达背压？—— `drain()` 是**拉模式**：写协程主动询问"缓冲高水位了吗"，是则挂起等待；调用与否由你决定，忘了就无背压。`pause_writing` 是**推模式**：transport 写缓冲越过高水位（默认 64KB）时框架主动回调，你可以在此停止投递任务或切换到排队；`resume_writing` 在低于低水位时恢复。框架级保障是 `transport.write` 永远不阻塞但会无限堆缓冲——所以两套 API 里背压都不是白给的：Streams 靠纪律（记得 drain），Protocol 靠状态机（在 pause_writing 里接住）。真正可靠的写法是两者都用：Protocol + 应用层发送队列 + pause/resume 驱动。

## 背诵要点
- Streams 是 Protocol/Transport 的封装：await 易用、`readline` 内置分帧但有 64KB 行限；Protocol 回调直达、半包缓冲自己写。
- 高并发长连接/自定义二进制帧选 Protocol：省封装、显式内存预算、`pause_writing` 推式背压；`drain()` 是拉式、靠自觉。
- `transport.write` 永不阻塞但缓冲会无限堆——两套 API 的背压都必须显式接住。

## 复盘追问
- 客户端发 128KB 超长行把 Streams 版连接搞断了，根因与迁移方案？（readline 64KB 上限 LimitOverrunError；Protocol 自定义帧限与踢除）
- 两个 echo 服务行为一样，生产选型的决定因素是什么？（帧协议复杂度、连接量级、背压与内存控制精度）
