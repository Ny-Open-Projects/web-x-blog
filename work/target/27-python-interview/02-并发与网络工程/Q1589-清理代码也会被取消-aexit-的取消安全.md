---
title: [Q1589] 清理代码也会被取消:__aexit__ 的取消安全
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1589 · 清理代码也会被取消:__aexit__ 的取消安全

> 难度:★★★★ | 标签:asyncio, 取消, 清理

**问**:任务在 async with 里被取消时,清理代码(flush、commit)还保证执行吗?清理本身又被打断呢?

**答**:第一问有保证:CancelledError 在体内抛出时流经 __aexit__,finally 与资源释放一定执行——这是 async with 的契约。第二问没有保证:__aexit__ 里如果清理本身是慢 IO(它 await),下一次取消会把清理拦腰打断,留下半个事务。取消安全模式:清理交给 ensure_future 起独立任务,用 shield 保护;即便 shield 的等待被取消,except 里也要 await 把清理真正等完,再把取消上抛——语义变成"取消可以打断我,但不能打断我的收尾"。演示里双重取消(体内一次、清理中一次)也能保证 flush 完整落地。

```python
# file: code/02_并发与网络工程/q1589_aexit_cancel.py
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
```

**追问**:1) shield 里的任务在循环关闭时怎么办?——循环关闭前会取消所有残留任务,所以清理任务必须在 shutdown 流程里被显式 await,不能悬着。2) shield 的正确用法为什么是「护清理不护业务」?——shield 保护的内层任务是独立 Future,外层 await 被取消时内层继续跑;业务主体不该 shield(否则取消失效,任务杀不掉);清理段 shield+显式 await 完成再上抛——「取消可以打断我,但不能打断我的收尾」就是完整语义。3) 双重取消怎么防?——第二次 cancel 打在清理 await 上,except CancelledError 里继续 await 清理任务(它有 shield 保护,仍在跑),等完再 re-raise——要点是区分「外层等待被取消」与「清理任务本身被取消」。4) 生产陷阱?——清理任务用 fire-and-forget(没人 await,循环关闭时被取消,flush 丢失);shield 后忘记处理外层取消(取消被永久吞掉);__aexit__ 里再抛新异常盖掉原异常(要用 ExceptionGroup 或先保存原异常);认为「async with 一定完整执行清理」忽略清理本身可被取消。

---
