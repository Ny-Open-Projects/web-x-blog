import asyncio

trace = []


async def job(name: str) -> str:
    trace.append(f"run:{name}")
    return name.upper()


async def main() -> None:
    t = asyncio.create_task(job("A"))
    trace.append("created")
    print("创建后 Task 状态:", "已调度未运行" if not t.done() else "?")

    await asyncio.sleep(0)  # 让出控制权: Task 的第一步 __step 此时才执行
    print("sleep(0) 后 trace:", trace)

    result = await t
    trace.append(f"awaited:{result}")
    print("最终 trace:", trace)

    # ensure_future 对三种输入的行为
    coro = job("B")
    t2 = asyncio.ensure_future(coro)   # 协程 → Task
    fut = asyncio.ensure_future(t2)    # Task → 原样返回
    print("ensure_future(Task) 返回同一对象:", fut is t2)
    print("ensure_future 结果:", await t2)


asyncio.run(main())
