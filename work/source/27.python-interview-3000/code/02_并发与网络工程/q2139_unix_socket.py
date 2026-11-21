# -*- coding: utf-8 -*-
"""Unix 域 socket: 本机 IPC 的高速通道。

- AF_UNIX 不走 IP 栈, 地址是文件系统路径, 无端口冲突与路由开销;
- asyncio.start_unix_server 与 TCP 版 API 完全同构, 迁移成本低;
- 退出前要主动 unlink, 否则残留路径会让下次 bind 报 EADDRINUSE。
"""
import asyncio
import os
import tempfile

SOCK_PATH = tempfile.mktemp(prefix="q2139_unix_")


async def handle(reader, writer):
    while True:
        line = await reader.readline()
        if not line:
            break
        writer.write(b"unix-echo: " + line)
        await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_unix_server(handle, path=SOCK_PATH)
    print("监听地址是文件系统路径:", SOCK_PATH)
    asyncio.ensure_future(server.serve_forever())
    await asyncio.sleep(0.15)

    reader, writer = await asyncio.open_unix_connection(SOCK_PATH)
    for msg in (b"hello", b"ipc"):
        writer.write(msg + b"\n")
        await writer.drain()
        print("发出 %s -> %s" % (msg.decode(), await reader.readline()))
    writer.close()
    await writer.wait_closed()
    server.close()
    await server.wait_closed()
    os.unlink(SOCK_PATH)      # 清理套接字文件, 防止残留
    print("文件已清理, 存在性:", os.path.exists(SOCK_PATH))
    print("同机通信选 AF_UNIX: 少一层 IP 头, 权限可直接用文件权限表达")


if __name__ == "__main__":
    asyncio.run(main())
