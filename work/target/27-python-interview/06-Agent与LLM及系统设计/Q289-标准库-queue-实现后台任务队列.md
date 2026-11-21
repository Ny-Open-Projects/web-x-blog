---
title: [Q289] 标准库 queue 实现后台任务队列
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q289 · 标准库 queue 实现后台任务队列
> 难度:★★★★ | 标签:并发, 任务队列

**问**:不用 Celery,如何用标准库实现一个进程内后台任务队列?要考虑哪些细节?

**答**:生产者 `queue.Queue.put` 投递任务,worker 线程循环 `get` 执行。细节:用 `queue.Queue(task_done/join)` 做优雅退出与背压;异常要 catch 并记录,不能让 worker 死掉;worker 用 `daemon=False` + 哨兵值(None)通知退出;阻塞型任务注意超时与重试。进程崩溃队列即丢,可靠任务仍需持久化队列如 Redis/RabbitMQ。

```python
# file: code/06_Agent与LLM及系统设计/q289_task_queue.py
import queue
import threading


class TaskQueue:
    def __init__(self, workers: int = 2):
        self.q: queue.Queue = queue.Queue(maxsize=100)
        self.workers: list[threading.Thread] = []
        for i in range(workers):
            t = threading.Thread(target=self._run, name=f"worker-{i}")
            t.start()
            self.workers.append(t)

    def submit(self, fn, *args, **kwargs) -> None:
        self.q.put((fn, args, kwargs))  # 队列满时自动阻塞,形成背压

    def _run(self) -> None:
        while True:
            item = self.q.get()
            if item is None:      # 哨兵:退出信号
                self.q.task_done()
                break
            fn, args, kwargs = item
            try:
                fn(*args, **kwargs)
            except Exception as exc:
                print(f"[error] task failed: {exc}")
            finally:
                self.q.task_done()

    def shutdown(self) -> None:
        for _ in self.workers:
            self.q.put(None)
        for t in self.workers:
            t.join()


if __name__ == "__main__":
    tq = TaskQueue(workers=2)
    tq.submit(print, "send email")
    tq.submit(print, "generate report")
    tq.q.join()
    tq.shutdown()
```

**追问**:
- Queue 满了怎么办?——put 阻塞形成背压,或用 put_nowait + 拒绝策略(记录/丢弃/持久化)。
- worker 死了任务就丢吗?——get 后未 task_done 崩溃即丢;关键任务先落持久层(Redis/DB)再投内存队列,内存队列只当调度。
- 背压怎么落地?——有界 maxsize + put 阻塞,或 put_nowait+拒绝策略记录;无界队列在高生产速率下内存无限涨。
- 优雅退出怎么编排?——停接新任务→哨兵×worker 数→join;只放一个哨兵其余 worker 永久阻塞。
