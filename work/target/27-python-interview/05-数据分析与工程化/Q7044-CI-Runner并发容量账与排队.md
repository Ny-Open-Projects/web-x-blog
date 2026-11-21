---
title: [Q7044] CI Runner 并发容量账：排队时间与 runner 数的推算
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7044 · 容量规划：CI 上的任务排队 40 分钟，是加 runner 还是拆任务？

> 难度:★★★ | 标签:容量规划, CI, 排队论

**问**：团队 30 人，每人每天触发 6 次 CI，单次流水线 12 分钟，现有 runner 并发数 4，高峰期任务排队 40 分钟。怎么定量推算需要多少 runner？"排队=加机器"在什么前提下成立？加机器与拆任务（并行化/缓存）怎么组合决策？

**答**：结论：先用账算清楚——**到达率 λ = 30 人 × 6 次 ÷ 8h 工作时间 ≈ 0.0625 次/分钟**，但 CI 到达是突发分布（集中在上下午），峰值到达率取均值的 3-5 倍；并发容量 c 要满足"峰值排队时间 < 目标反馈时长"。本题均值负载 0.75 runner 就够，为什么排 40 分钟？因为**突发集中 + 流水线长尾任务占住 runner**——加机器能解突发，解不了长尾；长尾要用拆任务与缓存把 P99 压下来，两者组合而非二选一。

机理与实战：
- **容量公式**：目标反馈 T_target = 排队 T_q + 执行 T_s。用 Little's Law 与 M/M/c 近似：ρ = λ_peak × T_s / c，ρ 逼近 1 时排队爆炸（排队时间按 (ρ/(1-ρ)) 量级增长），所以工程上把 **ρ 上限压到 0.7**：c ≥ λ_peak × T_s / 0.7。取 λ_peak=0.25 次/分钟（突发系数 4）、T_s=12 分钟 → c ≥ 4.3，即 5 个 runner 起步，再按 P99 执行时长修正。
- **长尾问题**：总排队时间 ≈ Σ(前方每个任务剩余时长)，一个 45 分钟的集成测试占住 runner，后面 8 个 2 分钟任务全部陪跑——**runner 数解决的是并发带宽，任务时长分布决定 P99 体验**。治理长尾：把 45 分钟任务拆成并行 shard（pytest-xdist/分片矩阵）、依赖安装用缓存命中压到 1 分钟内。
- **成本侧账**：runner 单价 × 并发数是线性成本，任务时长 × 触发次数是分钟账单——两者相乘才是总成本。拆任务/缓存是"降分子"，加 runner 是"提分母的并发"；先降分子再提并发，因为降分子对成本与延迟双收益。
- **突发应对**：λ 不可控（人的行为），给 runner 加自动弹性（自托管 K8s runner 按队列深度扩容），并设"排队时长告警"作为容量触发器而不是人肉感知。

```python
# 基线:Python 3.10+;纯标准库,CI 容量推算:Little's Law + 利用率上限 + 排队模拟
from __future__ import annotations
import random


def required_runners(arrivals_per_min: float, burst_factor: float,
                     task_minutes: float, utilization_cap: float = 0.7) -> int:
    """c >= lambda_peak * T_s / utilization_cap。"""
    lam_peak = arrivals_per_min * burst_factor
    return max(1, -(-int(lam_peak * task_minutes * 100) // int(utilization_cap * 100)))


def simulate_queue(task_minutes: list[float], runners: int,
                   seed: int = 3) -> tuple[float, float]:
    """FCFS 排队模拟:返回(平均等待, P99 等待)分钟。"""
    rng = random.Random(seed)
    arrivals: list[tuple[float, float]] = []
    t = 0.0
    for dur in task_minutes:
        arrivals.append((t, dur))
        t += rng.expovariate(1 / 1.5)  # 平均 1.5 分钟到达一个任务
    free_at = [0.0] * runners
    waits: list[float] = []
    for arrival, dur in arrivals:      # FCFS:分配最早空闲的 runner
        start = max(arrival, min(free_at))
        waits.append(start - arrival)
        free_at[free_at.index(min(free_at))] = start + dur
    waits.sort()
    return sum(waits) / len(waits), waits[-1]


def demo() -> None:
    # 现状:0.0625 次/分钟 × 突发 4 = 峰值 0.25,单任务 12 分钟
    c = required_runners(0.0625, 4, 12)
    print(f"利用率 0.7 上限 -> 建议 runner: {c}")
    assert c == 5
    # 模拟:长尾任务(1 个 45 分钟)对 P99 等待的杀伤
    tasks = [2.0] * 40 + [12.0] * 6 + [45.0]
    avg4, p99_4 = simulate_queue(tasks, 4)
    avg8, p99_8 = simulate_queue(tasks, 8)
    print(f"runner=4: 平均等 {avg4:.1f}min / P99 {p99_4:.1f}min")
    print(f"runner=8: 平均等 {avg8:.1f}min / P99 {p99_8:.1f}min")
    assert avg8 < avg4
    # 拆长尾:45min -> 5x9min 后,P99 显著下降
    tasks_sharded = [2.0] * 40 + [12.0] * 6 + [9.0] * 5
    avg5s, p99_5s = simulate_queue(tasks_sharded, 5)
    print(f"runner=5+长尾拆分: 平均 {avg5s:.1f}min / P99 {p99_5s:.1f}min")
    assert p99_5s < p99_4
    print("CI 容量账:rho<=0.7 定并发,长尾拆分定 P99,先降分子再提并发 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么利用率的红线是 0.7 而不是 0.9？
答：排队论里排队时间与 (1-ρ) 成反比：ρ=0.7 时平均排队可控，ρ=0.9 时排队时间放大近 4 倍且方差剧增，ρ→1 时任何到达波动都会让队列指数堆积。容量规划要留的是"波动吸收余量"，0.7 是工程经验值——这也解释了"加到 90% 利用率反而更慢"的反直觉现象。

**追问二**：共享 runner 池上，A 团队的长任务会影响 B 团队的反馈时长，怎么治理？
答：① 按"流水线分钟数"给团队配预算并限额（超过的排队降权）；② 关键分支（main/release）走独立高优先级队列实现公平共享（DRF 加权）；③ 长任务强制打标签并要求 shard 化才能进共享池。本质是把 CI 当多租户系统治理——容量、隔离、优先级三件套缺一不可。

## 背诵要点
- 容量公式 c ≥ λ_peak×T_s/0.7（ρ 上限 0.7 吸收波动，λ 取突发系数 3-5 倍）；利用率 0.9 时排队时间放大数倍，ρ→1 队列爆炸。
- runner 数管并发带宽，任务时长分布管 P99：一个 45 分钟长尾任务让后面短任务全陪跑，治理靠 shard 拆分+依赖缓存先降分子。
- 总成本 = runner 单价×并发 + 分钟账单；排队时长告警是容量触发器，多团队共享池按预算限额+优先级队列治理。

## 复盘追问
- 为什么"每人每天 6 次"这个到达率在季度末会突然翻倍？（提示：deadline 行为（集中提交/rebase 触发链式流水线）让 λ 与工作日历相关；容量要按峰值周建模并设季度容量评审，不能按年均值）
- 缓存命中率从 60% 提到 95% 后还需要 5 个 runner 吗？（提示：命中把安装类时长从 8 分钟压到 1 分钟，T_s 降一半以上，容量公式 c 同比下降——先降分子再提并发，加机器决策要在缓存优化之后重算）
