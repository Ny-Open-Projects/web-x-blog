---
title: [Q5621] call_soon 跨线程误用与回调丢失事故
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5621 · call_soon 跨线程误用与回调丢失事故

> 难度:★★★★☆ | 标签:事故复盘, 事件循环, 线程边界

**问**:工作线程里调 `loop.call_soon(cb)` 想把活儿丢回事件循环，多数时候"好像也能跑"，偶发回调永不执行。这是为什么？`call_soon` 与 `call_soon_threadsafe` 在唤醒机制上差在哪？正确的线程边界协议怎么写？

**答**:结论：`call_soon` 只做了"往 loop 自己的 `_ready` 队列 append"一件事，**不做线程唤醒**——它假设自己运行在 loop 所在线程。跨线程调用时两重风险：a) 非原子的 deque append 在 CPython 下勉强"看起来安全"，但若 loop 正阻塞在 `select/epoll` 上且没有新 fd 事件，它会**一直睡下去**，回调挂在队列里直到下一个不相关事件才被执行——这就是"偶发延迟数秒/永不执行"的来源；b) 没有内存屏障保证，其他线程写入的数据对 loop 可见性无保证。`call_soon_threadsafe` 多做两件事：队列操作 + **向 self-pipe 写一个字节**唤醒 epoll，回调立刻被调度。同类陷阱还有：`loop.call_later/call_at` 永远不是线程安全的（要用 `call_soon_threadsafe` 包一层），以及 `asyncio.run_coroutine_threadsafe(coro, loop)`（返回 concurrent Future，可跨线程等结果）。实战协议：**任何从别的线程触碰 loop 的 API 都必须带 threadsafe**，并在线程边界传递 `concurrent.futures.Future` 或 `queue.Queue`，而不是裸引用。

```python
import asyncio, threading, time

loop = asyncio.new_event_loop()
done = []

def run_loop():
    asyncio.set_event_loop(loop)
    loop.run_forever()

t = threading.Thread(target=run_loop, daemon=True)
t.start()
time.sleep(0.1)                       # 等 loop 起来并阻塞在 epoll

def cb():
    done.append("threadsafe")

# ---- 正确：call_soon_threadsafe 会写 self-pipe 唤醒 epoll ----
loop.call_soon_threadsafe(cb)
deadline = time.time() + 2
while not done and time.time() < deadline:
    time.sleep(0.01)
print("threadsafe 回调执行:", bool(done), f"（等待 {2-(deadline-time.time()):.2f}s 内完成）")

# ---- 错误示范：跨线程 call_soon（不唤醒，回调滞留） ----
def cb2():
    done.append("unsafe")
loop.call_soon(cb2)                   # 仅入队，loop 仍睡在 epoll 上
time.sleep(0.3)
print("0.3s 后 unsafe 回调执行了吗:", "unsafe" in done, "-> 仍滞留在 _ready 队列")

# 用一个无关事件把 loop 吵醒，滞留回调才被冲出来
loop.call_soon_threadsafe(lambda: None)
time.sleep(0.1)
print("无关唤醒后:", done)

# ---- 实战模板：线程 -> loop 传值并拿回结果 ----
async def work(x):
    await asyncio.sleep(0.05)
    return x * 2

fut = asyncio.run_coroutine_threadsafe(work(21), loop)   # 返回 concurrent.futures.Future
print("跨线程提交协程结果:", fut.result(timeout=2))
loop.call_soon_threadsafe(loop.stop)
```

**追问一层**:self-pipe 的写端满了怎么办？（pipe 缓冲 64KB，唤醒字节 1B 不可能满；真正的问题是 loop 不消费——这正是 Q5598 管道缓冲的边界场景，标准实现里 self-pipe 只在 loop 内读，不会溢出）。
**追问二层**:`loop.call_later` 跨线程为什么"看起来工作"却危险？（定时器只进 `_scheduled` 堆且不唤醒；loop 睡眠时长按堆顶定时器算，若堆顶很远，新近的定时器要等 loop 醒来才被看到，超时可能整体延后）。
**追问三层**:如何在 review 中制度性防这类 bug？（封装"唯一入口"：线程侧只允许 `run_coroutine_threadsafe` / `call_soon_threadsafe` 两个 API，lint 禁用其余 loop API 的跨线程调用）。

## 背诵要点
- `call_soon` 非线程安全：只入队不唤醒，跨线程回调可能滞留到下一个无关事件。
- `call_soon_threadsafe` = 入队 + self-pipe 写 1B 唤醒 epoll；跨线程提交协程用 `run_coroutine_threadsafe`（返回 concurrent Future）。
- `call_later/call_at` 也非线程安全；线程侧 API 收口为两个 threadsafe 入口。

## 复盘追问
- 服务偶发"回调延迟 30 秒"，如何用 asyncio debug 日志/loop 时间戳证明是未唤醒而不是慢回调？
- 线程池任务完成后再触发异步上报，你会在 worker 里写哪一行代码？为什么不用 `loop.call_later`？
