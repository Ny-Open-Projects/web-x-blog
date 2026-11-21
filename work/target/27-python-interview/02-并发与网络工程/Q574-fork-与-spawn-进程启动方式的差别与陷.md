---
title: [Q574] fork 与 spawn:进程启动方式的差别与陷阱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q574 · fork 与 spawn:进程启动方式的差别与陷阱

> 难度:★★★☆ | 标签:multiprocessing, fork, spawn

**问**:fork 和 spawn 两种进程启动方式有什么区别?为什么"多线程程序里 fork"是著名的坑?

**答**:fork 复制父进程整个地址空间,启动快、天然继承所有对象,但只复刻调用线程,其他线程(以及它们持有的锁)消失——如果 fork 瞬间某线程正持有锁,子进程里这把锁永远没人释放,直接死锁,这就是日志库/数据库连接在子进程里卡死的标准剧情。spawn 重新启动解释器、通过 pickle 传参数,慢但干净安全,是 macOS(3.8+)和 Windows 的默认。原则:有守护线程/持锁资源的程序用 spawn;fork 模式下必须在进入多线程之前创建进程池。

```python
# file: code/02_并发与网络工程/q574_fork_spawn.py
import multiprocessing as mp
import os


def child(name: str) -> None:
    ctx = mp.get_start_method()
    print(f"[{name}] pid={os.getpid()} 启动方式={ctx}")


def run_with(ctx_name: str) -> None:
    ctx = mp.get_context(ctx_name)  # 显式选择启动方式
    p = ctx.Process(target=child, args=(ctx_name,))
    p.start()
    p.join()


def fork_demo_with_thread() -> None:
    """演示 fork 只复制当前线程: 子进程看到的线程数是 1。"""
    ctx = mp.get_context("fork")

    def background() -> None:
        pass

    t = threading.Thread(target=background, name="phantom")
    t.start()
    # fork 发生时 phantom 线程存在, 但子进程里它不存在
    p = ctx.Process(target=lambda: print("子进程 threading.active_count =",
                                         threading.active_count()))
    p.start()
    p.join()
    t.join()


if __name__ == "__main__":
    import threading  # 放在模块层避免 spawn 重复执行时缺名字

    available = mp.get_all_start_methods()
    print("平台支持:", available, "当前默认:", mp.get_start_method())
    for m in available:
        run_with(m)
    if "fork" in available:
        fork_demo_with_thread()
```

**追问**:1) 为什么 macOS 从 Python 3.8 起默认 spawn?——Apple 的 fork+exec 之外混用系统库(尤其 Objective-C runtime)在多线程下不安全,频繁导致子进程崩溃,官方改成 spawn 规避。2) fork 的隐患清单?——fork 只复制调用线程,其他线程持有的锁(含 import 锁,Q550)在子进程成死锁;连接/缓冲区状态复制后双写;gc/信号状态混乱;3.12 引入 os.register_at_fork 缓解部分。3) spawn 的代价与适配?——启动慢(重新 import);入口必须可导入(无 __main__ 副作用,Q2106);Windows 只支持 spawn——跨平台代码按 spawn 设计。4) 生产陷阱?——fork 后日志重复/连接复用;spawn 下模块级重初始化拖慢启动;forkserver 与预加载资源的配合误解。

---
