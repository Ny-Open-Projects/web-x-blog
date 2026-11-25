---
title: [Q7134] pytest-xdist 并行 worker 的内存与核数配比容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7134 · pytest-xdist 并行 worker 的内存与核数配比容量账

难度：P6 ｜ 标签：容量规划 / 测试工程 / CI

**问**：测试套件里几个"大用例"（加载真实数据集、起浏览器、连测试容器）让 `-n auto` 的 xdist 并行跑到一半被 OOM killer 杀掉。怎么给 xdist 建 worker 数的容量账：内存账怎么算、CPU 和内存谁是瓶颈、CI Runner 上怎么落地？

**答**：
- **结论**：xdist 每个 worker 是**独立解释器进程**，内存 = 解释器+依赖基线（import pandas/matplotlib 后 200-500MB 量级）+ 用例自身数据 + fixture 状态。容量账三条：① **内存账是常见真瓶颈**：`worker数上限 = (Runner内存 - 系统与主进程余量) / 单worker峰值内存`，单 worker 峰值要按**最重用例**实测（tracemalloc/resource 或容器 cgroup 峰值），不是平均值——OOM 按峰值触发；② CPU 账：worker 数 > 物理核数后只是排队不加速（纯 CPU 用例），但 IO 等待型用例可以超卖；③ `pytest-xdist` 的 `-n auto` 按核数定 worker，完全不考虑内存——所以内存紧的环境必须显式 `-n N` 或 `--maxprocesses`，这是 OOM 事故的直接原因。另外 grouping（`--dist loadscope`）把同模块用例粘到同一 worker，能避免重复 import 大库，间接降总内存。
- **取舍**：worker 数加倍的收益曲线是先陡后平——超过核数或"重用例串行化"之后边际收益为负，还要付内存与 flaky（共享环境并发访问）代价。内存紧的替代方案：拆分慢套件到不同 CI job（矩阵分片，Q7003），比单机硬堆 worker 更稳。
- **实战**：① CI 里给 runner 容器显式内存 limit 并对 worker 峰值做一次实测标定，写进仓库文档；② 用 `--dist loadscope` + 重用例单独 job 的组合；③ 把"套件内存峰值"做成可观测指标（每次 CI 采 RSS 峰值），回归超阈值告警——与 Q7044 的 Runner 并发账拼成完整 CI 容量模型。

```python
# xdist worker 容量账: 内存优先定 worker 数, CPU 只影响加速比
# 基线: Python 3.9+ 标准库; 线上用容器 cgroup / resource.getrusage 实测峰值
import math
from dataclasses import dataclass


@dataclass
class RunnerCap:
    ram_gb: float
    reserved_gb: float        # 系统 + 主进程 + 余量
    worker_peak_gb: float     # 最重用例的 worker 峰值内存
    cores: int
    io_bound: bool = False

    def max_workers_by_ram(self) -> int:
        return max(1, int((self.ram_gb - self.reserved_gb)
                          / self.worker_peak_gb))

    def effective_workers(self) -> int:
        """最终 worker 数 = min(内存上限, CPU 上限)。IO 等待型可超卖 2 倍核。"""
        cpu_cap = self.cores * 2 if self.io_bound else self.cores
        return min(self.max_workers_by_ram(), cpu_cap)


def main() -> None:
    # 16GB runner, pandas 套件单 worker 峰值 1.2GB, 8 核
    cap = RunnerCap(ram_gb=16, reserved_gb=2, worker_peak_gb=1.2, cores=8)
    assert cap.max_workers_by_ram() == 11     # (16-2)/1.2 = 11
    assert cap.effective_workers() == 8       # CPU 先成为瓶颈
    # 浏览器套件: 单 worker 峰值 3GB, 内存成为瓶颈
    browser = RunnerCap(ram_gb=16, reserved_gb=2, worker_peak_gb=3.0,
                        cores=8, io_bound=True)
    assert browser.max_workers_by_ram() == 4
    assert browser.effective_workers() == 4   # 内存压过 CPU 超卖
    # OOM 反例: -n auto(=8) 用浏览器套件 -> 需求 8*3=24GB > 16GB
    assert 8 * browser.worker_peak_gb > browser.ram_gb
    print(f"pandas 套件: 8 workers (CPU 瓶颈); "
          f"浏览器套件: 4 workers (内存瓶颈, auto 必 OOM)")
    print("OK: worker 数 = min(内存账, CPU 账); 峰值按最重用例实测")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 OOM 按峰值而不是按均值触发？
→ 一句话提示：内核 OOM killer 看的是触发瞬间的实际内存，用例错峰时均值 800MB 也可能在同时跑到峰值用例时叠加出 24GB——容量账必须按同刻最坏叠加。

**追问 2**：`--dist loadscope` 为什么能间接降内存？
→ 一句话提示：同 scope 用例固定在同一 worker，避免大模块 import 与 fixture 在多个 worker 各复制一份；代价是负载可能不均，某个 scope 拖长尾。

## 背诵要点
- worker 数 = min(内存账, CPU 账)；内存账 = (Runner 内存 - 余量) / 单 worker 峰值（按最重用例实测）。
- `-n auto` 只按核数分配、不看内存——内存紧环境必须显式 `-n`/`--maxprocesses`，这是 OOM 事故直接原因。
- IO 等待型用例 CPU 可超卖 2 倍；`--dist loadscope` 合并 scope 省 import 内存，重套件拆分 CI job 更稳。

## 复盘追问
- 如何在 CI 里持续监控套件内存峰值？提示：每次 job 采集 cgroup memory.peak 或 worker RSS 峰值上报，设基线阈值，回归超 20% 告警。
- 内存与 CPU 都不够时，加 Runner 还是拆套件？提示：拆套件到矩阵 job 的边际成本更低（可并行到多台），加 Runner 内存规格的钱通常贵于时间收益；先分片再谈规格。
