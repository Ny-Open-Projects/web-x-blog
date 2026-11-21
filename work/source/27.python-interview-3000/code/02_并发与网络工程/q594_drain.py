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
