import asyncio
import time


async def blocking_way() -> float:
    start = time.perf_counter()
    for i in range(3):
        time.sleep(0.3)  # 错误: 同步阻塞事件循环
        print(f"阻塞式 第 {i} 次")
    return time.perf_counter() - start


async def async_way() -> float:
    start = time.perf_counter()
    await asyncio.gather(*(asyncio.sleep(0.3, result=i) for i in range(3)))
    print("异步式 三次等待重叠")
    return time.perf_counter() - start


async def main() -> None:
    t1 = await blocking_way()
    t2 = await async_way()
    print(f"阻塞式耗时 {t1:.2f}s, 异步式耗时 {t2:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
