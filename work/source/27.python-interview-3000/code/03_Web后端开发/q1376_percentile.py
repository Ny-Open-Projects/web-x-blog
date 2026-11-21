"""线性插值分位数与均值对比(纯标准库)。"""

LAT = sorted([12, 13, 13, 14, 15, 15, 16, 18, 21, 24, 30, 45, 90, 120, 260])


def percentile(sorted_vals, p):
    if not sorted_vals:
        raise ValueError("空样本")
    k = (len(sorted_vals) - 1) * p
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


mean = sum(LAT) / len(LAT)
print(f"mean={mean:.1f}ms p50={percentile(LAT, 0.5):.1f}ms "
      f"p95={percentile(LAT, 0.95):.1f}ms p99={percentile(LAT, 0.99):.1f}ms max={LAT[-1]}ms")
print("结论:均值 47ms 看似健康,p99 已到 240ms,超时与体验要按分位数设计")
