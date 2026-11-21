import asyncio
import random


async def fetch(i: int) -> str:
    await asyncio.sleep(random.uniform(0.1, 0.4))
    if i == 2:
        raise ValueError(f"任务 {i} 失败")
    return f"result-{i}"


async def main() -> None:
    coros = [fetch(i) for i in range(4)]

    # gather: 顺序对应, 容忍异常
    results = await asyncio.gather(*coros, return_exceptions=True)
    print("gather:", results)

    # wait: 任一完成即处理
    tasks = [asyncio.create_task(fetch(i)) for i in range(4)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for t in done:
        print("wait 首个完成:", t.result() if not t.exception() else t.exception())
    for t in pending:
        t.cancel()

    # as_completed: 按完成顺序
    tasks2 = [asyncio.create_task(fetch(i + 10)) for i in range(4)]
    for fut in asyncio.as_completed(tasks2):
        try:
            print("as_completed:", await fut)
        except ValueError as e:
            print("as_completed 异常:", e)


if __name__ == "__main__":
    asyncio.run(main())
