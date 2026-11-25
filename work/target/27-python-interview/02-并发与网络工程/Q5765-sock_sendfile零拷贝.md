---
title: "[Q5765] loop.sock_sendfile：零拷贝发送与 transport 占用 fd 的冲突"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5765 · loop.sock_sendfile：零拷贝发送与 transport 占用 fd 的冲突

难度：P7 ｜ 标签：asyncio、sock_sendfile、零拷贝、sendfile、文件下载、transport

基线：CPython 3.12.2，纯标准库；用原始非阻塞 socket + `loop.sock_sendfile` 传文件，并验证 `offset/count` 与 transport 冲突。

**问**：文件下载服务从 `StreamWriter` 拿到底层 socket，调用 `loop.sock_sendfile(writer.get_extra_info("socket"), f)` 想省掉用户态拷贝，结果直接 `RuntimeError: File descriptor 7 is used by transport`。改用裸 socket 后能发了，但断点续传的 `Range` 逻辑传了 `offset=10, count=5`，客户端收到的却是从文件开头开始的 5 字节；另一条链路在发送过程中 `f.tell()` 变了，导致后续重试从错误位置开始。`sock_sendfile` 到底要求什么样的 socket？`offset` 和文件位置是什么关系？

**答**：

- **结论**：`loop.sock_sendfile(sock, file, offset=0, count=None, fallback=True)` 用内核 `sendfile` 把文件页直接送到 socket，省掉"读文件到用户缓冲 → 写 socket"的两次拷贝；它要求 `sock` 是**非阻塞、未被任何 transport 接管**的 socket，`file` 是带 `fileno()` 的普通文件（不能是 `BytesIO`），且不能是 SSL socket（内核无法在发送时加密）。一旦 socket 已被 `StreamReader/StreamWriter` 的 transport 注册到 selector，`loop.add_writer` 会检测到 fd 冲突并抛 `RuntimeError`——正确用法是裸 `socket.socket()` + `loop.sock_connect()`，或 `loop.sock_accept()` 拿到的原始连接。`offset/count` 是显式的发送区间；实测调用后文件位置会推进到 `offset + sent`（本例 `seek(5)`、`offset=10,count=5` 后 `tell()==15`），所以不要用调用前的文件位置推断发送起点，续传必须显式传 `offset`。
- **取舍**：零拷贝在"大文件 + 明文 HTTP"下收益明显（CPU 降、内存带宽省），但和 TLS、用户态压缩、Range 之外的自定义加密都不兼容——一旦要 `ssl`，只能退回 `read/write` 循环（`fallback=True` 只在平台不支持 sendfile 时兜底，不会帮你处理 TLS）。另一个取舍是错误处理：`sock_sendfile` 返回实际发送字节数，可能小于 `count`（对端关闭、信号中断），调用方必须循环续发并处理 `BrokenPipeError`；不能假设一次调用就发完。小文件（<64KB）用 sendfile 的 syscall 开销可能不如直接 `write`，框架通常设阈值。
- **实战**：下载网关最初把 `StreamWriter` 的 socket 直接传给 `sock_sendfile`，100% 失败；改成 `asyncio.start_server` 的 handler 里用 `writer.transport` 的 socket 也不行，因为 transport 仍持有 fd。最终方案：文件下载走独立的 `loop.create_server` 原始协议，`connection_made` 里拿 `transport.get_extra_info("socket")` 仍然不行——必须让 transport 不接管，改用 `loop.sock_accept` 自己管理连接。落地时用了更简单的路径：明文下载用 `socket.sendfile` 放到 `run_in_executor`，TLS 下载用 `read/write` + `fallback`；`sock_sendfile` 只留给内部明文大文件通道。Range 逻辑统一用 `offset=start, count=end-start+1`，并在发送后校验 `sent == count`，否则记 `short_send` 并断开。

下面验证整文件发送、`offset/count` 的精确区间与 `tell()` 推进、transport 占用 fd 时的 `RuntimeError`。

```python
# loop.sock_sendfile: 裸 socket + 显式 offset/count; transport 持有的 fd 不能用
import asyncio
import os
import socket
import tempfile


async def main():
    payload = b"0123456789" * 10_000
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(payload)
        path = tmp.name

    received = []

    async def handler(reader, writer):
        buf = bytearray()
        while True:
            chunk = await reader.read(65536)
            if not chunk:
                break
            buf += chunk
        received.append(bytes(buf))
        writer.close()

    server = await asyncio.start_server(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    loop = asyncio.get_running_loop()

    # 1) 裸 socket: 整文件发送
    raw = socket.socket()
    raw.setblocking(False)
    await loop.sock_connect(raw, ("127.0.0.1", port))
    with open(path, "rb") as f:
        sent = await loop.sock_sendfile(raw, f)
        position_after = f.tell()
    raw.close()
    await asyncio.sleep(0.1)

    print("[1] 整文件 sent =", sent, "tell =", position_after)
    assert sent == len(payload)
    assert position_after == len(payload)
    assert received[0] == payload

    # 2) offset/count: 只发 [10, 15)
    raw2 = socket.socket()
    raw2.setblocking(False)
    await loop.sock_connect(raw2, ("127.0.0.1", port))
    with open(path, "rb") as f:
        f.seek(5)                       # 调用前的文件位置不影响 offset
        sent2 = await loop.sock_sendfile(raw2, f, offset=10, count=5)
        tell2 = f.tell()
    raw2.close()
    await asyncio.sleep(0.1)

    print("[2] offset 发送 sent =", sent2, "tell =", tell2, "内容 =", received[-1])
    assert sent2 == 5
    assert received[-1] == b"01234"
    assert tell2 == 15, "调用后位置推进到 offset + sent"

    # 3) transport 已持有的 socket 不能直接用
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    with open(path, "rb") as f:
        try:
            await loop.sock_sendfile(writer.get_extra_info("socket"), f)
            raise AssertionError("transport 持有的 fd 本应冲突")
        except RuntimeError as exc:
            print("[3] transport 冲突:", str(exc)[:60])
            assert "used by transport" in str(exc)
    writer.close()
    await writer.wait_closed()

    server.close()
    await server.wait_closed()
    os.unlink(path)
    print("[4] 完成")


asyncio.run(main())
```

**追问一**：为什么 `sock_sendfile` 不能用于 SSL socket？—— `sendfile` 是内核把文件页直接挂到 socket 的发送队列，数据不经过用户态；TLS 需要在用户态对每个字节加密并加记录头，内核没有密钥，无法完成。对 SSL socket 调用会抛 `ValueError`（或依赖具体实现报错）。要加密传输，只能用 `read` + `SSLObject.write` 的循环，或者让反向代理终结 TLS，后端明文用 sendfile。

**追问二**：`fallback=True` 到底 fallback 什么？—— 当平台没有 `sendfile`（如某些 Windows 配置）或文件类型不支持时，asyncio 会退化成"用 `run_in_executor` 读文件块 + `sock_sendall`"的异步循环，仍然是异步的、不会阻塞事件循环，但不是零拷贝。它**不会**在 TLS、transport 冲突、文件被截断这些场景兜底；这些是用法错误，应该显式报错。生产上如果要兼容多平台，保留 `fallback=True`，但监控里区分"native sendfile"和"fallback"两条路径的耗时。

## 背诵要点

- `sock_sendfile` 要求非阻塞、未被 transport 接管的裸 socket + 普通文件；SSL 不支持。
- `offset/count` 是显式区间，调用后文件位置推进到 `offset + sent`；续传不要依赖调用前的位置。
- 返回值是实际发送字节数，可能 short send；小文件走 sendfile 未必划算，TLS 场景只能 read/write。

## 复盘追问

- 为什么 `StreamWriter` 的 socket 不能直接传给 `sock_sendfile`？（transport 已把 fd 注册进 selector，`add_writer` 检测到冲突）
- `sock_sendfile` 返回小于 `count` 时该怎么处理？（循环续发剩余区间，处理 `BrokenPipeError`/对端关闭，记录 short send）
