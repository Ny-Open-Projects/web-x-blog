---
title: [Q056] GIL 是什么
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q056 · GIL 是什么

> 难度:★★★ | 标签:GIL, CPython

**问**:解释 GIL 的作用。为什么多线程无法利用多核做 CPU 计算?

**答**:GIL 是 CPython 解释器中的全局互斥锁,保证同一时刻只有一个线程执行 Python 字节码。因此 CPU 密集任务在多线程下无法并行,多核只用于 IO 等待时释放 GIL 的场景。注意:GIL 只存在于 CPython 实现(历史上 PyPy 同样有,Jython/IronPython 没有);C 扩展如 NumPy 在计算时可主动释放 GIL。

```python
# file: code/02_并发与网络工程/q056_gil.py
import threading
import time

N = 10_000_000


def cpu_task() -> None:
    x = 0
    for i in range(N):
        x += i


def run_threads(n: int) -> None:
    threads = [threading.Thread(target=cpu_task) for _ in range(n)]
    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start


if __name__ == "__main__":
    t1 = run_threads(1)
    t2 = run_threads(4)
    print(f"1 线程: {t1:.2f}s")
    print(f"4 线程: {t2:.2f}s  (受 GIL 限制, 几乎不加速甚至更慢)")
```

**追问**:
- PEP 703 / free-threaded Python 是什么?——CPython 3.13 起提供可关闭 GIL 的实验性构建,移除 GIL 后靠细粒度锁和偏置引用计数保证线程安全。
- GIL 什么时机释放?——每 5ms 解释器检查点、阻塞系统调用之前、NumPy/hashlib 等大块 C 计算进出时;这解释了「多线程在 IO 场景仍有效」。
- free-threading 构建下写扩展要注意什么?——不能再依赖 GIL 的隐式串行,扩展内部状态自己加锁;3.13 起单独安装实验构建验证。
- 怎么判断程序受 GIL 限制?——对比单线程与多线程吞吐:CPU 密集多线程无增益甚至更慢,就是 GIL 限制,应转进程池或 C 扩展。
