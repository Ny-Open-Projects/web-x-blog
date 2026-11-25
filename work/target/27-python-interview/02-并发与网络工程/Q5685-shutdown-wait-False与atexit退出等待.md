---
title: "[Q5685] shutdown(wait=False) 不等于停掉：池线程与 atexit 的退出等待"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5685 · shutdown(wait=False) 不等于停掉：池线程与 atexit 的退出等待

难度：P6 ｜ 标签：concurrent.futures、ThreadPoolExecutor、shutdown、atexit、优雅停机

**问**：停机钩子里写了 `executor.shutdown(wait=False)`，为什么容器还是等满 30 秒才被 SIGKILL？线程池的 worker 是 daemon 吗？`cancel_futures=True` 到底取消了什么、没取消什么？"优雅停机"在这层该怎么写？

**答**：
结论：3.9 起 `ThreadPoolExecutor` 的 worker 是**非 daemon** 线程，并注册了 atexit 钩子（`_python_exit`）在解释器退出时 join 所有 worker。`wait=False` 只是"调用方不阻塞"，不改变"退出时仍要等线程跑完"这个事实——实测子进程里主线程先打印结束，整个进程还是要 1.22 秒才退出（任务本身 1.0 秒）。`cancel_futures=True` 只取消**队列里还没开始**的任务，正在跑的无法取消（Python 没有线程中断）。

取舍：三种语义要分清——a) `wait=False`：立即返回、线程继续跑、退出时仍等；b) `cancel_futures=True`：丢掉排队任务、跑完在跑的；c) 真正的"强制停"在 Python 线程模型里做不到，只能"停止投喂 + 等排空 + 超时放弃（接受线程泄漏）"。优雅停机应该"先关入口（不再接新请求）→ 等 in-flight 完成（wait=True + 计时）→ 超时则记录并退出"，而不是假装停掉。

实战：事故形态是"K8s 里 preStop 只有 5 秒，应用 shutdown 里 wait=False 后立刻 return，但解释器退出被 atexit 卡住 20 秒，最终 SIGKILL 打断正在写的事务"。下面演示：wait=False 后线程仍活、没 cancel 的任务一个都没取消、`cancel_futures=True` 只取消排队的、以及子进程退出耗时证明 atexit 在等。

```python
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

ex = ThreadPoolExecutor(max_workers=2, thread_name_prefix="worker")
futs = [ex.submit(time.sleep, 0.8) for _ in range(4)]
time.sleep(0.1)

ex.shutdown(wait=False)                       # 立刻返回，线程还在跑
alive = [t.name for t in threading.enumerate() if t.name.startswith("worker")]
print("[1] shutdown(wait=False) 后仍存活:", alive)
print("[2] 队列里未开始的任务是否已取消:",
      [f.cancelled() for f in futs])

ex2 = ThreadPoolExecutor(max_workers=1)
f1 = ex2.submit(time.sleep, 0.5)
f2 = ex2.submit(lambda: "never")
ex2.shutdown(wait=False, cancel_futures=True)
print("[3] cancel_futures=True：排队的取消、running 的不取消:",
      f1.cancelled(), f2.cancelled())

code = (
    "import time\n"
    "from concurrent.futures import ThreadPoolExecutor\n"
    "ex = ThreadPoolExecutor(1)\n"
    "ex.submit(time.sleep, 1.0)\n"
    "ex.shutdown(wait=False)\n"
    "print('主线程结束', flush=True)\n"
)
t0 = time.perf_counter()
subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
print(f"[4] 子进程只 sleep 1s，实际退出耗时 {time.perf_counter() - t0:.2f}s ->")
print("    解释器退出时会 join 非 daemon 的池线程（_python_exit）")
```

**追问一**：为什么 3.9 要把池线程从 daemon 改成非 daemon？—— daemon 线程在解释器退出时会被直接掐死，正在写的文件/正在提交的事务被截断，产生"半个请求"的脏数据。改成 join 是拿"退出变慢"换"退出前把活干完"，这也意味着**停机时长由最慢的任务决定**，所以必须有超时兜底。

**追问二**：`shutdown` 之后还能 submit 吗？—— 不能，会抛 `RuntimeError: cannot schedule new futures after shutdown`；但已经在跑的 future 仍然可以 `result()`。所以"关入口"要在业务层做（置标志、拒绝新请求），执行器的 shutdown 只是资源释放，不负责限流——顺序反了会出现"新请求进来直接 500"。

## 背诵要点
- 3.9+ 池 worker 非 daemon + atexit join：`wait=False` 不阻止退出等待，退出耗时 = 最慢任务。
- `cancel_futures=True` 只取消排队任务；运行中的线程无法中断（Python 无强制停止）。
- 优雅停机 = 关入口 → 等排空（带超时）→ 记录残留退出；先 shutdown 再拒流量是错的顺序。

## 复盘追问
- 停机钩子 `wait=False` 但容器仍等 30 秒，如何解释并重写？（非 daemon + atexit、超时兜底）
- `cancel_futures` 能取消什么、不能取消什么？强制停线程的代价是什么？（排队 vs 运行中、线程泄漏）
