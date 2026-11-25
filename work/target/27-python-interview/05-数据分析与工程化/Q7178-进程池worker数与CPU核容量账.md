---
title: [Q7178] 进程池 worker 数与 CPU 核的容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7178 · 开多少个进程才对：worker 数与 CPU/内存的容量账

难度：P6 ｜ 标签：容量规划、multiprocessing、worker 配比
基线：Python 3.11+；multiprocessing.Pool / concurrent.futures.ProcessPoolExecutor。

**问**：一台 8 核 32GB 的数据处理机器，CPU 利用率长期 30%，主管让"把进程数开大点"就能跑满吗？worker 数的容量账要考虑哪些维度，CPU 型与 IO 型负载的公式差在哪？

**答**：**结论**：CPU 型负载的账是**worker 数 ≈ 核数**（超配只增加上下文切换，GIL 下 Python 进程各占一核），利用率 30% 说明瓶颈多半不在并行度，而在 **IO 等待或任务粒度**（主进程喂数据跟不上、子进程在等磁盘/网络）。IO 型负载公式不同：`worker 数 ≈ 核数 × (1 + 等待时间/计算时间)`，等待占比越高可开的 worker 越多，但上限受**内存**约束——每 worker 加载一份业务数据（如 pandas DataFrame）时，`worker 数 × 单 worker 峰值内存 ≤ 可用内存 × 0.8` 才是真正的天花板。另外账里必须含**主进程串行段**：任务提交、结果序列化都在主进程，worker 再多也压不平它，吞吐上限 = min(主进程喂数速率, worker 总处理速率)。

**取舍**：进程池 vs 线程池 vs 异步：CPU 密集只有进程池有效（绕开 GIL）；IO 密集优先 asyncio 或线程池（创建与切换成本低一个量级）；进程池里跑 IO 等待是浪费——一个 8 核机器跑 32 个"等网络"的进程不如 4 个进程 + 每进程内 asyncio。内存维度的取舍：worker 共享大数据用 fork（Linux 享页）省内存，但 macOS 默认 spawn（全量复制）——跨平台容量账不一样，spawn 场景单 worker 内存要按完整拷贝算。

**实战**：worker 数容量账与实测框架（macOS spawn 加 `__main__` 守卫）：

```python
# worker 数容量账：CPU 型 vs IO 型 + 内存约束
import os, sys

CORES = os.cpu_count() or 8
MEM_GB, per_worker_gb = 32.0, 3.5      # 单 worker 峰值内存

cpu_workers = CORES                    # CPU 型: worker = 核数
io_wait_ratio = 0.75                   # IO 型: 75% 时间在等
io_workers = int(CORES * (1 + io_wait_ratio / (1 - io_wait_ratio)))
mem_cap = int(MEM_GB * 0.8 / per_worker_gb)
print(f"CPU 型建议 {cpu_workers} workers；IO 型公式得 {io_workers}，"
      f"但内存上限 {mem_cap} -> 实际取 {min(io_workers, mem_cap)}")

# 主进程串行段：喂数速率决定吞吐上限
serialize_ms_per_task, tasks = 8, 100_000
feed_cap_s = serialize_ms_per_task / 1000 * tasks
worker_rate = 50                        # 每秒每 worker 任务数
process_cap_s = cpu_workers * worker_rate
print(f"主进程喂数 {feed_cap_s:.0f}s vs worker 处理 {tasks/worker_rate/ cpu_workers:.0f}s "
      f"-> 瓶颈在{'主进程序列化' if feed_cap_s > tasks/worker_rate/cpu_workers else 'worker'}")

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":              # macOS spawn 必须守卫
    from concurrent.futures import ProcessPoolExecutor
    import time
    payloads = [200_000] * CORES * 2
    for workers in (CORES // 2, CORES, CORES * 2):
        t0 = time.perf_counter()
        with ProcessPoolExecutor(max_workers=workers) as ex:
            list(ex.map(cpu_task, payloads))
        dt = time.perf_counter() - t0
        print(f"workers={workers:2d}: {dt:.2f}s "
              f"({'核数附近最优' if workers == CORES else ''})")
    print("观察：超配到 2x 核数不提速，上下文切换反噬")
```

**追问 1**：为什么 CPU 利用率 30% 不能直接推出"加进程"？诊断顺序是什么？
提示：先看 wait 占比（iowait、网络等待）、任务队列是否空转、主进程序列化瓶颈；利用率低可能是"没任务可跑"而不是"并行不够"，加 worker 只会把等的时间复制 32 份。

**追问 2**：spawn 与 fork 对容量账的具体影响？
提示：fork 写时复制可共享大对象（内存账打折），但与线程混用有死锁风险；spawn 每个 worker 全量 import + 复制，启动慢、内存账全价，macOS/Windows 默认 spawn——账要按目标平台分开算。

**追问 3**：ProcessPoolExecutor 的任务怎么设计才能压住主进程串行段？
提示：粗粒度任务（一次传一批）、避免大对象 pickle（传引用+worker 内自取，或用共享内存）、结果尽量返回摘要而不是全量数据。

## 背诵要点
1. CPU 型 worker ≈ 核数，超配只添切换开销；IO 型 worker ≈ 核 × (1+等待/计算)，且受内存上限 `0.8×总内存/单 worker 峰值` 约束。
2. 吞吐上限 = min(主进程喂数速率, worker 总速率)：序列化/任务提交是隐形串行段，粗粒度批量任务化解。
3. fork 共享省内存、spawn 全价复制（macOS 默认），容量账必须按平台分开算；进程池代码必须有 `__main__` 守卫。

## 复盘追问
1. 你们那台 30% 利用率的机器，最终诊断出的真瓶颈是什么？当时用哪些指标排除"并行不够"这个假设？
2. 单 worker 的峰值内存是怎么测出来的（RSS 采样还是 tracemalloc）？内存上限估算留了多少余量、依据是什么？
