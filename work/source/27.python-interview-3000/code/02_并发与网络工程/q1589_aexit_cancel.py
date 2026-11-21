"""清理代码也会被取消: __aexit__ 的取消安全。

任务在 async with 体内被取消时, CancelledError 会流经 __aexit__。
如果清理本身是慢 IO(flush、commit), 它也可能被下一次取消打断,
留下"半个事务"。模式: 清理交给 ensure_future, 用 shield 保护,
就算 shield 被取消, 也要先 await 把清理等完再上抛取消。
"""
import asyncio


class Resource:
    def __init__(self, name):
        self.name = name
        self.flushed = False

    async def flush(self):
        await asyncio.sleep(0.1)            # 清理本身是慢 IO
        self.flushed = True

    async def __aenter__(self):
        print("acquire", self.name)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        task = asyncio.ensure_future(self.flush())
        cancelled_during_cleanup = False
        try:
            await asyncio.shield(task)      # shield: 别让取消打断清理
        except asyncio.CancelledError:
            cancelled_during_cleanup = True
            await task                      # 即便被取消, 也等 flush 落地
            raise                           # 然后把取消继续上抛
        print("flush 完成 %-4s 清理期间被取消: %s"
              % (self.name, cancelled_during_cleanup))


async def hold(resource, seconds):
    async with resource:
        await asyncio.sleep(seconds)        # 在体内被取消


async def main():
    # 场景 1: 体内被取消, 清理必须完整执行
    r1 = Resource("db-1")
    t1 = asyncio.create_task(hold(r1, 0.5))
    await asyncio.sleep(0.05)
    t1.cancel()
    try:
        await t1
        raise AssertionError("任务应已取消")
    except asyncio.CancelledError:
        pass
    assert r1.flushed, "场景 1: 取消穿透后 flush 必须完整"

    # 场景 2: 清理进行中又被取消一次(双重取消)
    r2 = Resource("db-2")
    t2 = asyncio.create_task(hold(r2, 0.5))
    await asyncio.sleep(0.05)
    t2.cancel()                             # 打断体内
    await asyncio.sleep(0.02)
    t2.cancel()                             # 打断清理中的 shield
    try:
        await t2
        raise AssertionError("任务应已取消")
    except asyncio.CancelledError:
        pass
    assert r2.flushed, "场景 2: 双重取消也不能丢下半个事务"

    print("结论: 两次取消都干净落地——清理不是普通代码, 它是恢复点")


if __name__ == "__main__":
    asyncio.run(main())
