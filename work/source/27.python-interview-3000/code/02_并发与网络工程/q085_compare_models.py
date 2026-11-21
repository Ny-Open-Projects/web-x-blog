import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def sync_io(i: int) -> int:
    time.sleep(0.05)  # 模拟阻塞 IO
    return i


async def async_io(i: int) -> int:
    await asyncio.sleep(0.05)
    return i


N = 200


def bench_threads() -> float:
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=50) as pool:
        list(pool.map(sync_io, range(N)))
    return time.perf_counter() - start


async def bench_async() -> float:
    start = time.perf_counter()
    await asyncio.gather(*(async_io(i) for i in range(N)))
    return time.perf_counter() - start


if __name__ == "__main__":
    t_thread = bench_threads()
    t_async = asyncio.run(bench_async())
    print(f"线程池 {N} 个任务: {t_thread:.2f}s")
    print(f"asyncio {N} 个任务: {t_async:.2f}s")
    print("结论: 任务量大时 asyncio 内存与调度开销更优, 线程池胜在生态兼容")
