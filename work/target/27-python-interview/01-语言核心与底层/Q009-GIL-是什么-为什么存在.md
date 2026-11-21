---
title: [Q009] GIL 是什么,为什么存在
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q009 · GIL 是什么,为什么存在

> 难度:★★★ | 标签:GIL, 并发

**问**:请解释 GIL 的设计初衷和基本工作方式。

**答**:GIL 是 CPython 解释器的全局互斥锁,保证同一时刻只有一个线程执行 Python 字节码。它简化了 CPython 内存管理的线程安全实现(引用计数不必每对象加锁),也让非线程安全的 C 扩展集成变简单。线程切换默认每 5 毫秒(`sys.getswitchinterval()`)由持有线程主动释放,GIL 会在阻塞式 IO 调用前释放。注意 GIL 是 CPython 实现产物,Jython、IronPython 没有。

```python
# file: code/01_语言核心与底层/q009_gil_basics.py
import sys
import threading

counter = 0

def worker(n):
    global counter
    for _ in range(n):
        counter += 1   # 字节码层面是 读-加-写 三步,并不原子

if __name__ == "__main__":
    print(sys.getswitchinterval())  # 默认 0.005 秒
    threads = [threading.Thread(target=worker, args=(100_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter, "!= 400000 时说明竞态存在")
```

**追问**:1) GIL 保护了我的数据吗?——没有,GIL 只保证字节码不交错,`counter += 1` 这类多字节码操作仍有竞态,共享状态仍需 `threading.Lock`。2) 为什么 CPython 不直接去掉 GIL?——引用计数不是原子操作,去掉后要么给每个对象加锁(细粒度锁性能崩塌),要么改成延迟/分段回收;PEP 703 free-threading 走的就是后者,还要连带解决 C 扩展的隐式线程安全依赖。3) GIL 都在什么时机释放?——每 5ms(`sys.getswitchinterval()`)的解释器检查点、进入阻塞系统调用(IO/sleep/lock.acquire)之前、以及 NumPy/hashlib/zlib 等大块 C 代码进出时。
