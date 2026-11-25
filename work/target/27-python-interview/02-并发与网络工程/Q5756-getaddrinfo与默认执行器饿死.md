---
title: "[Q5756] getaddrinfo 与默认执行器饿死：DNS 为什么要独立线程池、为什么取消不掉"
date: 2026-11-25
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5756 · getaddrinfo 与默认执行器饿死：DNS 为什么要独立线程池、为什么取消不掉

难度：P7 ｜ 标签：getaddrinfo、run_in_executor、ThreadPoolExecutor、DNS、线程池饿死、取消语义、线程数规划

**问**：一个异步网关用 `loop.run_in_executor(None, socket.getaddrinfo, host, port)` 做域名解析，平时 P99 是 3ms。某天接入了"导出大文件"功能（用 `run_in_executor` 调阻塞的磁盘/压缩库），DNS 解析 P99 突然涨到 2s，超时后 `await` 已经取消，但线程还在跑、CPU 还在烧。默认执行器为什么会被业务阻塞调用拖死？`getaddrinfo` 的 future 取消了为什么线程停不下来？DNS 池该开多大？

**答**：

- **结论**：`loop.run_in_executor(None, fn, *args)` 和 `asyncio.to_thread` 用的是**同一个默认 ThreadPoolExecutor**，默认 `max_workers = min(32, cpu_count + 4)`。任何在这个池里跑的阻塞调用（文件 IO、压缩、同步 DB 驱动、CPU 计算）都会占住 worker；worker 满了之后，后续提交的任务（包括 DNS 解析）只能在队列里排队，于是"解析 3ms"变成"排队 2s"。`getaddrinfo` 本身是阻塞的系统调用（底层可能走 nsswitch/DNS，超时 5s 起步），它在池里跑的时候无法被取消：`future.cancel()` 只能把 asyncio 侧的 Future 标记为 cancelled、丢弃结果，**线程仍在执行**，直到系统调用返回；`asyncio.wait_for` 超时也一样，取消不了线程。正确做法是给 DNS 单独一个小的 ThreadPoolExecutor（或专用 resolver），与业务阻塞池隔离，并给 DNS 结果加缓存/TTL。

- **取舍**：a) 隔离：DNS 池 4–16 个线程通常够（解析是 IO 等待型，单次几十毫秒），业务阻塞池按"并发阻塞任务数 × 平均耗时"规划，两个池互不占坑；b) 共享：省线程、省内存，但一个慢任务就能拖垮全部解析，只适合"阻塞调用很少且都很快"的服务；c) 取消：不要指望 `cancel()` 停线程，要在业务层加超时（`wait_for`）并接受"线程可能泄漏到调用返回"；对不可信域名，限制并发解析数，避免慢解析把 DNS 池也占满；d) 不要用 `socket.setdefaulttimeout` 试图给 `getaddrinfo` 设超时：它影响的是 socket 操作，不是解析器的超时，而且会全局污染（Q5715 的事故源）。

- **实战**：事故形态是"导出功能上线后，所有依赖域名调用的接口一起变慢"——导出用 `run_in_executor` 跑 gzip（CPU 密集、几十秒），默认池 8 个 worker 被 8 个导出任务占满，DNS 解析全部排队；更糟的是导出超时后 `wait_for` 取消了 future，但 gzip 线程继续跑，CPU 打满，形成正反馈。修复：①DNS 用独立 `ThreadPoolExecutor(max_workers=8, thread_name_prefix="dns")`，通过 `loop.run_in_executor(dns_pool, ...)` 调用；②导出改走进程池/独立队列，不占事件循环的默认池；③DNS 加 `cachetools` 风格的 TTL 缓存（或自写 dict + 过期时间），把重复解析降到接近零；④监控加"DNS 队列等待时间"和"默认池活跃线程数"两个指标。

```python
# 默认执行器被阻塞任务占满 -> DNS 排队; 独立执行器隔离; 线程取消不掉
import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

gate = threading.Event()

def blocking_job():
    gate.wait(5)                 # 模拟慢 IO/压缩, 占住 worker
    return "job-done"

def fake_dns():
    return "1.2.3.4"

async def main():
    loop = asyncio.get_running_loop()
    loop.set_default_executor(ThreadPoolExecutor(max_workers=1, thread_name_prefix="default"))

    job = asyncio.ensure_future(loop.run_in_executor(None, blocking_job))
    await asyncio.sleep(0.05)    # 让 job 占住唯一的 worker

    # 同一个默认池里的 DNS 被饿死
    try:
        await asyncio.wait_for(loop.run_in_executor(None, fake_dns), 0.2)
        raise AssertionError("默认池不应有空闲 worker")
    except TimeoutError:
        print("→ 默认池被占满: DNS 排队超时")

    # 独立 DNS 池: 不受业务阻塞影响
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix="dns") as dns_pool:
        t0 = time.perf_counter()
        ip = await asyncio.wait_for(loop.run_in_executor(dns_pool, fake_dns), 0.5)
        cost = time.perf_counter() - t0
        print("→ 独立 DNS 池解析:", ip, "耗时", round(cost, 3), "s")
        assert ip == "1.2.3.4" and cost < 0.1

    # 取消 future 不会停掉已经跑起来的线程
    ran = []
    def slow_worker():
        time.sleep(0.1)
        ran.append("finished")   # 即使 future 被取消, 这一行仍会执行
        return "late"

    with ThreadPoolExecutor(max_workers=1) as pool:
        fut = loop.run_in_executor(pool, slow_worker)
        assert fut.cancel() is True
        assert fut.cancelled()
        await asyncio.sleep(0.3)
        print("→ 取消后线程是否仍执行完:", ran)
        assert ran == ["finished"]

    gate.set()
    assert await job == "job-done"

asyncio.run(main())
```

**追问一**：为什么 `getaddrinfo` 不能用 `asyncio` 原生异步实现，标准库为什么只给线程池方案？—— 解析要走系统解析器（glibc 的 nsswitch、macOS 的 mDNSResponder、Windows 的 DNS Client），这些 API 都是同步阻塞的，没有可移植的异步接口；`getaddrinfo` 内部还可能读 `/etc/hosts`、LDAP、systemd-resolved，行为由系统配置决定。标准库的选择是"用线程池包一层"（`loop.getaddrinfo`），保证跨平台可用；代价就是本卡说的饿死与不可取消。想要真正异步/可控超时，只能换第三方 resolver（`aiodns` 走 c-ares、`dnspython` 的 async），或者自建 DNS 客户端 + 缓存。注意：即使换成 aiodns，底层 UDP 查询可以取消，但系统级的 search domain/重试逻辑仍可能带来长尾。

**追问二**：DNS 池开多大？为什么不是越大越好？—— 解析是"等待型"任务，理论上少量线程就能撑很高 QPS（单次 20ms，8 线程 ≈ 400 QPS）；开太大反而有害：①每个线程 8MB 栈 + 调度开销；②并发打到上游 DNS 会被限流/丢包，重试放大；③GIL 虽然在大头（系统调用）释放，但结果处理仍要 GIL。经验值：4–16 个线程，配合 TTL 缓存与并发上限（Semaphore），并用"队列等待时间"而不是"线程数"做扩容信号。如果解析量真的很大，应该上本地缓存（如 `dnspython` + 内存 TTL，或 sidecar DNS 缓存），而不是继续加线程。

## 背诵要点

- `run_in_executor(None, ...)`/`to_thread` 共用默认池（`min(32, cpu+4)`），任何阻塞调用都会占住 worker，DNS 只能在队列里等。
- `getaddrinfo` 是同步系统调用，`future.cancel()` 只丢弃结果、线程照跑；超时控制要在业务层做，不能指望取消线程。
- DNS 用独立小池（4–16 线程）+ TTL 缓存 + 并发上限；不要用 `socket.setdefaulttimeout` 给解析设超时。

## 复盘追问

- 为什么导出功能会让 DNS 解析变慢 2 秒？（默认执行器被长时间阻塞任务占满，DNS 任务排队；两者共享同一个池）
- 取消 DNS 的 future 为什么 CPU 还在烧？（线程无法被取消，系统调用继续执行到返回；future 只是不再交付结果）
