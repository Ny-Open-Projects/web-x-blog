---
title: [Q2406] run_coroutine_threadsafe:线程把协程寄回循环
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2406 · run_coroutine_threadsafe:线程把协程寄回循环

> 难度:★★★ | 标签:run_coroutine_threadsafe, 线程池, Future

**问**:线程池里的回调想用异步能力,怎么办?

**答**:协程只能跑在事件循环线程上,线程侧的正确姿势是 run_coroutine_threadsafe(coro, loop):协程被寄回循环执行,线程侧拿到 concurrent.futures.Future,用 result(timeout) 等待。

- 实测成功路径:线程侧提交、拿到"查询-done",concurrent Future 的语义与线程池一致;

- 实测异常路径:协程里的 ValueError 原样穿到线程侧的 result() 调用点,类型不丢;

- 实测超时路径:循环线程被占住时,线程侧 result(timeout=0.1) 抛 concurrent.futures.TimeoutError,注意 3.9 里它与内建 TimeoutError 不同,要显式捕获;

- 超时只是线程侧放弃等待,协程还在循环里,停机前要补收或取消,别留悬空任务。

```python
# file: code/02_并发与网络工程/q2406_run_coroutine_threadsafe.py
# -*- coding: utf-8 -*-
"""run_coroutine_threadsafe: 线程世界的代码, 把协程寄回事件循环执行。

- 线程池里的回调想调异步能力, 不能直接 await, 要把协程寄回循环线程;
- run_coroutine_threadsafe 返回 concurrent.futures.Future, 线程侧用 result 等待;
- 异常与超时都通过这个 Future 传递, 线程侧要处理超时与目标异常两种失败。
"""
import asyncio
import concurrent.futures
import threading
import time


async def async_job(name, seconds):
    await asyncio.sleep(seconds)
    if name == "boom":
        raise ValueError("异步侧的业务异常")
    return "%s-done" % name


def main_entry():
    loop = asyncio.new_event_loop()
    started = threading.Event()

    def loop_runner():
        asyncio.set_event_loop(loop)
        loop.call_soon(started.set)
        loop.run_forever()

    lt = threading.Thread(target=loop_runner, daemon=True)
    lt.start()
    started.wait(timeout=2)

    # 成功路径: 线程侧提交, 拿 concurrent Future 等结果
    fut = asyncio.run_coroutine_threadsafe(async_job("查询", 0.1), loop)
    res = fut.result(timeout=2.0)
    print("线程侧拿到:", res)

    # 异常路径: 协程里的 ValueError 原样穿到线程侧
    fut2 = asyncio.run_coroutine_threadsafe(async_job("boom", 0.05), loop)
    try:
        fut2.result(timeout=2.0)
        raise AssertionError("必须抛出异步侧异常")
    except ValueError as e:
        print("线程侧捕获:", e)

    # 超时路径: 循环被卡住时, 线程侧不能无限等
    def blocker():
        time.sleep(0.5)                      # 占住循环线程
    loop.call_soon(blocker)
    fut3 = asyncio.run_coroutine_threadsafe(async_job("卡住", 0.01), loop)
    try:
        fut3.result(timeout=0.1)
        raise AssertionError("应当超时")
    except concurrent.futures.TimeoutError:
        print("线程侧等待超时, 没有被卡死的循环拖住")
    # 超时只是线程侧放弃等待, 协程还在循环里, 停机前补收干净
    print("循环解封后补收:", fut3.result(timeout=1.5))

    loop.call_soon_threadsafe(loop.stop)
    lt.join(timeout=2)
    assert not lt.is_alive(), "循环要能干净地停下来"


if __name__ == "__main__":
    main_entry()
```

**追问**:1) 反过来,循环里想调阻塞函数呢?——run_in_executor 扔线程池,两座桥方向相反,别搭反了。 run_coroutine_threadsafe 的 Future 能 cancel 吗?——能,取消会被投回循环侧注入 CancelledError,与直接 cancel Task 等效。2) 两座桥的方向与超时语义?——线程→循环:run_coroutine_threadsafe(返回 concurrent Future);循环→线程:run_in_executor/to_thread(返回 asyncio Future)——「协程只能在循环线程跑」是两桥存在的根本原因;concurrent Future 的超时抛 concurrent.futures.TimeoutError(3.9 与内建 TimeoutError 不同,3.11+ 归一,要显式捕)。3) 超时后的悬空任务怎么收?——超时只是线程侧放弃,协程还在循环里跑:停机前补收(注册表 Q1588)或 cancel;与 as_completed 超时(Q2399)同构——「放弃等待≠任务终止」。4) 生产陷阱?——线程里直接 await(语法或语义错);超时后不收尾(悬空协程);异常类型捕获错(3.9 的双 TimeoutError);桥接方向搭反;result(timeout) 无限等(线程永久阻塞);concurrent Future 与 asyncio Future 混用 API(result/cancel 语义不同)。

---
