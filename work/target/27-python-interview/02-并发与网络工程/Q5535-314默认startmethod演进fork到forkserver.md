---
title: [Q5535] 3.14 默认 start method 演进：fork 弃用到 forkserver
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5535 · 3.14 默认 start method 演进：fork 弃用到 forkserver

> 难度:★★★★ | 标签:版本演进, multiprocessing, fork, forkserver, start method

**问**：为什么 3.14 起多线程进程里调 fork 会发 DeprecationWarning、Linux 默认 start method 也要变？fork/spawn/forkserver 三者的启动成本与兼容面差在哪？迁移要注意什么？

**答**：演进时间线：1) **3.12**：`os.fork()` 在**多线程进程**中调用发 DeprecationWarning——fork 只复制调用线程，锁状态被继承（Q2124 的死锁禁忌），还有 fd/缓冲区继承坑（Q2125）与随机数双胞胎（Q5526）；2) **3.14**：Linux 上 multiprocessing 默认 start method 从 fork 改为 **forkserver**（macOS 3.8 起已是 spawn，Windows 只有 spawn），显式 `fork` 的场景发 DeprecationWarning。三种方式对比：**fork**：最快（COW 零拷贝，Q413），但继承一切隐患；**spawn**：全新解释器重 import（启动 50-200ms/个），干净但慢、要求参数可 pickle、入口需 `__main__` 守卫；**forkserver**：首次起一个干净的服务进程，之后 fork 自它——**既快（无重 import）又干净（服务进程是单线程纯净态）**，代价是多一跳 IPC 与"必须提前创建 server"的生命周期管理（`set_forkserver_preload` 可预载常用模块）。迁移清单：a) 显式 `get_context()` 钉住策略，别依赖默认值；b) 依赖"fork 继承连接/状态"的代码（预先打开的 DB 连接、内存态缓存）必须改 spawn 兼容（参数化传递）；c) 容器里用 forkserver 注意 PID 1 信号与 server 生命周期；d) Pool initializer 的每进程初始化语义（Q575）在三种方式下等价，但 server 预载能省 spawn 式重复成本。

```python
# file: code/02_并发与网络工程/q5535_start_method.py
"""start method 探测与三策略的启动成本对比. macOS spawn 需 __main__ 守卫."""
import multiprocessing as mp
import os
import time
import sys

def probe(_):
    return os.getpid()

def bench(method: str, n: int = 4) -> float:
    ctx = mp.get_context(method)
    t0 = time.perf_counter()
    ps = [ctx.Process(target=probe, args=(None,)) for _ in range(n)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    return (time.perf_counter() - t0) * 1000

if __name__ == "__main__":                      # spawn/forkserver 必需
    print("默认 start method:", mp.get_start_method())
    print("可用方法:", mp.get_all_start_methods(), "| python:", sys.version_info[:3])

    for m in mp.get_all_start_methods():
        try:
            ms = bench(m)
            print(f"{m:10s} 启动 4 进程: {ms:.0f}ms")
        except (ValueError, RuntimeError) as e:
            print(f"{m:10s} 不可用: {str(e)[:50]}")

    # 钉住策略: 生产代码显式 get_context, 不依赖默认值随版本漂移
    ctx = mp.get_context("spawn")               # 最可移植
    q = ctx.Queue()
    p = ctx.Process(target=probe, args=(None,))
    p.start(); p.join(timeout=5)
    print("显式 ctx(spawn) 子进程 OK")

    # forkserver 预载(3.14 默认路径): server 起一次, 后续 fork 快而干净
    if "forkserver" in mp.get_all_start_methods():
        mp.set_forkserver_preload(["os", "time"])   # server 启动时预 import
        fctx = mp.get_context("forkserver")
        p2 = fctx.Process(target=probe, args=(None,))
        p2.start(); p2.join(timeout=5)
        print("forkserver 子进程 OK, preload=['os','time']")
```

**追问**：1) 为什么 forkserver 的子进程"干净"？——server 进程由 spawn 式全新解释器创建、单线程、未执行用户代码，fork 它不会继承锁状态或用户线程，把 fork 的速度和 spawn 的安全合到一起。2) COW 与 forkserver 冲突吗？——forkserver 依然走 fork+COW，内存账（Q413）不变；区别是继承的是干净 server 的镜像而不是"跑了一半业务"的父进程。3) fork 在 3.14 后还能用吗？——能，显式 `get_context("fork")` 只是警告；但多线程进程里 fork 的锁继承风险没有变，warning 是在提醒风险而非禁止。

## 背诵要点
- 3.12 多线程 fork 警告 → 3.14 Linux 默认 start method 变 forkserver；spawn 干净慢、fork 快险、forkserver 兼得。
- 迁移三件事：显式 get_context 钉策略、去掉"fork 继承状态"依赖、`__main__` 守卫与参数可 pickle。
- forkserver = 纯净单线程 server + fork；set_forkserver_preload 预载常用模块抵消启动成本。

## 复盘追问
- 你的进程池代码如果依赖"fork 后父进程内存态配置自动可见"，3.14 升级会怎么坏？改造成本怎么估？
- 容器内 PID 1 直接跑 forkserver 的 server 有什么信号/退出风险？怎么兜底？
