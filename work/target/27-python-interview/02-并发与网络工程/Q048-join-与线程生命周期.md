---
title: [Q048] join 与线程生命周期
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q048 · join 与线程生命周期

> 难度:★☆☆ | 标签:threading, join

**问**:join 的作用是什么?join 不加超时有什么风险?

**答**:`t.join()` 让当前线程阻塞直到 t 结束,可传 timeout。多线程程序收尾时通常对所有 worker join,保证结果完整;若不加超时且 worker 死循环,主线程会永久卡死,工程上建议带超时 join 并检查 `is_alive()`。

```python
# file: code/02_并发与网络工程/q048_join_timeout.py
import threading
import time


def worker(seconds: float) -> None:
    time.sleep(seconds)
    print(f"耗时 {seconds}s 的任务完成")


if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(s,)) for s in (0.3, 0.6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=0.5)
        if t.is_alive():
            print(f"{t.name} 超时仍未结束, 不再等待")
    print("主线程收尾")
```

**追问**:
- 不带超时的 join 卡死怎么办?——传 `timeout` 并循环检查 `is_alive()`,超时后记录线程名并走降级,收尾逻辑不能允许永久阻塞。
- 对没 start 的线程 join 会怎样?——抛 RuntimeError: cannot join thread before it is started;start/join 必须成对出现,代码评审按对检查。
- 主线程不 join 直接退出,子线程的输出会丢吗?——非守护线程会等子线程结束,守护线程被截断、finally 不保证执行,所以关键落盘要在子线程内完成或显式 join。

---
