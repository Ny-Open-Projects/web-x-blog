---
title: [Q5638] 线程池默认 max_workers 的演进与误用
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5638 · 线程池默认 max_workers 的演进与误用

难度：P6 | 标签：ThreadPoolExecutor、默认参数、os.cpu_count、版本演进

**问**：不传 `max_workers` 时 `ThreadPoolExecutor` 会开多少线程？这个默认值从 3.8 起经历了什么变化，为什么要从"CPU 数"改成 `min(32, cpu+4)`？在容器里这个默认值为什么经常是错的？`ProcessPoolExecutor` 的默认值又是另一套逻辑吗？

**答**：

**结论**：演进脉络：3.8 之前默认 `os.cpu_count()`；Python 3.8 起（bpo-33076）改为 `min(32, os.cpu_count() + 4)`——动机是"IO 型任务占多数"：CPU 核数只约束 CPU 型线程，IO 等待期间线程空转，+4 给一点并发余量，32 是防失控上限。`ProcessPoolExecutor` 则默认 `os.cpu_count()`（CPU 型假设，无 32 上限；macOS/Windows 注意 spawn 开销）。容器里这两个默认值都可能错：`os.cpu_count()` 读的是宿主机核数而不是 cgroup quota——8 核配额的容器在 64 核宿主机上默认开 32 线程（thread）或 64 进程（process），前者浪费栈内存，后者直接 OOM/CPU 超卖。3.13 加了 `os.process_cpu_count()`（感知 affinity），仍是理想化的，cgroup 配额仍需自行读 `/sys/fs/cgroup`。

**取舍**：生产代码永远显式传 max_workers：IO 型按线程池公式（QPS×平均延迟推导）或下游连接池对齐；CPU 型取配额核数。`ProcessPoolExecutor(max_workers=None)` 在 spawn 平台上还要乘"每个进程的启动成本"，扩容速度比线程慢两个数量级，压测启动风暴时要预估。

**实战**：基线示例 3.12：`os.cpu_count()` 与 `os.process_cpu_count()`（3.13+）差异演示，容器部署建议启动时读 cgroup 并打日志固化实际使用的 worker 数。

```python
import os, sys, multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor

print("python", sys.version.split()[0])
print("os.cpu_count()            =", os.cpu_count())
if hasattr(os, "process_cpu_count"):          # 3.13+
    print("os.process_cpu_count()    =", os.process_cpu_count())
print("len(os.sched_getaffinity(0)) =",
      len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else "N/A")

# 默认行为复现（不真创建：只读内部推导，避免一次性起几十线程）
import concurrent.futures.thread as tmod
max_workers = min(32, (os.cpu_count() or 1) + 4)
print("ThreadPoolExecutor 默认 max_workers =", max_workers)

# 容器内正确做法：读 cgroup 配额（v2），失败回退 cpu_count
def container_cpu_quota():
    try:
        with open("/sys/fs/cgroup/cpu.max") as f:
            quota, period = f.read().split()
            if quota != "max":
                return max(1, int(int(quota) / int(period)))
    except OSError:
        pass
    return os.cpu_count() or 1

quota = container_cpu_quota()
print("cgroup 配额核数 =", quota,
      "-> CPU 型池 worker =", quota,
      "; IO 型池 worker = min(32, quota+4) 自定")
```

**追问 1**：为什么 +4 而不是 ×2 或不限？
答：bpo-33076 的目标是"给 IO 型场景一个不 完全绑死 CPU 的合理起点"，32 上限防止新手脚本开几百线程吃光栈内存（默认栈 8MB×N）；它只是"比错误好一点"的兜底，不是容量规划公式。

**追问 2**：线程默认栈大小对默认值的影响？
答：`threading.stack_size()` 默认跟随平台（macOS/Linux 主线程 8MB，工作线程一般 512KB-8MB），32 个默认线程即数百 MB 虚拟内存（RSS 按实际使用计）；万级线程场景必须调 stack_size 或换协程。

**追问 3**：`ProcessPoolExecutor` 默认 worker 数为什么不设上限？
答：CPU 型并行任务 worker 多于核数无收益，cpu_count 天然就是上限；但容器配额场景同理失真，且 spawn 平台每个 worker 重导入主模块，64 进程启动风暴很危险。

## 背诵要点

- 3.8 起线程池默认 `min(32, cpu+4)`：IO 型余量+失控上限；进程池默认 cpu_count 无上限。
- 容器里 os.cpu_count 是宿主机核数，须读 cgroup quota（v2: cpu.max）；3.13 的 process_cpu_count 只感知 affinity。
- 生产一律显式 max_workers：IO 型按吞吐公式，CPU 型取配额核数。

## 复盘追问

- K8s 里如何把 cgroup 配额接入统一的"worker sizing"配置中心？(提示：entrypoint 探测 + 环境变量下发)
- 为什么"默认 32 线程 + 每线程访问下游连接池 10 连接"会击穿下游？(提示：320 并发突刺 > 下游池)
