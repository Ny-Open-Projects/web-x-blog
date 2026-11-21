---
title: [Q079] time.sleep vs asyncio.sleep
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q079 · time.sleep vs asyncio.sleep

> 难度:★★☆ | 标签:asyncio, 阻塞陷阱

**问**:在协程里误用 time.sleep 会发生什么?如何发现和规避这类阻塞?

**答**:time.sleep 阻塞整个事件循环线程,期间所有协程、所有定时器都停摆;asyncio.sleep 只挂起当前协程,循环继续跑别的任务。排查手段:开启 `loop.set_debug(True)`(慢回调警告)、Python 3.12+ 的 asyncio debug 工具,或监控中告警事件循环延迟。规避:换 async 库(aiohttp 而非 requests),无法替换的阻塞调用丢进线程池 `run_in_executor`。

```python
# file: code/02_并发与网络工程/q079_sleep_trap.py
import asyncio
import time


async def ticker() -> None:
    for i in range(6):
        print(f"tick {i}")
        await asyncio.sleep(0.1)


async def bad_blocker() -> None:
    print("坏例子: time.sleep 0.3s, ticker 应该卡住")
    time.sleep(0.3)


async def good_blocker() -> None:
    print("好例子: run_in_executor, ticker 继续跳")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, time.sleep, 0.3)


async def main() -> None:
    await asyncio.gather(ticker(), bad_blocker())
    await asyncio.gather(ticker(), good_blocker())


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- 怎么自动发现协程里的阻塞调用?——`loop.set_debug(True)` 配合 `slow_callback_duration` 阈值,超过的回调打警告;线上再加事件循环延迟指标。
- asyncio.to_thread 和 run_in_executor 的区别?——to_thread(3.9+)用默认线程池的便捷封装;run_in_executor 可指定自定义池、控制大小与生命周期。
- 哪些「看似无害」的调用实际阻塞?——requests、time.sleep、大文件同步读写、CPU 密集 pandas/正则回溯;要么换 async 库,要么下放线程/进程池。

---
