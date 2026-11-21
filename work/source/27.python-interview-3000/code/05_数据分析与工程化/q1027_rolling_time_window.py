try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:3 天移动平均,缺日不补")
    days = ["01-01", "01-03", "01-04", "01-05"]
    values = [1, 2, 3, 4]
    for i in range(len(values)):
        lo = max(0, i - 2)
        window = values[lo:i + 1]
        print(days[i], window, sum(window) / len(window))
else:
    idx = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-04", "2026-01-05"])
    s = pd.Series([1.0, 2.0, 3.0, 4.0], index=idx)
    print(s.rolling(3, min_periods=1).mean(), end="\n\n")
    # 时间窗:即使 01-02 缺失,窗口仍是自然 3 天跨度
    print(s.rolling("3D", min_periods=1).mean())
