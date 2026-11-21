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
