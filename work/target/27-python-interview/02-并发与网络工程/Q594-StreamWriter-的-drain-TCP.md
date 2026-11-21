---
title: [Q594] StreamWriter 的 drain:TCP 层的背压
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q594 · StreamWriter 的 drain:TCP 层的背压

> 难度:★★★★ | 标签:drain, asyncio, TCP 背压

**问**:asyncio 里 writer.write 不是立即发送,那缓冲区爆了怎么办?drain 到底在等什么?

**答**:write 只是把数据放进传输层写缓冲,由事件循环异步刷到 socket;如果对端读得慢,内核发送缓冲和 Python 写缓冲都会积压。`await writer.drain()` 在缓冲区超过高水位(`set_write_buffer_limits`)时挂起,降到低水位以下才返回——这就是 asyncio 给你的 TCP 背压阀门:push 大文件时每次 write 后 drain,客户端不读你的发送速率就自动降下来。不 drain 的后果是内存里缓冲无限增长,大文件传输必须配对使用。写完最后一块还要 `writer.close()` + `wait_closed()` 收尾。

```python
# file: code/02_并发与网络工程/q594_drain.py
import asyncio


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    transport = writer.transport
    transport.set_write_buffer_limits(high=2048, low=1024)  # 观察背压阈值
    try:
        for i in range(8):
            writer.write(f"chunk-{i}-".encode())
            buffered = transport.get_write_buffer_size()
            await writer.drain()  # 客户端读得慢时, 这里挂起
            print(f"服务端发出 chunk {i}, 写前缓冲 {buffered} 字节")
            await asyncio.sleep(0.02)
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def slow_client(port: int) -> None:
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    for i in range(8):
        await asyncio.sleep(0.1)  # 故意慢读: 触发服务端 drain 挂起
        data = await reader.read(100)
        print("客户端收到:", data.decode())
    writer.close()
    await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    await slow_client(port)
    server.close()
    await server.wait_closed()


asyncio.run(main())
```

**追问**:1) get_write_buffer_size 一直涨说明什么?——对端不读而你没 drain,数据全堆在用户态缓冲里;修复是每次 write 后 await drain,并检查高水位设置是否合理(默认 64KB)。2) drain 的语义?——「写缓冲超过高水位时挂起,降回低水位恢复」;它不是「数据已发出」,而是「缓冲可控」;漏 drain = 放弃 TCP 层背压。3) 与协议层的配合?——pause_writing/resume_writing 协议回调是 drain 的底层;写大文件分块 write+drain;限流窗口与水位联动(Q593)。4) 生产陷阱?——大响应一次 write(OOM 面);drain 在 no-await 回调里没法用(协议层用 pause);把「write 返回」当「对端收到」。

---
