import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_io(n: int, factor: int = 2) -> int:
    time.sleep(0.1)  # 模拟阻塞 IO
    return n * factor


async def main() -> None:
    # 场景一: 偶发调用 → to_thread 简洁
    t0 = time.perf_counter()
    r1 = await asyncio.to_thread(blocking_io, 10, factor=3)  # 支持 kwargs
    print(f"to_thread 单次: {r1}, {time.perf_counter() - t0:.2f}s")

    # 场景二: 大量并发 → 默认池够用性检查
    t0 = time.perf_counter()
    rs = await asyncio.gather(*[asyncio.to_thread(blocking_io, i) for i in range(10)])
    print(f"to_thread 10 并发: 完成 {len(rs)}, {time.perf_counter() - t0:.2f}s")

    # 场景三: 需要限流 → 自定义 2 线程池, 10 个任务分 5 批
    pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="db")
    try:
        loop = asyncio.get_running_loop()
        t0 = time.perf_counter()
        rs = await asyncio.gather(
            *[loop.run_in_executor(pool, blocking_io, i) for i in range(10)]
        )
        print(f"run_in_executor(max_workers=2): {len(rs)} 个, "
              f"{time.perf_counter() - t0:.2f}s (被 2 线程限流)")
    finally:
        pool.shutdown()


asyncio.run(main())
