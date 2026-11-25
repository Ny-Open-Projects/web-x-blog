---
title: [Q7186] 调度 DAG 并发与 worker 内存容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7186 · 调度 DAG 并发数与 worker 内存容量账

难度：P6 ｜ 标签：容量规划、调度系统、并发上限、内存

基线：Python 3.9+；Airflow 2.x / Celery worker / Prefect 3；pandas 2.x 任务负载。

**问**：Airflow 上百个 DAG，每天 2 点到 4 点集中跑批，某个时段 8 个 pandas 任务并发，每个峰值 6GB 内存，worker 机 32GB 内存却 OOM 了。为什么 8×6=48GB 的账没人提前算？并发数该怎么定？

**答**：
- **结论**：调度系统的并发上限默认是"任务个数"口径（max_active_tasks / worker slots），不是"资源"口径——slot 数 × 单任务真实峰值内存才是真实需求，而单任务峰值 ≠ 稳态内存，pandas 读一个大 CSV 的峰值可能是稳态的 3~5 倍（解析中间态 + 副本）。容量账公式：`安全并发 = worker 内存 × 0.7（余量） / 单任务 P95 峰值`。按此例：32×0.7/6 ≈ 3.7，安全并发只有 3，配 8 个 slot 必然 OOM。
- **取舍**：三选一——(1) 降并发（pool/slot 按资源口径拆分：内存池、CPU 池分开限额）；(2) 降单任务峰值（chunked 读、Arrow 后端、改为数据库聚合）；(3) 弹性扩 worker（K8s executor 按需起 pod，但要算 cold start 与配额）。批量错峰也是合法手段：把内存大户在时间轴上排开，等效降低峰值并发。
- **实战**：先给每个任务打标（预估内存档位 small/mid/large），调度池按档位分池；监控用"worker 内存水位 + 各池排队长度"双指标，排队变长说明池子太小而不是机器不够。

```python
# 并发容量账：资源口径的 slot 规划模拟（标准库可运行）。
import math

def plan_pool(tasks: list[dict], worker_mem_gb: float, safety: float = 0.7):
    """tasks: [{'name':..., 'peak_gb': 单任务P95峰值内存, 'count': 每天任务数}]"""
    usable = worker_mem_gb * safety
    small = [t for t in tasks if t["peak_gb"] <= 1]
    large = [t for t in tasks if t["peak_gb"] > 1]
    large_mem = max(t["peak_gb"] for t in large) if large else 1
    large_slots = math.floor(usable / large_mem)          # 大内存池并发
    small_slots = math.floor(usable / 1.0)                # 小内存池并发
    return {
        "可用内存GB": usable,
        "large池并发": max(large_slots, 1),
        "small池并发": small_slots,
        "建议": "按资源拆池，禁止用一个任务数口径的 slot 承载不同内存档位",
    }

def simulate_oom(tasks_peak: list[float], slots: int, worker_mem_gb: float,
                 safety: float = 0.7) -> list[str]:
    """不同 slot 并发下的瞬时峰值内存：8 个 slot 全开 vs 按大内存档拆池。"""
    usable = worker_mem_gb * safety
    peak = 0.0
    running: list[float] = []
    for p in tasks_peak:
        running.append(p)
        if len(running) > slots:
            running.pop(0)
        peak = max(peak, sum(running))
    return [f"slots={slots}: 瞬时峰值 {peak:.0f}GB / 可用 {usable:.0f}GB -> "
            + ("OOM 风险" if peak > usable else "安全")]

if __name__ == "__main__":
    print(plan_pool([{"name": "a", "peak_gb": 6, "count": 8}],
                    worker_mem_gb=32))
    # 4 个 6GB 大户 + 4 个 1GB 小户：
    for line in simulate_oom([6, 6, 6, 6, 1, 1, 1, 1], slots=8, worker_mem_gb=32):
        print(line)
    for line in simulate_oom([6, 6, 6, 6, 1, 1, 1, 1], slots=3, worker_mem_gb=32):
        print(line)
```

**追问**：
- 一层：为什么单任务内存要按 P95 峰值而不是均值？→ 提示：OOM 是瞬时事件，均值口径的 pool 必然被峰值击穿；峰值数据从任务历史监控取。
- 二层：K8s 上用 memory request=limit=6GB 的 pod 跑这类任务有什么副作用？→ 提示：超过 limit 直接 OOMKill 无重试现场；request 留余量又拉低节点装箱率，要按 P95+buffer 定。

**背诵要点**：
1. 并发上限要从"任务数口径"换成"资源口径"：安全并发 = 可用内存×0.7 / 单任务 P95 峰值。
2. 单任务峰值可能是稳态 3~5 倍，账必须按峰值算；降峰手段：chunked/Arrow/下推数据库聚合。
3. 治理手段三选一或组合：按内存档位拆池、时间轴错峰、K8s 弹性；排队长度是池子太小信号。

**复盘追问**：
1. 为什么没人算 8×6 这笔账？提示：slot 默认值沿用模板，资源口径评审缺失；加入"新任务上量要报峰值内存"流程。
2. 错峰和降峰都做了还不够怎么办？提示：说明进入分片/外置计算（数据库聚合、Spark/Polars on cluster）的结构性改造区。
