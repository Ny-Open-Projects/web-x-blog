---
title: [Q5552] SIGTERM 优雅停机导致任务丢失的事故复盘
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5552 · SIGTERM 优雅停机导致任务丢失的事故复盘

> 难度:★★★★ | 标签:SIGTERM, 优雅停机, ThreadPoolExecutor, cancel_futures, 事故复盘

**问**：滚动发布后每天定时任务少跑一批：进程收到 SIGTERM 直接退出，线程池里排队的任务凭空消失。优雅停机的完整流程应该有哪几步？`shutdown(wait=True)` 和 `cancel_futures=True` 各管什么？K8s 环境里还有哪个时间参数在暗中使坏？

**答**：默认信号处理下 SIGTERM = 立即终止，排队的 future、进行中的任务全部蒸发——这是丢任务的根因。优雅停机四步：a) 信号处理器只做一件事：**置停止标志 + 关入口**（停止 accept 新任务/新连接），不在 handler 里做重活；b) **drain 在跑的任务**：`executor.shutdown(wait=True, cancel_futures=True)`——wait 让进行中的任务跑完，cancel_futures（3.9+）把队列里还没开始的 future 直接置 CANCELLED，避免"停机前又空转十分钟"；c) **持久化未执行任务**：cancel 掉的 future 不是"完成"，要把原任务重新落回队列/DB，下个实例接手；d) 幂等兜底：进行中任务停机被杀（下面第三点）后重跑不产生副作用。K8s 的坑在 **terminationGracePeriodSeconds（默认 30s）**：drain 超过 30s 直接 SIGKILL，任务又丢了——要么把 drain 时间压进宽限期，要么调大宽限并配合 preStop。另注意：信号处理器里不能用锁/复杂同步（handler 在主线程字节码间隙异步执行），只改 Event；非主线程收不到 SIGTERM（signal 只能主线程注册处理）。

```python
# file: code/02_并发与网络工程/q5552_graceful_shutdown.py
import threading, time, signal, os
from concurrent.futures import ThreadPoolExecutor

stop = threading.Event()

def _on_term(signum, frame):
    stop.set()            # handler 只置标志, 不做清理

signal.signal(signal.SIGTERM, _on_term)

done, cancelled = [], []
def worker(n):
    while not stop.is_set():
        time.sleep(0.01)
    done.append(n)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads: t.start()
time.sleep(0.05)
os.kill(os.getpid(), signal.SIGTERM)   # 模拟收到 SIGTERM
for t in threads: t.join(timeout=2)
print("worker 收尾退出:", done, "| 存活:", [t.is_alive() for t in threads])

# 线程池停机: 先 cancel 排队, 再等待在跑
ex = ThreadPoolExecutor(max_workers=1)
f_running = ex.submit(time.sleep, 0.1)
f_queued = ex.submit(print, "排队任务将被取消")
ex.shutdown(wait=True, cancel_futures=True)   # 3.9+
print("排队 future 状态:", f_queued.cancelled() or f_queued, "| 在跑 future 完成:", f_running.done())
try:
    ex.submit(print)
except RuntimeError as e:
    print("停机后拒绝新任务:", e)
# 丢任务兜底: 被 cancel 的任务原单据重新落库, 交给下一个实例
```

**追问**：1) `atexit` 里做 drain 行不行？——不行且危险：SIGTERM 默认行为直接 `exit` 不走 atexit 的前提已变（注册了 handler 后进程不会自动退出，要显式 sys.exit）；atexit 里阻塞 join 长任务会把退出拖成挂死，drain 必须在信号处理后的主流程里做。2) 怎么验证"不丢任务"？——埋点三计数器（received/started/finished），发布窗口后对账：received == finished + cancelled + (落到下一实例的 pending)；任何差值都是泄漏。3) asyncio 服务的等价物？——`loop.add_signal_handler(SIGTERM, stop)` 置事件 → 停止 accept → `asyncio.gather(*inflight, return_exceptions=True)` 等在跑任务 → TaskGroup 剩余任务取消并持久化，整体包进 lifespan 的 shutdown 阶段。

## 背诵要点
- 默认 SIGTERM = 立即终止，排队+在跑任务全丢；优雅停机 = handler 置标志 → shutdown(wait=True, cancel_futures=True) → 被取消任务重新落库 → 幂等兜底。
- `cancel_futures=True`（3.9+）清空未开始的队列，进行中的任务靠 `wait=True` drain。
- K8s terminationGracePeriodSeconds（默认 30s）超时 SIGKILL，drain 必须压进宽限期；信号 handler 只能改 Event，不能拿锁。

## 复盘追问
- 你们服务收到 SIGTERM 后到真正退出的时间线是怎样的？有没有计数对账？（提示：received/started/finished/pending 四个计数器 + 发布窗口对账单）
- 定时任务类 worker 丢失后怎么补偿？靠人还是靠机制？（提示：任务状态机 + 交接协议，或改交给外部调度器避免进程内排程）
