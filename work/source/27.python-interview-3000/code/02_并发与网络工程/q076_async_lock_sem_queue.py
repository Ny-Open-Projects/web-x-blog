import asyncio


async def limited_call(i: int, sem: asyncio.Semaphore) -> int:
    async with sem:  # 最多 2 个并发
        print(f"请求 {i} 发出")
        await asyncio.sleep(0.2)
        return i * 2


async def single_flight(key: str, lock: asyncio.Lock, cache: dict) -> str:
    async with lock:
        if key not in cache:
            print(f"计算 {key}")
            await asyncio.sleep(0.2)
            cache[key] = f"value-{key}"
        return cache[key]


async def main() -> None:
    sem = asyncio.Semaphore(2)
    results = await asyncio.gather(*(limited_call(i, sem) for i in range(5)))
    print("限流结果:", results)

    lock = asyncio.Lock()
    cache: dict[str, str] = {}
    vals = await asyncio.gather(*(single_flight("k1", lock, cache) for _ in range(3)))
    print("单飞结果:", vals)

    q: asyncio.Queue[int] = asyncio.Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    print("队列已满, 再 put 会等待, 当前 qsize:", q.qsize())
    print("get:", await q.get(), await q.get())


if __name__ == "__main__":
    asyncio.run(main())
