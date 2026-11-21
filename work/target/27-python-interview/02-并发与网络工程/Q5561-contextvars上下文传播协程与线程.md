---
title: [Q5561] contextvars 上下文在协程与线程间的传播
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5561 · contextvars 上下文在协程与线程间的传播

> 难度:★★★★★ | 标签:原理深挖, contextvars, 请求上下文, 链路追踪

**问**：trace_id 用 threading.local 在 asyncio 下全串了——同一个 worker 的所有请求共享同一个值。为什么 `threading.local` 在协程模型下失效？`contextvars.ContextVar` 的复制语义是什么？在 Task、线程池（run_in_executor）、Request Handler 三条边界上各怎么传播？

**答**：结论：`threading.local` 的粒度是**线程**，asyncio 单线程跑所有协程，全协程共享一份 → 请求 A 设置的 trace_id 被请求 B 覆盖。`contextvars.ContextVar` 的粒度是**上下文（Context）**：每个 Task 创建时**浅拷贝**当前 Context，之后 Task 内 set 只影响自己的副本（快照语义，解决交叉写）；ContextVar.set 后整个 Task 内可见，这正是 APM 库（opentelemetry、sentry）打 trace_id 的标准机制。三条边界的规则：a) **asyncio.create_task**：自动拷贝当前上下文——在 await 前后 set 的时机要注意，"创建 Task 后再 set，子 Task 看不到"；b) **run_in_executor / to_thread**：asyncio 自动把当前 Context 带进线程（3.8+ to_thread 语义显式），线程里 set 改的是线程的副本，**改不回主协程**；c) **手动线程**（threading.Thread）：不自动传播，要显式 `ctx = contextvars.copy_context(); threading.Thread(target=lambda: ctx.run(fn))`。坑：uvicorn/ASGI 每请求建 Task，ContextVar 天然隔离；但**中间件里全局 set 不 copy** 就会漏；另一个经典坑是 ContextVar 存可变对象——快照的是引用，两个 Task 改同一个 list 仍然互相污染，要存不可变值或进 set 前拷贝。

```python
# file: code/02_并发与网络工程/q5561_contextvars.py
import asyncio, contextvars, threading

trace_id: contextvars.ContextVar[str] = contextvars.ContextVar("trace_id", default="-")

async def handle(name):
    trace_id.set(name)                     # 每个 Task 自己的副本
    await asyncio.sleep(0.01)
    await sub()
    await asyncio.to_thread(sync_work)     # Context 自动跟到线程
    return trace_id.get()

async def sub():
    await asyncio.sleep(0.01)
    print(f"  sub sees: {trace_id.get()}")  # 同 Task 内可见

def sync_work():
    print(f"  thread sees: {trace_id.get()}")   # to_thread 自动传播

async def main():
    # 并发两个请求: 互不污染(threading.local 会串)
    r = await asyncio.gather(handle("req-A"), handle("req-B"))
    print("返回值:", r)

asyncio.run(main())

# 1) 经典坑: create_task 之后再 set, 子 Task 看不到
async def pitfall():
    outer = contextvars.ContextVar("v", default="old")
    t = asyncio.create_task(asyncio.sleep(0))
    outer.set("new")
    await t
    print("create_task 前创建 -> 子 Task 用快照:", end=" ")
    async def read():
        print(outer.get())
    await asyncio.create_task(read())

asyncio.run(pitfall())

# 2) 手动线程不自动传播: 用 copy_context().run
ctx = contextvars.copy_context()
trace_id.set("req-C")
def worker():
    ctx.run(lambda: print("手动线程显式传播:", trace_id.get()))()
t = threading.Thread(target=worker); t.start(); t.join()

# 3) 存可变对象: 快照的是引用, 依旧互相污染
bad: contextvars.ContextVar[list] = contextvars.ContextVar("bad", default=[])
async def mutate(tag):
    bad.get().append(tag)
    await asyncio.sleep(0.01)
    print(f"  {tag} sees list: {bad.get()}")

async def main_mutate():
    await asyncio.gather(mutate("A"), mutate("B"))
asyncio.run(main_mutate())
print("结论: ContextVar 存不可变值; set 时机在 create_task 之前")
```

**追问**：1) Context 的快照是浅拷贝，那 HVAR 底层存什么？——Context 是"var → 值"的不可变映射（CPython 用 HAMT 持久化数据结构），set 产生新映射 O(log n)，拷贝 O(1)——这就是为什么每 Task 拷贝不贵，也是"存可变对象仍污染"的根源。2) ASGI 里怎么保证中间件/Handler/日志 filter 全链路拿到 trace_id？——uvicorn 每请求一个 Task 天然隔离；日志侧用 `logging.Handler` 里 `record` 无法直接拿 ContextVar，业界做法是 logging.Filter 在 emit 时读 ContextVar 注入 record（stdlib logging 3.12+ 支持 `stack_info`/自定义，或用 structlog 的 merge_contextvars processor），线程池里的日志要确认传播链没断。3) 为什么 ContextVar 不能代替锁？——它只隔离"标识类"数据，跨协程共享的可变状态照样要锁/队列，别把上下文机制当并发安全机制。

## 背诵要点
- threading.local 粒度是线程，asyncio 单线程全协程共享必串；ContextVar 粒度是 Context，Task 创建时浅拷贝快照（HAMT O(1)）。
- 传播规则：create_task 自动拷贝（创建后再 set 子 Task 看不到）、to_thread/run_in_executor 自动带入且线程 set 不回传、手动线程要 `copy_context().run`。
- ContextVar 存不可变值：快照引用，可变对象照样互相污染；上下文机制不替代锁。

## 复盘追问
- 你们的 trace_id/log 上下文现在挂在哪？asyncio 下有没有"日志串请求"的案例？（提示：grep threading.local 换 ContextVar，演练本卡三个边界）
- 有没有在中间件里"全局 set 不 copy"或 ContextVar 存 dict/list 的写法？（提示：对照快照引用语义逐个改 immutable，APM 接入方核对传播链）
