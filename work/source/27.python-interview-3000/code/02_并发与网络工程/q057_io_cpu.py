import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def io_task(i: int) -> int:
    time.sleep(0.2)  # 模拟网络 IO
    return i


def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(io_task, range(8)))
    print(f"IO 密集 + 线程池: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda n: cpu_task(n), [2_000_000] * 4))
    print(f"CPU 密集 + 线程池: {time.perf_counter() - start:.2f}s (GIL 下串行)")

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(cpu_task, [2_000_000] * 4))
    print(f"CPU 密集 + 进程池: {time.perf_counter() - start:.2f}s (真并行)")
