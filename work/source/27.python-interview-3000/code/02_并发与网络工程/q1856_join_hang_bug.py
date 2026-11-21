# -*- coding: utf-8 -*-
"""join 永久阻塞的经典事故: worker 死前忘了 task_done, 计数永远回不到零。

- 事故链: 某条数据触发 worker 抛异常 -> 该次 get 没有 task_done -> 未完成计数卡住;
- join 无限等, 表面像 "任务丢了", 实质是队列计数器的账没平;
- 修复: 处理逻辑放进 try/finally, task_done 放 finally, 成败都记账;
- 排查手段: join 永远套 wait_for, 把永久阻塞变成可观测的超时。
"""
import asyncio


async def buggy_worker(q, results):
    while True:
        item = await q.get()
        if item == 7:
            raise ValueError("毒丸数据 7, worker 当场死亡")   # 没有 task_done!
        await asyncio.sleep(0.003)
        results.append(item)
        q.task_done()


async def fixed_worker(q, results):
    while True:
        item = await q.get()
        try:
            if item == 7:
                raise ValueError("毒丸数据 7")
            await asyncio.sleep(0.003)
            results.append(item)
        finally:
            q.task_done()                              # 成败都记账


async def run(worker_fn):
    q = asyncio.Queue()
    results = []
    workers = [asyncio.create_task(worker_fn(q, results)) for _ in range(2)]
    for i in range(20):
        await q.put(i)
    try:
        await asyncio.wait_for(q.join(), timeout=1.0)
        ok = True
    except (asyncio.TimeoutError, TimeoutError):
        ok = False                                     # join 永久阻塞的实锤
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    return ok, results


async def main():
    ok1, r1 = await run(buggy_worker)
    print("有 bug 版: join 在 1s 内返回吗 -> %s, 已处理 %d 条"
          % (ok1, len(r1)))
    assert ok1 is False, "毒丸吃掉一次 task_done, join 必然超时"

    ok2, r2 = await run(fixed_worker)
    print("修复版  : join 返回 -> %s, 已处理 %d 条(毒丸被记账但跳过)"
          % (ok2, len(r2)))
    assert ok2 is True and len(r2) == 19, "除毒丸外全部处理完成"

    print("结论: join 卡死先查 task_done 账目, finally 是唯一的保险")


if __name__ == "__main__":
    asyncio.run(main())
