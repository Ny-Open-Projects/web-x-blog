"""稀疏事件平滑:伪计数与贝叶斯收缩,小样本率向全局均值收缩防跳变"""

EVENTS = {"页面A": (3, 40), "页面B": (28, 320), "页面C": (0, 6),
          "页面D": (5, 50), "页面E": (11, 900), "页面F": (2, 4)}


def fit_prior(pairs):
    """矩估计 Beta 先验:均值取全体比率,离散度人工给定并夹底防负"""
    n_total = sum(n for _, n in pairs)
    k_total = sum(k for k, _ in pairs)
    mean = k_total / n_total
    var = max(0.004, 1e-6)
    common = max(mean * (1 - mean) / var - 1, 1.0)
    return mean * common, (1 - mean) * common


def shrink(k, n, a, b):
    """平滑率 = (k + a) / (n + a + b),n 越小越贴近先验均值"""
    return (k + a) / (n + a + b)


if __name__ == "__main__":
    a, b = fit_prior(list(EVENTS.values()))
    print(f"Beta 先验: a={a:.3f} b={b:.3f},先验均值 {a / (a + b):.3f}")
    print(f"{'页面':<6}{'原始比率':>10}{'拉普拉斯':>10}{'贝叶斯收缩':>11}")
    for name, (k, n) in sorted(EVENTS.items()):
        raw = k / n if n else 0.0
        lap = (k + 1) / (n + 2)
        sm = shrink(k, n, a, b)
        print(f"{name:<6}{raw:>10.1%}{lap:>10.1%}{sm:>11.1%}")
    print("要点:小样本页面的原始率会在 0% 和 50% 之间乱跳;拉普拉斯是均匀先验,贝叶斯收缩向真实全局均值收;样本越大收缩越弱,两万级样本无需平滑")
