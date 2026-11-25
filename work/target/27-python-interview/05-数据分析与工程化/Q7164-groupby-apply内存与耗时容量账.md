---
title: [Q7164] groupby-apply内存与耗时容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7164 · groupby-apply 的内存与耗时容量账：什么时候会爆

难度：P6 ｜ 标签：容量规划、pandas、性能
基线：pandas 2.x/3.0（3.0 对 groupby.apply 的 include_groups 默认值有变，写法注意）。

**问**：一条 `df.groupby("user").apply(custom_fn)` 在百万行数据上跑挂了内存。groupby-apply 的内存与耗时上限怎么估？什么写法能把它降下来？

**答**：**结论**：groupby-apply 的成本由两个数决定：**组数 G**（apply 被调用 G 次，Python 层函数调用开销 G × 单次耗时）和**最大组行数**（每组的中间结果都要物化）。内存爆点通常不是原始数据，而是 apply 内部构造的中间 DataFrame：若每组结果都收集进列表再 concat，峰值内存 ≈ 原始 df + 全部中间结果之和。耗时上，G 大（百万级组）+ fn 慢（>1ms）就是小时级任务，这是 apply 与向量化聚合的量级差距来源。

**取舍**：降本三级台阶：① 能用向量化聚合（sum/mean/自定义 numba 化）就不用 apply——G 次解释器调用消失；② 必须 apply 时用 `engine="numba"` 或把 fn 改成只接收 ndarray、避免每组构造 DataFrame；③ G 真的大就换 polars 的 groupby + 表达式，或分块处理 + 进程池（注意每组结果的合并也要记账）。

**实战**：容量估算公式先跑：`G × per_call_ms` 估耗时、`df 内存 + 组数 × 中间结果均内存` 估峰值；超过容器内存 70% 就强制分块。给 apply 任务加进度与每组耗时采样，定位慢在"组多"还是"单组慢"。

```python
import pandas as pd
import numpy as np
import time, resource

df = pd.DataFrame({
    "user": [i % 5_000 for i in range(50_000)],   # 5000 组
    "v": range(50_000),
})

def cost_model(n_rows: int, n_groups: int, per_call_ms: float,
               inter_per_group_kb: float, container_mb: int = 2048) -> dict:
    est_ms = n_groups * per_call_ms
    peak_mb = n_rows * 0.08 + n_groups * inter_per_group_kb / 1024  # 粗估
    return {"est_seconds": est_ms / 1000, "peak_mb": peak_mb,
            "safe": peak_mb < container_mb * 0.7,
            "bottleneck": "组数多(调用开销)" if n_groups > 10_000
                          else "单组fn慢"}

print(cost_model(50_000, 5_000, per_call_ms=2, inter_per_group_kb=4))

# 实测对照：向量化聚合 vs groupby-apply
t0 = time.perf_counter()
vec = df.groupby("user")["v"].sum()
t_vec = time.perf_counter() - t0

def slow_fn(g: pd.DataFrame) -> pd.Series:
    # 模拟"每组构造中间对象"的反模式
    tmp = g.assign(double=g["v"] * 2)
    return pd.Series({"s": tmp["double"].sum()})

t0 = time.perf_counter()
app = df.groupby("user").apply(slow_fn, include_groups=False)
t_app = time.perf_counter() - t0

assert np.allclose(vec.values * 2, app["s"].values)   # apply 里是 2 倍和
print(f"向量化 {t_vec*1000:.1f}ms vs apply {t_app*1000:.1f}ms "
      f"-> {t_app/t_vec:.0f}x（组数越多差距越大）")
print("apply 期间峰值内存(MB):",
      resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024)
```

**追问 1**：为什么 apply 每组调用一次的开销在 G 大时会主导总耗时？
提示：每组都有解释器调用、DataFrame 切片物化、结果打包三层固定开销；G=10 万、单组 1ms 就是 100 秒，而这 1ms 里可能 0.9ms 是固定开销。

**追问 2**：`df.groupby(...).agg(lambda ...)` 与 `.apply` 的成本差异在哪？
提示：agg 对每列做聚合、能被 Cython 加速的路径会走 C；apply 整组传 Python 函数必走解释器；还有 transform/filter 的语义差异（保持原形状 vs 降维）决定能否互换。

**追问 3**：分块 + 多进程处理 groupby 时，结果的合并成本怎么记账？
提示：每组结果集大小决定合并是 concat（内存翻倍风险）还是落盘后二次聚合；分块还会打散跨块的全局排序/TopK 语义，要留全局归并阶段。

## 背诵要点
1. groupby-apply 成本 = G 次解释器调用（耗时主导）+ 全部组中间结果物化（内存主导）。
2. 容量估算：G × 单组耗时估时长；原始 df + 组数 × 中间均内存估峰值，超容器 70% 强制分块。
3. 降本顺序：向量化聚合 → ndarray/numba 化 fn → polars 表达式或分块进程池。

## 复盘追问
1. 你如何区分一个 groupby 任务是"组多"还是"单组慢"？有没有现成的每组耗时采样？
2. 如果明天数据量 ×10，你的 apply 任务第一个爆的会是内存还是时长？预案分别是什么？
