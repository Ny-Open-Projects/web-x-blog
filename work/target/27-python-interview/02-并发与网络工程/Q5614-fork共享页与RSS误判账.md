---
title: [Q5614] fork 共享页与 RSS 误判容量账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5614 · fork 共享页与 RSS 误判容量账

> 难度:★★★★★ | 标签:容量规划, fork, 内存观测

**问**:pre-fork 模型下父进程 2GB，起 16 个 worker 后监控上 RSS 总和 32GB，告警内存翻倍；但 K8s Pod 的 OOM 却按 4GB limit 没触发。到底占了多少内存？RSS、PSS、USS 各在算什么，容量该按哪个估？

**答**:结论：fork 的 COW（写时复制）让子进程与父进程**共享物理页**：RSS 是"每个进程看到的虚拟映射量"，共享页被**每个进程重复计入**，16 个 worker 的 RSS 求和把同一份 2GB 算了 17 遍——纯观测误判。内核真实消耗看 **PSS（按共享比例分摊）**：某页被 N 进程共享则各计 1/N，PSS 求和≈物理真实占用；**USS（独占内存）** 是子进程真实新增的部分。容量规划公式：`峰值物理内存 ≈ 父进程 RSS + Σ(每 worker 的 USS)`，而 COW 的动态性在于：Python 对象一被写入（refcount 变更也算写！）就触发页复制，**引用计数让几乎所有 Python 对象页随时间被逐页"写脏"**，`gc.freeze()`（把现存对象标记为不朽、跳过 refcount 写）能把导入后的常驻对象保住共享——这就是 pre-fork 服务"先 import、再 freeze、后 fork"套路（对照 Q413/Q5013 immortal objects）的原理。观测落地：macOS 用 `footprint`/vmmap，Linux 读 `/proc/[pid]/smaps_rollup` 的 Pss/Private_*。注意容器 OOM 按 cgroup 的**物理页**算，与 RSS 求和无关——所以"RSS 告警翻倍"多半是监控口径错误，先修观测再谈扩容。

```python
import os, sys, subprocess, textwrap

if sys.platform == "darwin":
    # macOS: 用 footprint 看真实占用（RSS 同样存在共享页重复计入）
    pid = os.getpid()
    out = subprocess.run(["footprint", str(pid)], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if "phys_footprint" in line or "RESIDENT" in line:
            print("[macOS]", line.strip()[:100])
else:
    # Linux: smaps_rollup 是 PSS/USS 的标准读取点
    def rollup(pid):
        d = {}
        for line in open(f"/proc/{pid}/smaps_rollup"):
            k = line.split(":")[0]
            if k in ("Rss", "Pss", "Private_Clean", "Private_Dirty"):
                d[k] = int(line.split()[1])          # 单位 kB
        return d
    print("[Linux] 父进程:", rollup(os.getpid()))

# fork 共享页的最小实验：父进程持大对象，子进程只读 → 物理页共享
big = bytearray(64 * 1024 * 1024)             # 64MB
big[:] = b"\x01" * len(big)                   # 触碰所有页，确保真实分配

pid = os.fork() if sys.platform != "win32" else None
if pid == 0:
    # 子进程：先只读 → 共享；再写一个字节 → 4KB 页复制
    _ = big[0]                                # 只读，COW 不复制
    os._exit(0)
else:
    _, status = os.waitpid(pid, 0)
    print("子进程只读退出，物理内存未翻倍：64MB 页在父子间共享（RSS 各计 64MB，PSS 各计一半）")

# 写脏演示：子进程改一个字节触发 4KB 页复制
if sys.platform != "win32":
    pid = os.fork()
    if pid == 0:
        big[0] = 2                            # 只复制 1 页，不是 64MB
        os._exit(0)
    os.waitpid(pid, 0)
    print("子进程写 1 字节 → 仅 1 个 4KB 页复制（COW 页粒度），而非整段对象")

# Python 对象为什么更糟：refcount 就是写
print("结论：GC 头引用计数随访问变化，导入后的对象页会被逐页写脏；")
print("      gc.freeze()（导入后调用）可冻结这些对象保住共享。")
print("gc.freeze 存在:", hasattr(__import__("gc"), "freeze"))
```

**追问一层**:为什么"引用计数也算写"？`gc.freeze()` 之后又 import 了新模块、新建了对象，共享率会怎么变？
**追二层**:RSS/PSS/USS 三者在容器 limit、HPA 弹性、告警阈值三个场景各应该用哪个？为什么 `multiprocessing` 的 spawn 模式下 PSS≈RSS（共享消失，引 Q5535）？

**背诵要点**
- fork COW：RSS 每进程重复计入共享页，求和是观测误判；物理真实占用看 PSS（分摊）与 USS（独占）。
- 容量公式 ≈ 父 RSS + Σ(每 worker USS)；Python refcount 是写操作，对象页会逐页被复制。
- "先 import → gc.freeze() → 后 fork"保住共享；容器 OOM 按 cgroup 物理页计，与 RSS 求和无关。

**复盘追问**
- 监控已按 RSS 求和跑了两年才在容量评审翻车，观测口径怎么一次性修正？提示：采集端直接读 smaps_rollup Pss，或用 cgroup 级 memory.current。
- gc.freeze 后内存共享率仍持续下降，怎么定位"谁在写脏页"？提示：/proc/pid/pagemap 差分或 psutil shared_memory 趋势，常见是模块级缓存在 fork 后被写。
