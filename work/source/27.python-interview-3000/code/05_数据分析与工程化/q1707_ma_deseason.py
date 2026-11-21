"""移动平均去季节性:居中移动平均估趋势,按星期因子去季节"""

SERIES = [120, 135, 130, 128, 150, 210, 195,   # 周内规律:周末高
          122, 140, 132, 130, 155, 215, 200,
          118, 138, 129, 127, 152, 208, 198]
W = 7  # 窗口=周期长度,奇数无需二次居中


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def centered_ma(xs, w):
    half = w // 2
    out = []
    for i in range(len(xs)):
        lo, hi = i - half, i + half + 1
        if lo < 0 or hi > len(xs):
            out.append(None)  # 边界不补,避免用残缺窗口伪造趋势
        else:
            out.append(sum(xs[lo:hi]) / w)
    return out


def weekday_factors(xs, trend, period=7):
    """季节因子 = 实际值 / 趋势值,按星期几取中位数并归一到均值 1"""
    ratios = [[] for _ in range(period)]
    for i, (x, t) in enumerate(zip(xs, trend)):
        if t is not None:
            ratios[i % period].append(x / t)
    factors = [median(rs) for rs in ratios]
    mean_f = sum(factors) / len(factors)
    return [f / mean_f for f in factors]


if __name__ == "__main__":
    trend = centered_ma(SERIES, W)
    factors = weekday_factors(SERIES, trend)
    print("星期因子(周一-周日):", [f"{f:.3f}" for f in factors])
    print("去季节序列:")
    for i, (x, f) in enumerate(zip(SERIES, factors)):
        print(f"  第{i:>2}天 原值{x:>4} 去季节 {x / f:>6.1f}")
    print("要点:窗口取周期长度(周规律取7)才能把季节波动平均掉;因子按星期几聚合;去季节后的序列才是真正的趋势主体")
