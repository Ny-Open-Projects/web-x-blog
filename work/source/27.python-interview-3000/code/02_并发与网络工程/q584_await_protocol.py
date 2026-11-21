import asyncio


class Sleep:
    """自定义 awaitable: 手工实现 asyncio.sleep 的语义。"""

    def __init__(self, delay: float) -> None:
        self.delay = delay

    def __await__(self):
        # yield from 一个协程: 其中的 yield(Future) 会穿透到 Task 层
        return _sleep_impl(self.delay).__await__()


async def _sleep_impl(delay: float) -> None:
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.call_later(delay, fut.set_result, None)  # 到点唤醒
    return await fut


async def main() -> None:
    print("开始")
    await Sleep(0.2)  # await 一个普通对象, 只要它有 __await__
    print("0.2 秒后继续")

    # 验证协程与生成器同源
    coro = _sleep_impl(0.05)
    print("协程有 send/close:", hasattr(coro, "send"), hasattr(coro, "close"))
    print("协程有 __await__:", hasattr(coro, "__await__"))
    coro.close()  # 不想跑完就手动关闭

    # Future 的 __await__ 会 yield 自身 — 这就是挂起机制的核心
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    agen = fut.__await__()
    yielded = next(agen)  # 手动驱动一步
    print("__await__ yield 出的是 Future 自身:", yielded is fut)
    fut.set_result("done")
    try:
        agen.send(None)
    except StopIteration as e:
        print("send 后得到结果:", e.value)


asyncio.run(main())
