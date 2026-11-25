---
title: "[Q5763] BufferedProtocol 的零拷贝接收：get_buffer 与 buffer_updated 契约"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5763 · BufferedProtocol 的零拷贝接收：get_buffer 与 buffer_updated 契约

难度：P7 ｜ 标签：asyncio、BufferedProtocol、零拷贝、get_buffer、buffer_updated、流式解析

基线：CPython 3.12.2，纯标准库；实现一个 `BufferedProtocol` 回声服务器，记录每次 `get_buffer`/`buffer_updated` 的缓冲区身份与字节数。

**问**：一个日志转发网关每秒收 8 万条、单条平均 1.2KB 的换行 JSON，用 `asyncio.Protocol.data_received` 处理，profile 显示 23% 的时间耗在 `bytes` 拷贝与切片上。改成 `BufferedProtocol` 后 CPU 降了 11%，但一周后出现"偶发 JSON 截断/串行"：解析器把 `get_buffer()` 返回的 `bytearray` 存进待处理队列，等协程调度回来时内容已经被下一次读覆盖。另一版返回了 `memoryview` 的切片，transport 直接报错。`get_buffer` 返回的缓冲区到底归谁？`buffer_updated` 返回后还能不能持有它？

**答**：

- **结论**：`BufferedProtocol` 让 transport 把内核数据**直接读进你提供的可写缓冲区**，避免 `data_received(bytes)` 那次"内核 → 临时 bytes → 你的对象"的拷贝。契约是：`get_buffer(sizehint)` 返回一个支持 buffer protocol 的**可写**对象（通常是 `bytearray` 或 `memoryview`），transport 最多写 `len(buf)` 字节；写完后调用 `buffer_updated(nbytes)`，告诉你有效字节数。这个缓冲区是**借给 transport 的**：`buffer_updated` 返回后，transport 可能在下一次 `get_buffer` 时复用/覆盖它，所以你只能在回调内消费（解析、拷贝、写走），**不能**把引用存起来跨事件循环使用。`sizehint` 只是建议，返回更小/更大的缓冲区都可以，但不能返回空缓冲区。
- **取舍**：零拷贝适合"大块、可增量解析"的协议（文件传输、帧协议、日志行），收益在减少一次内存拷贝与对象分配；代价是状态机复杂度：你必须自己处理半包/粘包、缓冲区边界、解析失败后的丢弃策略。`Protocol.data_received` 简单、每次拿到独立 `bytes`，可以安全排队给其他协程，但多一次拷贝。另一个坑是 `memoryview`：`get_buffer` 需要**可写**缓冲区，`memoryview(b"...")` 只读不行；切片 `mv[a:b]` 虽然是 view，但 transport 需要能写入，且生命周期更难管，容易踩 "existing exports" 或只读错误。生产上优先返回预分配的 `bytearray`，在回调内 `memoryview(buf)[:n]` 做只读解析，回调结束即失效。
- **实战**：事故版本在 `buffer_updated` 里 `queue.put(self.buf)`，消费者异步解析；下一次 `get_buffer` 返回同一个 `self.buf`，transport 覆盖了前半段，消费者读到的是"新帧的头 + 旧帧的尾"。修复：① `buffer_updated` 内同步完成"找换行 + 拷贝完整帧到 `bytes`"，只把不可变的 `bytes` 入队；② 半包留在 `self.pending`（自己管理的 `bytearray`），不再引用 transport 借出的 buffer；③ 给 `get_buffer` 返回固定 64KB 的 `bytearray`，并用 `nbytes` 严格切片。修复后串行归零，CPU 仍比 `Protocol` 低 8%。

下面用 10KB 数据触发多次读，验证 `get_buffer` 的 `sizehint`、缓冲区被复用（同一 `id`）、`buffer_updated` 的字节数累计，以及"只能同步消费"的约束。

```python
# BufferedProtocol: transport 直接写入 get_buffer 返回的缓冲区
import asyncio


class BufferedEcho(asyncio.BufferedProtocol):
    def __init__(self):
        self.buf = bytearray(4096)
        self.buffer_ids = []
        self.sizehints = []
        self.received = bytearray()
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def get_buffer(self, sizehint):
        self.sizehints.append(sizehint)
        self.buffer_ids.append(id(self.buf))
        return self.buf                     # 必须是可写缓冲区

    def buffer_updated(self, nbytes):
        # 只能在这里同步消费: 回调返回后 buf 可能被下一次读覆盖
        chunk = bytes(self.buf[:nbytes])
        self.received += chunk
        self.transport.write(chunk)         # 回声

    def connection_lost(self, exc):
        pass


async def main():
    created = []

    def factory():
        proto = BufferedEcho()
        created.append(proto)
        return proto

    loop = asyncio.get_running_loop()
    server = await loop.create_server(factory, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]

    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    payload = b"x" * 10_000
    writer.write(payload)
    await writer.drain()

    echoed = await asyncio.wait_for(reader.readexactly(len(payload)), timeout=2)
    print("[1] 回声字节数:", len(echoed))
    assert echoed == payload

    proto = created[0]
    print("[2] get_buffer 调用次数:", len(proto.sizehints), "sizehint:", proto.sizehints[:3],
          "(-1 表示 transport 没有给出建议)")
    print("[3] 缓冲区 id 是否复用:", len(set(proto.buffer_ids)) == 1)
    print("[4] 累计接收:", len(proto.received), "字节")
    assert len(proto.sizehints) >= 2, "10KB 超过 4KB 缓冲区, 应分多次读"
    assert all(hint == -1 or hint > 0 for hint in proto.sizehints)
    assert len(set(proto.buffer_ids)) == 1, "transport 复用同一个缓冲区"
    assert len(proto.received) == len(payload)

    # 反例: 只读 memoryview 不能作为 get_buffer 的返回值
    readonly = memoryview(b"abc")
    try:
        readonly[0] = 65
        raise AssertionError("只读 view 不应可写")
    except TypeError as exc:
        print("[5] 只读缓冲区不可写:", exc)

    writer.close()
    await writer.wait_closed()
    server.close()
    await server.wait_closed()
    print("[6] 完成: 回调返回后不得持有 buf 引用")


asyncio.run(main())
```

**追问一**：`buffer_updated` 里能不能 `await`？—— 不能，它是普通同步回调，事件循环不会在这里挂起。需要异步处理时，必须在回调内把数据**拷贝**成 `bytes` 或写入自己的队列，再 `create_task` 交给消费者；不能把 transport 借出的 buffer 直接传出去。若处理很重，考虑在回调内只做 framing、把完整帧拷贝出来，消费者再做 JSON 解析，避免阻塞读循环。

**追问二**：`get_buffer` 返回的缓冲区比 `sizehint` 小会怎样？—— 不会报错，transport 会按实际 `len(buf)` 读，下次再要；返回空缓冲区（长度 0）才会出问题（无法推进）。`sizehint` 通常来自 transport 的内部水位/最大读大小，返回一个固定 64KB 的缓冲区是常见做法；如果你返回一个巨大的缓冲区，注意内存占用与多连接叠加。`BufferedProtocol` 不会自动帮你扩容，也不会在 `buffer_updated` 之间保留未消费的数据——半包必须自己存。

## 背诵要点

- `get_buffer(sizehint)` 返回**可写**缓冲区，transport 直接写入；`buffer_updated(nbytes)` 给出有效长度，回调返回后缓冲区可能被复用。
- 只能在回调内同步消费/拷贝；跨协程排队必须传不可变 `bytes`，不能传借出的 buffer。
- 零拷贝省一次复制，代价是半包/粘包与生命周期自己管；只读 `memoryview` 不能作为返回缓冲区。

## 复盘追问

- 为什么 `buffer_updated` 里保存 `self.buf` 的引用会在下一次读时被覆盖？（transport 复用同一个预分配缓冲区，避免每次分配）
- `BufferedProtocol` 和 `Protocol.data_received` 的拷贝次数差在哪？（后者由 transport 构造独立 bytes 再回调；前者直接写入用户缓冲区）
