try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [100, 110, 105, 120, 130]
    for i, v in enumerate(values):
        mom = v / values[i - 1] - 1 if i > 0 else None
        print(f"day{i} 值 {v} 环比 {mom if mom is None else f'{mom:.1%}'}")
else:
    s = pd.Series(
        [100, 110, 105, 120, 130],
        index=pd.date_range("2026-01-01", periods=5, freq="D"),
        name="gmv",
    )
    mom = s.pct_change()                 # 环比
    wow = s / s.shift(7) - 1             # 周同比思路,月度数据用 shift(12)
    diff = s.diff()                      # 绝对增量
    out = pd.DataFrame({"gmv": s, "mom": mom, "wow": wow, "delta": diff})
    print(out)
    # 有缺日时先补齐日历轴再算,否则 shift 的是位置不是时间
    s2 = s.drop(s.index[1])
    fixed = s2.reindex(pd.date_range(s2.index[0], s2.index[-1], freq="D"))
    print("缺日时 pct_change 错位:", fixed.pct_change().tolist())
