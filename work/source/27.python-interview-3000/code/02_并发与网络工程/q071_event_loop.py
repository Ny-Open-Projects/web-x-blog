import asyncio


async def worker(name: str, delay: float) -> str:
    print(f"{name} 开始")
    await asyncio.sleep(delay)  # 让出控制权给事件循环
    print(f"{name} 结束")
    return f"{name} 的结果"


async def main() -> None:
    # 三个协程在同一个线程里交错执行
    results = await asyncio.gather(
        worker("A", 0.3),
        worker("B", 0.2),
        worker("C", 0.1),
    )
    print(results)
    print("运行线程:", __import__("threading").current_thread().name)


if __name__ == "__main__":
    asyncio.run(main())
