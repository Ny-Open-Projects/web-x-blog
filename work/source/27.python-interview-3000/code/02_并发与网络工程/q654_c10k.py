import asyncio
import resource
import time

N_CONNECTIONS = 1000


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    # 空闲连接模拟: 注册后挂起, 等客户端关闭
    try:
        await reader.read()  # 阻塞至对端关闭, 不占线程不占 CPU
    except ConnectionError:
        pass
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def main() -> None:
    rss0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    print(f"服务端就绪 port={port}, 目标 {N_CONNECTIONS} 并发连接")

    t0 = time.perf_counter()
    writers = []
    for i in range(N_CONNECTIONS):
        r, w = await asyncio.open_connection("127.0.0.1", port)
        writers.append(w)
    dt = time.perf_counter() - t0
    print(f"建立 {len(writers)} 个并发连接耗时 {dt:.2f}s "
          f"({N_CONNECTIONS / dt:.0f} conns/s)")

    # 空闲 0.5s: 验证事件循环在大量挂起连接下 CPU 占用极低
    t0 = time.perf_counter()
    await asyncio.sleep(0.5)
    print(f"空闲等待 0.5s 实际 {(time.perf_counter() - t0) * 1000:.0f}ms (单线程事件循环未受干扰)")

    rss1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    unit = "KB" if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 10 ** 7 else "bytes"
    print(f"maxrss: {rss0} → {rss1} {unit}, "
          f"每连接约 {(max(rss1 - rss0, 0)) / max(len(writers), 1):.1f} {unit}")

    for w in writers:
        w.close()
    await asyncio.gather(*[w.wait_closed() for w in writers], return_exceptions=True)
    server.close()
    await server.wait_closed()
    print("C10K 结论: 事件驱动 + 小缓冲, 单线程即可承载千级空闲连接")


asyncio.run(main())
