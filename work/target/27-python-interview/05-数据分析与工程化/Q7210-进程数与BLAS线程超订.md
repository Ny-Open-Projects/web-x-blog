---
title: "[Q7210] 进程数 × BLAS 线程：CPU 超订把吞吐拖垮"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7210 · 进程数 × BLAS 线程：CPU 超订把吞吐拖垮

难度：P6 ｜ 标签：BLAS、OMP_NUM_THREADS、进程池、CPU 超订

基线：Python 3.12；numpy/OpenBLAS 线程模型；纯 Python 模拟线程超订的吞吐曲线。

**问**：16 核机器上跑 16 个 worker 进程做矩阵运算，每个 worker 的 numpy 默认又开 16 个 BLAS 线程。监控显示 load average 冲到 250+，CPU 利用率 100%，但任务总吞吐只有 8 核跑 8 个 worker 时的一半。核没少、线程更多，为什么反而更慢？

**答**：
- **结论**：这是 **CPU 超订**：16 进程 × 16 BLAS 线程 = 256 个可运行线程抢 16 个核，每个线程都只能拿到 1/16 的时间片。BLAS 的并行收益依赖线程间同步（fork-join、barrier），线程被频繁抢占会让同步等待放大、cache 反复失效，实际吞吐大幅下降。核数不是"越多线程越快"，而是"可运行线程数 ≈ 核数"时效率最高。
- **取舍**：两种并行模型：**多进程**（每个进程单线程 BLAS，进程数≈核数）适合大量小任务，隔离好、无 GIL；**单进程多线程 BLAS**（进程数=1，线程数=核数）适合单个大矩阵运算，避免数据复制。混用时要显式限制：`OMP_NUM_THREADS=1`、`OPENBLAS_NUM_THREADS=1`、`MKL_NUM_THREADS=1`，再按"进程数 × 线程数 ≤ 核数"分配。
- **实战**：① 容器里用 `os.cpu_count()` 可能拿到宿主机核数，必须读 cgroup quota；② 进程池启动前设置环境变量（BLAS 在 import 时读）；③ 用 `taskset`/cpuset 绑核，减少迁移；④ 监控 `load average / 核数`、context switches、CPU steal，超订时先降线程而不是加机器。

```python
def throughput(cores: int, processes: int, threads_per_process: int) -> dict[str, float]:
    total_threads = processes * threads_per_process
    # 超订越严重，同步与调度开销越大；效率上限归一到核数
    efficiency = min(1.0, cores / total_threads) ** 0.7
    useful = min(cores, total_threads) * efficiency
    return {"threads": total_threads, "efficiency": efficiency, "throughput": useful}


if __name__ == "__main__":
    for procs, threads in ((16, 16), (8, 8), (16, 1), (8, 2), (4, 4)):
        r = throughput(16, procs, threads)
        print(f"{procs:>2} 进程 × {threads:>2} 线程 = {r['threads']:>3} 线程, "
              f"效率 {r['efficiency']:.0%}, 吞吐 {r['throughput']:.1f}")
    print("结论：进程数 × 线程数接近核数时效率最高，超订会因同步与调度反噬")
```

**追问一**：为什么在 Python 里设置 `OMP_NUM_THREADS` 必须在 import numpy 之前？
→ 解析：OpenBLAS/MKL 在**库加载时**读取环境变量并初始化线程池，import 之后再改环境变量不会重新配置已经创建的线程池。容器启动脚本、supervisor 配置或进程池 initializer 里设置才有效。

**追问二**：容器里 `nproc` 显示 64，但配额只有 4 核，会出什么问题？
→ 解析：numpy/BLAS 和进程池会按 64 核开线程/进程，实际只有 4 核配额，造成严重超订与 CPU throttling；`os.cpu_count()` 也可能返回宿主机核数。应读 cgroup v2 的 `cpu.max` 或 v1 的 `cpu.cfs_quota_us`，按配额设置并发度。
