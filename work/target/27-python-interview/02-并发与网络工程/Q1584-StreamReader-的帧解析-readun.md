---
title: [Q1584] StreamReader 的帧解析:readuntil 与 LimitOverrunError
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1584 · StreamReader 的帧解析:readuntil 与 LimitOverrunError

> 难度:★★★☆ | 标签:StreamReader, 帧解析, 异常

**问**:asyncio 的流上做帧解析,readuntil 碰到超长帧抛 LimitOverrunError 之后,流还能继续用吗?

**答**:能,关键在恢复路径。readuntil(分隔符) 在缓冲区找不到分隔符且超过 limit 时抛 LimitOverrunError,异常带 consumed 属性——已确认的 consumed 字节还在缓冲区,先 await read(consumed) 丢弃,再把残余读到分隔符一并作废,流就继续向前,后续正常帧不丢。readexactly(n) 是另一半:精确读 n 字节,半包会挂起等齐;对端断流时抛 IncompleteReadError,.partial 里是已读到的残包,正好用于断连诊断。三者组合:readuntil 管边界,readexactly 管凑齐,异常对象管残局。

```python
# file: code/02_并发与网络工程/q1584_stream_frames.py
"""StreamReader 的帧解析: readuntil 与 LimitOverrunError。

- readuntil(b"\\n"): 读到分隔符, 但行长超过 limit 时抛 LimitOverrunError,
  异常携带 consumed(缓冲区里已确认的字节数), 先 read(consumed) 丢弃再继续,
  流才不会卡死;
- readexactly(n): 精确读 n 字节, 半包会一直等到凑齐; 对端提前断流抛
  IncompleteReadError, .partial 里是已读到的部分。
"""
import asyncio
import struct

LIMIT = 64


async def lines_server(reader, writer):
    for i in range(1, 4):
        writer.write(("frame-%d\n" % i).encode())
    writer.write(b"x" * 100 + b"\n")            # 超长行: 触发 LimitOverrunError
    for i in range(4, 6):
        writer.write(("frame-%d\n" % i).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def frame_server(reader, writer):
    payload = b"payload-ok"
    writer.write(struct.pack(">I", len(payload)) + payload)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def short_server(reader, writer):
    writer.write(b"AB")                          # 半截帧就断流
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def read_lines(port):
    reader, writer = await asyncio.open_connection("127.0.0.1", port, limit=LIMIT)
    got, skipped = [], 0
    while True:
        try:
            line = await reader.readuntil(b"\n")
            got.append(line.decode().strip())
        except asyncio.LimitOverrunError as e:
            # 行长超过 limit: 先丢弃已确认的 consumed 字节, 再把残余读到分隔符,
            # 整行作废, 流继续向前——这是超长帧的标准恢复路径
            await reader.read(e.consumed)
            dropped = e.consumed
            while True:
                try:
                    dropped += len(await reader.readuntil(b"\n"))
                    break
                except asyncio.LimitOverrunError as e2:
                    await reader.read(e2.consumed)
                    dropped += e2.consumed
            skipped += 1
            print("丢弃超长行 %d 字节" % dropped)
        except asyncio.IncompleteReadError:
            break
    writer.close()
    await writer.wait_closed()
    return got, skipped


async def read_frame(port):
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    head = await reader.readexactly(4)
    (n,) = struct.unpack(">I", head)
    payload = await reader.readexactly(n)
    writer.close()
    await writer.wait_closed()
    return payload


async def read_short(port):
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    try:
        await reader.readexactly(4)
        return None
    except asyncio.IncompleteReadError as e:
        return e.partial                          # b"AB": 断流时已凑到的半包
    finally:
        writer.close()


async def main():
    srv1 = await asyncio.start_server(lines_server, "127.0.0.1", 0)
    srv2 = await asyncio.start_server(frame_server, "127.0.0.1", 0)
    srv3 = await asyncio.start_server(short_server, "127.0.0.1", 0)
    p1 = srv1.sockets[0].getsockname()[1]
    p2 = srv2.sockets[0].getsockname()[1]
    p3 = srv3.sockets[0].getsockname()[1]

    got, skipped = await read_lines(p1)
    print("解析到的行帧:", got, "| 丢弃超长行:", skipped)
    assert got == ["frame-1", "frame-2", "frame-3", "frame-4", "frame-5"]
    assert skipped == 1, "超长行应被识别并跳过"

    payload = await read_frame(p2)
    print("定长帧读出:", payload)
    assert payload == b"payload-ok"

    partial = await read_short(p3)
    print("断流半包 partial:", partial)
    assert partial == b"AB", "IncompleteReadError 应带出已读半包"

    for srv in (srv1, srv2, srv3):
        srv.close()
        await srv.wait_closed()
    print("结论: readuntil 管'边界', readexactly 管'凑齐', 异常对象管'残局'")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) limit 设多大合适?——略大于最大合法帧:太小误杀合法帧,太大(默认 64KB)会放过恶意超大帧耗内存。2) LimitOverrunError 的恢复路径为什么不能跳过?——异常后缓冲区里仍有「已确认的 consumed 字节+残余」,不读掉它们,下一帧解析就从垃圾中间开始;「read(consumed) 丢弃→读到分隔符作废」是把流指针推回正轨的固定动作。3) readexactly 与 IncompleteReadError 怎么配合诊断?——对端断流时 partial 告诉你「收到了多少」:半包数量级可推断断点位置;配合字节级日志(Q644)能还原「断在帧头还是帧尾」——异常对象携带的信息就是诊断材料,别只看异常名。4) 生产陷阱?——limit 设太小误杀合法帧(慢站点长响应);把 LimitOverrunError 当致命错误断连(其实可恢复);readuntil 后忘了流指针已越过分隔符(重复消费);在 IncompleteReadError 后继续用同一个 reader(流已死)。

---
