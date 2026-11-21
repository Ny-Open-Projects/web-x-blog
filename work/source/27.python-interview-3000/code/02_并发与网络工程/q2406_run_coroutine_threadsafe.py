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
