---
title: [Q1053] z-score 的误用与重尾分布
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1053 · z-score 的误用与重尾分布

> 难度:★★★☆ | 标签:统计, 异常检测

**问**:都说"3 倍标准差之外是异常",这个规则什么时候会失效?

**答**:z-score 隐含近正态假设。重尾分布(收入、请求耗时、GMV)里,均值和标准差本身被极端值拉偏:少数大值把 σ 撑大,3σ 边界宽到几乎抓不到异常,误检率远偏离正态假设的 0.3%;小样本时单个离群点就能主导 σ。改进路径:先看分布,重尾先 log 变换再标准化;或改用稳健的 MAD/分位数边界;比例类指标直接用业务分位数。面试时要能说出"z-score 是假设检验思路,前提不成立结论就是噪音"这一层。

```python
# file: code/05_数据分析与工程化/q1053_zscore_misuse.py
try:
    import numpy as np
    rng = np.random.default_rng(0)
    x = rng.lognormal(0, 1.5, 500)  # 重尾样本
    z = (x - x.mean()) / x.std()
    print("z>3 占比:", round(float((np.abs(z) > 3).mean()), 4), "正态假设下应约 0.0027")
    print("99 分位:", round(float(np.quantile(x, 0.99)), 1), "3σ 上界:", round(float(x.mean() + 3 * x.std()), 1))
    lz = (np.log(x) - np.log(x).mean()) / np.log(x).std()
    print("log 变换后 z>3 占比:", round(float((np.abs(lz) > 3).mean()), 4))
except ImportError:
    import random, statistics
    random.seed(0)
    x = [random.lognormvariate(0, 1.5) for _ in range(500)]
    m, sd = statistics.mean(x), statistics.pstdev(x)
    z = [(v - m) / sd for v in x]
    print("z>3 占比:", round(sum(1 for t in z if abs(t) > 3) / len(z), 4))
    lx = [ __import__("math").log(v) for v in x ]
    lm, lsd = statistics.mean(lx), statistics.pstdev(lx)
    lz = [(v - lm) / lsd for v in lx]
    print("log 变换后 z>3 占比:", round(sum(1 for t in lz if abs(t) > 3) / len(lz), 4))
```

**追问**:
- 追问 1:为什么 log 对重尾有效?—— 乘性过程取对数变加性,分布被压缩到近似对称,标准化前提恢复。
- 追问 2:样本只有 30 个能算 z-score 吗?—— 能算但 σ 估计极不稳,建议 t 分布分位数或直接 bootstrap 分位区间。
