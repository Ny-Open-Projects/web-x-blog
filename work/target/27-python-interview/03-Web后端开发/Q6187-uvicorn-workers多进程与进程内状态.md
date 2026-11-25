---
title: "[Q6187] uvicorn --workers 多进程：进程内状态各一份"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6187 · uvicorn --workers 多进程：进程内状态各一份

难度：P6 ｜ 标签：uvicorn、多进程、进程内缓存、定时任务、WebSocket 广播

**问**：单 worker 一切正常，改成 `uvicorn --workers 4` 之后：定时清理任务每小时跑 4 次；接口限流变成实际 4 倍；WebSocket 推送只有 1/4 的客户端收到；本地缓存命中率还掉了一半。代码一行没改，为什么？"进程内单例"到底单在哪？

**答**：
结论：`--workers` 起的是 4 个**独立进程**，各有自己的堆、锁、全局字典、连接表，没有共享内存。所谓"进程内单例"就是"每个进程一个"：定时任务在每个进程都注册了调度器并各自触发（实测 4 次）；限流计数器各算各的（实际额度 ×4）；WS 连接分散在 4 个进程里，广播只能触达本进程的连接；缓存被 4 份瓜分，命中率约掉到 1/4 并出现"同一请求命中不同版本缓存"。

取舍：多进程是为了绕开 GIL 吃满多核（CPU 密集/同步 ORM 场景），代价是所有"跨请求共享的状态"都要外置。修法按状态类型分：定时任务用独立 beat 进程或文件锁/分布式锁选主；限流/缓存放 Redis；广播走 Redis pub/sub 或消息队列；会话要么无状态（JWT）要么集中存储。反过来，如果业务本身 IO 密集、状态很重，单 worker + 异步（甚至退回线程池）往往比硬上多进程更省心。

实战：事故形态是"上线加 worker 提升吞吐，结果对账任务重复执行 4 次导致金额翻倍"，这类事故的排查线索是"重复条数恰好等于 worker 数"。下面用 4 个真进程各自维护"只跑一次"的进程内锁，统计实际执行次数，验证"每个进程都认为自己是唯一的"。

```python
import multiprocessing as mp
import os
import time

RUNS = 5


def worker(wid, out):
    hits = 0
    own_lock = {"job_done": False}      # 进程内"只跑一次"的锁
    for _ in range(RUNS):
        if not own_lock["job_done"]:
            hits += 1
            own_lock["job_done"] = True
        time.sleep(0.01)
    out.put((wid, hits, os.getpid()))


if __name__ == "__main__":
    q = mp.Queue()
    procs = [mp.Process(target=worker, args=(i, q)) for i in range(4)]   # 4 个 worker
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("[1] 每个 worker 都认为自己是唯一的执行者:")
    total = 0
    pids = set()
    while not q.empty():
        wid, hits, pid = q.get()
        total += hits
        pids.add(pid)
        print(f"    worker-{wid} pid={pid} 执行次数={hits}")
    print(f"[2] 定时任务实际执行 {total} 次（期望 1 次）")

    print(f"[3] {len(pids)} 个独立地址空间：进程内缓存/计数器各一份，RSS 近似 N 倍")
    print("[4] 修正：定时任务只让 1 个进程跑（独立 beat/文件锁），或改用 Redis 分布式锁 + 共享缓存")
```

**追问一**：为什么不是多线程而是多进程？—— CPython 有 GIL，纯 Python 字节码同一时刻只有一个线程在跑；同步 ORM/大量字符串处理这类 CPU 活靠线程无法并行。uvicorn 的 worker 是进程，所以"共享状态"这件事从"加锁"变成了"外置"。

**追问二**：内存真的翻 N 倍吗？—— 不是简单 ×N，但也不乐观：代码段和只读数据在 fork 后 COW 共享，堆上的缓存、连接、请求上下文、GC arena 各一份。实测经验是"单进程工作集 × N + 共享只读部分"，容器 memory limit 要按 N 倍留余量，否则 OOMKilled 会随流量出现。用 `--workers` 前先量一下单进程 RSS 峰值。

## 背诵要点
- `--workers N` = N 个独立进程：定时任务 N 次、限流 N 倍、WS 广播只覆盖本进程、缓存被 N 份瓜分。
- 跨请求状态必须外置：Redis（限流/缓存/pubsub）、独立 beat 进程、分布式锁选主。
- 内存按 N × 单进程工作集估算；多进程是为绕 GIL，不是免费的吞吐。

## 复盘追问
- 加 worker 后对账跑 4 次、推送只到 1/4 客户端，如何统一解释并逐项修复？（独立地址空间、外置状态）
- 什么时候不该加 worker？如何估算内存与 worker 数？（IO 密集、单进程 RSS × N、容器 limit）
