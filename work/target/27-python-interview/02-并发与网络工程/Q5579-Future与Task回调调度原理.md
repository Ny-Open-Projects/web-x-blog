---
title: [Q5579] Future 与 Task 的回调调度原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5579 · Future 与 Task 的回调调度原理

> 难度:★★★★ | 标签:原理深挖, asyncio, Future, Task

**问**：`Future` 的状态机有哪些状态转换？`add_done_callback` 注册的回调什么时候真正执行——是在 set_result 的调用线程里同步跑吗？`Task` 怎么把协程和 Future 缝起来（`__step`/`__wakeup` 与 `call_soon` 的循环）？为什么 `await future` 有时要"让出控制权一轮"才看到结果，即"协程看到的结果总是落后一拍"的问题出在哪？

**答**：结论：Future 是"**一次性结果容器 + 回调分发器**"：内部状态 `_PENDING → _CANCELLED / _FINISHED`，`set_result` 做三件事——检查状态防重设（二次 set_result 抛 InvalidStateError）、记录结果、把 `_callbacks` 里每个回调经 `loop.call_soon` **投递到事件循环下一轮执行**。关键设计：回调**不在 set_result 调用方线程同步执行**，统一经 call_soon 排队（线程安全版 `call_soon_threadsafe` 还会唤醒 selector），保证回调永远在 loop 线程串行跑，消除并发重入。Task 是"自驱协程机器"：`Task.__step` 启动协程，协程 `await` 一个未完成 Future 时，`Task.__wakeup` 被 `future.add_done_callback` 注册；Future 完成后 `__wakeup` 经 call_soon 回到 loop，把结果/异常 `coro.send/throw` 回协程，协程跑到底（Done）或再次 await（再注册）。"落后一拍"的机制解释：`set_result` 后回调入队，**当前这轮循环里 await 该 future 的协程还没恢复**——如果代码在 `set_result` 后立刻读 task.result() 能拿到值（结果已存），但协程体没继续跑；错误模式是同步代码里 set 完就期待协程副作用已发生（如数据库已写、状态已改），实际要等下一轮 `call_soon` 消费回调。实战守则：a) 回调里做轻活、重活丢 task（`loop.create_task(handle())`）；b) 跨线程 set 结果用 `loop.call_soon_threadsafe(fut.set_result, v)`（Q5561 上下文传播同理）；c) 测试里 `await asyncio.sleep(0)` 的一轮让出正是为了消化这些排队的回调。

```python
# file: code/02_并发与网络工程/q5579_future_task.py
import asyncio, sys, threading

async def main():
    loop = asyncio.get_running_loop()

    # 1) Future 状态机: set_result 只能一次
    fut = loop.create_future()
    order = []
    fut.add_done_callback(lambda f: order.append("callback"))    # 回调排队
    fut.set_result(42)                                            # 已 FINISHED
    try:
        fut.set_result(43)
    except asyncio.InvalidStateError as e:
        print("二次 set_result:", type(e).__name__)
    print("set 后立刻读 result:", fut.result(), "| 协程回调已执行吗:", order)

    await asyncio.sleep(0)                                        # 让出一轮
    print("一轮让出后回调执行:", order, "(落后一拍: call_soon 排队所致)")

    # 2) Task 缝合原理: await future -> __wakeup 经 call_soon 恢复
    async def worker(f):
        v = await f                       # __step 遇未完成 future -> 挂起注册 __wakeup
        return ("got", v)
    t = asyncio.create_task(worker(fut2 := loop.create_future()))
    await asyncio.sleep(0)                # 让 task 跑到 await 处挂起
    fut2.set_result("data")               # 结果已存, 但协程还没恢复
    print("set_result 后协程 done 吗:", t.done())
    await asyncio.sleep(0)                # 消费 __wakeup 回调
    await asyncio.sleep(0)
    print("再让一轮后:", t.done(), t.result())

    # 3) 回调不在 set_result 线程同步执行: 跨线程演示
    fut3 = loop.create_future()
    def from_thread():
        loop.call_soon_threadsafe(fut3.set_result, "from-thread")   # 线程安全投递
    threading.Thread(target=from_thread).start()
    print("跨线程结果:", await fut3)

asyncio.run(main())

# 4) 源码级佐证: set_result -> schedule_callbacks -> call_soon
import asyncio.base_events, inspect, asyncio.futures
src = inspect.getsource(asyncio.futures.Future._schedule_callbacks)
print("源码佐证: 回调经 _call_soon 投递 =", "_call_soon" in src)
print("python:", sys.version.split()[0])
```

**追问**：1) `Task.__step` 里的异常路径怎么走？——`coro.send` 抛 StopIteration = 协程完成，取 `.value` set_result；抛其他异常 = `task.set_exception`，同时 **Task 把异常存着不抛**，如果没人 await 这个 Task，3.12 前只会在 GC 时打"exception was never retrieved"日志，TaskGroup（Q5503）就是为了强制聚合这些异常而生的。2) `await asyncio.sleep(0)` 为什么能推进回调？——sleep(0) 让协程挂起并经 `call_soon` 重排到队列尾，这轮循环里先执行完所有已排回调（包括 future 的 `__wakeup`），协程再恢复——它是"消化一拍"的惯用手法；依赖它写测试是味道，说明生产代码里也可能有对时序的隐式依赖。3) eager_task_factory（3.12，Q5502）改变了什么？——创建 Task 时**同步**先跑一步协程，若立即完成则省掉整轮 call_soon 调度，本卡的"落后一拍"在该优化下部分消失——但语义保证不变（回调仍经 loop），只是常见快路径不再付调度成本。

## 背诵要点
- Future 状态机 `_PENDING→FINISHED/CANCELLED`，set_result 防重设（InvalidStateError），回调经 call_soon 投递到 loop 下一轮，永不在调用线程同步执行。
- Task = `__step` 启动 + await 未完成 future 时挂起注册 `__wakeup`，完成经 call_soon 恢复 send/throw；未 await 的 Task 异常只在 GC 时告警（TaskGroup 补洞）。
- "落后一拍"= 结果已存但协程恢复靠下一轮回调；测试用 sleep(0) 消化，3.12 eager_task_factory 把快路径的调度轮省掉。

## 复盘追问
- 你们有没有"set_result 之后协程里的写库还没执行"这类时序事故？（提示：把跨线程同步 set 结果改为 await 或事件式同步，副作用断言放在 await 之后）
- done_callback 里做过重活导致 loop 抖动吗？（提示：回调只投递轻任务，重逻辑 create_task 化，配合 Q5524 慢回调监控）
