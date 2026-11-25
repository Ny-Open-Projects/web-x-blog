---
title: "[Q5596] threading.Timer 泄漏与进程退出阻塞事故"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5596 · threading.Timer 泄漏与进程退出阻塞事故复盘

难度：P6 | 标签：事故复盘 | threading.Timer | 线程生命周期

**问**：一个用 `threading.Timer` 做"延迟兜底回执"的服务，运行数天后 kill 时进程要几十秒才退出，且监控发现线程数缓慢上涨。Timer 泄漏的机制是什么？非 daemon 的 Timer 对进程退出有什么影响？正确治理姿势是什么？

**答**：
结论：`threading.Timer(interval, fn)` 每个实例就是一个**独立线程**：`t.start()` 后它在 `Event.wait(interval)` 上挂起，到点执行函数。泄漏机制有两个：① 用完不 `cancel()` 也不让它自然到期——pending 的 Timer 线程持续存在（线程对象 + 栈内存 ~8MB 虚拟/实际取决于 stack_size）；② Timer 默认**非 daemon 线程**：解释器退出时要等所有非 daemon 线程跑完 `run()`，pending 的 Timer 会让 `kill`（SIGTERM→Python 优雅退出）拖到最长 interval 才结束。若 Timer 函数本身又卡在 IO，退出阻塞无上限。
取舍：Timer 适合"少量、短延迟、必须执行"的兜底；高频定时需求应换成 `sched` 单线程调度器、时间轮（自研）或 `call_later`（有 loop 时）——一万个 Timer = 一万个线程，栈内存与调度开销都不可接受。
实战：① 所有 Timer 建议显式 `t.daemon = True` 或统一走调度器；② 生命周期与请求/会话绑定：请求结束/对端断开时 `cancel()`；③ 退出路径 `atexit` 里集中 cancel + `Event.set` 快速收尾；④ 把"进程内 pending Timer 数"暴露成指标。

```python
import threading, time, os, sys

def receipt(order_id):
    # 模拟兜底回执（真实场景可能是网络调用）
    pass

class TimerRegistry:
    """请求级 Timer 注册表：请求结束统一 cancel，防泄漏。"""
    def __init__(self):
        self._pending: set = set()
        self._lock = threading.Lock()
    def schedule(self, delay, fn, *args):
        t = threading.Timer(delay, fn, args)
        t.daemon = True              # 退出不被 pending Timer 拖住
        with self._lock:
            self._pending.add(t)
        t.start()
        return t
    def cancel_all(self):
        with self._lock:
            for t in self._pending:
                t.cancel()
            self._pending.clear()
    @property
    def pending(self):
        with self._lock:
            return len([t for t in self._pending if t.is_alive()])

reg = TimerRegistry()
# 模拟业务：下了一堆延迟回执
for i in range(100):
    reg.schedule(60, receipt, f"order-{i}")     # 60 秒后才触发
print("pending Timer 线程:", reg.pending)         # 100 个线程在 wait

# 正常业务路径：大多数回执在到期前由"主路径已完成"触发 cancel
time.sleep(0.2)
reg.cancel_all()
time.sleep(0.1)                                   # 等线程从 wait 醒来退出
print("cancel 后 pending:", reg.pending)

# 对照：非 daemon Timer 拖慢退出（短间隔演示，不真挂 60s）
t = threading.Timer(2.0, lambda: print("non-daemon timer fired"))
t.start()
t0 = time.perf_counter()
t.join()               # 解释器退出时等价于等待所有非 daemon 线程
print(f"非 daemon 退出阻塞实测 {time.perf_counter()-t0:.1f}s（生产里 interval=60s 时 kill 就卡 60s）")

# 结论要点：一万个 Timer = 一万个线程；高频换调度器
print("高频定时 → sched/time轮/call_later，一实例一线程不可扩展")
```

**追问 1**：为什么 `cancel()` 之后线程不会立刻消失？
- 追问 2 层：cancel 只是 `Event.set`，线程从 wait 醒来后发现 finished 标志直接返回——需要一小段调度时间；注册表统计要容忍这个窗口。
- 追问 3 层：若 Timer 已进入函数执行，cancel 无效，函数不可中断——兜底函数必须自身可安全重入/幂等。

**追问 2**：sched 调度器与 asyncio.call_later 怎么选？
- 追问 2 层：`sched.scheduler` 单线程堆调度（delayfunc 轮询），无线程爆炸但要自己喂时钟；有事件循环时 `call_later` 是 O(log n) 堆、零线程。
- 追问 3 层：跨线程投递到期事件用 `call_soon_threadsafe` 或 Queue；把"每请求一个 Timer"反模式重构为"一个调度器 + 到期表"。

## 背诵要点
1. 每个 Timer = 一个真实线程；默认非 daemon，pending Timer 会把进程退出拖到最长 interval。
2. 治理三件套：daemon=True、注册表随请求 cancel_all、退出路径集中收尾 + pending 数指标。
3. 高频定时不可用 Timer 一实例一线程，换 sched/时间轮/事件循环 call_later。

## 复盘追问
1. 为什么线程数上涨几天后才告警？——泄漏速率 = 每请求 1 个线程但 cancel 缺失只发生在异常分支，低频泄漏被日级监控阈值掩盖。
2. kill 时几十秒退出怎么定位到 Timer？——py-spy dump 看到大量线程栈在 Event.wait；对照 pending Timer 计数即可实锤。
