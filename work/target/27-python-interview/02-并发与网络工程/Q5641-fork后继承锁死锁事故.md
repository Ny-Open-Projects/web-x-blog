---
title: "[Q5641] fork 继承线程锁死锁事故"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5641 · fork 继承线程锁死锁事故

难度：P7 ｜ 标签：multiprocessing、fork、线程锁、事故复盘

**问**：多线程服务里一个后台线程持有日志锁写文件，此时主线程触发 fork 派生工作子进程，子进程打印日志永久卡死。为什么 fork 会把"别人的锁"带进单线程子进程？如何根治？

**答**：
结论：`fork` 只复制**调用它的那个线程**，但把整个进程的内存（包括所有锁的当前状态）原样带过去。如果其他线程此刻正持有锁（已 lock 未 unlock），子进程里那把锁永远没人释放——子进程单线程访问它必然永久阻塞。这是 POSIX 著名的 fork+thread 死锁问题，Python 的 `os.fork()` 与 `multiprocessing` 的 fork context 都不免疫。

取舍与根治：① **spawn/forkserver 上下文**——干净进程不继承锁状态，代价是启动慢 + 需要可 pickle 的入口；② fork 前提下，把 fork 动作收敛到"单线程窗口"（fork 前暂停所有持锁线程）；③ 子进程入口第一时间清场（重置 logging handler、避免任何锁依赖）；④ `os.register_at_fork(before/after_in_parent/after_in_child)` 给必须的锁做 fork-aware 管理（CPython 内部 import 锁就是这么保护的）。

实战：macOS 默认 spawn（3.8+），Linux 默认 fork——同一份代码跨平台行为不同，容器里要么显式 `get_context("spawn")` 锁定语义，要么保证 fork 安全审计。子进程卡死排查特征：py-spy dump 看到子进程栈停在一个 acquire 上且父进程该锁被另一线程持有。

```python
import os
import sys
import threading
import time

lock = threading.Lock()

def holder():
    """模拟：后台线程长期持锁（fork 发生在它持锁期间）"""
    with lock:
        time.sleep(0.3)          # 期间主线程会 fork

def main():
    if sys.platform == "darwin":
        print("macOS 默认 spawn，本演示显式使用 fork 上下文复现问题")
        ctx = __import__("multiprocessing").get_context("fork")
    else:
        import multiprocessing
        ctx = multiprocessing.get_context("fork")

    t = threading.Thread(target=holder)
    t.start()
    time.sleep(0.05)             # 确保 t 已拿到锁

    def child():
        got = lock.acquire(timeout=0.5)   # 继承来的锁：无人能释放
        if got:
            print("child got lock (unexpected)")
            lock.release()
        else:
            print("child: deadlock reproduced - lock held by vanished thread")
        os._exit(0)

    p = ctx.Process(target=child)
    p.start()
    p.join(timeout=2)
    print("child exitcode:", p.exitcode)
    t.join()

if __name__ == "__main__":       # spawn/fork 派生进程必须有 __main__ 守卫
    main()
```

**追问一**：CPython 自己如何避免 import 期间的 fork 死锁？——`_PyRuntime` 里 import 锁通过 `PyOS_AfterFork_Child` 在子进程重置；`os.register_at_fork` 就是暴露给扩展/应用的同款机制，谁的锁谁负责 fork 前获取/子进程重置。

**追问二**：为什么 forkserver 能规避而 forkserver 自己也可能踩坑？——forkserver 是独立进程按需 fork，应用线程不会在那个进程里持锁；但 forkserver 进程在首次 spawn 时会 import 主模块，模块级副作用（建连接、拿锁）会进到它里面，入口必须幂等无副作用。

**追问三**：线上如何提前发现 fork 不安全？——fork 后子进程做"锁存活探针"（对关键锁 acquire(timeout=ε)），失败即告警；以及评审规则：fork 上下文服务禁止在 fork 路径可达的代码里用非 fork-aware 的全局锁。

## 背诵要点
- fork 只复制调用线程，却继承全部锁状态；他人持有的锁在子进程永远无人释放。
- 根治顺序：spawn/forkserver > 单线程窗口 fork > register_at_fork 治理关键锁。
- macOS 默认 spawn、Linux 默认 fork（3.8+），跨平台必须显式 get_context 锁定语义。

## 复盘追问
- 服务同时需要 fork 的 COW 内存优势与线程安全，架构上怎么兼得？（forkserver + 预热，或把持锁状态外置到 Redis/文件，讨论改造优先级）
- os.register_at_fork 的回调里能安全做什么、不能做什么？（fork 后的子进程里只能 async-signal-safe 级别的最小操作，重置锁可以、分配内存/日志危险）
