---
title: "[Q5656] 绑核 sched_setaffinity 与多进程缓存亲和成本账"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5656 · 绑核 sched_setaffinity 与多进程缓存亲和成本账

难度：P6 ｜ 标签：CPU 亲和性、sched_setaffinity、多进程、成本工程、NUMA

**问**：多进程 Python 服务在什么场景值得绑核（`os.sched_setaffinity`）？绑核的收益（缓存/局部性）与风险（核间负载不均、与容器配额冲突）怎么算？NUMA 机器上"worker 数 = 核数"为什么可能是错配？

**答**：
结论：绑核收益来自**减少迁移**：线程/进程在核间漂移会让 L1/L2 缓存与 TLB 反复失效，对"热数据集小、每核缓存敏感"的工作负载（大表扫描、正则引擎、压缩）迁移代价显著；对 IO 密集或 GIL 串行化的普通服务，绑核几乎无收益还引入调度僵硬。风险账：绑死后某核被其他进程占用（或容器 CPU 配额收缩）时，该 worker 无处可去直接饥饿；与 cgroup 配额叠加时绑核掩码超出配额核数会触发 CFS 限流加倍毛刺。NUMA 机器的正确配比是 **worker 数 = NUMA 节点数 × 每节点核数的整数倍**，且 worker 尽量绑定在"内存分配所在节点"的核上（numa_balancing 自动迁移有代价），单节点插满 worker 会跨节点访存、延迟翻倍。

取舍：绑核三个前置条件——① 物理机/独占 VM（共享宿主上绑核是与邻居的赌局）；② 工作负载 CPU 密集且数据局部性可预期；③ 有配套的 NUMA 内存绑定策略。容器/K8s 场景交给 CPU Manager static policy（整核分配）比自己绑核可控，应用层只做"核数感知"（`os.process_cpu_count`/cgroup 配额）。

实战：验证收益的实测法：固定 worker 与数据，`taskset`/affinity 对比开关两组跑 p99 与每秒指令数（`perf stat`），看缓存命中率（LLC miss）变化再决定；上线前把掩码与 cgroup 配额做一致性检查（`len(affinity) <= quota 核数`）。

```python
import os, sys, multiprocessing as mp

def report_affinity():
    try:
        allowed = os.sched_getaffinity(0)         # 当前可用核掩码（Linux）
        print("affinity cores:", sorted(allowed), "count:", len(allowed))
        return allowed
    except AttributeError:                         # macOS 无此 API
        print("sched_getaffinity 不可用（macOS）—— 用 os.cpu_count 降级感知:", os.cpu_count())
        return None

allowed = report_affinity()

def pin_and_run(worker_id, cores):
    if cores:
        os.sched_setaffinity(0, {cores[worker_id % len(cores)]})   # Linux 才生效
    # 模拟缓存敏感计算：重复扫同一个热列表
    data = list(range(200_000))
    s = 0
    for _ in range(3):
        for x in data:
            s ^= x
    return s

def bench(pinned):
    cores = sorted(allowed) if (allowed and pinned) else None
    with mp.Pool(min(4, mp.cpu_count())) as pool:
        return pool.starmap(pin_and_run, [(i, cores) for i in range(4)])

if __name__ == "__main__":                    # macOS spawn 必须
    print("unpinned run ok:", bench(False) is not None)
    if sys.platform.startswith("linux") and allowed:
        print("pinned run ok:", bench(True) is not None)
        # 配额一致性检查：绑核掩码不得超过 cgroup 配额核数（示例读取 quota）
        quota_path = "/sys/fs/cgroup/cpu.max"
        if os.path.exists(quota_path):
            quota = open(quota_path).read().split()
            print("cgroup cpu.max:", quota, " 掩码核数:", len(allowed))
    else:
        print("绑核实验需 Linux + sched_setaffinity，其他平台降级为仅核数感知")
```

**追问一**：为什么 NUMA 上"内存亲和"比"核亲和"更难自动做好？——Linux 的自动 NUMA balancing 靠缺页采样猜测"进程该搬到内存边还是页该搬过去"，Python 对象分配点分散（pymalloc arena 跨节点），猜测经常抖动；显式策略（`numactl --membind` + worker 分节点）在启动期就定死映射，比运行期自动迁移稳定得多。

**追问二**：绑核与 GIL 多线程组合为什么无意义？——同一进程内多线程共享一把 GIL，任意时刻只有一个线程执行 Python 字节码，绑核只减少线程间迁移，但真正的瓶颈是 GIL 串行化；绑核 + 多进程（各自独立解释器）才是有意义的组合，多线程场景应去解决"是否该用子解释器/自由线程"。

## 背诵要点
- 绑核收益 = 减少核间迁移的缓存/TLB 失效，仅对 CPU 密集 + 热数据集敏感负载值得；IO/GIL 负载无意义。
- 风险：掩码超配额触发 CFS 限流、共享宿主不可控；K8s 交给 CPU Manager static policy。
- NUMA 配比按节点整分，worker 绑"内存所在节点"的核；验证靠 perf LLC miss 对比。

## 复盘追问
- 一台 2 路 NUMA 机器上 32 个 worker 表现不如 16 个，如何定位到跨节点访存并重排？（perf/numastat 看远程访存比例；按节点分组绑核，讨论容器化后如何保留策略）
- 为什么把"绑核"写进部署基线常在换机器后翻车？（掩码与配额/拓扑耦合，讨论以探测+检查代替硬编码）
