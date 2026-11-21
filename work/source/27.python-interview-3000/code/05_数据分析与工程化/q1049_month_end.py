try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from calendar import monthrange
    from datetime import date
    for y, m in ((2026, 2), (2026, 4)):
        last = monthrange(y, m)[1]
        print(f"{y}-{m:02d} 自然月末 {last} 日")
else:
    daily = pd.Series(
        range(10),
        index=pd.date_range("2026-02-20", periods=10, freq="D"),
    )
    print("按自然月聚合:", daily.groupby(daily.index.to_period("M")).sum().to_dict())
    ts = pd.Timestamp("2026-02-05")
    print("自然月末:", ts + pd.offsets.MonthEnd(0).normalize())
    print("工作日月末:", ts + pd.offsets.BMonthEnd(0).normalize())
    print("resample ME:", daily.resample("ME").sum().to_dict())
