---
title: [Q6010] 3.12 perf 与 py-spy 生产定位路径
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6010 · 3.12+ perf 与 py-spy 生产定位路径

> 难度:★★☆ | 标签:py-spy 0.3.14+, Linux perf, Python 3.12+

**问**：生产服务 CPU 打满，py-spy 和 3.12 的 perf 集成怎么分工？各自的开销和限制是什么？

**答**：分工是「现场急救 vs 持续观测」：1) **py-spy**（外部进程 attach，`pip install py-spy`）：不重启、不侵入目标进程，`py-spy dump --pid X` 先抓一次栈快照定性（卡在哪个调用），`py-spy record -o flame.svg --pid X -d 30` 采 30 秒出火焰图。优势是秒级上手、对业务零改造；限制是**外部采样**——靠读进程内存推断调用栈，C 扩展内部、释放 GIL 的等待段可能失真，且需要 ptrace 权限（容器里要注意 capabilities/`SYS_PTRACE`）。2) **Python 3.12 的 perf 集成**：`PYTHONPERFUPPORT=1` 启动（构建需启用 perf trampolines），解释器会为 JIT 风格的样本生成 map 文件，Linux `perf record -F 99 -g -p X` 采集后 `perf script | stackcollapse-perf.pl | flamegraph.pl` 出图，样本能精确归属到 Python 帧。优势：开销更低、与系统级视图（内核栈、off-CPU）同源，能做持续采样与 `perf sched/offcputime` 类分析；限制：仅 Linux、依赖 3.12+ 与特定构建选项、拿到的是采样后要二次处理的数据。实践路径：故障时先 `py-spy dump` 看现场（不采数据先定性），再 `record` 采样定热点；长期治理把 perf/ebpf 接入持续观测。别忘了两个前置：确认进程不是 IO 等待（CPU 100% 才是这两把刀的战场），以及线上进程要保留符号（strip 过的部署会让归属失效）。

```python
# 基线:Python 3.9+(demo 本身);py-spy 0.3.14+/perf 集成需 Python 3.12+ 且仅 Linux。
# 以下用标准库 sys._current_frames 做一个"穷人版采样器",演示 py-spy 的原理:外部轮询读栈。
import collections, sys, threading, time

def cpu_burn():
    x = 0
    while True:
        x += sum(i * i for i in range(100))   # 模拟热点函数

stop = threading.Event()
t = threading.Thread(target=cpu_burn, daemon=True); t.start()

def sample(times=20, interval=0.02):
    """轮询所有线程当前栈,统计热点 —— py-spy/perf 的最小原理模型"""
    counts = collections.Counter()
    for _ in range(times):
        for tid, frame in sys._current_frames().items():
            names = []
            f = frame
            while f:
                names.append(f.f_code.co_name)
                f = f.f_back
            counts[" > ".join(reversed(names))] += 1
        time.sleep(interval)
    return counts

for stack, n in sample().most_common(3):
    print(f"{n:3d}  {stack[:90]}")
print("—— 真实工具:py-spy record(火焰图)/ perf record(PYTHONPERFUPPORT=1, 3.12+, Linux)")
print("命令参考:")
print("  py-spy dump --pid <PID>                # 单次栈快照,先定性")
print("  py-spy record -o flame.svg --pid <PID> -d 30 -r 100   # 30s 采样出火焰图")
print("  PYTHONPERFUPPORT=1 perf record -F 99 -g -p <PID> -- sleep 30  # 3.12+ 精确归属 Python 帧")
```

**追问**：
1) py-spy 能测 off-CPU 时间吗？——能但要换姿势：`py-spy dump` 只看瞬时栈；off-CPU 分析（进程「卡着不烧 CPU」）更适合 perf/ebpf 的 offcputime，或者应用层加 span。判断依据：CPU 100% 用采样器，CPU 低但延迟高用 off-CPU 工具/链路追踪，别拿火焰图去查锁等待。
2) 容器里 py-spy attach 失败的常见原因？——缺 `SYS_PTRACE` capability、共享 pid namespace 没有（kubectl exec 进的容器看不到宿主进程）、或者安全模块限制 ptrace；K8s 的对策是 ephemeral container 共享进程命名空间，或 sidecar 里有权限时用 `--nonblocking` 降低对目标进程的暂停影响。
3) 3.12 的 perf 支持为什么要环境变量开关而不是默认开？——启用后会为每个 Python 函数调用经过 trampoline 并写 map 文件，有轻微开销和磁盘写入；默认关闭保证零回归，也避免长期生产进程无限增长 map 文件。开启要评估：定位窗口期临时开（滚动重启带变量），而不是全量常开。
