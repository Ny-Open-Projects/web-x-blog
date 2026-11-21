"""价格弹性粗估: 对数回归斜率与自助法区间"""

import math
import random

try:
    import pandas as pd
except ImportError:
    pd = None

random.seed(7)

# 城市-周级别的价格与销量观测, 来自不同促销时点
OBS = [
    (9.9, 820), (10.9, 745), (11.9, 690), (12.9, 610),
    (13.9, 560), (14.9, 520), (15.9, 470), (16.9, 430),
]


def log_log_slope(pairs):
    xs = [math.log(p) for p, _ in pairs]
    ys = [math.log(q) for _, q in pairs]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    return cov / var


def bootstrap_ci(pairs, times=500):
    stats = []
    n = len(pairs)
    for _ in range(times):
        sample = [pairs[random.randrange(n)] for _ in range(n)]
        stats.append(log_log_slope(sample))
    stats.sort()
    return stats[int(0.025 * times)], stats[int(0.975 * times)]


if __name__ == "__main__":
    slope = log_log_slope(OBS)
    lo, hi = bootstrap_ci(OBS)
    print(f"弹性点估计 {slope:.2f}, 95% 区间 [{lo:.2f}, {hi:.2f}]")
    print(f"|E|={abs(slope):.2f} -> {'富有弹性, 提价损失收入' if abs(slope) > 1 else '缺乏弹性, 提价短期增收'}")
    mixed = [(p, q * 0.6 if p >= 13.9 else q) for p, q in OBS]   # 高价档恰逢淡季的失真
    print(f"混入同向需求波动后弹性变成 {log_log_slope(mixed):.2f}, 粗估前必须控季节与趋势")
    if pd is not None:
        df = pd.DataFrame(OBS, columns=["price", "qty"])
        df["lp"] = df["price"].apply(math.log)
        df["lq"] = df["qty"].apply(math.log)
        print("pandas 视角: 弹性 =", round(df["lp"].cov(df["lq"]) / df["lp"].var(), 2))
