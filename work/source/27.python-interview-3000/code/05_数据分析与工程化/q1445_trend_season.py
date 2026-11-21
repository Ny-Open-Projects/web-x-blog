"""趋势基线与季节性识别:移动平均基线 x 星期因子,异常日一目了然"""
try:
    import pandas as pd
except ImportError:
    pd = None

import datetime as dt

BASE = 1000
DAYS = [(dt.date(2025, 6, 2) + dt.timedelta(days=i),
         int(BASE * (1 + 0.4 * ((dt.date(2025, 6, 2) + dt.timedelta(days=i)).weekday() >= 5))
             + (i * 37 % 60) - 30)) for i in range(14)]
DAYS.append((dt.date(2025, 6, 16), 480))  # 注入一个异常低点


def weekday_factor(days):
    """星期因子 = 该星期均值 / 全体均值,滚动窗口越长越稳"""
    overall = sum(v for _, v in days) / len(days)
    buckets = {}
    for d, v in days:
        buckets.setdefault(d.weekday(), []).append(v)
    return {wd: sum(vs) / len(vs) / overall for wd, vs in buckets.items()}


def stdlib_version(days, window=7):
    factors = weekday_factor(days[:-1])
    print("date        actual  expected  偏差")
    for i, (d, v) in enumerate(days):
        if i < window:
            continue
        history = [v2 for _, v2 in days[i - window:i]]
        expected = (sum(history) / len(history)) * factors[d.weekday()]
        dev = v / expected - 1
        flag = "  <-- 异常" if abs(dev) > 0.3 else ""
        print(f"{d}  {v:>6}  {expected:>8.0f}  {dev:+.0%}{flag}")


if pd is None:
    print("标准库降级:移动平均 x 星期因子")
    stdlib_version(DAYS)
else:
    s = pd.Series({d: v for d, v in DAYS}).sort_index()
    factor = s.groupby(s.index.weekday).mean() / s.mean()
    baseline = s.rolling(7).mean().shift(1) * s.index.map(factor)
    dev = s / baseline - 1
    out = dev[dev.abs() > 0.3]
    print("pandas 结果:异常日")
    print(out.dropna().to_string())
