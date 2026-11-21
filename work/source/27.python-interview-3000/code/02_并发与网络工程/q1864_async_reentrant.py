# -*- coding: utf-8 -*-
"""asyncio.Lock 不可重入: 嵌套获取死锁, 需要时自己实现可重入版。

- 内建 asyncio.Lock 没有属主概念, 同一任务重复 acquire 永远等不到自己释放;
- 死锁现场是 await 挂起, 没有异常没有日志, 只能靠 wait_for 兜底暴露;
- 可重入锁: 记住属主 task 与深度, 同任务重入只加计数, 退出计数归零才真正放锁。
"""
import asyncio


async def nested_acquire(lock):
    async with lock:
        await asyncio.sleep(0.01)
        async with lock:                       # 同一任务重复获取 -> 死锁
            return "nested-ok"


class AsyncReentrantLock:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._owner = None
        self._depth = 0

    async def acquire(self):
        me = asyncio.current_task()
        if self._owner is me:
            self._depth += 1                   # 重入只加计数
            return
        await self._lock.acquire()
        self._owner = me
        self._depth = 1

    async def release(self):
        me = asyncio.current_task()
        if self._owner is not me:
            raise RuntimeError("锁属于别的任务, 不能代为释放")
        self._depth -= 1
        if self._depth == 0:
            self._owner = None
            self._lock.release()

    async def __aenter__(self):
        await self.acquire()
        return self

    async def __aexit__(self, *exc):
        await self.release()


async def main():
    plain = asyncio.Lock()
    try:
        await asyncio.wait_for(nested_acquire(plain), timeout=0.4)
        raise AssertionError("不应到达这里")
    except asyncio.TimeoutError:
        print("内建 asyncio.Lock 嵌套获取: 死锁, 被 wait_for 兜底发现")

    rlock = AsyncReentrantLock()
    r = await asyncio.wait_for(nested_acquire(rlock), timeout=1.0)
    print("可重入锁嵌套获取:", r)
    assert r == "nested-ok"

    order = []

    async def user(tag):
        async with rlock:                      # 不同任务仍然互斥
            order.append(tag + "-in")
            await asyncio.sleep(0.02)
            order.append(tag + "-out")

    await asyncio.gather(user("A"), user("B"))
    print("两任务互斥序列:", order)
    assert order in (["A-in", "A-out", "B-in", "B-out"],
                     ["B-in", "B-out", "A-in", "A-out"]), "不同任务必须互斥"
    print("结论: 重入是属主特权, 互斥是任务间义务, 二者不冲突")


if __name__ == "__main__":
    asyncio.run(main())
