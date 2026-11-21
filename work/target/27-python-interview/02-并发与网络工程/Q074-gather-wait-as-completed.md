---
title: [Q074] gather / wait / as_completed 对比
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q074 · gather / wait / as_completed 对比

> 难度:★★★ | 标签:asyncio, gather, wait, as_completed

**问**:asyncio 的 gather、wait、as_completed 各适合什么场景?

**答**:`gather` 按提交顺序返回结果列表,默认一个异常会导致整体取消(可 return_exceptions=True),适合"全部完成取全部结果";`wait` 返回 done/pending 两个集合,支持 FIRST_COMPLETED 等触发条件,适合"任一完成就行动";`as_completed` 按完成顺序逐个产出,适合流式处理和整体超时。

```python
# file: code/02_并发与网络工程/q074_gather_wait_as_completed.py
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
```

**追问**:
- gather(return_exceptions=True) 的结果怎么判断成败?——成功值与异常对象混排在结果列表里,逐个 `isinstance(x, Exception)` 分类处理。
- 什么场景必须用 wait?——需要 FIRST_COMPLETED/FIRST_EXCEPTION 触发的竞赛与快速失败模式,gather 表达不了。
- gather 会不会创建 Task?——传入协程会被包装成 Task;传入已有 Task 时,取消 gather 也会取消它们,生命周期要心里有数。

---
