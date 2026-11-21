"""重尾客单价:均值被大单拉高,报表口径用中位数与均值并列"""

try:
    import pandas as pd
except ImportError:
    pd = None

ORDERS = [79, 99, 128, 89, 159, 109, 69, 139, 119, 95,
          149, 88, 129, 105, 79, 199, 9990, 149, 115, 89]


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def trimmed_mean(xs, cut=0.1):
    s = sorted(xs)
    k = int(len(s) * cut)
    body = s[k:len(s) - k]
    return sum(body) / len(body)


def quantile(xs, q):
    s = sorted(xs)
    pos = (len(s) - 1) * q
    lo, hi = int(pos), min(int(pos) + 1, len(s) - 1)
    frac = pos - lo
    return s[lo] * (1 - frac) + s[hi] * frac


if __name__ == "__main__":
    n = len(ORDERS)
    print(f"订单数 {n}")
    print(f"均值 {sum(ORDERS) / n:.0f}  中位数 {median(ORDERS):.0f}  "
          f"p90 {quantile(ORDERS, 0.9):.0f}  截尾均值 {trimmed_mean(ORDERS):.0f}")
    print(f"剔除最大单后均值 {(sum(ORDERS) - max(ORDERS)) / (n - 1):.0f}")
    print("要点:一单 9990 把均值抬了约 500,客单价报表固定'中位数+均值'并列;大单单独走 B2B 视图;对比两期客单价先看分布再谈均值")
    if pd is not None:
        s = pd.Series(ORDERS)
        print("pandas 视角:", {"mean": round(s.mean(), 1), "median": s.median(),
                             "p90": float(s.quantile(0.9))})
