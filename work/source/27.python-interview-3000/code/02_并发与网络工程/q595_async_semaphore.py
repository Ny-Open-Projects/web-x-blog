import asyncio
import time


async def api_call(i: int, sem: asyncio.Semaphore, meter: dict) -> int:
    async with sem:  # 临界区: 整个请求生命周期
        meter["current"] += 1
        meter["peak"] = max(meter["peak"], meter["current"])
        await asyncio.sleep(0.05)  # 模拟外部 API 延迟
        meter["current"] -= 1
        return i * 2


async def main() -> None:
    sem = asyncio.Semaphore(5)  # 并发窗口 = 5
    meter = {"current": 0, "peak": 0}

    t0 = time.perf_counter()
    results = await asyncio.gather(*[api_call(i, sem, meter) for i in range(30)])
    dt = time.perf_counter() - t0

    print(f"30 个请求, 峰值并发 {meter['peak']} (上限 5), 耗时 {dt:.2f}s")
    assert meter["peak"] <= 5
    print("结果前 5 个:", results[:5])

    # 对照: 无限流会同时打满 30 个并发
    meter2 = {"current": 0, "peak": 0}
    await asyncio.gather(*[api_call(i, asyncio.Semaphore(100), meter2)
                           for i in range(30)])
    print("无限制峰值并发:", meter2["peak"])


asyncio.run(main())
