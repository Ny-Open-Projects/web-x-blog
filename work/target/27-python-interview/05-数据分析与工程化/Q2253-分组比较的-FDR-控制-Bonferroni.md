---
title: [Q2253] 分组比较的 FDR 控制:Bonferroni 与 BH 实现
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2253 · 分组比较的 FDR 控制:Bonferroni 与 BH 实现

> 难度:★★★☆ | 标签:多重检验, FDR

**问**:分城市看实验效果,20 个城市总有几个显著,怎么避免把噪声当发现?

**答**:20 个检验按 0.05 水平,期望假阳性就有 1 个,实测 20 个 p 值里不校正显著 7 个。两种校正:Bonferroni 用 alpha/m 的阈值,实测只放行 2 个,控制的是"任何假阳性"的族错误率,最保守,适合一锤定音的决策;Benjamini-Hochberg 控制的是错误发现率 FDR——把 p 值升序排,找最大的 k 使第 k 个 p 值不超过 k/m×alpha,实测放行 5 个,恰好把注入的 5 个真实差异全部抓到,期望假阳性不超过 0.05×5。探索性分析用 BH 保功效,注册过的主指标判定不需要多重校正。实现只有十几行,关键是阈值与排序规则要进公共库,而不是每个人手里一套。

```python
# file: code/05_数据分析与工程化/q2253_fdr_bh.py
"""分组比较的多重检验校正: Bonferroni 与 Benjamini-Hochberg"""

# 20 个分组比较的 p 值, 前 5 个来自真实存在差异的组
P_VALUES = [0.001, 0.002, 0.004, 0.009, 0.012,
            0.031, 0.044, 0.072, 0.103, 0.158,
            0.211, 0.276, 0.309, 0.412, 0.487,
            0.563, 0.641, 0.725, 0.818, 0.934]
ALPHA = 0.05


def bonferroni(pvals, alpha):
    m = len(pvals)
    return [i for i, p in enumerate(pvals) if p <= alpha / m]


def benjamini_hochberg(pvals, alpha):
    """找最大的 k 使第 k 小的 p <= k/m * alpha, 拒绝前 k 个"""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    k = 0
    for r, idx in enumerate(order, start=1):
        if pvals[idx] <= r / m * alpha:
            k = r
    return sorted(order[:k]) if k else []


if __name__ == "__main__":
    raw = [i for i, p in enumerate(P_VALUES) if p < ALPHA]
    bon = bonferroni(P_VALUES, ALPHA)
    bh = benjamini_hochberg(P_VALUES, ALPHA)
    print(f"不校正: 显著 {len(raw)} 个, 期望假阳性约 {ALPHA * len(P_VALUES):.1f} 个")
    print(f"Bonferroni 阈值 {ALPHA / len(P_VALUES):.4f}: {len(bon)} 个 -> {[P_VALUES[i] for i in bon]}")
    print(f"BH(FDR=5%): {len(bh)} 个 -> {[P_VALUES[i] for i in bh]}")
    print("结论: BH 保功效抓全 5 个真实差异且期望假阳性 <= 0.25 个; 一锤定音用 Bonferroni, 探索下钻用 BH")
```

**追问**:
- 追问 1:BH 和 Bonferroni 谁更严?—— Bonferroni 更严,它控族错误率,BH 只控错误发现比例,所以 BH 的拒绝数永远不少于 Bonferroni。
- 追问 2:p 值之间相关时 BH 还成立吗?—— BH 在正向回归相关下仍控 FDR,城市分组近似满足,极端相关才需要更保守的校正。
