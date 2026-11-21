import asyncio


async def job(name: str) -> str:
    await asyncio.sleep(0.2)
    return f"{name} done"


async def main() -> None:
    coro = job("裸协程")          # 不会执行
    task = asyncio.create_task(job("任务"))  # 创建即调度

    # 裸协程需要 await 才执行: 顺序执行
    print("await 裸协程:", await coro)
    print("await Task:", await task)

    # 更底层的 Future 手动控制完成
    fut: asyncio.Future[str] = asyncio.get_running_loop().create_future()
    fut.set_result("future 完成")
    print("await Future:", await fut)


if __name__ == "__main__":
    asyncio.run(main())
