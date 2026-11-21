import asyncio


async def background_work(n: int) -> int:
    await asyncio.sleep(0.3)
    if n == 1:
        raise RuntimeError("后台任务 1 出错")
    return n


async def main() -> None:
    tasks: set[asyncio.Task] = set()

    def on_done(task: asyncio.Task) -> None:
        tasks.discard(task)
        if not task.cancelled() and task.exception() is not None:
            print("后台任务异常:", repr(task.exception()))

    for i in range(3):
        t = asyncio.create_task(background_work(i))
        tasks.add(t)               # 保存引用, 防止被 GC
        t.add_done_callback(on_done)  # 观察异常

    await asyncio.sleep(0.5)
    if tasks:
        print("仍有未完成任务, 统一取消")
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
    print("退出, 无泄漏")


if __name__ == "__main__":
    asyncio.run(main())
