import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def blocking_fetch(url_id):
    time.sleep(0.2)              # 模拟阻塞 IO
    return f"resp-{url_id}"

async def async_fetch(url_id):
    await asyncio.sleep(0.2)     # 模拟非阻塞 IO
    return f"resp-{url_id}"

if __name__ == "__main__":
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(blocking_fetch, range(10)))
    print("线程池:", round(time.perf_counter() - t0, 2), "s")

    async def main():
        return await asyncio.gather(*(async_fetch(i) for i in range(10)))
    t0 = time.perf_counter()
    results = asyncio.run(main())
    print("协程:", round(time.perf_counter() - t0, 2), "s")
