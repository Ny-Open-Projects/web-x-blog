---
title: [Q327] pandas 性能剖析与优化路径
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q327 · pandas 性能剖析与优化路径

> 难度:★★★ | 标签:pandas, profiling

**问**:一段 pandas 代码很慢,你的分析定位流程是什么?

**答**:先用 %timeit / time.perf_counter 粗测各步骤耗时,找到热点而不是猜;再用 df.memory_usage(deep=True) 看内存、df.dtypes 看类型问题(object 大字符串和高基数列常是元凶)。常见优化次序:换更优 dtype → 消除 iterrows/apply 换向量化 → 减少中间副本用就地链路 → 大表 join 前先缩小行/列 → 仍不够则换 Polars/DuckDB/分块。优化必须带前后基准数据,避免"感觉变快了"。

```python
# file: code/05_数据分析与工程化/q327_pandas_profile.py
import time

try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    result = fn(*args, **kwargs)
    return result, time.perf_counter() - t0

if __name__ == "__main__":
    if PANDAS:
        rng = np.random.default_rng(0)
        n = 500_000
        df = pd.DataFrame({"k": rng.integers(0, 100, n),
                           "v": rng.random(n)})
        # 热点对比:逐行 apply vs 向量化
        _, slow = timed(lambda: df.apply(lambda r: r["v"] * 2, axis=1))
        _, fast = timed(lambda: df["v"] * 2)
        print(f"apply(axis=1): {slow:.3f}s  vectorized: {fast:.4f}s")
        print(f"speedup ~{slow / max(fast, 1e-9):.0f}x")
        print(df.memory_usage(deep=True).to_dict())
    else:
        print("标准库:用 time.perf_counter 分段计时定位热点")
```

**追问**:
- memory_usage(deep=True) 为什么更准?——默认不统计 object 字符串的真实内容;deep=True 遍历对象,object 列的真实占用常是默认值的数倍。
- 优化到什么程度该停?——满足下游时延与内存预算即停;换 Polars/DuckDB 是结构性改动,收益要与迁移测试成本比。
- 怎么证明优化有效?——记录前后三件套:耗时(分步)、内存峰值、输出校验和一致;没有基线的优化不可信。

---
