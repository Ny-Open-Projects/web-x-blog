---
title: [Q5554] 进程池 worker 数与 RSS 的内存容量账
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5554 · 进程池 worker 数与 RSS 的内存容量账

> 难度:★★★★ | 标签:multiprocessing, Pool, RSS, spawn, fork, 容量规划

**问**：给 2GB 的容器配了 8 个进程池 worker，跑批时被 OOMKilled。进程池的内存账怎么算？fork 和 spawn 的基线差多少？worker 数到底该按什么定？

**答**：进程池内存账是乘法：**总 RSS ≈ n_worker × (解释器基线 + 导入模块 + 每任务工作集峰值)**，再叠加共享读写数据与 IPC 缓冲。账目明细：纯解释器基线 spawn 约 15MB 量级、fork 与父进程共享更小（但 COW 会在写入后逐步碎掉）；一个 import 了 pandas/numpy 的 worker 基线轻松 200-400MB——8 个 worker 就是 2-3GB，OOMKilled 完全符合账面。worker 数的确定顺序：a) 按 CPU 数定 CPU 密集上限（`os.cpu_count()`，或 3.13+ `os.process_cpu_count()`），超配只增内存不加吞吐；b) 按 IO 阻塞比放大（worker = cpu × (1 + 等待比)，等价线程池公式）；c) **用内存预算反向裁剪**：`max_workers = min(按 CPU 算的值, (limit - 主进程预留) / 单 worker 峰值)`——大多数 OOM 事故就是漏了第三步。配套手段：`maxtasksperchild` 定期回收漂移内存；任务数据用 initializer 挂到 worker 全局只载一次；大返回值改写共享内存/落盘路径，别全走管道 pickle。

```python
# file: code/02_并发与网络工程/q5554_pool_rss.py
import resource
import multiprocessing as mp

def _rss_worker(i):
    import sys
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    mb = rss / (1024 * 1024) if sys.platform == "darwin" else rss / 1024  # mac:bytes linux:KB
    return i, mb

if __name__ == "__main__":          # spawn 必须有 __main__ 守卫(macOS 默认 spawn)
    ctx = mp.get_context("spawn")   # 显式选启动方式, 与生产一致
    with ctx.Pool(2) as pool:
        for i, mb in pool.map(_rss_worker, range(4)):
            print(f"spawn worker 任务{i} 峰值RSS≈{mb:.0f}MB")

    # 容量账: 实测单 worker 峰值后反推安全 worker 数
    per_worker_mb = 15          # 替换成你们实测值; import 重库后会是几百 MB
    limit_mb = 2048             # 容器 limit
    reserve_mb = 300            # 主进程+内核缓冲预留
    safe_workers = (limit_mb - reserve_mb) // per_worker_mb
    cpu_cap = mp.cpu_count()
    print(f"内存允许 {safe_workers} 个, CPU 上限 {cpu_cap} -> 取 min = {min(safe_workers, cpu_cap)}")
    print("公式: min(内存反推, CPU 上限), 且峰值按任务最大工作集算, 不是平均值")
```

**追问**：1) fork 方式下父进程已 import pandas，worker 的 200MB 算不算账？——启动时算共享（省了），但 GC/引用计数会写页触发 COW，跑一段时间后逐步变成独占——内存账要按"最终独占量"预估，这就是 `gc.freeze()` 配 fork 的动机。2) `maxtasksperchild` 的代价？——worker 重启要重新 import/初始化（initializer 重跑），频繁回收会让固定成本反复付；用它治"内存缓慢漂移"，阈值设在漂移明显处而不是拍脑袋的小数字。3) 怎么实测单 worker 峰值？——压测时从父进程读 `subprocess` 子进程 RSS（psutil 按父子关系聚合），或子进程内 `getrusage(SELF).ru_maxrss` 上报；注意取**峰值**不是均值，OOM 是按峰值撞的。

## 背诵要点
- 总内存 ≈ n_worker × (基线 + 导入模块 + 任务峰值工作集)；OOM 事故几乎都漏了"内存反推 worker 数"这步。
- worker 数 = min(CPU 上限, (limit − 预留) / 单 worker 峰值)；import 重库的 worker 基线几百 MB 起步。
- macOS 默认 spawn：Pool/Pool 相关代码必须套 `if __name__ == "__main__"`；`maxtasksperchild` 治内存漂移，代价是重复初始化。

## 复盘追问
- 你们进程池的"单 worker 峰值"有实测数字吗？重库 import 进 worker 后账变了没？（提示：initializer 里 import，用 getrusage 上报建基线表）
- fork COW 后 RSS 涨到独占，怎么观测这个转化过程？（提示：/proc/<pid>/smaps_rollup 的 Shared_Clean 逐小时对比，或 psutil memory_full_info 的 uss/pss）
