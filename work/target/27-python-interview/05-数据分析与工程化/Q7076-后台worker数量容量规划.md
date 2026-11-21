---
title: "[Q7076] 后台 Worker 数量的容量规划账"
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7076 · 后台 Worker 数量的容量规划账

难度：P6 ｜ 标签：容量规划 / Celery / 队列 / worker

**问**：后台任务（Celery/RQ 类）队列高峰积压 40 分钟，团队直接把 worker 数从 4 加到 32，结果 DB 连接被抽干、任务超时反而变多。怎么算 worker 该开多少，而不是拍脑袋？

**答**：

**结论**：worker 数量账的公式：`所需 worker 数 = 到达率(任务/秒) × 单任务耗时(秒) / 1`（Little's Law 的并行版），再叠加约束项：每个 worker 进程/协程会占 N 个 DB 连接（连接池大小 × worker 数 ≤ DB max_connections 的 70%）、下游 API 配额（下游限 100 QPS 时 worker 吞吐被钳制）、单任务内存 × 并发 ≤ 机器内存。盲目加 worker 时这三个约束先崩：32 个 worker × 每个池 10 连接 = 320 连接直接打爆 DB，任务变慢重试增多，队列更堵——负反馈。

**取舍**：纵向（加大单 worker 并发）与横向（加进程数）的选择取决于任务瓶颈：CPU 型任务（图片处理）并发数 ≈ CPU 核数，加进程；IO 型任务（调 API、写 DB）并发数可以高（协程/线程），但要核对下游配额与连接池。另一个维度是"任务分级"：把快任务与慢任务分队列分 worker，避免一个 30 分钟的大任务占住 worker 让 10 万个小任务排队——积压 40 分钟常常不是 worker 不够，是队列没分级。

**实战**：容量账做成压测数据表：单任务耗时分布（P50/P95，注意长尾任务）、任务到达率按小时曲线、下游配额。三个产出：稳态 worker 数、峰值 worker 数与弹性触发条件、以及"约束先崩点"（DB 连接/下游配额/内存哪个先到顶）。Python 侧模拟不同 worker 数下的队列时延，找到"边际收益拐点"——加 worker 到某数量后 P95 时延不再降，就是停止点。

```python
# Worker 容量账：Little's Law + 约束先崩点（仅标准库，Python 3.9+）
from __future__ import annotations


def workers_needed(arrival_qps: float, task_p95_s: float,
                   concurrency_per_worker: int = 1) -> float:
    """IO 型任务：每 worker 可并发处理 concurrency 个任务。"""
    return arrival_qps * task_p95_s / concurrency_per_worker


def constraint_ceiling(db_max_conn: int, pool_per_worker: int,
                       memory_gb: int, mem_per_worker_gb: float,
                       downstream_qps: float, qps_per_worker: float) -> dict:
    return {
        "db": db_max_conn * 0.7 // pool_per_worker,       # DB 连接约束
        "memory": int(memory_gb / mem_per_worker_gb),      # 内存约束
        "downstream": int(downstream_qps / qps_per_worker),# 下游配额约束
    }


def main() -> None:
    # 到达 80 任务/s，P95 耗时 2s（IO 型），每 worker 8 并发
    need = workers_needed(80, 2, concurrency_per_worker=8)
    print(f"理论需要 worker 数: {need:.0f}")

    ceil = constraint_ceiling(db_max_conn=200, pool_per_worker=10,
                              memory_gb=16, mem_per_worker_gb=1.5,
                              downstream_qps=300, qps_per_worker=12)
    print("各约束允许的最大 worker 数:", ceil)
    limit = min(ceil.values())
    assert limit <= ceil["db"], "DB 连接通常先崩"
    print(f"约束先崩点: {min(ceil, key=ceil.get)} 上限 {limit} 个 worker")

    # 32 worker × 10 连接 = 320 > 200×0.7=140 → 连接打爆，正是事故现场
    assert 32 * 10 > 200 * 0.7
    # 正确解：每 worker 池缩到 3，开 8 个 worker = 24 连接，并发 64 够用
    assert 8 * 3 <= 140 and 8 * 8 >= need
    print("结论：8 worker × 8 并发 × 3 连接，吞吐够且连接安全")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么按 P95 而不是 P50 耗时算 worker 数？——P50 只覆盖一半任务，长尾任务（下游偶发慢）按 P50 算会让积压在长尾时段形成；且长尾任务占住并发槽的时长是普通任务的数倍，对"在制品"数量的贡献不成比例。更严格按 P99 加惩罚系数。
- 追问 1.1：Little's Law 算出的数为什么还要再打折？——公式假设到达均匀；真实到达是脉冲（整点跑批），瞬时到达率可能是均值的 5 倍，worker 数按峰值脉冲校验而不是平均值，否则整点必积压。
- 追问 2：队列分级（快慢分队列）后怎么防"慢任务饿死"？——给慢队列限流（并发上限 + 每 N 分钟配额）而非无限排队；再加死信队列与任务 TTL，让过期的慢任务直接失败进死信，不占活 worker。监控上分队列看积压时长 SLO。

**背诵要点**：

1. worker 数 = 到达率 × 任务耗时(P95) / 单 worker 并发，再被三个约束钳制：DB 连接（worker×池 ≤ 70% max_conn）、内存、下游配额，取最小。
2. 盲目横向扩 worker 的负反馈：连接打爆 → 任务变慢重试增多 → 队列更堵。
3. 积压常见根因是队列未分级：快慢分队列 + 慢队列限流 + 死信队列，比加 worker 便宜且有效。

**复盘追问**：

1. 如果 DBA 拒绝提高 max_connections，你还有哪三条路消化 80 QPS 的任务量？
2. 单任务 P95 从 2s 涨到 6s（下游变慢），worker 账怎么自动重算而不是等事故？
