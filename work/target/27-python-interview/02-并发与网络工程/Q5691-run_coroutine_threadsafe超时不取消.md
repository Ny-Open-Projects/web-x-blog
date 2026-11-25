---
title: "[Q5691] run_coroutine_threadsafe 超时不会取消协程：cancel 只是协作式请求"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5691 · run_coroutine_threadsafe 超时不会取消协程：cancel 只是协作式请求

难度：P7 ｜ 标签：asyncio、run_coroutine_threadsafe、跨线程、取消语义、超时

**问**：同步线程里用 `asyncio.run_coroutine_threadsafe(coro, loop)` 调异步写入，`future.result(timeout=0.1)` 抛 `TimeoutError`，接口返回 504，可协程照样跑完并写了数据库。`cancel()` 有时返回 `True`，副作用却也发生了。`result(timeout=)` 到底会不会停任务？`cancel()` 成功代表什么？什么情况下"取消成功"但业务已经落地？

**答**：
结论：三层语义必须拆开。a) `result(timeout=)` 只控制**当前线程等多久**，超时抛异常，对事件循环里的 Task 没有任何影响，协程继续跑——这是"超时 ≠ 取消"的根源。b) `cancel()` 作用在返回的 `concurrent.futures.Future` 上，`_chain_future` 会把这个取消**传播**给源 Task（`source.cancel()`），所以对"正常让出控制权"的协程，它确实能停。c) 但 asyncio 的取消是**协作式**的：取消只是在下一次可中断点抛 `CancelledError`，协程若捕获后不重抛（清理逻辑、`except Exception` 之外的宽泛捕获、shield 保护段），Task 会继续跑完并提交，而 `cancel()` 早已返回 `True`。

取舍：a) 超时后必须显式 `cancel()`，否则幽灵任务会一直跑到结束；b) 不要用 `cancel()` 的返回值判断"业务没发生"——它只表示"取消请求已发出/已置位"，真正的判据是 Task 最终状态与业务幂等键；c) 协程内的 `finally` 清理要短、要可被取消，长清理用 `asyncio.shield` 保护关键段落，但要清楚 shield 段内取消会被延迟而不是生效；d) 跨线程 API 的超时值要大于内部最坏耗时，并配合幂等键，避免"结果未知"导致重复写。

实战：事故形态是"网关线程 100ms 超时返回 504，用户重试三次；后台三个协程都写完了，账单出现三倍扣款，而日志里 `cancel()` 全是 True"。下面演示：只超时不停、cancel 能停正常协程、以及吞掉 `CancelledError` 后 cancel 成功但副作用照常发生。

```python
import asyncio
import threading

state = {"timed_out": False, "cancelled": False, "stubborn": False}
ev1, ev2, ev3 = threading.Event(), threading.Event(), threading.Event()


async def commit(flag, started):
    started.set()
    await asyncio.sleep(0.3)
    state[flag] = True
    return "committed"


async def stubborn_commit():
    ev3.set()
    try:
        await asyncio.sleep(0.2)
    except asyncio.CancelledError:
        print("[6] 捕获 CancelledError 后没有重抛，继续清理")
        await asyncio.sleep(0.05)
    state["stubborn"] = True
    return "committed-anyway"


loop = asyncio.new_event_loop()
thread = threading.Thread(target=loop.run_forever, daemon=True)
thread.start()

# 1) 只超时，不 cancel
fut = asyncio.run_coroutine_threadsafe(commit("timed_out", ev1), loop)
ev1.wait()
try:
    fut.result(timeout=0.1)
except TimeoutError:
    print("[1] 0.1s 超时返回，协程仍在跑")
threading.Event().wait(0.4)
print("[2] 未 cancel -> 副作用已发生:", state["timed_out"])

# 2) 超时后显式 cancel：正常协程会被停住
fut2 = asyncio.run_coroutine_threadsafe(commit("cancelled", ev2), loop)
ev2.wait()
try:
    fut2.result(timeout=0.1)
except TimeoutError:
    print("[3] 第二个任务超时")
print("[4] cancel() ->", fut2.cancel())
threading.Event().wait(0.4)
print("    取消后副作用是否发生:", state["cancelled"])

# 3) 协程吞掉 CancelledError：cancel 返回 True，但业务照常完成
fut3 = asyncio.run_coroutine_threadsafe(stubborn_commit(), loop)
ev3.wait()
print("[5] cancel() ->", fut3.cancel(), "（请求已发出）")
threading.Event().wait(0.4)
print("[7] 副作用仍然发生:", state["stubborn"])

loop.call_soon_threadsafe(loop.stop)
thread.join()
loop.close()
```

**追问一**：`cancel()` 返回 `True`/`False` 分别代表什么？—— `True` 表示 future 当时是 `PENDING`，已置为 `CANCELLED` 并把取消传播给 Task；`False` 表示已经 `FINISHED`（结果已抄写），取消来得太晚。但 `True` 只说明"请求送达"，不说明"协程已停"——本卡第三段就是反例：Task 捕获了 `CancelledError` 后继续执行，最终仍然提交。判断业务是否落地要看数据库/幂等键，不看 future 状态。

**追问二**：为什么协程会"吞掉"取消？—— 常见三种：`try/except Exception` 虽然接不住 `CancelledError`（3.8 起它是 `BaseException`），但 `except BaseException` 或裸 `except:` 会接住；二是 `finally` 里写了长耗时的同步清理或再次 `await`（若期间又收到取消，清理本身会被打断，反而留下半成品）；三是 `asyncio.shield` 保护段让取消延迟到 shield 结束。规范做法是：捕获 `CancelledError` 只做最小清理并**立即重抛**，不要把"取消"当成业务异常处理。

## 背诵要点
- `result(timeout=)` 只影响等待，不取消 Task；超时后必须显式 `cancel()`。
- `cancel()` 经 `_chain_future` 传播给 Task，返回 `True` 仅表示请求送达，不代表协程已停。
- 取消是协作式的：吞掉 `CancelledError` / shield 段会让副作用照常发生；判据是幂等状态而非 future 状态。

## 复盘追问
- 接口 504 后仍写库，日志里 `cancel()` 却是 True，如何解释？（超时≠取消；取消是请求）
- 如何在跨线程调用中保证"超时后不产生重复副作用"？（显式 cancel + 幂等键 + 内部超时预算）
