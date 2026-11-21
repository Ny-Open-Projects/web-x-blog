---
title: [Q2888] 上下文变量的任务隔离:ContextVar 的传播边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2888 · 上下文变量的任务隔离:ContextVar 的传播边界

> 难度:★★★☆☆ | 标签:contextvars, asyncio, 线程

**问**:要在协程和线程里分别存「当前请求 ID」,threading.local 有什么问题?ContextVar 是怎么解决任务隔离的?

**答**:`threading.local` 以**线程**为隔离边界,协程场景下同一个线程串行跑成百上千个任务,前一个任务 set 的值会泄漏给后一个任务,这正是 Q1281 讲过的请求上下文串号事故。`ContextVar` 以**上下文**为边界:每个 asyncio Task 启动时复制当前上下文,任务里 set 只改自己的副本,await 之后读到的仍是本任务的值——三个并发任务各自拿到 A-req、B-req、C-req,任务之外仍是默认值。线程场景 ContextVar 同样成立,每个线程有独立上下文,线程里的 set 不影响主线程。传播方向是单向的:父上下文复制给任务,子任务写不回父;这正是日志 trace、请求 ID、事务标记想要的语义。

```python
# file: code/01_语言核心与底层/q2888_contextvar_isolation.py
"""上下文变量的任务隔离:ContextVar 在协程与线程里的传播边界。"""
import asyncio
import threading
from contextvars import ContextVar

request_id = ContextVar("request_id", default="-")


async def handle(tag):
    request_id.set(f"{tag}-req")
    await asyncio.sleep(0.01)
    # await 之后仍看到本任务 set 的值:任务启动时复制了上下文
    return request_id.get()


async def main():
    results = await asyncio.gather(handle("A"), handle("B"), handle("C"))
    print("协程任务各自隔离:", results)
    print("任务外仍是默认值:", request_id.get())


def thread_worker(tag, out):
    out[tag] = request_id.get()          # 线程读自己上下文里的值
    request_id.set(f"{tag}-req")         # 只影响本线程


if __name__ == "__main__":
    asyncio.run(main())

    out = {}
    threads = [threading.Thread(target=thread_worker, args=(t, out)) for t in ("T1", "T2")]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("线程各自读到默认值:", out)
    print("主线程不受影响:", request_id.get())
```

**追问**:1) 把协程里的活儿丢进线程池,上下文还跟过去吗?——不跟,run_in_executor 在新线程里跑新上下文;需要时用 contextvars.copy_context 拿到副本,再以 ctx.run(func) 显式带过去。2) 传播边界的完整清单?——Task 创建拷贝快照(Q1281);线程池/子进程不带;第三方库回调可能丢上下文——横切信息(请求 id)显式传参比依赖隐式传播更稳。3) 与 threading.local 的对照?——contextvars 是协程粒度、Task 隔离;threading.local 是线程粒度、同线程协程共享(Q1281);混用两者的代码要明确边界。4) 生产陷阱?——日志/链路追踪 id 在线程池里丢失;依赖「隐式传播」跨边界;忘记 reset 污染下一请求。
