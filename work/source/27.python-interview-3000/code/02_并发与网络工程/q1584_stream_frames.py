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
