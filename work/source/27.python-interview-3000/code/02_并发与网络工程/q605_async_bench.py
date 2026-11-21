import asyncio
import statistics
import time


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        data = await reader.read(100)
        await asyncio.sleep(0.02)  # 模拟后端处理 20ms
        writer.write(data)
        await writer.drain()
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def worker(port: int, sem: asyncio.Semaphore, latencies: list) -> None:
    async with sem:  # 并发窗口
        t0 = time.perf_counter()
        r, w = await asyncio.open_connection("127.0.0.1", port)
        w.write(b"ping")
        await w.drain()
        await r.read(100)
        w.close()
        await w.wait_closed()
        latencies.append(time.perf_counter() - t0)


async def bench(port: int, concurrency: int, total: int) -> None:
    latencies: list = []
    sem = asyncio.Semaphore(concurrency)
    t0 = time.perf_counter()
    await asyncio.gather(*[worker(port, sem, latencies) for _ in range(total)])
    dt = time.perf_counter() - t0
    latencies.sort()
    n = len(latencies)
    print(f"并发={concurrency:>3} QPS={total / dt:7.0f} "
          f"p50={latencies[n // 2] * 1000:5.1f}ms "
          f"p95={latencies[int(n * 0.95)] * 1000:5.1f}ms "
          f"p99={latencies[int(n * 0.99)] * 1000:5.1f}ms")


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]

    # 爬坡: 逐步加并发, 观察延迟拐点。
    # 规模注意: 每个请求都完整建连/断连, 本机连接 churn 开销大,
    # total 控制在 200、并发取两档, 保证 25s 内跑完
    for conc in (10, 50):
        lats: list = []
        await asyncio.gather(*[worker(port, asyncio.Semaphore(conc), lats)
                               for _ in range(20)])  # 预热
        await bench(port, conc, total=200)

    server.close()
    await server.wait_closed()


asyncio.run(main())
