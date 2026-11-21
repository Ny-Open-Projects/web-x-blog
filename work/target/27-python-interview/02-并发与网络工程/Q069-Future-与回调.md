---
title: [Q069] Future 与回调
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q069 · Future 与回调

> 难度:★★★ | 标签:concurrent.futures, Future

**问**:Future 对象承载了什么信息?add_done_callback 在哪个线程执行?

**答**:Future 是"一个尚未完成的结果"的占位:保存执行状态、返回值、异常,提供 result/get、done、cancel、add_done_callback 等接口。回调在任务完成的线程里执行(线程池是 worker 线程,进程池是结果处理线程),因此回调里不要再做重活或直接更新 UI。result() 会阻塞并重新抛出任务异常。

```python
# file: code/02_并发与网络工程/q069_future_callback.py
import time
from concurrent.futures import ThreadPoolExecutor


def slow_task(n: int) -> int:
    time.sleep(0.2)
    if n == 2:
        raise ValueError("任务 2 故意失败")
    return n * 10


def on_done(fut) -> None:
    if fut.exception() is not None:
        print(f"回调: 任务失败 {fut.exception()!r}")
    else:
        print(f"回调: 任务成功, 结果 {fut.result()}")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(slow_task, i) for i in range(4)]
        for fut in futures:
            fut.add_done_callback(on_done)
        # 阻塞等待全部结束
        results = [fut.result() if fut.exception() is None else None for fut in futures]
        print("收集结果:", results)
```

**追问**:
- add_done_callback 的回调里抛异常会怎样?——被 Future 吞掉,GC 时才打印;回调内必须自己 try/except 并记录。
- Future.cancel 什么时候成功?——任务还没开始执行才可取消;线程池里已在运行的任务无法强停,只能协作式检查退出标志。
- 回调在哪个线程执行,要注意什么?——完成它的 worker 线程(或结果处理线程);回调里访问共享数据要加锁,别再做重活。

---
