---
title: [Q5542] 线程栈内存与 stack_size 容量账
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5542 · 线程栈内存与 stack_size 的容量账

> 难度:★★★☆ | 标签:threading, stack_size, 容量规划, 内存

**问**："每线程 8MB 内存"这个说法哪里对哪里错？给一个"千线程转储任务"的服务做内存容量规划，`threading.stack_size` 能省多少、有什么坑？线程数上限到底受什么约束？

**答**：8MB 是 Linux 默认**虚拟内存**每线程栈预留（`ulimit -s`），不是 RSS——实际物理内存按触页分配，通常只有几十 KB 到几百 KB。所以容量账要分两个口径：**虚拟地址空间**（64 位几乎无限，但容器/内核 mapping 数量与 overcommit 策略仍可能拒绝）与 **RSS**（真实约束，含线程对象、解释器帧、TLS 等）。Python 侧可用 `threading.stack_size(bytes)` 设置新线程栈大小（对之后的线程生效），下限受平台限制（macOS 最低 512KB 的对齐值、Linux 32KB 量级），缩小栈能同时压虚拟与物理占用，但**栈太深会爆**：Python 级递归还受 `sys.setrecursionlimit` 限制（Q2610），C 扩展深递归直接段错误且无保护。真正的线程数上限约束排序：内存（RSS 账）> 内核线程/调度成本 > fd 等资源。容量公式：`线程内存预算 = N × (栈实际触页 + 解释器开销 ~ 数十KB)`，做规划时按"栈预留 × 5% 触页率 + 每线程 100KB 运行时"起步，压测校准。对比项：IO 密集场景更该考虑换协程（每任务 KB 级，Q5546），线程栈账是"为什么不能万级线程"的量化答案。

```python
# file: code/02_并发与网络工程/q5542_thread_stack.py
import threading
import sys

print("python:", sys.version_info[:3])

# 1) 平台默认与下限
print("默认栈预留(ulimit -s 口径, KB):", threading.stack_size() // 1024 or "未设置")

# 2) 设置更小的栈: 对"之后创建"的线程生效, 必须在 start 前调用
threading.stack_size(512 * 1024)               # 512 KB

def probe():
    import ctypes
    # 读真实触发页数(RSS 口径近似): 触碰页面才分配物理内存
    depth = 0
    try:
        def recur(n):
            return recur(n + 1) if n < 2000 else n
        recur(0)                               # 深递归验证栈是否够用
        depth = 2000
    except RecursionError:
        pass
    print(f"线程内: 512KB 栈上 Python 深递归 {'可达' if depth else '受限'}")

t = threading.Thread(target=probe)
t.start(); t.join()

# 3) 千线程内存账: 虚拟预留 vs 估算 RSS
N = 1000
default_reserve = 8 * 1024 * 1024              # Linux 默认 8MB/线程(虚拟)
tiny_reserve = 512 * 1024
per_thread_runtime = 100 * 1024                # 解释器对象/TLS 经验值
print(f"千线程虚拟预留: 默认栈 {N*default_reserve/1e9:.1f} GB | 512KB 栈 {N*tiny_reserve/1e9:.1f} GB")
print(f"千线程 RSS 量级估算(5% 触页 + 运行时): 约 {N*(default_reserve*0.05+per_thread_runtime)/1e9:.2f} GB")

# 4) 上限探测: 实际能起多少线程(受 RLIMIT_NPROC/内存约束, 谨慎小规模验证)
def try_spawn(n):
    made = 0
    for _ in range(n):
        th = threading.Thread(target=lambda: None)
        try:
            th.start(); made += 1; th.join()
        except RuntimeError as e:
            return made, str(e)
    return made, "ok"

made, msg = try_spawn(200)
print(f"本轮启动线程 {made}/200: {msg}")
```

**追问**：1) 为什么容器里 8MB 虚拟预留也"看不见"但在极端下仍会炸？——cgroup memory 只算 RSS，但内核 `vm.max_map_count`（每个线程至少一个栈 mapping）与 overcommit 拒绝策略在万级线程时先撞上限；排查用 `cat /proc/<pid>/maps | wc -l`。2) `stack_size` 与 `sys.setrecursionlimit` 什么关系？——前者是物理栈空间（C 层），后者是 Python 层帧数上限；两者任一先到顶都表现为栈溢出，调大 recursionlimit 时必须同步确保 C 栈够大，否则 C 扩展/解释器自身递归段错误。3) 为什么说"线程数上限"本质上是个经济问题？——每线程固定成本（栈+调度+缓存失效）随数量线性增长而吞吐不增，Q5513 的池大小公式就是找这个收益拐点。

## 背诵要点
- 8MB/线程是虚拟预留非 RSS；RSS 按"5% 触页 + 每线程 ~100KB 运行时"起步估算，压测校准。
- `threading.stack_size()` 在线程 start 前设置，压栈省虚拟与物理内存，但栈深与 recursionlimit 要配套。
- 真实上限：内存 RSS > 内核 mapping（max_map_count）> 调度成本；IO 密集换协程更省。

## 复盘追问
- 千线程服务在容器里出现"无法创建新线程"报错，你的排查顺序是什么？（提示：先看 cgroup RSS 与 max_map_count，再看 RLIMIT_NPROC，最后才是代码泄漏未 join）
- 把 8MB 栈改 512KB 后个别线程随机段错误，如何定位是栈不够还是 C 扩展问题？（提示：faulthandler 栈回溯 Q1836 + 对比默认栈复跑，隔离递归深度）
