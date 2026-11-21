---
title: [Q609] asyncio 调试模式:揪出慢回调与未 await
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q609 · asyncio 调试模式:揪出慢回调与未 await

> 难度:★★★☆ | 标签:asyncio debug, 诊断, 慢回调

**问**:async 服务时不时卡一下,怎么用 asyncio 自带的调试设施定位?

**答**:三件套:1) `loop.set_debug(True)`(或环境变量 PYTHONASYNCIODEBUG=1)开启:未 await 的协程、跨线程误用、非阻塞 fd 上跑阻塞调用等都会告警;2) 慢回调检测:`loop.slow_callback_duration = 0.1` 后,任何超过 100ms 的回调(包括忘了 await 的阻塞调用)会打日志并给出创建时的 traceback——这依赖 debug 模式记录协程创建点;3) `loop.get_debug()` + logging 配置让告警可见。配合 `asyncio.all_tasks()` 在卡顿瞬间打印所有任务栈,基本能锁定卡源头。

```python
# file: code/02_并发与网络工程/q609_asyncio_debug.py
import asyncio
import logging
import time

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")


async def suspicious_task() -> None:
    time.sleep(0.3)  # 错误: async 函数里的阻塞调用


async def fast_task() -> None:
    await asyncio.sleep(0.01)


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.set_debug(True)                 # 打开 asyncio 调试
    loop.slow_callback_duration = 0.1    # 超过 100ms 的回调告警

    # 未 await 的协程: debug 模式会记录创建点并告警
    asyncio.ensure_future(fast_task())   # 有引用? ensure_future 返回值被丢弃 — 演示告警
    coro = fast_task()                   # 创建但从未 await
    del coro

    await suspicious_task()  # 触发 "Executing <Task ...> took 0.3s" 告警
    await fast_task()

    # 卡顿现场排查: 打印所有任务栈
    for t in asyncio.all_tasks():
        if t is not asyncio.current_task():
            print(f"任务 {t.get_name()} 状态 {t._state}")
    print("调试输出应包含 Executing ... took 与 never awaited 告警")


asyncio.run(main())
```

**追问**:1) 生产环境开 debug 模式安全吗?——有额外内存与 CPU 开销(记录协程创建栈),建议灰度/压测环境开,或只在收到卡顿告警时对单个实例临时开启。2) debug 模式检测的四类问题?——回调超 slow_callback_duration(默认 0.1s)、未 await 协程、callback 未从 yield、非线程安全 API 误用(跨线程);loop.slow_callback_duration 可调。3) 诊断工作流?——告警→单实例开 debug→复现→看日志定位慢回调/未 await→修复→关;与 py-spy/aiomonitor 配合(Q475/571)。4) 生产陷阱?——生产常开(成本);debug 日志被日志级别吞掉;只修症状不找「为什么回调慢」。

---
