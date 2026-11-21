---
title: [Q7009] 特征/数据漂移监控的统计口径:PSI 与 KS
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7009 · 数据漂移监控的统计口径(PSI/KS)实现

> 难度:★★★ | 标签:数据质量, 统计, 监控

**问**：模型上线三个月后效果悄悄变差，怀疑特征分布漂移。PSI 和 KS 两种口径各适合什么场景？分箱怎么定才不是自欺欺人？给出可落地的监控实现。

**答**：结论：**PSI（Population Stability Index）适合分类型/分箱后的漂移度量与阈值管理**（<0.1 稳定，0.1~0.25 关注，>0.25 显著漂移），对样本量不敏感、可加权重，是风控/特征平台标配；**KS 统计量适合连续分布的两样本比较**（训练集 vs 近期窗口），无需分箱但只看最大间距、对尾部漂移不敏感。两者都做，PSI 管趋势告警、KS 做显著性检验兜底。

分箱的设计陷阱（这是口径可信的前提）：
- 分箱必须**用训练期分布定死**（等频或业务分位），线上对比时沿用同一套边界；如果每天按线上数据重新分箱，PSI 永远接近 0——自我欺骗是漂移监控的头号坑。
- 类别型特征：合并长尾（低于 0.5% 频次的类并成 OTHER）再算，否则新类别出现会把 PSI 打爆成噪音；同时"新类别出现率"本身要单列监控。
- 样本量约束：单日样本 < 1000 时 PSI 波动大，改周窗或先做 KS 检验（p<0.05 且 D>0.1 才告警）。PSI 的零值偏差：某箱实际占比为 0 时要用平滑（+1e-6）避免除零。
- 事故复盘：某特征平台 PSI 天天报警，排查发现监控 SQL 用了"当天分箱"。改为训练期冻结分箱后，告警从日均 20 条降到每周 2 条且条条可归因（上游埋点改版、App 版本分布变化）。

```python
# 基线:Python 3.9+ 标准库;PSI/KS 的纯标准库实现(可运行)
import math

def psi(expected: list[float], actual: list[float], eps: float = 1e-6) -> float:
    """PSI = Σ (a-e) * ln(a/e);expected/actual 为同一套分箱下的占比。"""
    total = 0.0
    for e, a in zip(expected, actual):
        e, a = max(e, eps), max(a, eps)
        total += (a - e) * math.log(a / e)
    return total

def ks_stat(x: list[float], y: list[float]) -> float:
    """两样本 KS 统计量:经验 CDF 的最大绝对差。"""
    xs = sorted(x) + [math.inf]
    ys = sorted(y) + [math.inf]
    i = j = 0
    d = 0.0
    while i < len(x) and j < len(y):
        if xs[i] <= ys[j]:
            i += 1
        else:
            j += 1
        d = max(d, abs(i / len(x) - j / len(y)))
    return d

if __name__ == "__main__":
    # 训练期冻结分箱占比(等频 5 箱)
    train_bins = [0.2, 0.2, 0.2, 0.2, 0.2]
    today_bins = [0.05, 0.15, 0.25, 0.25, 0.30]           # 分布右移
    v = psi(train_bins, today_bins)
    print(f"PSI={v:.3f}", "->", "显著漂移" if v > 0.25 else "关注" if v > 0.1 else "稳定")
    print("KS=", round(ks_stat([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 2))
```

**追问**：
- 一层追问：特征没漂但模型效果变差，还可能是什么？——目标漂移（y 分布变了，如风控政策改变坏账定义）、概念漂移（x→y 关系变了）、或特征上游计算 bug（值"稳定"在错误状态）。所以监控要三层：特征分布、label 分布、特征-label 相关性（如分箱坏账率曲线）。
- 二层追问：PSI 对小样本为什么不可靠？——占比估计的方差随样本量缩小，100 样本的 0.2 占比箱噪声就有 ±4%，PSI 天然虚高；要配最小样本门槛或用 bootstrap 置信区间判断 PSI 是否显著大于阈值。
- 三层追问：漂移告警之后的动作是什么？——分级响应：关注级（进周报归因）、显著级（触发特征回测：用近期数据重训 baseline，看 AUC 降幅）、严重级（降级到备用模型/规则兜底）；漂移监控的价值在触发动作，光报警不闭环等于没有。
