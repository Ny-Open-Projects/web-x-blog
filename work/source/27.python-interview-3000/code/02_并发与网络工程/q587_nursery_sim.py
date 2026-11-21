import asyncio
import sys
from contextlib import asynccontextmanager


class Nursery:
    """用纯 asyncio 模拟 trio nursery 的核心语义。"""

    def __init__(self) -> None:
        self._tasks: set = set()
        self._errors: list = []

    async def start_soon(self, coro) -> None:
        t = asyncio.create_task(self._wrap(coro))
        self._tasks.add(t)

    async def _wrap(self, coro) -> None:
        try:
            await coro
        except BaseException as e:  # 子任务异常全部收集, 不逃逸
            self._errors.append(e)

    async def join(self) -> None:
        if self._tasks:
            await asyncio.gather(*self._tasks)  # 等全部子任务退出
        if self._errors:
            if sys.version_info >= (3, 11):
                raise ExceptionGroup("nursery 子任务失败", self._errors)  # 3.11+ 原生聚合
            # 3.9/3.10 没有内置 ExceptionGroup: 用普通异常携带列表聚合
            agg = RuntimeError(f"nursery 子任务失败: 共 {len(self._errors)} 个")
            agg.exceptions = self._errors  # 模拟 ExceptionGroup.exceptions
            raise agg


@asynccontextmanager
async def open_nursery():
    n = Nursery()
    try:
        yield n
    finally:
        await n.join()


async def child(name: str, delay: float, fail: bool = False) -> None:
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"{name} 失败")
    print(f"{name} 完成")


async def main() -> None:
    try:
        async with open_nursery() as n:
            await n.start_soon(child("fast", 0.05))
            await n.start_soon(child("slow", 0.15))
            await n.start_soon(child("bad", 0.08, fail=True))
    except BaseException as eg:  # 原生 ExceptionGroup 与模拟聚合都能接住
        for e in getattr(eg, "exceptions", [eg]):
            print("nursery 收集到:", repr(e))
    print("作用域结束: 所有子任务已被等待, 无任务逃逸")


if __name__ == "__main__":
    asyncio.run(main())
