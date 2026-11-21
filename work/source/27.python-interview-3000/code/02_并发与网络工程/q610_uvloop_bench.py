import asyncio
import time

try:
    import uvloop  # 第三方, 演示环境没有则退化为纯 asyncio 对比
    HAVE_UVLOOP = True
except ImportError:
    HAVE_UVLOOP = False

N = 10000   # 调度量级适中, 保证低配/高负载机器也能在实跑超时预算内跑完


def micro_bench() -> float:
    """测事件循环调度开销: N 个立即到期回调。"""
    loop = asyncio.new_event_loop()
    t0 = time.perf_counter()

    async def run() -> None:
        done = loop.create_future()
        counter = [0]

        def tick():
            counter[0] += 1
            if counter[0] >= N:
                done.set_result(None)
                return
            loop.call_soon(tick)

        loop.call_soon(tick)
        await done

    loop.run_until_complete(run())
    dt = time.perf_counter() - t0
    loop.close()
    return dt


async def http_like_bench() -> float:
    """测 IO 路径: 本机回环 N 次小请求。"""

    async def handle(r, w):
        try:
            await r.read(64)
            w.write(b"ok")
            await w.drain()
        finally:
            w.close()
            try:
                await w.wait_closed()
            except Exception:
                pass

    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    t0 = time.perf_counter()

    sem = asyncio.Semaphore(64)   # 限流并发连接, 避免 500 个 connect 同时打满 listen backlog

    async def one():
        async with sem:
            r, w = await asyncio.open_connection("127.0.0.1", port)
            w.write(b"x")
            await w.drain()
            await r.read(10)
            w.close()
            try:
                await w.wait_closed()
            except Exception:
                pass

    await asyncio.gather(*[one() for _ in range(500)])
    dt = time.perf_counter() - t0
    server.close()
    await server.wait_closed()
    return dt


if __name__ == "__main__":
    if HAVE_UVLOOP:
        uvloop.install()
        print("uvloop 已启用:", type(asyncio.new_event_loop()).__name__)
    else:
        print("未安装 uvloop, 展示默认循环基线 (安装后重跑对比)")
    print(f"回调调度 {N} 次: {micro_bench():.3f}s")
    print(f"回环 IO 500 次: {asyncio.run(http_like_bench()):.3f}s")  # 协程必须跑进事件循环再计时
