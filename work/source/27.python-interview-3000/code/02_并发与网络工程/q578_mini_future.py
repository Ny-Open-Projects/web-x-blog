import asyncio

PENDING = "PENDING"
CANCELLED = "CANCELLED"
FINISHED = "FINISHED"


class MiniFuture:
    """复刻 asyncio.Future 的状态机与回调调度语义。

    教学同构体, 刻意不实现 __await__: 若 yield self 交给 asyncio.Task,
    Task.__step 无法识别会抛 RuntimeError("Task got bad yield");
    要真正接入事件循环必须实现完整的 Future 协议(如 _asyncio.Future)。
    """

    def __init__(self, loop) -> None:
        self._state = PENDING
        self._result = None
        self._exception = None
        self._callbacks = []
        self._loop = loop

    def set_result(self, value) -> None:
        assert self._state == PENDING, "已完成状态不可再 set_result"
        self._result = value
        self._state = FINISHED
        self.__schedule_callbacks()

    def set_exception(self, exc: Exception) -> None:
        assert self._state == PENDING
        self._exception = exc
        self._state = FINISHED
        self.__schedule_callbacks()

    def cancel(self) -> bool:
        if self._state != PENDING:
            return False
        self._state = CANCELLED
        self.__schedule_callbacks()
        return True

    def __schedule_callbacks(self) -> None:
        cbs, self._callbacks = self._callbacks, []
        for cb in cbs:  # 关键: 经 call_soon 排队, 下一轮循环执行
            self._loop.call_soon(cb, self)

    def add_done_callback(self, cb) -> None:
        if self._state != PENDING:
            self._loop.call_soon(cb, self)
        else:
            self._callbacks.append(cb)

    def result(self):
        """读取结果: 带 exception 时原地重抛(同真 Future 语义)。"""
        if self._exception is not None:
            raise self._exception
        return self._result


async def main() -> None:
    loop = asyncio.get_running_loop()
    order = []

    # 1) 回调经 call_soon 排队: set 的下一轮才执行
    fut = MiniFuture(loop)
    fut.add_done_callback(lambda f: order.append("callback"))
    loop.call_soon(lambda: (order.append("set"), fut.set_result(42)))
    await asyncio.sleep(0)  # 让出一次: 排队的 set 执行(并继续把回调排进队列)
    await asyncio.sleep(0)  # 再让出一次: 回调这一轮才真正执行
    print("状态:", fut._state, "结果:", fut.result(), "顺序:", order)
    assert order == ["set", "callback"], "回调在 set 之后的下一轮循环执行"

    # 2) 已完成的 Future 拒绝再次 set
    try:
        fut.set_result(1)
    except AssertionError as e:
        print("重复 set 被拒绝:", e)

    # 3) set_exception / cancel 语义
    fut2 = MiniFuture(loop)
    fut2.set_exception(ValueError("boom"))
    try:
        fut2.result()
    except ValueError as e:
        print("set_exception 后取结果重抛:", e)
    fut3 = MiniFuture(loop)
    print("cancel 返回:", fut3.cancel(), "状态:", fut3._state)

    # 4) 挂起-唤醒语义用真 Future 演示(Task 只认 asyncio.Future)
    real = loop.create_future()
    loop.call_soon(lambda: real.set_result(99))
    print("真 Future await 唤醒:", await real)


if __name__ == "__main__":
    asyncio.run(main())
