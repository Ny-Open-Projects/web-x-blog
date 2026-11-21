---
title: [Q420] asyncio 调试模式:慢回调、未 await 与循环堵塞
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q420 · asyncio 调试模式:慢回调、未 await 与循环堵塞

> 难度:★★★★☆ | 标签:asyncio, 调试, asyncio.run

**问**:`asyncio.run(main(), debug=True)` 到底打开了哪些检查?"Executing <Handle ...> took 0.25 seconds" 警告的阈值哪来的?协程对象没 await 为什么只在销毁时警告?

**答**:debug 模式开启四类检测:(1) **慢回调检测**——任何回调/任务步进超过 `loop.slow_callback_duration`(默认 0.1s)就打日志并附 traceback,这是定位"事件循环被同步代码堵塞"的第一工具;(2) 未 await 协程在销毁时记录创建点 traceback(默认只警告位置,debug 补全来源);(3) 非线程安全 API 跨线程调用直接报错(如从其他线程直接 `loop.call_soon` 而非 `call_soon_threadsafe`);(4) Future/Task 构造时记录来源栈,便于追查"谁创建的"。配套手段:`loop.set_debug(True)`、`PYTHONASYNCIODEBUG=1`、3.12 的 `asyncio.eager_task_factory`(降低任务启动延迟)。生产上还可以用 `loop.set_exception_handler` 统一收集 never-retrieved 异常,以及 `sampler` 类工具(如 py-spy)直接抓被堵塞循环的栈。

```python
# file: code/01_语言核心与底层/q420_asyncio_debug.py
import asyncio
import gc
import logging
import time

logging.basicConfig(level=logging.WARNING)

async def blocker():
    time.sleep(0.3)            # 同步阻塞整个事件循环 —— debug 会点名

async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.05    # 阈值默认 0.1s,调低更敏感
    await blocker()            # 警告: Executing <Task ...> took 0.3 seconds

# debug=True 同时开启 慢回调检测 未await协程来源 非线程安全检测
asyncio.run(main(), debug=True)

# 未 await 协程:协程对象销毁时警告,debug 版会附创建 traceback
coro = blocker()
del coro                      # 触发 coroutine was never awaited
gc.collect()
```

**追问**:1) `slow_callback_duration` 计的什么?——单次回调(任务步进/定时器回调)的同步执行时长,await 让出点之间的每一段分别计。2) 怎么区分"阻塞在 C 扩展"和"阻塞在纯 Python"?——py-spy dump 看栈:停在扩展帧说明 GIL 被 C 代码持有,停在 Python 帧则检查该协程里是否混入同步 IO。
