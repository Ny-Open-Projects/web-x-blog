---
title: "[Q5679] transport.write 在关闭后静默丢弃数据"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5679 · transport.write 在关闭后静默丢弃数据

难度：P7 ｜ 标签：asyncio、Transport、abort、is_closing、背压

**问**：一个 WebSocket 广播服务对每个连接 `transport.write(frame)`，连接断了也不报错；监控发现"发送成功率 100%"，但客户端根本没收到。为什么 `write()` 对已关闭的 transport 不抛异常？`transport.close()` 和 `transport.abort()` 有什么区别？`await drain()` 返回是不是就代表对端收到了？`is_closing()` 应该在什么时候检查？

**答**：
结论：`transport.write(data)` 是**同步入队**：它把 data 追加到 transport 的发送缓冲，尽量立刻写 socket，写不完就留在缓冲里等可写事件，函数本身返回 `None`。它不保证送达，也不保证对端还活着；当 transport 已经 `close()/abort()`/`connection_lost` 后，多数实现只是把数据丢掉（或记一条 debug 日志），**不会抛异常**——这是为了不让"对端已断开"这种常态把业务代码炸掉。`close()` 是优雅关闭：停止接收新数据、把缓冲写完再发 FIN；`abort()` 是立即关闭：丢弃未发送缓冲、直接 RST/关闭，缓冲里的数据永久丢失。`drain()` 只等到"发送缓冲低于高水位"（Q5573），不代表对端应用层收到，更不代表对端处理了。

取舍：需要在关闭后停止写入，就在写之前检查 `transport.is_closing()`（或在 `connection_lost` 里把连接从广播表移除）；关键消息要有应用层 ACK/重试，不能把 `write()` 当可靠投递。要"尽量送达"用 `close()` + `await wait_closed()`；要"立刻断、丢弃积压"用 `abort()`。广播场景还应限流：慢客户端的发送缓冲会无限涨，`drain()` 的背压必须用上，否则内存先炸。

实战：事故形态是"连接池里混入大量半开连接，广播循环对它们 write 全部'成功'，CPU 空转、消息全丢"。下面用本地 server/client 复现：server 先 `write` 1000 字节并 `drain`，然后 `abort()`，再 `write` 1000 字节——不抛异常，客户端只收到前 1000 字节，且 `is_closing()` 前后都是 `True`。

```python
import asyncio

received = bytearray()
state = {}


async def handler(reader, writer):
    tr = writer.transport
    tr.write(b"A" * 1000)
    await writer.drain()
    tr.abort()                                  # 立即丢弃未发送缓冲并关闭
    state["is_closing"] = tr.is_closing()
    tr.write(b"B" * 1000)                       # 不抛异常，静默丢弃
    state["after_write_closing"] = tr.is_closing()
    writer.close()


async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    while True:
        chunk = await reader.read(65536)
        if not chunk:
            break
        received.extend(chunk)
    writer.close()
    await writer.wait_closed()
    server.close()
    await server.wait_closed()


asyncio.run(main())
print("客户端收到字节:", len(received), " 全是 A:", set(received) == {ord("A")})
print("abort 后 is_closing:", state["is_closing"], " 再写后:", state["after_write_closing"])
```

**追问一**：`close()` 之后还能 `write()` 吗？`wait_closed()` 等到什么？——`close()` 之后 transport 进入 closing 状态，新的 `write()` 通常被丢弃/警告；`wait_closed()` 等的是底层连接真正关闭（缓冲发完或 abort），不是"对端已读"。要确保数据发出，必须在 `close()` 前 `await drain()`，并接受"drain 只代表写入内核/SSL 缓冲，不代表对端应用收到"这一层语义。HTTP/2/gRPC 等还有自己的流控窗口，`drain` 与窗口是两回事。

**追问二**：为什么广播服务必须用 `drain()` 做背压？——`write()` 不阻塞，慢客户端会让 transport 发送缓冲持续增长（内存涨），而广播循环还在一路 `write`。正确模式是每连接一个有界队列 + 独立发送协程，`await drain()` 在缓冲高水位时暂停，队列满则丢帧/断开慢客户端（Q5670 的背压思路）。只检查 `is_closing()` 不够：连接还活着但读得慢，同样会吃内存。

## 背诵要点
- `transport.write()` 同步入队、不保证送达；关闭/abort 后写入被静默丢弃，不抛异常。
- `close()` 优雅发送完再 FIN；`abort()` 丢弃缓冲立即断；`drain()` 只等到缓冲低于高水位。
- 写前查 `is_closing()`、广播用有界队列 + `drain()` 背压，关键消息另加应用层 ACK。

## 复盘追问
- 广播服务"发送成功率 100%"但客户端没收到，如何用 transport 缓冲/静默丢弃解释？（write 语义、is_closing、半开连接）
- `drain()` 返回是否代表对端收到？为什么慢客户端仍会撑爆内存？（水位/背压、有界队列、应用层 ACK）
