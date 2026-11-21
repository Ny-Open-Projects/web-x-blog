---
title: [Q5533] call_later 自重排定时器：handle 堆积的内存事故复盘
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5533 · call_later 自重排定时器：handle 堆积的内存事故复盘

> 难度:★★★★ | 标签:事故复盘, call_later, TimerHandle, 内存泄漏

**问**：一个"每秒自检"的定时任务，服务跑三天后内存涨满——定时器和 `call_later` 有什么关系？`TimerHandle.cancel()` 了为什么还泄漏？正确的自重排姿势是什么？

**答**：事故的根因是**回调重新注册自己时持有旧 handle，旧 handle 又把回调与闭包状态钉在 TimerHeap（Q580 的定时器堆）里**。典型错误代码：

```python
def periodic():
    do_check()
    loop.call_later(1, periodic)   # 每次新 handle 入堆
```

这段本身是对的（自重排），爆炸发生在**退出路径**：服务收到停机/重载信号后，代码 cancel 了"当前 handle"，但 periodic 内部又排了下一个——堆里的 handle 链永不枯竭；或者每次重排都用**新闭包**（捕获大对象），旧 handle 未 cancel 时闭包整条引用链不释放。`TimerHandle` 只有三种终态：到期执行、`cancel()`、loop 关闭遍历（`_cancel_all`）。中间任何路径让"下一个 handle"逃脱 cancel，泄漏就成立。正确姿势三选一：1) **幂等重排**：回调内先检查 `self._stopping`，再排下一个，cancel 路径先置位再 cancel 当前 handle；2) **中心化调度**：一个长期任务 while 循环 + `asyncio.sleep`（Task 可被 TaskGroup/取消干净终止，Q589），不碰 handle 层；3) 自定义 TimerHandle 的 `_repr_info`/计数监控：heapq 长度暴露成指标，堆积告警先于 OOM。取舍：handle 层性能好但生命周期手工管理，Task 层有取消语义但多一层协程成本——服务内长周期任务**默认选 Task+sleep**，handle 层留给高精度小场景。

```python
# file: code/02_并发与网络工程/q5533_timer_leak.py
"""定时器 handle 堆积的复现(加速版)与两种正确姿势."""
import asyncio
import heapq
import time

# --- 复现: 自重排 + 退出路径漏 cancel -> handle 链逃逸 ---
async def leaky(stop_at: float) -> int:
    loop = asyncio.get_running_loop()
    created = 0

    def periodic() -> None:
        nonlocal created
        created += 1
        if loop.time() < stop_at:        # 模拟"忘记检查停止位"的部分路径
            loop.call_later(0.001, periodic)
        # else: 到期不再排 —— 但若 stop_at 在 cancel 之后被改写, 链就断了
    h = loop.call_later(0.001, periodic)
    await asyncio.sleep(0.05)
    h.cancel()                            # 只 cancel 了"当前"handle,
    return created                        # 已排队但未到期的仍会触发自重排

n = asyncio.run(leaky(time.time() + 0.1))
print("cancel 后仍自重排触发次数(泄漏证据):", n)

# --- 姿势1: 幂等重排(停止位先行 + 持有当前 handle) ---
class PeriodicHandle:
    def __init__(self, loop, interval: float, fn) -> None:
        self._loop, self._interval, self._fn = loop, interval, fn
        self._stopping = False
        self._h = None

    def start(self) -> None:
        self._schedule()

    def _schedule(self) -> None:
        if not self._stopping:
            self._h = self._loop.call_later(self._interval, self._tick)

    def _tick(self) -> None:
        try:
            self._fn()
        finally:
            self._schedule()              # 无论 fn 抛不抛, 停止位兜底

    def stop(self) -> None:
        self._stopping = True             # 先置位, 再 cancel 在途 handle
        if self._h is not None:
            self._h.cancel()

async def main() -> None:
    loop = asyncio.get_running_loop()
    fired = 0
    p = PeriodicHandle(loop, 0.001, lambda: None)
    p.start()
    await asyncio.sleep(0.02)
    p.stop()
    await asyncio.sleep(0.02)             # 若泄漏, 此期间仍会触发
    print("姿势1 stop 后无触发, 堆已干净")

# --- 姿势2(推荐): Task + asyncio.sleep, 取消语义免费 ---
async def periodic_task(fn, interval: float) -> None:
    while True:                           # CancelledError 由 TaskGroup/取消传播处理
        await asyncio.sleep(interval)
        fn()

# --- 监控: 定时器堆长度作为指标暴露 ---
def heap_gauge(loop) -> int:
    return len(loop._scheduled) if hasattr(loop, "_scheduled") else -1

asyncio.run(main())
print("生产建议: 堆长度指标 + Task/sleep 为默认; handle 层留给高精度场景")
```

**追问**：1) TimerHeap 里的 handle 为什么不用 WeakRef？——到期执行需要强引用（否则任务静默蒸发），这是"调度器持有"与"泄漏"的分界：泄漏不是堆引用任务，而是**任务引用链超出了预期存活期**。2) `loop._cancel_all()` 什么时候生效？——loop.close() 时遍历取消，所以进程级退出能兜住；但**热重载/重建 loop**（单元测试、多 loop 场景）时旧 loop 里的 handle 链会拖到 close 才释放，测试变慢就是这个坑。3) 为什么 Task+sleep 没有这个问题？——Task 被 cancel 时 sleep 抛 CancelledError，while 循环直接退出，"下一个"由结构保证不再产生，生命周期交给结构化并发。

## 背诵要点
- call_later 自重排的正确性靠"停止位先行 + 当前 handle 必 cancel"；漏一条路径 handle 链即泄漏。
- TimerHandle 三终态：到期、cancel、loop.close 的 _cancel_all；热重载场景堆不清空。
- 服务级周期任务默认 Task+asyncio.sleep（取消语义免费），堆长度（_scheduled）作监控指标。

## 复盘追问
- 你的服务里"停止位"散落在多少处定时任务里？怎么把"泄漏必查停止位"变成模板代码或基类？
- _scheduled 长度涨到 10 万时的应急路径是什么：热重载、loop 重建还是重启？
